/**
 * File Browser Component
 * Manages the sidebar file tree navigation
 */

export class FileBrowser {
  constructor(containerId) {
    this.containerId = containerId;
    this.eventHandlers = new Map();
    this.currentFile = null;
  }

  init() {
    this.setupFolderToggle();
    this.setupFileSelection();
    console.log('✓ File browser initialized');
  }

  setupFolderToggle() {
    document.querySelectorAll('.tree-node.folder').forEach(folder => {
      const folderName = folder.querySelector('.folder-name');
      
      folderName.addEventListener('click', () => {
        folder.classList.toggle('expanded');
      });
    });
  }

  setupFileSelection() {
    document.querySelectorAll('.tree-item.file').forEach(file => {
      file.addEventListener('click', () => {
        // Remove previous selection
        document.querySelectorAll('.tree-item.file').forEach(f => {
          f.classList.remove('selected');
        });
        
        // Select current file
        file.classList.add('selected');
        
        const filePath = file.dataset.file;
        this.currentFile = filePath;
        
        // Trigger event
        this.trigger('fileSelected', filePath);
      });
    });
  }

  on(event, handler) {
    if (!this.eventHandlers.has(event)) {
      this.eventHandlers.set(event, []);
    }
    this.eventHandlers.get(event).push(handler);
  }

  trigger(event, data) {
    const handlers = this.eventHandlers.get(event) || [];
    handlers.forEach(handler => handler(data));
  }

  selectFile(filePath) {
    const fileElement = document.querySelector(`[data-file="${filePath}"]`);
    if (fileElement) {
      fileElement.click();
    }
  }

  getCurrentFile() {
    return this.currentFile;
  }
}
