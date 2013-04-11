 $(document).ready(function() 
 {
 	$('.success').hide();
 
 	getThermostatData();

	$("#thermostat").submit( function() {
		var formData = $('#thermostat').serialize();

		// Update Thermostat table with new form values.
	    $.ajax( {
	      type: "POST",
	      url: $("#thermostat").attr( 'action' ),
	      data: formData,
	      fail: function(xhr, status, error) {
			  var err = eval("(" + xhr.responseText + ")");
			  alert(err.Message);
			},
	      success: function( response ) {
	      	$('.success').fadeIn('slow', function() {
	      		$(this).fadeOut('slow');
	      	});
	      }
	    });
	    return false;
	  } );

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
                /*$('input[name=occupied-cool]').val();
                $('input[name=unoccupied-cool]').val();
                $('input[name=occupied-heat]').val();
                $('input[name=unoccupied-heat]').val();
                $('input[name=outdoor-lockout]').val();*/
            },
        });
    }// end getHistoryData
 
 });