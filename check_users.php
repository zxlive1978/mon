<?php
	$name_base="goodman";
	// $table=$_POST['table'];
	// $collid=$_POST['collid'];
	$table="USERS";
	$collid="name , pass";
	// $user=$_POST['user'];
	// $pass=$_POST['pass'];
	
	$dbc= mysqli_connect('127.0.0.1', 'goodman', 'NRywfHcXEmzenn7S', 'goodman',3306) or
		die(mysqli_sqlstate($dbc));
	
	
	$code_page="SET NAMES 'utf8';";
	mysqli_query($dbc,$code_page) or
		die(mysqli_sqlstate($dbc));
	
	$query="SELECT * FROM ".$name_base.".".$table." WHERE name=".
		"'".$_GET['email']."'"." AND "."pass="."'".$_GET['pass']."';" ;
	// echo $query;
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	// echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	
	if (mysqli_num_rows($result)>0){
		$_SESSION['start']=true;}
		// echo $row['pass']."<br />";}


    mysqli_close($dbc);

?>