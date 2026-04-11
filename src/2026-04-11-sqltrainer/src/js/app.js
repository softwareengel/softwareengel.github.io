/**
 * Main Application Controller
 * Entry point for the SQL Training Platform
 */

import { SQLiteManager } from './db/sqlite-manager.js';
import { SchemaLoader } from './db/schema-loader.js';
import { Editor } from './components/editor.js';
import { FileBrowser } from './components/file-browser.js';
import { ResultsViewer } from './components/results-viewer.js';
import { StorageManager } from './utils/storage.js';
import { ExportManager } from './utils/export.js';

class App {
  constructor() {
    this.db = null;
    this.editor = null;
    this.fileBrowser = null;
    this.resultsViewer = null;
    this.storage = null;
    this.config = null;
    this.currentDatabase = null;
  }

  async init() {
    console.log('Initializing SQL Training Platform...');
    
    try {
      // Load configuration
      await this.loadConfig();
      
      // Initialize components
      this.storage = new StorageManager();
      await this.storage.init();
      
      // Try to initialize SQLite - continue even if it fails
      try {
        this.db = new SQLiteManager();
        await this.db.init();
      } catch (dbError) {
        console.error('SQLite initialization failed:', dbError);
        this.db = null;
        this.showError('Database engine not available. Please install SQL.js library. See lib/README.md for setup instructions.');
      }
      
      this.editor = new Editor('editor', this.config.editor);
      await this.editor.init();
      
      this.fileBrowser = new FileBrowser('file-browser');
      this.fileBrowser.init();
      
      this.resultsViewer = new ResultsViewer('results-grid');
      this.resultsViewer.init();
      
      // Set up event listeners
      this.setupEventListeners();
      
      // Update UI
      const statusMessage = this.db ? 'Ready' : 'Ready (Database disabled - SQL.js not loaded)';
      const statusType = this.db ? 'success' : 'warning';
      this.updateStatus(statusMessage, statusType);
      
      console.log('✓ App initialized successfully');
    } catch (error) {
      console.error('Failed to initialize app:', error);
      this.showError('Failed to initialize application: ' + error.message);
    }
  }

  async loadConfig() {
    try {
      const response = await fetch('config/app-config.json');
      this.config = await response.json();
    } catch (error) {
      console.warn('Could not load config, using defaults:', error);
      this.config = {
        editor: { theme: 'dark', fontSize: 14 },
        resultGrid: { maxRows: 1000 }
      };
    }
  }

