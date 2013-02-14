 $(document).ready(function() 
 {
 
 	setDraggableAndResizable();


 	function setDraggableAndResizable()
 	{
 		var width = $('.resizable').width();

		$('.resizable').draggable({
			appendTo: 'body',
			containment: 'parent',
			axis: 'y',
			grid: [10,10],
			drag: function(event, ui)
			{
				updateTimes(this);
			}});

		$('.resizable').resizable({
			handles: 'n,s', 
			containment: 'parent',
			ghost: false, 
			animate: false,
			maxHeight: 480,
			minHeight: 20,
			grid: [10,10],
			start: function(event, ui)
			{
				width = $('.resizable').width();
			},
			resize: function(event, ui)
			{
				updateTimes(this);
				$('.resizable').css('width', width);
			},
			stop: function(event, ui)
			{
				$('.resizable').css('width', width);
			}});
	}// end setDraggableAndResizable

	function updateTimes(bar)
	{
		var barDay = '#' + $(bar).attr('id'); // green bar
		var barDayStartTimes = barDay + '-start-times'; // bottom hours:minute
		var barDayStopTimes = barDay + '-stop-times'; // bottom hours:minute

		var barHeight = $(barDay).height(); // height of green bar
		var barTop = $(barDay).css('top').replace('px',''); // value of css top
		var timeInMinutes = (barHeight / 10) * 30;

		// On time
		var startTimeInMinutes = Math.floor((barTop/10) * 30);
		var startHours = Math.floor(startTimeInMinutes / 60);
		var startMinutes = startTimeInMinutes % 60;


		// Off time
		var stopTimeInMinutes = timeInMinutes + startTimeInMinutes;
		var stopHours = Math.floor(stopTimeInMinutes / 60);
		var stopMinutes = stopTimeInMinutes % 60;

		$(barDayStartTimes).text(startHours + ':' + pad2(startMinutes));
		$(barDayStopTimes).text(stopHours + ':' + pad2(stopMinutes));
	}// end updateTimes(bar)

	function pad2(number) {
   
    	return (number < 10 ? '0' : '') + number;
   
	}

	$("#thermostat").submit( function() {
		var formData = $('#thermostat').serialize();

		console.log("Click");
	    $.ajax( {
	      type: "POST",
	      url: $("#thermostat").attr( 'action' ),
	      //url: ".",
	      data: formData,
	      success: function( response ) {
	      	console.log("Success");
	      }
	    });
	    return false;
	  } );
 
 
 });