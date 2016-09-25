import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';

import './article.html';

Template.article.helpers({
  hasEmotionalSentence(){
    return this.emotional_sentence !== "No content found.";
  }
});

Template.article.events({
  
});