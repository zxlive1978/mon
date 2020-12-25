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
	$xy_value110d=array();
	//$cur_time=1505176261-6*60*60;
	$timeshift =$_GET['Kzoom'];;
	$cur_time=time()-60*60*(float)$timeshift;
	$table="s20kr";
	//$table=$_GET['well_Name'];
	$x_id="Vrema";
	$y_id="Comment";
	$z1_id="left_txt";


	//$query="SELECT ".$x_id.",".$y_id.",".$z1_id.",".$z2_id.",".$z3_id.",".$z4_id.",".$z5_id.",".$z6_id.",".$z7_id.",".$z8_id.",".$z9_id.",".$z10_id.",".$z11_id.",".$z12_id.",".$z13_id.",".$z14_id.",".$z15_id.",".$z16_id.",".$z17_id.",".$z18_id.",".$z19_id.",".$z20_id.",".$z21_id." FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	#$query="SELECT * FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	$query="SELECT * FROM ".$name_base.".".$table.";";
	#echo $table;
	$result=mysqli_query($dbc,$query) or die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	//echo $result;
	
	$xy_value110d = array();
	while($row=mysqli_fetch_array($result,MYSQLI_ASSOC)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$cur_rec= array('Vrema' => $row['Vrema'],'Comment' => $row['Comment'],'left_txt' => $row['left_txt']);
		//$cur_rec['Wkp'] = $row['Wkp'];
		array_push($xy_value110d, $cur_rec);
		}
	mysqli_free_result($result);
	
	echo json_encode($xy_value110d);
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