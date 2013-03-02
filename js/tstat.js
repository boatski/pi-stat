 $(document).ready(function() 
 {
 	$('.success').hide();

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