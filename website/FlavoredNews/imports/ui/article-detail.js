import { Meteor } from 'meteor/meteor';
import { Template } from 'meteor/templating';
import {FlowRouter} from 'meteor/kadira:flow-router';

import { Articles } from '../api/articles.js';


import './article-detail.html';

Template.articleDetail.onCreated(function(){

    google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
      var data = google.visualization.arrayToDataTable([
        ["Emotion", "Percentage"],
        ["Anger", this.anger],
        ["Joy", this.joy],
        ["Fear", this.fear],
        ["Disgust", this.disgust],
        ["Sadness", this.sadness]
      ]);

      var view = new google.visualization.DataView(data);

      var options = {
        title: "Emotion of the news",
        width: 600,
        height: 400,
        bar: {groupWidth: "95%"}
      };
      var chart = new google.visualization.BarChart(document.getElementById("MoodGraph"));
      chart.draw(view, options);
  }
});

Template.articleDetail.helpers({
    article(){
        var _myid = FlowRouter.getParam("_id");
        var item = Articles.findOne(new Mongo.ObjectID(_myid));
        console.log(item);
        return item;
    }
});
