 $(document).ready(function() 
 {
 
 	getThermostatData();

    function getThermostatData() {
        $.ajax({
            type: 'POST',
            url: 'ajax/getThermostatData.php',
            dataType: 'json',
            error: function(xhr, status, error) {
                alert(status + " " + error);
            },
            success: function(result) {
                $('#indoorTemp').html(result.response.IndoorTemperature);
                $('#indoorHum').html(result.response.IndoorHumidity);
                $('#outdoorTemp').html(result.response.OutdoorTemperature);
                $('#outdoorHum').html(result.response.OutdoorHumidity);
                $('#fan').html(result.response.Fan);
                $('#heat').html(result.response.Heat);
                $('#cool').html(result.response.Cool);
            },
        });
    }// end getHistoryData
 
 });