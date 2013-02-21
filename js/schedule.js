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
    var barDayStartTimes = barDay + '-start-times'; // start hours:minute
    var barDayStopTimes = barDay + '-stop-times'; // stop hours:minute
    var barStartPeriod = barDay + '-start-period'; // start am/pm
    var barStopPeriod = barDay + '-stop-period'; // stop am/pm

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

    $(barStartPeriod).text(checkPeriod(startHours));
    $(barStopPeriod).text(checkPeriod(stopHours));

    if (startHours == 0)
    {// Change start hours to 12am if it is 0
      startHours = 12;
    }
    else if (startHours > 12)
    {// Convert to a 12 hour time
       startHours -= 12;
    }// end if

    // Convert to a 12 hour time
    if (stopHours > 12) stopHours -= 12;

    $(barDayStartTimes).text(startHours + ':' + pad2(startMinutes));
    $(barDayStopTimes).text(stopHours + ':' + pad2(stopMinutes));
  }// end updateTimes(bar)

  function checkPeriod(hour)
  {
    if (hour < 12 || hour == 24)
    {
      return 'am';
    } else
    {
      return 'pm';
    }
  }

  function pad2(number) 
  {
      return (number < 10 ? '0' : '') + number;
  }

  /*$("#thermostat").submit( function() {
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
          console.log("Success");
        }
      });
      return false;
    } );*/
 
 
 });