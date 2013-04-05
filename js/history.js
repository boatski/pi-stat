 $(document).ready(function() 
 {
    getHistoryData();

    function getHistoryData() {
        $.ajax({
            type: 'POST',
            url: 'ajax/getHistoryData.php',
            dataType: 'json',
            error: function(xhr, status, error) {
                alert(status);
            },
            success: function(result) {
                displayHistory(result.response);
            },
        });
    }// end getHistoryData

    function displayHistory(data) {
        // Build arrays for highcarts data
        var arrayData = buildArray(data);

     	$('#graph').highcharts({
            chart: {
                type: 'column',
                marginBottom: 75
            },
            title: {
                text: 'Pi-Stat 24 Hour Datalog',
                x: -20 //center
            },
            xAxis: {
                categories: ['1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00', '8:00', '9:00', '10:00', '11:00', '12:00',
                '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '24:00'],
                labels: {
                    rotation: -45,
                    align: 'right'
                }
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
                formatter: function() {
                    if (this.series.type === 'column' && this.y > 0) {
                        return '<b>' + this.series.name + ':</b> On';
                    } else if (this.series.type === 'line' && (this.series.name === 'Indoor Temperature' || this.series.name === 'Outdoor Temperature')) {
                        return '<b>' + this.series.name + ':</b> ' + this.y + '°F';
                    } else {
                        return '<b>' + this.series.name + ':</b> ' + this.y + '%';
                    }
                }
            },
            plotOptions: {
                column: {
                    stacking: 'normal'
                }
            },
            legend: {
                borderWidth: 0
            },
            series: [{
                name: 'Fan',
                data: arrayData['fan']
            }, {
                name: 'Heat',
                data: arrayData['heat']
            }, {
                name: 'Cool',
                data: arrayData['cool']
            }, {
                type: 'line',
                name: 'Indoor Temperature',
                data: arrayData['indoorTemps']
            }, {
                type: 'line',
                name: 'Indoor Humidity',
                data: arrayData['indoorHums']
            }, {
                type: 'line',
                name: 'Outdoor Temperature',
                data: arrayData['outdoorTemps']
            }, {
                type: 'line',
                name: 'Outdoor Humidity',
                data: arrayData['outdoorHums']
            }]
         });
    }// end displayHistory

    function buildArray(data) {
        var indoorTemps = [];
        var indoorHums = [];
        var outdoorTemps = [];
        var outdoorHums = [];
        var fan = [];
        var heat = [];
        var cool = [];

        $.each(data, function(index, element) {
            indoorTemps.push(parseFloat(element.IndoorTemperature));
            indoorHums.push(parseFloat(element.IndoorHumidity));
            outdoorTemps.push(parseFloat(element.OutdoorTemperature));
            outdoorHums.push(parseFloat(element.OutdoorHumidity));
            fan.push(parseFloat(element.Fan*10));
            heat.push(parseFloat(element.Heat*10));
            cool.push(parseFloat(element.Cool*10));
        });

        var array = {'indoorTemps':indoorTemps, 'indoorHums':indoorHums, 'outdoorTemps':outdoorTemps, 'outdoorHums':outdoorHums,
                        'fan':fan, 'heat':heat, 'cool':cool};
        return array;
    }// end buildIndoorTemperatureArray
});