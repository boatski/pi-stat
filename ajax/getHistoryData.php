<?php

	ini_set('display_errors',1);
    error_reporting(E_ALL);

    try{

        $db = new PDO('sqlite:../db/pi-stat.db');

        $db->setAttribute(PDO::ATTR_ERRMODE, 
                            PDO::ERRMODE_EXCEPTION);

        $query = 'SELECT * FROM History ORDER BY Date DESC LIMIT 24';

        $result = $db->query($query);

        $data = array();

        foreach ($result as $row) {

          $data[] = array("IndoorTemperature"=>$row['IndoorTemperature'], "IndoorHumidity"=>$row['IndoorHumidity'], "OutdoorTemperature"=>$row['OutdoorTemperature'], 
                          "OutdoorHumidity"=>$row['OutdoorHumidity'], "Fan"=>$row['Fan'], "Heat"=>$row['Heat'], "Cool"=>$row['Cool'], "Date"=>$row['Date']);
        }// end foreach
        echo json_encode(array("response"=>$data));

    }
    catch(PDOException $e) {echo $e->getMessage();}

?>