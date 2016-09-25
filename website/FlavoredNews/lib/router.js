import { FlowRouter } from 'meteor/kadira:flow-router';
import { BlazeLayout } from 'meteor/kadira:blaze-layout';



FlowRouter.route('/article/:_id', {
    action: function(params, queryParams) {
        BlazeLayout.render('mainLayout', {main: 'articleDetail'});
        console.log("Going to item " + params._id)
    }
});

FlowRouter.route('/', {
    action: function(params, queryParams) {
        BlazeLayout.render('mainLayout', {main: 'articleList'});
        console.log("Yeah! We are on the post:" + params.postId);
        console.log("Home!");
    }
});

FlowRouter.route('/data_visualization', {
    action: function(params, queryParams){
        BlazeLayout.render('mainLayout', {main: 'dataVisualization'});
    }
});