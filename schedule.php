<!DOCTYPE html>

  <?php

    /*ini_set('display_errors',1);
    error_reporting(E_ALL);

    $db = new PDO('sqlite:db/pi-stat.db') or die("fail to connect db");

    $result = $db->query('SELECT * FROM Thermostat');

    foreach ($result as $row) {

      $occCool = $row['OccupiedCool'];
      $unoccCool = $row['UnoccupiedCool'];
      $occHeat = $row['OccupiedHeat'];
      $unoccHeat = $row['UnoccupiedHeat'];

      $db = null;*/
    }
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

  <div class="row">
    <div class="twelve columns">

      <div class="row collapse">
        <div class="date-headers offset-by-one one columns">
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
        <div class="date-headers one columns offset-by-one">
          <span id="monday-start-times">7:00</span><span id="monday-start-period">am</span>
        </div>

        <div class="date-headers one columns">
          <span id="tuesday-start-times">7:00</span><span id="tuesday-start-period">am</span>
        </div>

        <div class="date-headers one columns">
          <span id="wednesday-start-times">7:00</span><span id="wednesday-start-period">am</span>
        </div>

        <div class="date-headers one columns">
          <span id="thursday-start-times">7:00</span><span id="thursday-start-period">am</span>
        </div>

        <div class="date-headers one columns">
          <span id="friday-start-times">7:00</span><span id="friday-start-period">am</span>
        </div>

        <div class="date-headers one columns">
          <span id="saturday-start-times">7:00</span><span id="saturday-start-period">am</span>
        </div>

        <div class="date-headers one columns end">
          <span id="sunday-start-times">7:00</span><span id="sunday-start-period">am</span>
        </div>
      </div><!-- end row -->

      <div class="row collapse">
        <div class="date-headers one columns offset-by-one">
          <span id="monday-stop-times">7:00</span><span id="monday-stop-period">pm</span>
        </div>

        <div class="date-headers one columns">
          <span id="tuesday-stop-times">7:00</span><span id="tuesday-stop-period">pm</span>
        </div>

        <div class="date-headers one columns">
          <span id="wednesday-stop-times">7:00</span><span id="wednesday-stop-period">pm</span>
        </div>

        <div class="date-headers one columns">
          <span id="thursday-stop-times">7:00</span><span id="thursday-stop-period">pm</span>
        </div>

        <div class="date-headers one columns">
          <span id="friday-stop-times">7:00</span><span id="friday-stop-period">pm</span>
        </div>

        <div class="date-headers one columns">
          <span id="saturday-stop-times">7:00</span><span id="saturday-stop-period">pm</span>
        </div>

        <div class="date-headers one columns end">
          <span id="sunday-stop-times">7:00</span><span id="sunday-stop-period">pm</span>
        </div>
      </div><!-- end row -->

    </div><!-- end col -->
  </div><!-- end row -->
  
  
  <!-- Included JS Files (Compressed) -->
  <script src="js/foundation/jquery.js"></script>
  <script src="js/foundation/foundation.min.js"></script>


  <script src="js/jquery-ui.js"></script>
  <script src="js/schedule.js"></script>
  
  <!-- Initialize JS Plugins -->
  <script src="js/foundation/app.js"></script>
  
</body>
</html>
