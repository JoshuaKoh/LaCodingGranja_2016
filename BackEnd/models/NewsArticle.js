var mongoose = require("mongoose");

//Set up MondgoDB Schema
var Schema = mongoose.Schema;

var NewsArticleSchema = new Schema({
    name: {type: String, required: true},
    source: {type: String, required: true},
    mood: {type: String, required: true},
    updated_at: Date,
    created_at: Date
});

//Save creation and updated date
NewsArticleSchema.pre('save', function(next){

    var curDate = new Date();

    this.updated_at = curDate;

    if(!this.created_at)
        this.created_at = curDate;

    next();
});


module.exports = mongoose.model('NewsMood', NewsArticleSchema);