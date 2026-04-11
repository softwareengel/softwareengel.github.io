/**
 * SQL Editor Component
 * Manages the CodeMirror editor instance
 */

export class Editor {
  constructor(elementId, config = {}) {
    this.elementId = elementId;
    this.config = config;
    this.editor = null;
  }

  async init() {
    const element = document.getElementById(this.elementId);
    
    if (!element) {
      throw new Error(`Element ${this.elementId} not found`);
    }

    // Check if CodeMirror is available
    if (typeof CodeMirror === 'undefined') {
      console.warn('CodeMirror not loaded, using textarea fallback');
      this.initFallback(element);
      return;
    }

    try {
      this.editor = CodeMirror.fromTextArea(element, {
        mode: 'text/x-sql',
        theme: this.config.theme || 'dracula',
        lineNumbers: this.config.lineNumbers !== false,
        indentUnit: this.config.tabSize || 2,
        tabSize: this.config.tabSize || 2,
        indentWithTabs: false,
        lineWrapping: true,
        autoCloseBrackets: true,
        matchBrackets: true,
        extraKeys: {
          'Ctrl-Enter': () => this.onExecute?.(),
          'Cmd-Enter': () => this.onExecute?.(),
          'Ctrl-Space': 'autocomplete'
        }
      });

      console.log('✓ CodeMirror editor initialized');
    } catch (error) {
      console.error('Failed to initialize CodeMirror:', error);
      this.initFallback(element);
    }
  }

  initFallback(element) {
    // Use plain textarea as fallback
    element.style.display = 'block';
    element.style.width = '100%';
    element.style.height = '100%';
    element.style.fontFamily = 'monospace';
    element.style.fontSize = '14px';
    this.editor = element;
    console.log('Using textarea fallback for editor');
  }

  getValue() {
    if (!this.editor) return '';
    
    if (this.editor.getValue) {
      return this.editor.getValue();
    }
    
    return this.editor.value || '';
  }

  setValue(value) {
    if (!this.editor) return;
    
    if (this.editor.setValue) {
      this.editor.setValue(value);
    } else {
      this.editor.value = value;
    }
  }

  clear() {
    this.setValue('');
  }

  formatSQL() {
    const sql = this.getValue();
    
    // Basic SQL formatting
    let formatted = sql
      .replace(/\s+/g, ' ')
      .replace(/\s*,\s*/g, ',\n  ')
      .replace(/\b(SELECT|FROM|WHERE|JOIN|LEFT JOIN|RIGHT JOIN|INNER JOIN|GROUP BY|ORDER BY|HAVING|LIMIT)\b/gi, '\n$1')
      .replace(/\b(AND|OR)\b/gi, '\n  $1')
      .trim();
    
    this.setValue(formatted);
  }

  insertAtCursor(text) {
    if (!this.editor) return;
    
    if (this.editor.replaceSelection) {
      this.editor.replaceSelection(text);
    } else {
      const start = this.editor.selectionStart;
      const end = this.editor.selectionEnd;
      const value = this.editor.value;
      this.editor.value = value.substring(0, start) + text + value.substring(end);
      this.editor.selectionStart = this.editor.selectionEnd = start + text.length;
    }
  }

  focus() {
    if (this.editor?.focus) {
      this.editor.focus();
    }
  }

  onExecute = null;
}
