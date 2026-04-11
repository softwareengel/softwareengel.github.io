/**
 * Storage Manager
 * Handles IndexedDB operations for persisting user data
 */

export class StorageManager {
  constructor() {
    this.db = null;
    this.dbName = 'SQLTrainingPlatform';
    this.version = 1;
  }

  async init() {
    return new Promise((resolve, reject) => {
      const request = indexedDB.open(this.dbName, this.version);

      request.onerror = () => {
        console.error('IndexedDB error:', request.error);
        reject(request.error);
      };

      request.onsuccess = () => {
        this.db = request.result;
        console.log('✓ IndexedDB initialized');
        resolve();
      };

      request.onupgradeneeded = (event) => {
        const db = event.target.result;

        // Create object stores
        if (!db.objectStoreNames.contains('queries')) {
          const queryStore = db.createObjectStore('queries', { keyPath: 'id', autoIncrement: true });
          queryStore.createIndex('timestamp', 'timestamp', { unique: false });
          queryStore.createIndex('name', 'name', { unique: false });
        }

        if (!db.objectStoreNames.contains('history')) {
          const historyStore = db.createObjectStore('history', { keyPath: 'id', autoIncrement: true });
          historyStore.createIndex('timestamp', 'timestamp', { unique: false });
        }

        if (!db.objectStoreNames.contains('databases')) {
          db.createObjectStore('databases', { keyPath: 'id' });
        }
      };
    });
  }

  async saveQuery(query) {
    return new Promise((resolve, reject) => {
      const transaction = this.db.transaction(['queries'], 'readwrite');
      const store = transaction.objectStore('queries');
      
      const request = store.add({
        ...query,
        timestamp: new Date().toISOString()
      });

      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }

  async getSavedQueries() {
    return new Promise((resolve, reject) => {
      const transaction = this.db.transaction(['queries'], 'readonly');
      const store = transaction.objectStore('queries');
      const request = store.getAll();

      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }

  async deleteQuery(id) {
    return new Promise((resolve, reject) => {
      const transaction = this.db.transaction(['queries'], 'readwrite');
      const store = transaction.objectStore('queries');
      const request = store.delete(id);

      request.onsuccess = () => resolve();
      request.onerror = () => reject(request.error);
    });
  }

  async addQueryToHistory(query) {
    return new Promise((resolve, reject) => {
      const transaction = this.db.transaction(['history'], 'readwrite');
      const store = transaction.objectStore('history');
      
      const request = store.add({
        ...query,
        timestamp: new Date().toISOString()
      });

      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }

  async getQueryHistory(limit = 100) {
    return new Promise((resolve, reject) => {
      const transaction = this.db.transaction(['history'], 'readonly');
      const store = transaction.objectStore('history');
      const index = store.index('timestamp');
      
      const request = index.openCursor(null, 'prev');
      const results = [];

      request.onsuccess = (event) => {
        const cursor = event.target.result;
        if (cursor && results.length < limit) {
          results.push(cursor.value);
          cursor.continue();
        } else {
          resolve(results);
        }
      };

      request.onerror = () => reject(request.error);
    });
  }

  async clearHistory() {
    return new Promise((resolve, reject) => {
      const transaction = this.db.transaction(['history'], 'readwrite');
      const store = transaction.objectStore('history');
      const request = store.clear();

      request.onsuccess = () => resolve();
      request.onerror = () => reject(request.error);
    });
  }
}
