import { Meteor } from 'meteor/meteor';
import { Mongo } from 'meteor/mongo';

Meteor.startup(() => {
  // code to run on server at startup
  Articles = new Mongo.Collection("articles");  //Connect to the articles collection
});
