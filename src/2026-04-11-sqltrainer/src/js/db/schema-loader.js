/**
 * Schema Loader
 * Loads and manages sample database schemas
 */

export class SchemaLoader {
  constructor() {
    this.schemas = new Map();
  }

  async loadSchema(dbId, filePath) {
    try {
      const response = await fetch(filePath);
      const sql = await response.text();
      
      this.schemas.set(dbId, {
        id: dbId,
        sql: sql,
        loadedAt: new Date()
      });
      
      return sql;
    } catch (error) {
      console.error(`Failed to load schema for ${dbId}:`, error);
      throw error;
    }
  }

  getSchema(dbId) {
    return this.schemas.get(dbId);
  }

  hasSchema(dbId) {
    return this.schemas.has(dbId);
  }

  clearSchemas() {
    this.schemas.clear();
  }
}
