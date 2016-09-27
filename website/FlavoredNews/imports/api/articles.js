import { Meteor } from 'meteor/meteor';
import { Mongo } from 'meteor/mongo';

export const Articles = new Mongo.Collection('articles');

Meteor.methods({
  'articles.pullList'() {

      return Articles.find({}, {fields: {title:1, dominant_emotion:1, emotional_sentence:1, url:1}}).fetch();
  }
});
