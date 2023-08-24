const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const router = express.Router();
const multer = require('multer');
const csv = require('csvtojson');


const storage = multer.diskStorage({
    destination:(req,file,cb)=>
    {
        cb(null,'Files');
    },
    filename: (req,file,cb)=>
    {
        cb(null,file.originalname);
    }
});

const upload = multer ({
    storage,
})



app.use(bodyParser.json())

//creating base route and assigning it to a port
app.route("/").get((req,res) =>
{
    res.json("Welcome");
});


app.route('/upload').post(upload.single('csvFile'),async (req,res)=>
{
    const jsonArray=await csv().fromFile('Files/test.csv');
    res.json(jsonArray);
});



let port = 8000;
app.listen(port, () => {
  console.log("the port is running on " + port);
});

