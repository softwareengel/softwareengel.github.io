
# node rest mysql


https://www.youtube.com/watch?v=WfCJ3sHnLBM&t=2178s

https://github.com/Tariqu/REST_API_WITH_MYSQL
    

node project init 

    npm init -y

file package.json

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

node express 

    npm install express

auto restart debuging 

    npm install --save-dev nodemon 

simple mock app: app.js  

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


## Database JS Hacks 


### 1 SQLite 

    npm install --save sqlite3 



