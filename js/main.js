 $(document).ready(function() 
 {
 
 	setDraggableAndResizable();


 	function setDraggableAndResizable()
 	{

		$('.resizable').draggable({
			appendTo: 'body',
			containment: '.not-resizable',
			axis: 'y',
			grid: [15,15]});

		$('.resizable').resizable({
			handles: 'n,s', 
			ghost: false, 
			animate: false,
			maxHeight: 360,
			minHeight: 60,
			grid: [15,15]});
	}
 
 
 });