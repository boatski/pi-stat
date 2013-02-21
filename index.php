<!DOCTYPE html>

  <?php

    ini_set('display_errors',1);
    error_reporting(E_ALL);

    $db = new PDO('sqlite:db/pi-stat.db') or die("fail to connect db");

    $result = $db->query('SELECT * FROM Thermostat');

    foreach ($result as $row) {

      $occCool = $row['OccupiedCool'];
      $unoccCool = $row['UnoccupiedCool'];
      $occHeat = $row['OccupiedHeat'];
      $unoccHeat = $row['UnoccupiedHeat'];

      $db = null;
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
  		  <li class="active"><a href="index.php">Thermostat</a></li>
        <li class=""><a href="schedule.php">Schedule</a></li>
  		  <li class=""><a href="history.php">History</a></li>
  		  <li class=""><a href="alarms.php">Alarms</a></li>
  		</ul>
    </div>
  </div>

  <form method="POST" action="ajax/updateThermostat.php" id="thermostat">

    <div class="form-elements row">
      <div class="six columns">
        <div class="row collapse">
          <div class="offset-by-two three columns">
            <label>Occupied</label>
          </div>
          <div class="offset-by-one three columns end">
            <label>Unoccupied</label>
          </div>
        </div>
      </div>
    </div><!-- end row -->

    <div class="form-elements row">
      <div class="six columns">
        <div class="row collapse">
          <div class="two mobile-two column">
            <label>Cooling</label>
          </div>
          <div class="two mobile-one columns">
            <input type="number" value="<?php echo $occCool ?>" min="60" max="80" placeholder="72" name="occupied-cool" id="occupied-cool" required>
            <span class="error" aria-live="polite"></span>
          </div>
          <div class="one mobile-one columns">
            <span class="postfix">&deg;F</span>
          </div>

          <div class="two mobile-one columns offset-by-one">
            <input type="number" value="<?php echo $unoccCool ?>" min="60" max="80" placeholder="72" name="unoccupied-cool" id="unoccupied-cool" required>
            <span class="error" aria-live="polite"></span>
          </div>
          <div class="one mobile-one columns end">
            <span class="postfix">&deg;F</span>
          </div>
        </div>
      </div>
    </div><!-- end row -->

    <div class="form-elements row">
      <div class="six columns">
        <div class="row collapse">
          <div class="two mobile-two column">
            <label>Heating</label>
          </div>
          <div class="two mobile-one columns">
            <input type="number" value="<?php echo $occHeat ?>" min="60" max="80" placeholder="72" name="occupied-heat" id="occupied-heat" required>
            <span class="error" aria-live="polite"></span>
          </div>
          <div class="one mobile-one columns">
            <span class="postfix">&deg;F</span>
          </div>

          <div class="two mobile-one columns offset-by-one">
            <input type="number" value="<?php echo $unoccHeat ?>" min="60" max="80" placeholder="72" name="unoccupied-heat" id="unoccupied-heat" required>
            <span class="error" aria-live="polite"></span>
          </div>
          <div class="one mobile-one columns end">
            <span class="postfix">&deg;F</span>
          </div>
        </div>
      </div>
    </div><!-- end row -->

    <div class="row">
      <div class="six columns">
          <input type="submit" name="submit" id="submit" class="button">
      </div>
    </div><!-- end row -->
  </form><!-- end form -->
  <div id="test"></div>

  <!-- Included JS Files (Compressed) -->
  <script src="js/foundation/jquery.js"></script>
  <script src="js/foundation/foundation.min.js"></script>


  <script src="js/jquery-ui.js"></script>
  <script src="js/tstat.js"></script>
  
  <!-- Initialize JS Plugins -->
  <script src="js/foundation/app.js"></script>
  
</body>
</html>
