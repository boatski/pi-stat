 $(document).ready(function() 
 {
 

 /********************
  On Page Load
 ********************/

  setDraggableAndResizable();
  setBarPositions();

  function setBarPositions()
  {
    var data = getScheduleTimes();
    console.log(data);
    var days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];

    for (var i = 0; i < days.length; i++)
    {
      var bar = days[i];

      var startTime = data[bar + '-start-time'];
      var startTimeSplit = startTime.split(':');

      var stopTime = data[bar + '-stop-time'];
      var stopTimeSplit = stopTime.split(':');

      // Convert hours to minutes
      var startTimeHours = startTimeSplit[0];
      var startTimeMinutes = startTimeSplit[1];
      var startTimeInMinutes = parseInt(startTimeHours*60) + parseInt(startTimeMinutes);

      var stopTimeHours = stopTimeSplit[0];
      var stopTimeMinutes = stopTimeSplit[1];
      var stopTimeInMinutes = parseInt(stopTimeHours*60) + parseInt(stopTimeMinutes);

      // Calculate and set start position
      var barTop = (startTimeInMinutes / 30) * 10;
      $('#' + bar).css('top', barTop);

      // Calculate and set bar height
      var onTimeInMinutes = stopTimeInMinutes - startTimeInMinutes;
      var barHeight = (onTimeInMinutes / 30) * 10;
      $('#' + bar).css('height', barHeight);
    }// end for
  }// end setBarPositions()

  /* 
    Allows the green bars to be draggable and resizable within the gray bar.
    10px = 30 mins, 480px = 24 hours
  */
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

/********************
  Schedule Time Changes
********************/

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

  // Sets the time to am or pm.
  function checkPeriod(hour)
  {
    if (hour < 12 || hour == 24)
    {
      return 'am';
    } else
    {
      return 'pm';
    }
  }// end checkPeriod(hour)

  // Adds a second zero to a number if it is < 10
  function pad2(number) 
  {
      return (number < 10 ? '0' : '') + number;
  }

  /*
  Called when the schedule submit button is clicked. Schedule times are grabbed and
  then the database is updated.
  */
  $("#schedule").submit( function() {
    var scheduleData = getScheduleTimes();

    // Update Thermostat table with new form values.
    $.ajax( {
      type: "POST",
      url: $("#schedule").attr( 'action' ),
      data: scheduleData,
      fail: function(xhr, status, error) {
      var err = eval("(" + xhr.responseText + ")");
      alert(err.Message);
      },
      success: function( response ) {
        $('#test').html(response);
        console.log("Success");
      }
    });
    return false;
  });

  function getScheduleTimes()
  {
    var days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'];
    var data = {};
    for (var i = 0; i < days.length; i++)
    {
      var startTime = $('#' + days[i] + '-start-times').text();
      var stopTime = $('#' + days[i] + '-stop-times').text();

      var startPeriod = $('#' + days[i] + '-start-period').text();
      var stopPeriod = $('#' + days[i] + '-stop-period').text();

      // Split hours and minutes
      var startTimeSplit = startTime.split(':');
      var stopTimeSplit = stopTime.split(':');

      // Convert to 24 hour time
      if (parseInt(startTimeSplit[0]) === 12 && startPeriod === 'am')
      {
        startTimeSplit[0] = 0;
      } else if (parseInt(startTimeSplit[0]) > 12 && startPeriod === 'pm')
      {
        startTimeSplit[0] = parseInt(startTimeSplit[0]) + 12;
      }// end if

      if (parseInt(stopTimeSplit[0]) === 12 && stopPeriod === 'am')
      {
        stopTimeSplit[0] = parseInt(stopTimeSplit[0]) + 12;
      } else if (parseInt(stopTimeSplit[0]) !== 12 && stopPeriod === 'pm')
      {
        stopTimeSplit[0] = parseInt(stopTimeSplit[0]) + 12;
      }// end if

      // Combine hour and minutes
      startTime = startTimeSplit[0] + ':' + startTimeSplit[1];
      stopTime = stopTimeSplit[0] + ':' + stopTimeSplit[1];

      data[days[i] + '-start-time'] = startTime;
      data[days[i] + '-stop-time'] = stopTime;

    }// end for
    return data;
  }// end getScheduleTimes()
 
 });