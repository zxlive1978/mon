<?php 
session_start();
$confMsg = '';
if ($_SESSION['start']<>1) {
	header("Location: /index.php");
	exit;
}
?>

<?php
	$dbc= mysqli_connect('127.0.0.1', 'goodman', 'NRywfHcXEmzenn7S') or
		die(mysqli_sqlstate($dbc));
	
	$code_page="SET NAMES 'utf8';";
	mysqli_query($dbc,$code_page) or
		die(mysqli_sqlstate($dbc));

	$name_base="pozitron";
	//$table="p372978226";
	$comment=array();
	//$cur_time=1505176261-6*60*60;
	$timeshift =4;
	$cur_time=time()-60*60*(float)$timeshift;
	$start_time = $_GET['start_time'];
	$end_time = $_GET['end_time'];
	$table= $_GET['namecmt'];
	//$table=$_GET['well_Name'];
	$x_id="Vrema";
	$y_id="Comment";
	$z1_id="left_txt";


	#$query="SELECT * FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	#$query="SELECT * FROM ".$name_base.".".$table.";";
	$query="SELECT * FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$start_time." AND ".$x_id."<".(int)$end_time.";";
	//echo $table;
	$result=mysqli_query($dbc,$query) or die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	//echo $result;
	
	$comment = array();
	while($row=mysqli_fetch_array($result,MYSQLI_ASSOC)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$cur_rec= array('Vrema' => $row['Vrema'],'Comment' => $row['Comment'],'left_txt' => $row['left_txt']);
		//$cur_rec['Wkp'] = $row['Wkp'];
		array_push($comment, $cur_rec);
		}
	mysqli_free_result($result);
	
	echo json_encode($comment);
	//echo json_encode($ass);
	
	/* $query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec110d=$row[0];
		} */
		
    mysqli_close($dbc);

		
?>