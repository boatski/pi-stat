<!DOCTYPE html>

  <?php

    ini_set('display_errors',1);
    error_reporting(E_ALL);

    // Get setpoints from the database.
    $db = new PDO('sqlite:db/pi-stat.db') or die("fail to connect db");

    $result = $db->query('SELECT * FROM Thermostat');

    foreach ($result as $row) {

      $occCool = $row['OccupiedCool'];
      $unoccCool = $row['UnoccupiedCool'];
      $occHeat = $row['OccupiedHeat'];
      $unoccHeat = $row['UnoccupiedHeat'];
      $lockout = $row['OutdoorLockout'];

      $db = null;
    }// end foreach

    // Poll the temperature sensor and get outdoor temperatures.
    //$output = exec("python /usr/share/nginx/www/pi-stat/json/sensor.py");
    $output = exec("python /Users/Boatski/Sites/pi-stat/json/sensor.py");
    $jsonOutput = json_decode($output);

    $indoorTemperature = $jsonOutput->sensor->indoorTemperature;
    $indoorHumidity = $jsonOutput->sensor->indoorHumidity;

    $outdoorTemperature = $jsonOutput->weather->current_observation->temp_f;
    $outdoorHumidity = $jsonOutput->weather->current_observation->relative_humidity;
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
  <div id="test"></div>
  
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
      <div>
        Indoor Temperature: <?php echo $indoorTemperature ?><br />
        Indoor Humidity: <?php echo $indoorHumidity ?><br />
        Outdoor Temperature: <?php echo $outdoorTemperature ?><br />
        Outdoor Humidity: <?php echo $outdoorHumidity ?>
      </div>
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
      <div class="eight columns">
        <div class="row collapse">
          <div class="column-margin offset-by-two three columns">
            <label>Occupied</label>
          </div>
          <div class="column-margin three columns">
            <label>Unoccupied</label>
          </div>
          <div class="three columns end">
            <label>Outdoor Lockout</label>
          </div>
        </div>
      </div>
    </div><!-- end row -->

    <div class="form-elements row">
      <div class="eight columns">
        <div class="row collapse">
          <div class="two columns">
            <label>Cooling</label>
          </div>
          <div class="two columns">
            <input type="number" value="<?php echo $occCool ?>" min="60" max="80" placeholder="72" name="occupied-cool" id="occupied-cool" required>
            <span class="error" aria-live="polite"></span>
          </div>
          <div class="column-margin one columns">
            <span class="postfix">&deg;F</span>
          </div>

          <div class="two columns">
            <input type="number" value="<?php echo $unoccCool ?>" min="60" max="80" placeholder="76" name="unoccupied-cool" id="unoccupied-cool" required>
            <span class="error" aria-live="polite"></span>
          </div>
          <div class="column-margin one columns">
            <span class="postfix">&deg;F</span>
          </div>

          <div class="two columns">
            <input type="number" value="<?php echo $lockout ?>" min="50" max="70" placeholder="60" name="outdoor-lockout" id="outdoor-lockout" required>
            <span class="error" aria-live="polite"></span>
          </div>
          <div class="one columns end">
            <span class="postfix">&deg;F</span>
          </div>
        </div>
      </div>
    </div><!-- end row -->

    <div class="form-elements row">
      <div class="eight columns">
        <div class="row collapse">
          <div class="two column">
            <label>Heating</label>
          </div>
          <div class="two columns">
            <input type="number" value="<?php echo $occHeat ?>" min="60" max="80" placeholder="72" name="occupied-heat" id="occupied-heat" required>
            <span class="error" aria-live="polite"></span>
          </div>
          <div class="column-margin one columns">
            <span class="postfix">&deg;F</span>
          </div>

          <div class="two columns">
            <input type="number" value="<?php echo $unoccHeat ?>" min="60" max="80" placeholder="72" name="unoccupied-heat" id="unoccupied-heat" required>
            <span class="error" aria-live="polite"></span>
          </div>
          <div class="one columns end">
            <span class="postfix">&deg;F</span>
          </div>
        </div>
      </div>
    </div><!-- end row -->

    <div class="row">
      <div class="eight columns">
          <div class="row collapse">
            <div class="two columns">
              <input type="submit" name="submit" id="submit" class="button">
            </div>
            <div class="success two columns end">
              <p>Success!</p>
            </div>
          </div>
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
