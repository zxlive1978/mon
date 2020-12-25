

var Remote_host="";
function assa(Remote_host) {
var rhost = Remote_host;
var person = prompt(rhost+" Введите пароль:", "");
  if (person == null || person == "") {
    //txt = "User cancelled the prompt.";
  } else {
	 go_fresh = false;
	$.ajax({
		type: "POST",
		url: 'js/assareset.php',
		data: {registration: person, host: rhost},
		success: function(data){
			
			alert(data);
			go_fresh = true;
		}
	});
	
   
  }
  
}

function ubi(Remote_host) {
var rhost = Remote_host;
var person = prompt(rhost+" Введите пароль:", "");
  if (person == null || person == "") {
    //txt = "User cancelled the prompt.";
  } else {
	 go_fresh = false;
	$.ajax({
		type: "POST",
		url: 'js/ubireboot.php',
		data: {registration: person, host: rhost},
		success: function(data){
			
			alert(data);
			go_fresh = true;
		}
	});
	
   
  }
  
}

function poz(Remote_host) {
var rhost = Remote_host;
var person = prompt(rhost+" Введите пароль:", "");
  if (person == null || person == "") {
    //txt = "User cancelled the prompt.";
  } else {
	 go_fresh = false;
	$.ajax({
		type: "POST",
		url: 'js/pozreboot.php',
		data: {registration: person, host: rhost},
		success: function(data){
			
			alert(data);
			go_fresh = true;
		}
	});
	
   
  }
  
}

function zyx(Remote_host) {
var rhost = Remote_host;
var person = prompt(rhost+" Введите пароль:", "");
  if (person == null || person == "") {
    //txt = "User cancelled the prompt.";
  } else {
	 go_fresh = false;
	$.ajax({
		type: "POST",
		url: 'js/zyxelreboot.php',
		data: {registration: person, host: rhost},
		success: function(data){
			
			alert(data);
			go_fresh = true;
		}
	});
	
   
  }
  
}

function camshoot(Remote_host, pic_name) {
var rhost = Remote_host;
var pname = pic_name;
window.location.replace('js/camshoot.php'+'?host='+rhost+'&type='+pic_name);
//var person = prompt(rhost+" Введите пароль:", "");
 /*  if (person == null || person == "") {
    
  } else { */
/* 	 go_fresh = false;
	$.ajax({
		type: "POST",
		url: 'js/camshoot.php',
		data: {host: rhost, name: pname},
		success: function(data){
			
			//alert(data);
			go_fresh = true;
			window.location.replace("camshoot.php"+"?host="+rhost);
		}
	}); */
	
   
  /* } */
  
}