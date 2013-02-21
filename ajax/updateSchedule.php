<?php

	ini_set('display_errors',1);
    error_reporting(E_ALL);
    try{

	    $db = new PDO('sqlite:../db/pi-stat.db');

    	$db->setAttribute(PDO::ATTR_ERRMODE, 
                            PDO::ERRMODE_EXCEPTION);

	    /*$occCool = $_POST['occupied-cool'];
	    $unoccCool = $_POST['unoccupied-cool'];
	    $occHeat = $_POST['occupied-heat'];
	    $unoccHeat = $_POST['unoccupied-heat'];

	    $query = "UPDATE Thermostat 
	    		  SET OccupiedCool = {$occCool},
	    		  UnoccupiedCool = {$unoccCool},
	    		  OccupiedHeat = {$occHeat},
	    		  UnoccupiedHeat = {$unoccHeat};";

	
		$db->exec($query);*/
	}
	catch(PDOException $e) {echo $e->getMessage();}

?>