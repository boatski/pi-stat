 $(document).ready(function() 
 {
 
 	setDraggableAndResizable();


 	function setDraggableAndResizable()
 	{
 		var width = $('.resizable').width();
 		console.log(width);

		$('.resizable').draggable({
			appendTo: 'body',
			containment: 'parent',
			axis: 'y',
			grid: [15,15],
			drag: function(event, ui)
			{
				updateTimes(this);
			}});

		$('.resizable').resizable({
			handles: 'n,s', 
			containment: 'parent',
			ghost: false, 
			animate: false,
			maxHeight: 360,
			minHeight: 60,
			grid: [15,15],
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
		var barDay = $(bar).attr('id');
		console.log(barDay);
	}// end updateTimes(bar)
 
 
 });