  setupEventListeners() {
    // Database selection
    const dbSelector = document.getElementById('database-selector');
    const loadDbBtn = document.getElementById('load-db-btn');
    
    loadDbBtn.addEventListener('click', () => {
      const dbId = dbSelector.value;
      if (dbId) {
        this.loadDatabase(dbId);
      }
    });

    // Also auto-load when selection changes
    dbSelector.addEventListener('change', () => {
      const dbId = dbSelector.value;
      if (dbId) {
        this.loadDatabase(dbId);
      }
    });

    // Query execution
    const runQueryBtn = document.getElementById('run-query-btn');
    runQueryBtn.addEventListener('click', () => this.executeQuery());

    // Editor controls
    document.getElementById('clear-editor-btn').addEventListener('click', () => {
      this.editor.clear();
    });

    document.getElementById('save-query-btn').addEventListener('click', () => {
      this.showSaveQueryModal();
    });

    // Modal confirm/cancel/close
    document.getElementById('confirm-save-btn').addEventListener('click', async () => {
      const name = document.getElementById('query-name').value.trim();
      const description = document.getElementById('query-description').value.trim();
      if (!name) return;
      const sql = this.editor.getValue();
      try {
        await this.storage.saveQuery({ name, description, sql });
        this.hideSaveQueryModal();
        this.addMessage('Query saved: ' + name, 'success');
        this.refreshSavedQueries();
      } catch (err) {
        this.addMessage('Failed to save query: ' + err.message, 'error');
      }
    });

    document.getElementById('cancel-save-btn').addEventListener('click', () => {
      this.hideSaveQueryModal();
    });

    document.querySelector('#save-query-modal .modal-close').addEventListener('click', () => {
      this.hideSaveQueryModal();
    });

    document.getElementById('format-sql-btn').addEventListener('click', () => {
      this.editor.formatSQL();
    });

    // Export buttons
    document.getElementById('export-btn').addEventListener('click', () => {
      ExportManager.exportAsCSV(this.resultsViewer.getCurrentResults());
    });

    document.getElementById('export-json-btn').addEventListener('click', () => {
      ExportManager.exportAsJSON(this.resultsViewer.getCurrentResults());
    });

    // Theme toggle
    document.getElementById('theme-toggle').addEventListener('click', () => {
      this.toggleTheme();
    });

    // Sidebar tabs
    document.querySelectorAll('.tab-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        this.switchTab(e.target.dataset.tab);
      });
    });

    // Results tabs
    document.querySelectorAll('.results-tab-btn').forEach(btn => {
      btn.addEventListener('click', (e) => {
        this.switchResultsTab(e.target.dataset.tab);
      });
    });

    // File browser events
    this.fileBrowser.on('fileSelected', (filePath) => {
      this.loadExample(filePath);
    });

    // Keyboard shortcuts
    document.addEventListener('keydown', (e) => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        e.preventDefault();
        this.executeQuery();
      }
    });

    // Editor resizer
    this.setupResizer();
  }

  async loadDatabase(dbId) {
    if (!this.db) {
      this.addMessage('Database engine not available. Please install SQL.js library.', 'error');
      return;
    }
    
    this.updateStatus(`Loading ${dbId} database...`, 'loading');
    
    try {
      const dbConfig = this.config.sampleDatabases.find(db => db.id === dbId);
      if (!dbConfig) {
        throw new Error('Database configuration not found');
      }

      // Load SQL file
      const response = await fetch(dbConfig.file);
      const sql = await response.text();

      // Execute schema
      await this.db.executeBatch(sql);
      
      this.currentDatabase = dbId;
      this.updateStatus(`Connected to ${dbConfig.name}`, 'success');
      
      // Load schema
      const schema = await this.db.getSchema();
      this.displaySchema(schema);
      
      this.addMessage(`Database '${dbConfig.name}' loaded successfully`, 'success');
    } catch (error) {
      console.error('Failed to load database:', error);
      this.updateStatus('Failed to load database', 'error');
      this.showError('Failed to load database: ' + error.message);
    }
  }

  async executeQuery() {
    const sql = this.editor.getValue().trim();
    
    if (!sql) {
      this.addMessage('Please enter a SQL query', 'warning');
      return;
    }

    if (!this.db) {
      this.addMessage('Database engine not available. Please install SQL.js library. See lib/README.md', 'error');
      return;
    }

    if (!this.db.isReady()) {
      this.addMessage('Please load a database first', 'warning');
      return;
    }

    const startTime = performance.now();
    
    try {
      const results = await this.db.execute(sql);
      const endTime = performance.now();
      const executionTime = (endTime - startTime).toFixed(2);

      // Display results
      this.resultsViewer.displayResults(results);
      
      // Update UI
      const rowCount = results.data ? results.data.length : 0;
      this.updateQueryInfo(`${rowCount} rows returned in ${executionTime}ms`);
      
      document.getElementById('execution-time').textContent = `⚡ ${executionTime}ms`;
      
      // Enable export buttons
      document.getElementById('export-btn').disabled = rowCount === 0;
      document.getElementById('export-json-btn').disabled = rowCount === 0;
      
      // Add to history
      await this.storage.addQueryToHistory({
        sql,
        timestamp: new Date().toISOString(),
        executionTime,
        rowCount
      });
      
      this.refreshQueryHistory();
      this.addMessage(`Query executed successfully (${executionTime}ms)`, 'success');
      
    } catch (error) {
      console.error('Query execution failed:', error);
      this.addMessage(`Error: ${error.message}`, 'error');
      this.resultsViewer.displayError(error.message);
    }
  }

  async loadExample(filePath) {
    try {
      const response = await fetch(filePath);
      const sql = await response.text();
      this.editor.setValue(sql);
      
      document.getElementById('current-file').textContent = filePath.split('/').pop();
      this.addMessage(`Loaded example: ${filePath}`, 'info');
    } catch (error) {
      console.error('Failed to load example:', error);
      this.showError('Failed to load example file');
    }
  }

  displaySchema(schema) {
    const schemaViewer = document.getElementById('schema-viewer');
    
    let html = '<div class="schema-tables">';
    
    for (const table of schema.tables) {
      html += `
        <div class="schema-table">
          <div class="table-header">
            <span class="table-icon">📋</span>
            <span class="table-name">${table.name}</span>
          </div>
          <ul class="table-columns">
      `;
      
      for (const column of table.columns) {
        const isPK = column.pk ? ' 🔑' : '';
        html += `
          <li class="column-item">
            <span class="column-name">${column.name}</span>
            <span class="column-type">${column.type}${isPK}</span>
          </li>
        `;
      }
      
      html += `
          </ul>
        </div>
      `;
    }
    
    html += '</div>';
    schemaViewer.innerHTML = html;
  }

  switchTab(tabName) {
    // Update tab buttons
    document.querySelectorAll('.tab-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.tab === tabName);
    });
    
    // Update tab content
    document.querySelectorAll('.tab-content').forEach(content => {
      content.classList.toggle('active', content.id === `tab-${tabName}`);
    });
  }

  switchResultsTab(tabName) {
    // Update tab buttons
    document.querySelectorAll('.results-tab-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.tab === tabName);
    });
    
    // Update tab content
    document.querySelectorAll('.results-tab-content').forEach(content => {
      content.classList.toggle('active', content.id === `${tabName}-tab`);
    });
  }

  updateStatus(text, type = 'info') {
    const statusIcon = document.querySelector('#status-indicator .status-icon');
    const statusText = document.querySelector('#status-indicator .status-text');
    
    const icons = {
      success: '🟢',
      error: '🔴',
      warning: '🟡',
      loading: '🔵',
      info: '⚪'
    };
    
    statusIcon.textContent = icons[type] || icons.info;
    statusText.textContent = text;
  }

  updateQueryInfo(text) {
    document.getElementById('query-info').textContent = text;
  }

  addMessage(text, type = 'info') {
    const messagesConsole = document.getElementById('messages-console');
    const icons = {
      success: '✅',
      error: '❌',
      warning: '⚠️',
      info: 'ℹ️'
    };
    
    const messageEl = document.createElement('div');
    messageEl.className = `message ${type}`;
    messageEl.innerHTML = `
      <span class="message-icon">${icons[type]}</span>
      <span class="message-text">${text}</span>
      <span class="message-time">${new Date().toLocaleTimeString()}</span>
    `;
    
    messagesConsole.appendChild(messageEl);
    messagesConsole.scrollTop = messagesConsole.scrollHeight;
  }

  showSaveQueryModal() {
    document.getElementById('query-name').value = '';
    document.getElementById('query-description').value = '';
    document.getElementById('modal-overlay').classList.remove('hidden');
  }

  hideSaveQueryModal() {
    document.getElementById('modal-overlay').classList.add('hidden');
  }

  async refreshQueryHistory() {
    try {
      const history = await this.storage.getQueryHistory();
      const container = document.getElementById('query-history');
      if (!container) return;
      if (history.length === 0) {
        container.innerHTML = '<p class="empty-state">No query history yet</p>';
        return;
      }
      container.innerHTML = history.map(h => `
        <div class="history-item" data-sql="${this.escapeAttr(h.sql)}">
          <span class="history-sql">${this.escapeHtml(h.sql)}</span>
          <span class="history-time">${new Date(h.timestamp).toLocaleTimeString()}</span>
        </div>
      `).join('');
      container.querySelectorAll('.history-item').forEach(item => {
        item.addEventListener('click', () => {
          this.editor.setValue(item.dataset.sql);
        });
      });
    } catch (err) {
      console.error('Failed to load query history:', err);
    }
  }

  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  escapeAttr(text) {
    return text.replace(/&/g, '&amp;').replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  async refreshSavedQueries() {
    try {
      const queries = await this.storage.getSavedQueries();
      const list = document.getElementById('saved-queries-list');
      if (!list) return;
      if (queries.length === 0) {
        list.innerHTML = '<p class="empty-state">No saved queries yet.</p>';
        return;
      }
      list.innerHTML = queries.map(q => `
        <div class="saved-query-item" data-id="${q.id}">
          <span class="saved-query-name">${q.name}</span>
          <span class="saved-query-sql">${q.sql}</span>
          <button class="delete-btn btn btn-danger btn-sm" data-id="${q.id}">&times;</button>
        </div>
      `).join('');
      list.querySelectorAll('.saved-query-item').forEach(item => {
        item.addEventListener('click', (e) => {
          if (e.target.classList.contains('delete-btn')) return;
          const sql = item.querySelector('.saved-query-sql').textContent;
          this.editor.setValue(sql);
        });
      });
      list.querySelectorAll('.delete-btn').forEach(btn => {
        btn.addEventListener('click', async (e) => {
          e.stopPropagation();
          const id = Number(btn.dataset.id);
          await this.storage.deleteQuery(id);
          this.refreshSavedQueries();
        });
      });
    } catch (err) {
      console.error('Failed to load saved queries:', err);
    }
  }

  showError(message) {
    alert(message); // TODO: Replace with better modal
  }

  toggleTheme() {
    document.body.classList.toggle('dark-theme');
    document.body.classList.toggle('light-theme');
    
    const icon = document.querySelector('#theme-toggle');
    icon.textContent = document.body.classList.contains('dark-theme') ? '🌙' : '☀️';
  }

  setupResizer() {
    const resizer = document.getElementById('editor-resizer');
    const editorContainer = document.querySelector('.editor-container');
    const resultsContainer = document.querySelector('.results-container');
    
    let isResizing = false;
    
    resizer.addEventListener('mousedown', () => {
      isResizing = true;
      document.body.style.cursor = 'row-resize';
    });
    
    document.addEventListener('mousemove', (e) => {
      if (!isResizing) return;
      
      const containerRect = document.querySelector('.content-area').getBoundingClientRect();
      const offsetY = e.clientY - containerRect.top - 60; // 60 = toolbar height
      
      editorContainer.style.height = `${offsetY}px`;
    });
    
    document.addEventListener('mouseup', () => {
      isResizing = false;
      document.body.style.cursor = 'default';
    });
  }
}

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
  const app = new App();
  app.init();
  
  // Make app globally available for debugging
  window.sqlApp = app;
});
