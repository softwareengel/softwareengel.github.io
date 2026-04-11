/**
 * Results Viewer Component
 * Displays query results in a table format
 */

export class ResultsViewer {
  constructor(containerId) {
    this.containerId = containerId;
    this.currentResults = null;
  }

  init() {
    console.log('✓ Results viewer initialized');
  }

  displayResults(results) {
    const container = document.getElementById(this.containerId);
    this.currentResults = results;

    if (!results.data || results.data.length === 0) {
      container.innerHTML = '<div class="empty-state"><p>Query executed successfully. No rows returned.</p></div>';
      return;
    }

    // Create table
    let html = '<table class="results-table"><thead><tr>';
    
    // Headers
    results.columns.forEach(col => {
      html += `<th>${this.escapeHtml(col)}</th>`;
    });
    html += '</tr></thead><tbody>';

    // Rows
    results.data.forEach((row, idx) => {
      html += `<tr class="${idx % 2 === 0 ? 'even' : 'odd'}">`;
      results.columns.forEach(col => {
        const value = row[col];
        html += `<td>${this.formatValue(value)}</td>`;
      });
      html += '</tr>';
    });

    html += '</tbody></table>';
    
    container.innerHTML = html;
  }

  displayError(errorMessage) {
    const container = document.getElementById(this.containerId);
    container.innerHTML = `
      <div class="error-state">
        <div class="error-icon">❌</div>
        <div class="error-message">${this.escapeHtml(errorMessage)}</div>
      </div>
    `;
  }

  getCurrentResults() {
    return this.currentResults;
  }

  formatValue(value) {
    if (value === null) {
      return '<span class="null-value">NULL</span>';
    }
    if (typeof value === 'boolean') {
      return value ? 'TRUE' : 'FALSE';
    }
    if (typeof value === 'number') {
      return `<span class="number-value">${value}</span>`;
    }
    return this.escapeHtml(String(value));
  }

  escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  clear() {
    const container = document.getElementById(this.containerId);
    container.innerHTML = '<div class="empty-state"><p>No results yet. Run a query to see results here.</p></div>';
    this.currentResults = null;
  }
}
