import { Meteor } from 'meteor/meteor';
import { Mongo } from 'meteor/mongo';

export const Articles = new Mongo.Collection('articles');

console.log("One item from articles:");
console.log(Articles);
console.log("Done");

Meteor.methods({
  'articles.pullAll'() {
      return Articles.find().fetch();
  }
});