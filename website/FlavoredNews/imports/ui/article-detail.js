import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';
import {FlowRouter} from 'meteor/kadira:flow-router';

import { Articles } from '../api/articles.js';


import './article-detail.html';

Template.articleDetail.onCreated(function(){

});

Template.articleDetail.helpers({
    article(){
        var _myid = FlowRouter.getParam("_id");
        var item = Articles.findOne(new Mongo.ObjectID(_myid));
        console.log(item);
        return item;
    }
});
