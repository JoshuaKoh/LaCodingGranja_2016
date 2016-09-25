// Load the Visualization API and the corechart package.
google.charts.load('current', { 'packages': ['bar'] });

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawChart() {

    //ASSUMING WE HAVE THE INFO FROM THE LAST 5 ITEMS
    var obj = {} //Magical object 

    $.getJSON("lastFiveNews2.json", function(json) {
        obj = json; // this will show the info it in firebug console

        console.log(json);

        //Create the data table.
        var data = new google.visualization.arrayToDataTable([
            ["Title", "Anger", "Disgust", "Fear", "Joy"],
            [obj[0].title, obj[0].anger, obj[0].disgust, obj[0].fear, obj[0].joy],
            [obj[1].title, obj[1].anger, obj[1].disgust, obj[1].fear, obj[1].joy],
            [obj[2].title, obj[2].anger, obj[2].disgust, obj[2].fear, obj[2].joy],
            [obj[3].title, obj[3].anger, obj[3].disgust, obj[3].fear, obj[3].joy],
            [obj[4].title, obj[4].anger, obj[4].disgust, obj[4].fear, obj[4].joy]
        ]);

        // Set chart options
        var options = {
            chart:{
                title: "Mood In The Last 5 News Items"
            },
            bars: 'vertical',
            hAxis: {format: 'decimal'},
            width: 800,
            height: 800,
            colors: ['red', 'orange', 'blue', 'green']
        };

        // Instantiate and draw our chart, passing in some options.
        var chart = new google.charts.Bar(document.getElementById('main'));
        chart.draw(data, options);
    });

    
}