var isMobile = false; //
// ТЕЛЕФОН ПЛАНШЕТ???
if(/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|ipad|iris|kindle|Android|Silk|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(navigator.userAgent) 
    || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(navigator.userAgent.substr(0,4))) isMobile = true;
/*
if (isMobile){
document.write('ТЕЛФОН');
} else {document.write('КОМПУКТЕР');}
*/



//Ширина участка данных
//var disp_time = d110d[d110d.length-1]["Vrema"] - d110d[0]["Vrema"];
//var disp_time_back = disp_time;
//Начало данных
var start_time = d110d[0]["Vrema"];
//Конец данных
var end_time = d110d[d110d.length-1]["Vrema"];
//Фейк массив для данных когда их нет
var comment = new Array();
var namecmt= wellName + "kr";
// Рисовать графики или нет 
//var drawGraf = true ;
//Маcштаб (час)
//var Kzoom = 4;

//if (timetime<2){setInterval("obnovit_stranicu()", 60*1000);}

//Чтение комментариев
function read_comment(){
	online = true;
	//refresh = false;
	//alert(wellName);
	//alert(Kzoom);
	//console.log (start_time);
	//console.log (end_time);
	$.ajax({
		type: "GET",
		url: 'read_comment.php',
		data: {name: 'Wayne',well_Name: wellName,  start_time: start_time, end_time: end_time, namecmt: namecmt},
		success: function(data){
			//var jsonn = JSON.encode(data);
			//console.log(jsonn);
			//<?php echo ' d110d = '.json_encode(data).';' ?>;
			//console.log(json["Vrema"]);
			//alert(json["Vrema"]);
			
			var comnt = eval(data);
			//var mass = data;
			
			//alert(comnt);
			
			comment = comnt;
			//console.log(comment);
			
			//numbs110d = null;
			//disp_time = end_time - start_time;
			//Kzoom = Math.floor(disp_time/3600);
			//console.log (comment);
			try {
			//$("#drawing").off();
			//$("#drawing").children().remove();
			//$("#drawing").clear();
			//$("#drawing").remove();
			//window.draw.clear();
			//$("#drawing").find("*").not("rect, g").remove();
			}
			catch(e){ }
			
			//init();
		}
	});
	
	//back_start_time = start_time;
	//back_end_time = end_time;
}

