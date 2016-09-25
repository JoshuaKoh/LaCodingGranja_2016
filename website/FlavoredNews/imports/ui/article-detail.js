import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';
import {FlowRouter} from 'meteor/kadira:flow-router';

import { Articles } from '../api/articles.js';


import './article-detail.html';

Template.articleDetail.onCreated(function(){

});

Template.articleDetail.helpers({
    article(){
        return Articles.findOne(FlowRouter.getParam("_id"));
    }
});
