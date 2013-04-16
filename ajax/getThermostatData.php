<?php

	ini_set('display_errors',1);
    error_reporting(E_ALL);

    // Poll the temperature sensor and get outdoor temperatures.
    $temp = exec("/usr/bin/python /home/pi/www/pi-stat/json/sensor.py");

    $jsonOutput = json_decode($temp);

    $indoorTemperature = $jsonOutput->sensor->indoorTemperature;
    $indoorHumidity = $jsonOutput->sensor->indoorHumidity;

    $outdoorTemperature = $jsonOutput->weather->current_observation->temp_f;
    $outdoorHumidity = $jsonOutput->weather->current_observation->relative_humidity;

    $fan = $jsonOutput->outputs->fan;
    $heat = $jsonOutput->outputs->heat;
    $cool = $jsonOutput->outputs->cool;

    // Need to optimize
    if ($fan == "1") {
      $fan = "On";
    } else {
      $fan = "Off";
    }// end if

    if ($heat == "1") {
      $heat = "On";
    } else {
      $heat = "Off";
    }// end if

    if ($cool == "1") {
      $cool = "On";
    } else {
      $cool = "Off";
    }// end if

    $data = array("IndoorTemperature"=>$indoorTemperature, "IndoorHumidity"=>$indoorHumidity, "OutdoorTemperature"=>$outdoorTemperature, 
                      "OutdoorHumidity"=>$outdoorHumidity, "Fan"=>$fan, "Heat"=>$heat, "Cool"=>$cool);

    echo json_encode(array("response"=>$data));

?>