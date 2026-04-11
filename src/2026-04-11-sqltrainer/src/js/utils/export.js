/**
 * Export Manager
 * Handles exporting query results to various formats
 */

export class ExportManager {
  static exportAsCSV(results) {
    if (!results || !results.data || results.data.length === 0) {
      alert('No data to export');
      return;
    }

    const columns = results.columns;
    const rows = results.data;

    // Create CSV content
    let csv = columns.join(',') + '\n';
    
    rows.forEach(row => {
      const values = columns.map(col => {
        const value = row[col];
        if (value === null) return '';
        if (typeof value === 'string' && (value.includes(',') || value.includes('"') || value.includes('\n'))) {
          return `"${value.replace(/"/g, '""')}"`;
        }
        return value;
      });
      csv += values.join(',') + '\n';
    });

    // Download
    this.downloadFile(csv, 'query-results.csv', 'text/csv');
  }

  static exportAsJSON(results) {
    if (!results || !results.data || results.data.length === 0) {
      alert('No data to export');
      return;
    }

    const json = JSON.stringify(results.data, null, 2);
    this.downloadFile(json, 'query-results.json', 'application/json');
  }

  static exportAsSQL(results, tableName = 'results') {
    if (!results || !results.data || results.data.length === 0) {
      alert('No data to export');
      return;
    }

    const columns = results.columns;
    const rows = results.data;

    let sql = `-- Exported query results\n`;
    sql += `-- Generated on ${new Date().toISOString()}\n\n`;
    sql += `CREATE TABLE ${tableName} (\n`;
    sql += columns.map(col => `  ${col} TEXT`).join(',\n');
    sql += '\n);\n\n';

    rows.forEach(row => {
      const values = columns.map(col => {
        const value = row[col];
        if (value === null) return 'NULL';
        if (typeof value === 'number') return value;
        return `'${String(value).replace(/'/g, "''")}'`;
      });
      sql += `INSERT INTO ${tableName} VALUES (${values.join(', ')});\n`;
    });

    this.downloadFile(sql, 'query-results.sql', 'text/plain');
  }

  static downloadFile(content, filename, mimeType) {
    const blob = new Blob([content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    link.click();
    
    // Clean up
    setTimeout(() => URL.revokeObjectURL(url), 100);
  }
}
