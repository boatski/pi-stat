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
                console.log(result);
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
                categories: arrayData['date'],
                labels: {
                    rotation: -45,
                    align: 'right'
                }
            },
            yAxis: {
                title: {
                    text: 'Thermostat'
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
                    stacking: 'normal',
                    dataLabels: {
                        enabled: true,
                        color: (Highcharts.theme && Highcharts.theme.dataLabelsColor) || 'white',
                        formatter: function() {
                            if (this.y > 0) {
                                return this.series.name[0];
                            }
                        }
                    }
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
        var dateTime = [];

        $.each(data, function(index, element) {
            indoorTemps.push(parseFloat(element.IndoorTemperature));
            indoorHums.push(parseFloat(element.IndoorHumidity));
            outdoorTemps.push(parseFloat(element.OutdoorTemperature));
            outdoorHums.push(parseFloat(element.OutdoorHumidity));
            fan.push(parseFloat(element.Fan*10));
            heat.push(parseFloat(element.Heat*10));
            cool.push(parseFloat(element.Cool*10));
            dateTime.push(element.Date);
        });

        formattedDateTime = formatDateTime(dateTime);

        var array = {'indoorTemps':indoorTemps, 'indoorHums':indoorHums, 'outdoorTemps':outdoorTemps, 'outdoorHums':outdoorHums,
                        'fan':fan, 'heat':heat, 'cool':cool, 'date':formattedDateTime};
        return array;
    }// end buildIndoorTemperatureArray

    function formatDateTime(data) {
        for (var i = 0; i < data.length; i++) {
            var splitData = data[i].split(':');
            data[i] = splitData[0] + ":00";
            splitData = data[i].split(' ');
            data[i] = splitData[1];
        }
        return data;
    }
});