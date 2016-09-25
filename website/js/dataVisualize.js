// Load the Visualization API and the corechart package.
google.charts.load('current', { 'packages': ['bar'] });

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(drawChart);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function drawChart() {

    var date = new Date();

    // Create the data table.
    var data = new google.visualization.arrayToDataTable([
        ["Day",                        "Aggressive", "Happy",   "Sad"],
        ["today", "99",         "87",      "01"],
        ["Yesterday", "95",         "87",      "10"],
        [date, "80",         "87",      "20"],
        [date, "70",         "87",      "50"],
        [date, "30",         "90",      "30"]
    ]);

    // Set chart options
    var options = {
        chart:{
            title: "Mood in the last 5 days"
        },
        bars: 'vertical',
        hAxis: {format: 'decimal'},
        width: 600,
        height: 800,
        colors: ['#1b9e77', '#d95f02', '#7570b3']
    };

    // Instantiate and draw our chart, passing in some options.
    var chart = new google.charts.Bar(document.getElementById('main'));
    chart.draw(data, options);
}