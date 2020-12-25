<?php
/* if (!$_SESSION['start']) {
	header("Location: /mon/index.php");
	exit;
} */
/* Отладка ошибок */
ini_set('display_errors',1);
error_reporting(E_ALL ^E_NOTICE);

// Check for safe mode
if( ini_get('safe_mode') ){
	echo "BAD";
    // Do it the safe mode way
}else{
	
	/* echo "GOOD"; */
    // Do it the regular way
}

$registration = $_POST['registration'];
$host= $_POST['host'];
/* echo $registration; */
/* $output = shell_exec('ls -lart');
echo "<pre>$output</pre>"; */
/* $cmd = 'python /var/www/html/mon/poz/assareset.py '.$host;
$output = passthru($cmd);
echo $cmd; */
if ($registration == "suck"){
 // some action goes here under php
	$cmd = '/usr/bin/python /var/www/html/mon/poz/zyxelreboot.py '.$host;
	$output = shell_exec($cmd);
	echo $output;
	/* echo var_dump($cmd; */
	/* $output = shell_exec('ls -lart');
	echo "<pre>$output</pre>"; */
 //echo json_encode(array("abc"=>'successfuly registered'));
} else{
	echo 'Неверный пароль!';
}
?>