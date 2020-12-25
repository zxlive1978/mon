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
	$timeshift = 4;
	$cur_time=time()-60*60*(float)$timeshift;
	//$table="s110";
	$table=$_GET['well'];
	$x_id="Vrema";
	$y_id="Wkp";
	$z1_id="Wdol";
	$z2_id="Mpot";
	$z3_id="Npot";
	$z4_id="Pbx";
	$z5_id="Qbx";
	$z6_id="Talblok";
	$z7_id="Zaboj";
	$z8_id="Instr";
	$z9_id="C1C5";
	$z10_id="C1";
	$z11_id="Xn1";
	$z12_id="Xn2";
	$z13_id="Potok";
	$z14_id="Tbix";
	$z15_id="V1";
	$z16_id="V2";
	$z17_id="V3";
	$z18_id="V4";
	$z19_id="Vdol";
	$z20_id="Vobj";
	$z21_id="Vinstr";


	$query="SELECT * FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	//echo $query;
	$result=mysqli_query($dbc,$query) or die(mysqli_sqlstate($dbc));
	//echo mysqli_sqlstate($dbc);
	// echo $_POST['email'];
	// echo $_POST['pass'];
	//Добавление значений в массив
	//$row = $result->fetch_array(MYSQLI_ASSOC);
	//printf ("%s (%s)\n", $row["Vrema"], $row["Wkp"]);
	//Добавление значений в массив
	//$cur_rec= array();
	$xy_value110d = array();
	while($row=mysqli_fetch_array($result,MYSQLI_ASSOC)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$cur_rec= array('Vrema' => $row['Vrema'],'Wkp' => $row['Wkp'],'Wdol' => $row['Wdol'],'Mpot' => $row['Mpot'],
		'Npot' => $row['Npot'],'Pbx' => $row['Pbx'],'Qbx' => $row['Qbx'],'Talblok' => $row['Talblok'],
		'Zaboj' => $row['Zaboj'],'Instr' => $row['Instr'],'C1C5' => $row['C1C5'],'C1' => $row['C1'],
		'Xn1' => $row['Xn1'],'Xn2' => $row['Xn2'],'Potok' => $row['Potok'],'Tbix' => $row['Tbix'],
		'V1' => $row['V1'],'V2' => $row['V2'],'V3' => $row['V3'],'V4' => $row['V4'],
		'Vdol' => $row['Vdol'],'Vobj' => $row['Vobj'],'Vinstr' => $row['Vinstr']);
		//$cur_rec['Wkp'] = $row['Wkp'];
		array_push($xy_value110d, $cur_rec);
		}
	mysqli_free_result($result);
	
	#$query="SELECT MIN(Vrema) as minimum, MAX(Vrema) as maximum FROM ".$name_base.".".$table.";";
	$query="SELECT MIN( Vrema ) AS  start  FROM ".$name_base.".".$table.";";
	//echo $query;
	$result2=mysqli_query($dbc,$query) or die(mysqli_sqlstate($dbc));
	$row = mysqli_fetch_assoc($result2);
	//echo $row['start'];
	//Умножаем дату на 1000 перевод из мсек в сек плюс часовой пояс +4 часа
	//echo count($xy_value110d);
	/* for ($i=0;$i<count($xy_value110d);$i++){
		$xy_value110d[$i][0]=$xy_value110d[$i][0]-14400;
		
	} */
	

	
	/* $query="SELECT COUNT(*) FROM ".$name_base.".".$table." WHERE ".$x_id.">".(int)$cur_time.";";
	
	$result=mysqli_query($dbc,$query) or
		die(mysqli_sqlstate($dbc));
	while($row = mysqli_fetch_array ($result)){
		//echo $row[$x_id]." - ".$row[$y_id]."<br />";
		$numbs_rec110d=$row[0];
		} */
		
    mysqli_close($dbc);
	include './sutki.html';

		
?>