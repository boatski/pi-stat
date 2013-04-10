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
                console.log(result);
                $('#indoorTemp').html(result.response.IndoorTemperature);
                //displayHistory(result.response);
            },
        });
    }// end getHistoryData
 
 });