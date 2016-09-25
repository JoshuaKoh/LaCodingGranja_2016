import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';

import './article.html';

Template.article.helpers({
  
  hasEmotionalSentence(){
    return this.emotional_sentence !== "No content found.";
  },

  shouldShow(){
    return !!Session.get("filter_"+this.dominant_emotion);
  }
});

Template.article.events({
  'click .article-item'(event){
    window.location = "/article/"+this._id;
  }
  
});