# Required Library Files

This folder should contain third-party libraries needed for the SQL Training Platform.

## Required Files

### 1. SQL.js (SQLite WASM)

Download from: https://sql.js.org/dist/sql-wasm.js

Required files:
- `sql-wasm.js` - Main SQL.js library
- `sql-wasm.wasm` - WebAssembly binary

**Installation:**
```bash
# Download latest release
curl -L https://sql.js.org/dist/sql-wasm.js -o lib/sql-wasm.js
curl -L https://sql.js.org/dist/sql-wasm.wasm -o lib/sql-wasm.wasm
```

Or use npm:
```bash
npm install sql.js
cp node_modules/sql.js/dist/sql-wasm.js lib/
cp node_modules/sql.js/dist/sql-wasm.wasm lib/
```

### 2. CodeMirror (Optional - for enhanced SQL editor)

Download from: https://codemirror.net/5/

Required files:
```
lib/
  codemirror/
    codemirror.js
    codemirror.css
    mode/
      sql/
        sql.js
    theme/
      dracula.css
```

**Installation:**
```bash
# Download CodeMirror 5.x
curl -L https://codemirror.net/5/codemirror.zip -o codemirror.zip
unzip codemirror.zip
cp -r codemirror-5.x/lib lib/codemirror
cp -r codemirror-5.x/mode/sql lib/codemirror/mode/
cp -r codemirror-5.x/theme lib/codemirror/
```

Or use npm:
```bash
npm install codemirror@5
mkdir -p lib/codemirror/mode/sql
mkdir -p lib/codemirror/theme
cp node_modules/codemirror/lib/codemirror.js lib/codemirror/
cp node_modules/codemirror/lib/codemirror.css lib/codemirror/
cp node_modules/codemirror/mode/sql/sql.js lib/codemirror/mode/sql/
cp node_modules/codemirror/theme/dracula.css lib/codemirror/theme/
```

## File Structure

After setup, your lib/ folder should look like:

```
lib/
├── README.md (this file)
├── sql-wasm.js
├── sql-wasm.wasm
└── codemirror/
    ├── codemirror.js
    ├── codemirror.css
    ├── mode/
    │   └── sql/
    │       └── sql.js
    └── theme/
        └── dracula.css
```

## Fallback Behavior

If libraries are not found:
- **SQL.js missing**: App will show error message and cannot execute queries
- **CodeMirror missing**: App will use plain textarea fallback (basic editing only)

## License Notes

- SQL.js: MIT License
- CodeMirror: MIT License

Make sure to comply with their respective licenses when distributing.
