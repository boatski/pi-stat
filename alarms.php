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
      <li class=""><a href="schedule.php">Schedule</a></li>
		  <li class=""><a href="history.php">History</a></li>
		  <li class="active"><a href="alarms.php">Alarms</a></li>
		</ul>
    </div>
  </div>

  <div class="row">
    <div class="twelve columns" id="graph">
      <p><a href="#" data-reveal-id="exampleModal" class="alert button">Alarms!</a></p>
    </div>
  </div>
  
  <div id="exampleModal" class="reveal-modal">
    <h2>I'm just kidding...</h2>
    <p>
      There aren't any alarms because they aren't implemented yet!
    </p>
    <a class="close-reveal-modal">×</a>
  </div>
  
  
  
  <!-- Included JS Files (Compressed) -->
  <script src="js/foundation/jquery.js"></script>
  <script src="js/foundation/foundation.min.js"></script>
  <script src="js/main.js"></script>
  
  <!-- Initialize JS Plugins -->
  <script src="js/foundation/app.js"></script>
  
</body>
</html>
