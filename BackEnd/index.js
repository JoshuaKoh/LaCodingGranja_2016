var mongoose = require("mongoose");
var express = require("express");
var bodyParser = require('body-parser');
var NewsMood = require("./models/NewsArticle");

//connect to MongoDB
// Insert Super Secret Connection String here
mongoose.connect("mongodb://newsmood:hLQp9PBtdRnJGmKI9FegaJJPLI9T3Yl8vGHrwcXzYLt41dUXYZTzsoA27NrH001CxZbgA0Aqjbio4liIVxKkIA==@newsmood.documents.azure.com:10250/?ssl=true");

var app = express();
// configure app to use bodyParser()
// this will let us get the data from a POST
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var router = express.Router();

app.get('/', function(req,res){
    res.json({message:"Routing works!"});
});

app.post('/insertNewsArticle', function(req, res){
    var newArticle = new NewsMood({
        name: "ABS",
        source: "Some",
        mood: "Some",
    });

    newArticle.save(function(err){
        if(err)
            res.json({message: "insert failed", error: err});
        else
            res.json({message: "insert successful"});
    })
});

app.get('/newsMoods', function(req, res){
    NewsMood.find(function(err, users){
        if(err) res.send(err);
        else res.json(users);
    });
});

app.listen(3000, function(){
    console.log('Server ON');
});
