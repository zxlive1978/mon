<?php

	// $host="localhost";
	// $user="goodman";
	// $pass="NRywfHcXEmzenn7S";

	$dbc= mysqli_connect('127.0.0.1', 'goodman', 'NRywfHcXEmzenn7S', 'goodman',3306) or
		die(mysqli_sqlstate($dbc));
	
	
	$code_page="SET NAMES 'utf8';";
	mysqli_query($dbc,$code_page) or
		die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);


?>