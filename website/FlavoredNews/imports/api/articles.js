import { Meteor } from 'meteor/meteor';
import { Mongo } from 'meteor/mongo';
import { check } from 'meteor/check';

export const Articles = new Mongo.Collection('articles');

if (Meteor.isServer) {
  console.log("I am in the server!");
}

Meteor.methods({
  'articles.pullAll'() {
      return Articles.find().fetch();
  }
});