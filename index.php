<!DOCTYPE html>

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

<?php

  ini_set('display_errors',1);
  error_reporting(E_ALL);
  class MyDB extends SQLite3
  {
      function __construct()
      {
          $this->open('db/pi-stat.db');
      }
  }

  $db = new MyDB();

  $result = $db->query('SELECT * FROM Thermostat');
  $row = $result->fetchArray();
  $occCool = $row['OccupiedCool'];
  $unoccCool = $row['UnoccupiedCool'];
  $occHeat = $row['OccupiedHeat'];
  $unoccHeat = $row['UnoccupiedHeat'];
  ?>



  <div class="row">
    <div class="twelve columns">
      <h2>Pi-Stat</h2>
  		<ul class="nav-bar">
  		  <li class="active"><a href="index.html">Thermostat</a></li>
  		  <li class=""><a href="history.html">History</a></li>
  		  <li class=""><a href="alarms.html">Alarms</a></li>
  		</ul>
    </div>
  </div>

  <div class="row">
    <div class="twelve columns">
      <dl class="tabs">
        <dd class="active"><a href="#simple1">Temperature</a></dd>
        <dd><a href="#simple2">Schedule</a></dd>
      </dl>

      <ul class="tabs-content">
        <li class="active" id="simple1Tab">

        <form>

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
                  <input type="number" value="<?php echo $occCool ?>" min="60" max="80" placeholder="72" id="occupied-cool" required>
                  <span class="error" aria-live="polite"></span>
                </div>
                <div class="one mobile-one columns">
                  <span class="postfix">&deg;F</span>
                </div>

                <div class="two mobile-one columns offset-by-one">
                  <input type="number" value="<?php echo $unoccCool ?>" min="60" max="80" placeholder="72" id="unoccupied-cool" required>
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
                  <input type="number" value="<?php echo $occHeat ?>" min="60" max="80" placeholder="72" id="occupied-heat" required>
                  <span class="error" aria-live="polite"></span>
                </div>
                <div class="one mobile-one columns">
                  <span class="postfix">&deg;F</span>
                </div>

                <div class="two mobile-one columns offset-by-one">
                  <input type="number" value="<?php echo $unoccHeat ?>" min="60" max="80" placeholder="72" id="unoccupied-heat" required>
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
                <button class="button">Submit</button>
            </div>
          </div><!-- end row -->
        </form>


		  </li>
      <li id="simple2Tab">
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
              <div class="date-headers one columns offset-by-one" id="monday-start-times">
                7:00
              </div>

              <div class="date-headers one columns" id="tuesday-start-times">
                7:00
              </div>

              <div class="date-headers one columns" id="wednesday-start-times">
                7:00
              </div>

              <div class="date-headers one columns" id="thursday-start-times">
                7:00
              </div>

              <div class="date-headers one columns" id="friday-start-times">
                7:00
              </div>

              <div class="date-headers one columns" id="saturday-start-times">
                7:00
              </div>

              <div class="date-headers one columns end" id="sunday-start-times">
                7:00
              </div>
            </div><!-- end row -->

            <div class="row collapse">
              <div class="date-headers one columns offset-by-one" id="monday-stop-times">
                7:00
              </div>

              <div class="date-headers one columns" id="tuesday-stop-times">
                7:00
              </div>

              <div class="date-headers one columns" id="wednesday-stop-times">
                7:00
              </div>

              <div class="date-headers one columns" id="thursday-stop-times">
                7:00
              </div>

              <div class="date-headers one columns" id="friday-stop-times">
                7:00
              </div>

              <div class="date-headers one columns" id="saturday-stop-times">
                7:00
              </div>

              <div class="date-headers one columns end" id="sunday-stop-times">
                7:00
              </div>
            </div><!-- end row -->

          </div>
        </div>


      </li>
    </ul>
	 </div>
  </div>
  
  
  
  <!-- Included JS Files (Compressed) -->
  <script src="js/foundation/jquery.js"></script>
  <script src="js/foundation/foundation.min.js"></script>


  <script src="js/jquery-ui.js"></script>
  <script src="js/main.js"></script>
  <script src="js/tstat.js"></script>
  
  <!-- Initialize JS Plugins -->
  <script src="js/foundation/app.js"></script>
  
</body>
</html>
