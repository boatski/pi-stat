<!DOCTYPE html>

  <?php

    ini_set('display_errors',1);
    error_reporting(E_ALL);

    $db = new PDO('sqlite:db/pi-stat.db') or die("fail to connect db");

    $result = $db->query("SELECT * FROM Schedule;");

    $data = array();

    foreach ($result as $row) {

      $day = $row['Day'];
      $startTime = $row['StartTime'];
      $stopTime = $row['StopTime'];

      // Split hours and minutes
      $startTimeSplit = explode(':', $startTime);
      $stopTimeSplit = explode(':', $stopTime);

      $startPeriod = '';
      $stopPeriod = '';

      // Convert to 12 hour clock and set period.
      if (intval($startTimeSplit[0] == 0))
      {
        $startPeriod = 'am';
        $startTimeSplit[0] = 12;
      } else if (intval($startTimeSplit[0] > 11))
      {
        $startPeriod = 'pm';
        if (intval($startTimeSplit[0]) > 12) $startTimeSplit[0] = intval($startTimeSplit[0]) - 12;
      } else
      {
        $startPeriod = 'am';
      }// end if

      // Combine hours and minutes
      $startTime = $startTimeSplit[0] . ':' . $startTimeSplit[1];

      if (intval($stopTimeSplit[0]) == 24)
      {
        $stopPeriod = 'am';
        if (intval($stopTimeSplit[0]) > 12) $stopTimeSplit[0] = intval($stopTimeSplit[0]) - 12;
      } else if (intval($stopTimeSplit[0]) > 11)
      {
        $stopPeriod = 'pm';
        if (intval($stopTimeSplit[0]) > 12) $stopTimeSplit[0] = intval($stopTimeSplit[0]) - 12;
      } else
      {
        $stopPeriod = 'am';
      }// end if

      // Combine hours and minutes
      $stopTime = $stopTimeSplit[0] . ':' . $stopTimeSplit[1];

      $data[$day . '-start-time'] = $startTime;
      $data[$day . '-stop-time'] = $stopTime;
      $data[$day . '-start-period'] = $startPeriod;
      $data[$day . '-stop-period'] = $stopPeriod;

    }// end

    $db = null;
  ?>

<!-- paulirish.com/2008/conditional-stylesheets-vs-css-hacks-answer-neither/ -->
<!--[if lt IE 7]> <html class="no-js lt-ie9 lt-ie8 lt-ie7" lang="en"> <![endif]-->
<!--[if IE 7]>    <html class="no-js lt-ie9 lt-ie8" lang="en"> <![endif]-->
<!--[if IE 8]>    <html class="no-js lt-ie9" lang="en"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js" lang="en"> <!--<![endif]-->
<head>
  <meta charset="utf-8" />

  <!-- Set the viewport width to device width for mobile -->
  <meta name="viewport" content="width=device-width" />

  <title>Pi-Stat</title>
  
  <!-- Included CSS Files (Compressed) -->
  <link rel="stylesheet" href="css/foundation/foundation.min.css">
  <link rel="stylesheet" href="css/foundation/app.css">
  <link rel="stylesheet" href="css/jquery-ui.css">
  <link rel="stylesheet" href="css/main.css">

  <script src="js/foundation/modernizr.foundation.js"></script>

  <!-- IE Fix for HTML5 Tags -->
  <!--[if lt IE 9]>
    <script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script>
  <![endif]-->

