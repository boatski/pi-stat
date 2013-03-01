 $(document).ready(function() 
 {
 	$('.success').hide();

 	$.getJSON("../pi-stat/json/sensor.py", function(data) {

        console.log("echo "+ data);
        //alert(data); //uncomment this for debug
        //alert (data.item1+" "+data.item2+" "+data.item3); //further debug
        $('#test').text(data);
    });

    /*$.ajax({
                 type:"GET",
                 url:"../pi-stat/json/sensor.py",
                 data: {},

                 success: function(b){
                    b = jQuery.parseJSON(b);

                    console.log(b);            

                    }
            });*/

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
 
 
 });