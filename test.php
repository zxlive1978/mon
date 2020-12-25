<?php
if(isset($_SERVER['HTTP_X_REQUESTED_WITH']) && !empty($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest') {
2
	    // Если к нам идёт Ajax запрос, то ловим его
3
	    echo 'Это ajax запрос!';
4
	    exit;
5
	}
6
	//Если это не ajax запрос
7
	echo 'Это не ajax запрос!';
		
?>