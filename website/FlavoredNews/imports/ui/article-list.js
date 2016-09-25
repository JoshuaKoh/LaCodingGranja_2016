import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';
import { ReactiveDict } from 'meteor/reactive-dict';

import { Articles } from '../api/articles.js';

import './article.js';
import './article-list.html';


Template.articleList.onCreated(function bodyOnCreated() {
  this.state = new ReactiveDict();
  Session.set("filter_joy", true);
  Session.set("filter_anger", true);
  Session.set("filter_sadness", true);
  Session.set("filter_disgust", true);
  Session.set("filter_fear", true);
});

Template.articleList.helpers({
  articles() {
      return Articles.find({}, {fields: {title:1, dominant_emotion:1, emotional_sentence:1, url:1}}).fetch();
  }
});

Template.articleList.events({
  'click .filter-check'(event, template) {
    
    Session.set("filter_joy", $('#test1').is(":checked"));
    Session.set("filter_anger", $('#test2').is(":checked"));
    Session.set("filter_sadness", $('#test3').is(":checked"));
    Session.set("filter_disgust", $('#test4').is(":checked"));
    Session.set("filter_fear", $('#test5').is(":checked"));
  }
});