</head>
<body>


  <div class="row">
    <div class="twelve columns">
      <h2>Pi-Stat</h2>
  		<ul class="nav-bar">
  		  <li class=""><a href="index.php">Thermostat</a></li>
        <li class="active"><a href="schedule.php">Schedule</a></li>
  		  <li class=""><a href="history.php">History</a></li>
  		  <li class=""><a href="alarms.php">Alarms</a></li>
  		</ul>
    </div>
  </div>
  <div id="test"></div>
  <form method="POST" action="ajax/updateSchedule.php" id="schedule">
    <div class="row collapse">
      <div class="twelve columns centered">

        <div class="row collapse">
          <div class="date-headers one columns">
            <!-- empty, offset-by-one doesn't add margin-right -->
          </div>

          <div class="date-headers one columns">
            Mon
          </div>

          <div class="date-headers one columns">
            Tues
          </div>

          <div class="date-headers one columns">
            Weds
          </div>

          <div class="date-headers one columns">
            Thurs
          </div>

          <div class="date-headers one columns">
            Fri
          </div>

          <div class="date-headers one columns">
            Sat
          </div>

          <div class="date-headers one columns end">
            Sun
          </div>
        </div><!-- end row -->
        
        <div class="row collapse">
          <div class="schedule-times one columns">
            <ul>
              <li>3:00am</li>
              <li>6:00am</li>
              <li>9:00am</li>
              <li>12:00pm</li>
              <li>3:00pm</li>
              <li>6:00pm</li>
              <li>9:00pm</li>
          </div>
          <div class="not-resizable one columns">
            <div class="resizable" id="monday">
            </div>
          </div><!-- Monday -->

          <div class="not-resizable one columns">
            <div class="resizable" id="tuesday">
            </div>
          </div><!-- Tuesday -->

          <div class="not-resizable one columns">
            <div class="resizable" id="wednesday">
            </div>
          </div><!-- Wednesday -->

          <div class="not-resizable one columns">
            <div class="resizable" id="thursday">
            </div>
          </div><!-- Thursday -->

          <div class="not-resizable one columns">
            <div class="resizable" id="friday">
            </div>
          </div><!-- Friday -->

          <div class="not-resizable one columns">
            <div class="resizable" id="saturday">
            </div>
          </div><!-- Saturday -->

          <div class="not-resizable one columns end">
            <div class="resizable" id="sunday">
            </div>
          </div><!-- Sunday -->
        </div><!-- end row -->

        <div class="row collapse">
          <div class="time-footers one columns">

          </div>

          <div class="time-footers one columns">
            <span id="monday-start-times"><?php echo $data['monday-start-time'] ?></span><span id="monday-start-period"><?php echo $data['monday-start-period'] ?></span>
          </div>

          <div class="time-footers one columns">
            <span id="tuesday-start-times"><?php echo $data['tuesday-start-time'] ?></span><span id="tuesday-start-period"><?php echo $data['tuesday-start-period'] ?></span>
          </div>

          <div class="time-footers one columns">
            <span id="wednesday-start-times"><?php echo $data['wednesday-start-time'] ?></span><span id="wednesday-start-period"><?php echo $data['wednesday-start-period'] ?></span>
          </div>

          <div class="time-footers one columns">
            <span id="thursday-start-times"><?php echo $data['thursday-start-time'] ?></span><span id="thursday-start-period"><?php echo $data['thursday-start-period'] ?></span>
          </div>

          <div class="time-footers one columns">
            <span id="friday-start-times"><?php echo $data['friday-start-time'] ?></span><span id="friday-start-period"><?php echo $data['friday-start-period'] ?></span>
          </div>

          <div class="time-footers one columns">
            <span id="saturday-start-times"><?php echo $data['saturday-start-time'] ?></span><span id="saturday-start-period"><?php echo $data['saturday-start-period'] ?></span>
          </div>

          <div class="time-footers one columns end">
            <span id="sunday-start-times"><?php echo $data['sunday-start-time'] ?></span><span id="sunday-start-period"><?php echo $data['sunday-start-period'] ?></span>
          </div>
        </div><!-- end row -->

        <div class="row collapse">
          <div class="time-footers one columns">
            
          </div>

          <div class="time-footers one columns">
            <span id="monday-stop-times"><?php echo $data['monday-stop-time'] ?></span><span id="monday-stop-period"><?php echo $data['monday-stop-period'] ?></span>
          </div>

          <div class="time-footers one columns">
            <span id="tuesday-stop-times"><?php echo $data['tuesday-stop-time'] ?></span><span id="tuesday-stop-period"><?php echo $data['tuesday-stop-period'] ?></span>
          </div>

          <div class="time-footers one columns">
            <span id="wednesday-stop-times"><?php echo $data['wednesday-stop-time'] ?></span><span id="wednesday-stop-period"><?php echo $data['wednesday-stop-period'] ?></span>
          </div>

          <div class="time-footers one columns">
            <span id="thursday-stop-times"><?php echo $data['thursday-stop-time'] ?></span><span id="thursday-stop-period"><?php echo $data['thursday-stop-period'] ?></span>
          </div>

          <div class="time-footers one columns">
            <span id="friday-stop-times"><?php echo $data['friday-stop-time'] ?></span><span id="friday-stop-period"><?php echo $data['friday-stop-period'] ?></span>
          </div>

          <div class="time-footers one columns">
            <span id="saturday-stop-times"><?php echo $data['saturday-stop-time'] ?></span><span id="saturday-stop-period"><?php echo $data['saturday-stop-period'] ?></span>
          </div>

          <div class="time-footers one columns end">
            <span id="sunday-stop-times"><?php echo $data['sunday-stop-time'] ?></span><span id="sunday-stop-period"><?php echo $data['sunday-stop-period'] ?></span>
          </div>
        </div><!-- end row -->

      </div><!-- end col -->
    </div><!-- end row -->
    <div class="schedule-submit row collapse">
      <div class="twelve columns">
          <input type="submit" name="submit" id="submit" class="button">
      </div>
    </div><!-- end row -->
  </form>
  
  
  <!-- Included JS Files (Compressed) -->
  <script src="js/foundation/jquery.js"></script>
  <script src="js/foundation/foundation.min.js"></script>


  <script src="js/jquery-ui.js"></script>
  <script src="js/schedule.js"></script>
  
  <!-- Initialize JS Plugins -->
  <script src="js/foundation/app.js"></script>
  
</body>
</html>
