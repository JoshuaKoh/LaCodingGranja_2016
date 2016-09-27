import { Meteor } from 'meteor/meteor';
import { Mongo } from 'meteor/mongo';

export const Articles = new Mongo.Collection('articles');

if(Meteor.isServer) {
    Meteor.publish('articles', function() {
        Articles.find();
    })
}
