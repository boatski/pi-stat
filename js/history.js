 $(document).ready(function() 
 {
 	$('#graph').highcharts({
        chart: {
            type: 'line',
            marginRight: 175,
            marginBottom: 25
        },
        title: {
            text: 'Pi-Stat 24 Hour Datalog',
            x: -20 //center
        },
        subtitle: {
            text: '',
            x: -20
        },
        xAxis: {
            categories: ['1:00', '2:00', '3:00', '4:00', '5:00', '6:00',
                '7:00', '8:00', '9:00', '10:00', '11:00', '12:00']
        },
        yAxis: {
            title: {
                text: 'Temperature (°F)'
            },
            plotLines: [{
                value: 0,
                width: 1,
                color: '#808080'
            }]
        },
        tooltip: {
            valueSuffix: '°F'
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            x: -10,
            y: 100,
            borderWidth: 0
        },
        series: [{
            name: 'Indoor Temperature',
            data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
        }, {
            name: 'Indoor Humidity',
            data: [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8, 24.1, 20.1, 14.1, 8.6, 2.5]
        }, {
            name: 'Outdoor Temperature',
            data: [-0.9, 0.6, 3.5, 8.4, 13.5, 17.0, 18.6, 17.9, 14.3, 9.0, 3.9, 1.0]
        }, {
            name: 'Outdoor Humidity',
            data: [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6, 14.2, 10.3, 6.6, 4.8]
        }]
     });
});