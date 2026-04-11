/**
 * SQLite Manager
 * Handles SQLite WASM initialization and query execution
 */

export class SQLiteManager {
  constructor() {
    this.db = null;
    this.ready = false;
  }

  async init() {
    try {
      console.log('Initializing SQLite WASM...');
      
      // Check if initSqlJs is available
      if (typeof initSqlJs === 'undefined') {
        console.error('SQL.js not loaded. Please include sql-wasm.js in lib/ folder.');
        throw new Error('SQL.js library not found. Please download from https://sql.js.org/');
      }
      
      // Initialize SQL.js (assumes sql-wasm.js is loaded globally)
      const SQL = await initSqlJs({
        locateFile: file => `lib/${file}`
      });
      
      // Create a new database
      this.db = new SQL.Database();
      this.ready = true;
      
      console.log('✓ SQLite initialized');
    } catch (error) {
      console.error('Failed to initialize SQLite:', error);
      throw error;
    }
  }

  isReady() {
    return this.ready && this.db !== null;
  }

  async execute(sql) {
    if (!this.isReady()) {
      throw new Error('Database not initialized');
    }

    try {
      const results = this.db.exec(sql);
      
      if (results.length === 0) {
        // Query executed but returned no results (INSERT, UPDATE, DELETE, etc.)
        return {
          success: true,
          data: [],
          columns: [],
          rowsAffected: this.db.getRowsModified()
        };
      }

      // Format results
      const firstResult = results[0];
      return {
        success: true,
        data: firstResult.values.map(row => {
          const obj = {};
          firstResult.columns.forEach((col, idx) => {
            obj[col] = row[idx];
          });
          return obj;
        }),
        columns: firstResult.columns,
        rowCount: firstResult.values.length
      };
    } catch (error) {
      console.error('Query execution error:', error);
      throw new Error(error.message || 'Query execution failed');
    }
  }

  async executeBatch(sql) {
    if (!this.isReady()) {
      throw new Error('Database not initialized');
    }

    try {
      // Create a fresh database to avoid "table already exists" errors on re-load
      const SQL = await initSqlJs({
        locateFile: file => `lib/${file}`
      });
      this.db = new SQL.Database();
      this.db.run(sql);
      return { success: true };
    } catch (error) {
      console.error('Batch execution error:', error);
      throw error;
    }
  }

  async getSchema() {
    const sql = `
      SELECT 
        name as table_name,
        sql as create_statement
      FROM sqlite_master 
      WHERE type = 'table' 
        AND name NOT LIKE 'sqlite_%'
      ORDER BY name;
    `;

    const result = await this.execute(sql);
    const tables = [];

    for (const table of result.data) {
      const columnsResult = await this.execute(`PRAGMA table_info(${table.table_name})`);
      
      tables.push({
        name: table.table_name,
        columns: columnsResult.data.map(col => ({
          name: col.name,
          type: col.type,
          notNull: col.notnull === 1,
          pk: col.pk === 1,
          defaultValue: col.dflt_value
        })),
        createStatement: table.create_statement
      });
    }

    return { tables };
  }

  async getTables() {
    const sql = `
      SELECT name 
      FROM sqlite_master 
      WHERE type = 'table' 
        AND name NOT LIKE 'sqlite_%'
      ORDER BY name;
    `;
    
    const result = await this.execute(sql);
    return result.data.map(row => row.name);
  }

  async getTableRowCount(tableName) {
    const result = await this.execute(`SELECT COUNT(*) as count FROM ${tableName}`);
    return result.data[0].count;
  }

  exportDatabase() {
    if (!this.isReady()) {
      throw new Error('Database not initialized');
    }
    
    return this.db.export();
  }

  importDatabase(data) {
    if (!this.isReady()) {
      throw new Error('Database not initialized');
    }
    
    this.db = new SQL.Database(data);
  }

  close() {
    if (this.db) {
      this.db.close();
      this.db = null;
      this.ready = false;
    }
  }
}
