const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');


const membership = require('./routes/membership.route')


const app = express();

// Connecting to database
let dev_db_url = 'mongodb+srv://somethingczar:Learn123@something.kcc4rcl.mongodb.net/';
let mongoDB = process.env.MONGODB_URI || dev_db_url;
mongoose.connect(mongoDB);
mongoose.Promise = global.Promise;
let db = mongoose.connection;
db.on('error', console.error.bind(console, 'MongoDB connection error:'));



app.use(bodyParser.json())

//CORS control
app.use(function(req, res, next) {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Credentials', true);
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    next();
  });

//creating base route and assigning it to a port
app.use('/membership',membership)


let port = 1234;
app.listen(port, ()=>
{
    console.log("the port is running on " + port);
});

