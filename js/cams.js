

switch(agrr){
	case 's630':
		var videoFile = window.atob('aHR0cDovL2h5ZHJvZmFsbGwuZGRucy5uZXQ6ODA5MC90ZXN0MS53ZWJt');
		break;
	case 's908':
		var videoFile = window.atob('aHR0cDovL2h5ZHJvZmFsbGwuZGRucy5uZXQ6ODA5MC90ZXN0Mi53ZWJt');
		break;
	case 's631':
		var videoFile = window.atob('aHR0cDovL2h5ZHJvZmFsbGwuZGRucy5uZXQ6ODA5MC90ZXN0My53ZWJt');
		break;
	case 's4450':
		var videoFile = window.atob('aHR0cDovL3NtLnJlZGlyZWN0bWUubmV0OjgwOTAvdGVzdDEud2VibQ==');
		break;
	case 's20':
		var videoFile = window.atob('aHR0cDovL2h5ZHJvZmFsbGwuZGRucy5uZXQ6ODA5MC90ZXN0NS53ZWJt');
		break;
}
var vidosik = document.getElementById("video");

vidosik.height = "576";
vidosik.width = "704";

vidosik.src = videoFile;
vidosik.load();
vidosik.play();

function goto(){
vidosik.pause();
var curhourse = document.getElementById("localtime");
var curdate = document.getElementById("localdate");
var next_step = videoFile+"?date="+curdate.value+"T"+curhourse.value+":00";	
vidosik.src=next_step;
vidosik.load();
vidosik.play();	
}

function gotonow(){
vidosik.pause();
var curhourse = document.getElementById("localtime");
var next_step = videoFile;	
vidosik.src=next_step;
vidosik.load();
vidosik.play();	
}
