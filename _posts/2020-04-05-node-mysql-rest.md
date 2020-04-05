Beispiel JSON Response von Sqlite3 Datenbank  

# Node Rest MySQL / Sqlite3

<https://www.youtube.com/watch?v=WfCJ3sHnLBM&t=2178s>

<https://github.com/Tariqu/REST_API_WITH_MYSQL>
    

## node project init 

    npm init -y

## File package.json

```config
{
  "name": "2020-04-05-node-rest-db",
  "version": "1.0.0",
  "description": "",
  "main": "app.js",
  "scripts": {
    "start": "nodemon app.js"
  },
  "keywords": [],
  "author": "",
  "license": "",
  "dependencies": {
    "express": "^4.17.1"
  },
  "devDependencies": {
    "nodemon": "^2.0.2"
  }
}
```

## Node Express 

    npm install express

## Auto Restart Debuging 

    npm install --save-dev nodemon 

## SQLite 

    npm install --save sqlite3 


## Database Create SQL

```sql
drop table t_lm;

CREATE TABLE T_LM (
	LM_ID INTEGER,
	LM_MAT TEXT,	
	LM_CHARGE TEXT,
	LM_X INTEGER ,
	LM_Y INTEGER ,
	LM_Z INTEGER ,
	LM_TYP TEXT
);

select * from t_lm;

drop table t_fauf;

CREATE TABLE T_FAUF (
	fauf_ID INTEGER,
	fauf_material TEXT, 
	fauf_charge text,
	fauf_anzahl integer,
	FAUF_X INTEGER,
	fauf_Y INTEGER,
-- 	fauf_z INTEGER,
	fauf_termin	text
);

``` 

## Simple Mock App: app.js  

```javascript 

const express = require("express")
const app = express();
const sqlite3 = require('sqlite3').verbose();

let db = new sqlite3.Database('./data/data.db', (err) => {
    if (err) {
      console.error(err.message);
    }
    console.log('Connected to the database.');
  });


app.use("/public",express.static('public')); 
app.get("/api/lm", (req,res) => {

    let sql = `SELECT lm_id as id, lm_x as x FROM t_lm`;
    sql = "select * from t_lm";
    db.all (sql, function(err, rows,fields) {
        console.log(rows);
        res.json({
            success:1,
            message: rows
        })
    })
});

app.get("/api", (req,res) => {
    res.json({
        success:1,
        message: "API working"
    })
});

app.get("/api/fauf", (req,res) => {
    let sql = `SELECT * FROM t_fauf`;
    db.all (sql, function(err, rows,fields) {
        console.log(rows);
        res.json({
            success:1,
            message: rows
        })
    })
});

app.listen(3000 , ()=> {
    console.log("Server started and running.");
})

```
