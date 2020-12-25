//Округление после операций с плавающей точкой
function roundPlus(x, n) { //x - число, n - количество знаков
	  if(isNaN(x) || isNaN(n)) return false;
	  var m = Math.pow(10,n);
	  return Math.round(x*m)/m;
	}


//Преобразование координат экрана в svg
function getCursorPosition(event, svgElement) {
  var svgPoint = svgElement.createSVGPoint();

  svgPoint.x = event.clientX;
  svgPoint.y = event.clientY;

  return svgPoint.matrixTransform(svgElement.getScreenCTM().inverse());
}


	
function init(){
	// A4 пропорция
	var width = window.innerWidth, height = width*1.44;
	var w1=width/100;
	var h1=height/100;

	var draw = SVG('drawing').size('100%',height);
	
	draw.viewbox(0,0,width,height);
	draw.attr('preserveAspectRatio', 'xMidYMid meet');
	
	//МЫШЬ Курсор перемещение
	/*
	var svg = document.querySelector('svg');

	svg.addEventListener('mousemove', function(e) {
	var cursor = getCursorPosition(e, svg);
	console.log(cursor);
	}, false);
	*/
	///////////////////////////////////
	//МЫШЬ Курсор клик
	var svg = document.querySelector('svg');
	var X_cur_mouse_click = 0;
	var Y_cur_mouse_click = 0;

	svg.addEventListener('mousedown', function(e) {
	var cursor = getCursorPosition(e, svg);
	X_cur_mouse_click = cursor.x;
	Y_cur_mouse_click = cursor.y;
	}, false);
	
	//ТЕСТ
	//Бакграунт
	/*
	var background = draw.rect(width, height).fill('#dde3e1')
	
	//Текст
	draw.text('Вес на крюке')
  	.move(w1*50, 1)
  	.font({ family: 'Inconsolata', size: 16 })
    .fill('#ff0066')
	
	//Линия
	var line10 = draw.line(0, 0, w1*50, h1*50)
	line10.stroke({ width: 2, color: '#f0f'});
	//Клик
	line10.click(function() {
	this.fill({ color: '#f06' });
	alert('ta-da!');
	})
	
	//Линия пунктирная
	var line = draw.line(width/2, 0, width/2, height);
	line.stroke({ width: 5, color: '#fff', dasharray: '5,5' });
	
	*/
	
	//Ширина шапки времени в %
	var time_w = 7;
	//Высота шапки по высоте в %
	var disp_up = 14;
	//Ширина Столбец 1 
	var weight_colmn1 = 23;
	
	//Шапка Угловой квадрат
	var colmn0 = draw.polygon('0, 0 '+w1*time_w+',0 ' + w1*time_w + ',' + h1*disp_up + ' 0,' + h1*disp_up)
	.fill({ color: '#fff' })
	.stroke({ width: 2 });
	
	//Шапка Столбец 1 
	var colmn1_x0 = w1*time_w;
	var colmn1_y0 = 0;
	var colmn1_x1 = w1*time_w;
	var colmn1_y1 = h1*disp_up;
	var colmn1_x2 = w1*(time_w+weight_colmn1);
	var colmn1_y2 = h1*disp_up;
	var colmn1_x3 = colmn1_x2;
	var colmn1_y3 = 0;
	var colmn1 = draw.polygon(colmn1_x0+','+colmn1_y0+' '+colmn1_x1+','+colmn1_y1+' '+colmn1_x2+','+colmn1_y2+' '+colmn1_x3+','+colmn1_y3 )
	.fill({ color: '#fff' })
	.stroke({ width: 2 });
	
	
	/*Wkp=-100.0
	Wdol=-100.0
	Mpot=-100.0
	Npot=-100.0
	Pbx=-100.0 */
	//Толщина шкалы
	var width_line_p = 2;
	//Число параметров в столбце
	var numbs_colmn1 = 6;
	//Высота одного параметра box
	var height_colmn1_p1 = colmn1_y2 / numbs_colmn1;
	//Число насечек
	var numbs_risk = 5;
	//Шаг насечек
	var steep_risk1= weight_colmn1/numbs_risk; 
	//Цвет параметра 1 в первом столбике
	var color11 = '#ff0066';
	//Цвет параметра 2 в первом столбике
	var color12 = '#006eea';
	//Цвет параметра 3 в первом столбике
	var color13 = '#a92ab8';
	//Цвет параметра 4 в первом столбике
	var color14 = '#006400';
	//Цвет параметра 5 в первом столбике(Глубина Забоя)
	var color15 = '#000000';
	//Цвет параметра 1 в 2 столбике
	var color21 = '#f40503';
	//Цвет параметра 2 в 2 столбике
	var color22 = '#006eea';
	//Цвет параметра 3 в 2 столбике
	var color23 = '#006400';
	//Цвет параметра 4 в 2 столбике
	var color24 = '#f21890';
	//Цвет параметра 5 в 2 столбике
	var color25 = '#855f30';
	//Цвет параметра 6 в 2 первом столбике(Инструмент)
	var color26 = '#000000';
	//Цвет параметра 1 в 3 столбике
	var color31 = '#f40503';
	//Цвет параметра 2 в 3 столбике
	var color32 = '#006eea';
	//Цвет параметра 3 в 3 столбике
	var color33 = '#f21890';
	//Цвет параметра 4 в 3 столбике
	var color34 = '#006400';
	//Цвет параметра 5 в 3 столбике
	var color35 = '#a92ab8';
	//Цвет параметра 1 в 4 столбике
	var color41 = '#f40503';
	//Цвет параметра 2 в 4 столбике
	var color42 = '#006eea';
	//Цвет параметра 3 в 4 столбике
	var color43 = '#f21890';
	//Цвет параметра 4 в 4 столбике
	var color44 = '#006400';
	//Цвет параметра 5 в 4 столбике
	var color45 = '#a92ab8';
	//Цвет параметра 6 в 4 столбике
	var color46 = '#000000';
	
	
	//Высота риски
	var height_risk = 0.4;
	//////////////
	//Размер шрифта для параметра
	//var K_size_txt=54.44;
	var K_size_txt = 73;
	var size_text_p = width/K_size_txt;
	//Шкала параметр 1 
	var line_new = draw.line(colmn1_x0, height_colmn1_p1, colmn1_x2, height_colmn1_p1);
	line_new.stroke({ width: width_line_p, color: color11});
	
	
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn1_x0+i*w1*steep_risk1, height_colmn1_p1, colmn1_x0+i*w1*steep_risk1, height_colmn1_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color11});
		}
	//Название параметра
	var name_p1 = 'Вес на крюке '+d110d[numbs110d-1]["Wkp"];
	var text_name_p1 = draw.text(name_p1)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn1_x0+w1*weight_colmn1/2, colmn1_y0+height_colmn1_p1/2)
		.center(colmn1_x0+w1*weight_colmn1/2, colmn1_y0+height_colmn1_p1/2)
		.fill(color11)
	//Границы параметра 
	var l_p1 = 0;
	var r_p1 = 270;
	var text_l_p1 = draw.text(String(l_p1))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn1_x0+1*w1*steep_risk1/2, colmn1_y0)
		.cx(colmn1_x0+1*w1*steep_risk1/2)
		.fill(color11)
	var text_r_p1 = draw.text(String(r_p1))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn1_x0+9*w1*steep_risk1/2, colmn1_y0)
		.cx(colmn1_x0+9*w1*steep_risk1/2)
		.fill(color11)
	
	
	//Шкала параметр 2
	var line_new = draw.line(colmn1_x0, 2*height_colmn1_p1, colmn1_x2, 2*height_colmn1_p1);
	line_new.stroke({ width: width_line_p, color: color12});
	
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn1_x0+i*w1*steep_risk1, 2*height_colmn1_p1, colmn1_x0+i*w1*steep_risk1, 2*height_colmn1_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color12});
		}
	//Название параметра
	var name_p2 = 'Нагрузка на дол. '+d110d[numbs110d-1]["Wdol"];
	var text_name_p2 = draw.text(name_p2)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn1_x0+w1*weight_colmn1/2, colmn1_y0+3*height_colmn1_p1/2)
		.center(colmn1_x0+w1*weight_colmn1/2, colmn1_y0+3*height_colmn1_p1/2)
		.fill(color12)
	//Границы параметра 
	var l_p2 = 0;
	var r_p2 = 70;
	var text_l_p2 = draw.text(String(l_p2))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn1_x0+1*w1*steep_risk1/2, colmn1_y0+height_colmn1_p1)
		.cx(colmn1_x0+1*w1*steep_risk1/2)
		.fill(color12)
	var text_r_p2 = draw.text(String(r_p2))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn1_x0+9*w1*steep_risk1/2, colmn1_y0+height_colmn1_p1)
		.cx(colmn1_x0+9*w1*steep_risk1/2)
		.fill(color12)
	
	
	//Шкала параметр 3
	var line_new = draw.line(colmn1_x0, 3*height_colmn1_p1, colmn1_x2, 3*height_colmn1_p1);
	line_new.stroke({ width: width_line_p, color: color13});
	
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn1_x0+i*w1*steep_risk1, 3*height_colmn1_p1, colmn1_x0+i*w1*steep_risk1, 3*height_colmn1_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color13});
		}
	//Название параметра
	var name_p3 = 'Обороты ротора '+ d110d[numbs110d-1]["Npot"];
	var text_name_p3 = draw.text(name_p3)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn1_x0+w1*weight_colmn1/2, colmn1_y0+5*height_colmn1_p1/2)
		.center(colmn1_x0+w1*weight_colmn1/2, colmn1_y0+5*height_colmn1_p1/2)
		.fill(color13)
	//Границы параметра 
	var l_p3 = 0;
	var r_p3 = 200;
	var text_l_p3 = draw.text(String(l_p3))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn1_x0+1*w1*steep_risk1/2, colmn1_y0+2*height_colmn1_p1)
		.cx(colmn1_x0+1*w1*steep_risk1/2)
		.fill(color13)
	var text_r_p3 = draw.text(String(r_p3))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn1_x0+9*w1*steep_risk1/2, colmn1_y0+2*height_colmn1_p1)
		.cx(colmn1_x0+9*w1*steep_risk1/2)
		.fill(color13)
	
	
	//Шкала параметр 4
	var line_new = draw.line(colmn1_x0, 4*height_colmn1_p1, colmn1_x2, 4*height_colmn1_p1);
	line_new.stroke({ width: width_line_p, color: color14});
	
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn1_x0+i*w1*steep_risk1, 4*height_colmn1_p1, colmn1_x0+i*w1*steep_risk1, 4*height_colmn1_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color14});
		}
	//Название параметра
	var name_p4 = 'Момент на роторе '+d110d[numbs110d-1]["Mpot"];
	var text_name_p4 = draw.text(name_p4)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn1_x0+w1*weight_colmn1/2, colmn1_y0+7*height_colmn1_p1/2)
		.center(colmn1_x0+w1*weight_colmn1/2, colmn1_y0+7*height_colmn1_p1/2)
		.fill(color14)
	//Границы параметра 
	var l_p4 = 0;
	var r_p4 = 5;
	var text_l_p4 = draw.text(String(l_p4))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn1_x0+1*w1*steep_risk1/2, colmn1_y0+3*height_colmn1_p1)
		.cx(colmn1_x0+1*w1*steep_risk1/2)
		.fill(color14)
	var text_r_p4 = draw.text(String(r_p4))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn1_x0+9*w1*steep_risk1/2, colmn1_y0+3*height_colmn1_p1)
		.cx(colmn1_x0+9*w1*steep_risk1/2)
		.fill(color14)
		
	//Глубина забоя
	var name_p5 = 'Глубина забоя '+d110d[numbs110d-1]["Zaboj"];
	var text_name_p5 = draw.text(name_p5)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn1_x0+2*w1*weight_colmn1/3, colmn1_y0+11*height_colmn1_p1/2)
		.center(colmn1_x0+2*w1*weight_colmn1/3, colmn1_y0+11*height_colmn1_p1/2)
		.fill(color15)
		
	//Время начало
	var last_time = d110d[0]["0"]/1;
	var day = new Date(last_time*1000);
	var last_hour = day.getHours();
	var minutes = day.getMinutes();
	var yearr = day.getFullYear();
	var dates = day.getDate();
	var month = day.getMonth();
	if (last_hour<10){last_hour="0"+last_hour}
	if (minutes<10){minutes="0"+minutes}
	if (yearr<10){yearr="0"+yearr}
	if (dates<10){dates="0"+dates}
	if (month<10){month="0"+month}
	var name_p6 = last_hour+":"+minutes+" "+dates+"."+month+"."+yearr;
	var text_name_p6 = draw.text("Скважина АГКМ"+ wellName.slice(1)+"-1")
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn1_x0+w1*weight_colmn1/2, colmn1_y0+9*height_colmn1_p1/2)
		.center(colmn1_x0+w1*weight_colmn1/2, colmn1_y0+9*height_colmn1_p1/2)
		.fill(color15)
	//Время конец
	var last_time = d110d[numbs110d-1]["0"]/1;
	var day = new Date(last_time*1000);
	var last_hour = day.getHours();
	var minutes = day.getMinutes();
	var yearr = day.getFullYear();
	var dates = day.getDate();
	var month = day.getMonth();
	if (last_hour<10){last_hour="0"+last_hour}
	if (minutes<10){minutes="0"+minutes}
	if (yearr<10){yearr="0"+yearr}
	if (dates<10){dates="0"+dates}
	if (month<10){month="0"+month}
	var name_p6 = name_p6+ " - "+last_hour+":"+minutes+" "+dates+"."+month+"."+yearr;
	var text_name_p6 = draw.text(name_p6)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn1_x0+w1*weight_colmn1/2, colmn1_y0+10*height_colmn1_p1/2)
		.center(colmn1_x0+w1*weight_colmn1/2, colmn1_y0+10*height_colmn1_p1/2)
		.fill(color15)
	/////////////////////////////////////////////////////
	
	
	
	
	//Шапка Столбец 2 
	var colmn2_x0 = w1*(time_w+weight_colmn1);
	var colmn2_y0 = 0;
	var colmn2_x1 = w1*(time_w+weight_colmn1);
	var colmn2_y1 = h1*disp_up;
	var colmn2_x2 = w1*(time_w+2*weight_colmn1);
	var colmn2_y2 = h1*disp_up;
	var colmn2_x3 = colmn2_x2;
	var colmn2_y3 = 0;
	var colmn2 = draw.polygon(colmn2_x0+','+colmn2_y0+' '+colmn2_x1+','+colmn2_y1+' '+colmn2_x2+','+colmn2_y2+' '+colmn2_x3+','+colmn2_y3 )
	.fill({ color: '#fff' })
	.stroke({ width: 2 });
	
	//Ширина Столбец 1 
	var weight_colmn2 = 23;
	var width_line_p = 2;
	//Число параметров в столбце
	var numbs_colmn2 = 6;
	//Высота одного параметра box
	var height_colmn2_p1 = colmn2_y2 / numbs_colmn2;
	
	//Шкала параметр 1 
	var line_new = draw.line(colmn2_x0, height_colmn2_p1, colmn2_x2, height_colmn2_p1);
	line_new.stroke({ width: width_line_p, color: color21});
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn2_x0+i*w1*steep_risk1, height_colmn2_p1, colmn2_x0+i*w1*steep_risk1, height_colmn2_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color21});
		}
	//Название параметра
	var name_p21 = 'Давление на входе '+ d110d[numbs110d-1]["Pbx"];
	var text_name_p21 = draw.text(name_p21)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn2_x0+w1*weight_colmn2/2, colmn2_y0+height_colmn2_p1/2)
		.center(colmn2_x0+w1*weight_colmn2/2, colmn2_y0+height_colmn2_p1/2)
		.fill(color21)
		
	//Границы параметра 
	var l_p21 = 0;
	var r_p21 = 200;
	var text_l_p21 = draw.text(String(l_p21))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn2_x0+1*w1*steep_risk1/2, colmn2_y0)
		.cx(colmn2_x0+1*w1*steep_risk1/2)
		.fill(color21)
	var text_r_p21 = draw.text(String(r_p21))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn2_x0+9*w1*steep_risk1/2, colmn2_y0)
		.cx(colmn2_x0+9*w1*steep_risk1/2)
		.fill(color21)
	
	//Шкала параметр 2
	var line_new = draw.line(colmn2_x0, 2*height_colmn2_p1, colmn2_x2, 2*height_colmn2_p1);
	line_new.stroke({ width: width_line_p, color: color22});
	
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn2_x0+i*w1*steep_risk1, 2*height_colmn2_p1, colmn2_x0+i*w1*steep_risk1, 2*height_colmn2_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color22});
		}
	//Название параметра
	var name_p22 = 'Пол. тальблока '+ d110d[numbs110d-1]["Talblok"];
	var text_name_p22 = draw.text(name_p22)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn2_x0+w1*weight_colmn2/2, colmn2_y0+3*height_colmn2_p1/2)
		.center(colmn2_x0+w1*weight_colmn2/2, colmn2_y0+3*height_colmn2_p1/2)
		.fill(color22)
	//Границы параметра 
	var l_p22 = 0;
	var r_p22 = 40;
	var text_l_p22 = draw.text(String(l_p22))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn2_x0+1*w1*steep_risk1/2, colmn2_y0+height_colmn2_p1)
		.cx(colmn2_x0+1*w1*steep_risk1/2)
		.fill(color22)
	var text_r_p22 = draw.text(String(r_p22))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn2_x0+9*w1*steep_risk1/2, colmn2_y0+height_colmn2_p1)
		.cx(colmn2_x0+9*w1*steep_risk1/2)
		.fill(color22)
	
	
	//Шкала параметр 3
	var line_new = draw.line(colmn2_x0, 3*height_colmn2_p1, colmn2_x2, 3*height_colmn2_p1);
	line_new.stroke({ width: width_line_p, color: color23});
	
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn2_x0+i*w1*steep_risk1, 3*height_colmn2_p1, colmn2_x0+i*w1*steep_risk1, 3*height_colmn2_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color23});
		}
	//Название параметра
	var name_p23 = 'Расход на входе '+d110d[numbs110d-1]["Qbx"];
	var text_name_p23 = draw.text(name_p23)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn2_x0+w1*weight_colmn2/2, colmn2_y0+5*height_colmn2_p1/2)
		.center(colmn2_x0+w1*weight_colmn1/2, colmn2_y0+5*height_colmn2_p1/2)
		.fill(color23)
	//Границы параметра 
	var l_p23 = 0;
	var r_p23 = 50;
	var text_l_p23 = draw.text(String(l_p23))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn2_x0+1*w1*steep_risk1/2, colmn2_y0+2*height_colmn2_p1)
		.cx(colmn2_x0+1*w1*steep_risk1/2)
		.fill(color23)
	var text_r_p23 = draw.text(String(r_p23))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn2_x0+9*w1*steep_risk1/2, colmn2_y0+2*height_colmn2_p1)
		.cx(colmn2_x0+9*w1*steep_risk1/2)
		.fill(color23)
	
	
	//Шкала параметр 4
	var line_new = draw.line(colmn2_x0, 4*height_colmn2_p1, colmn2_x2, 4*height_colmn2_p1);
	line_new.stroke({ width: width_line_p, color: color24});
	
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn2_x0+i*w1*steep_risk1, 4*height_colmn2_p1, colmn2_x0+i*w1*steep_risk1, 4*height_colmn2_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color24});
		}
	//Название параметра
	var name_p24 = 'С1(%) '+d110d[numbs110d-1]["C1"];
	var text_name_p24 = draw.text(name_p24)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn2_x0+w1*weight_colmn2/2, colmn2_y0+7*height_colmn2_p1/2)
		.center(colmn2_x0+w1*weight_colmn2/2, colmn2_y0+7*height_colmn2_p1/2)
		.fill(color24)
	//Границы параметра 
	var l_p24 = 0;
	var r_p24 = 0.5;
	var text_l_p24 = draw.text(String(l_p24))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn2_x0+1*w1*steep_risk1/2, colmn2_y0+3*height_colmn2_p1)
		.cx(colmn2_x0+1*w1*steep_risk1/2)
		.fill(color24)
	var text_r_p24 = draw.text(String(r_p24))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn2_x0+9*w1*steep_risk1/2, colmn2_y0+3*height_colmn2_p1)
		.cx(colmn2_x0+9*w1*steep_risk1/2)
		.fill(color24)
	
	//Шкала параметр 5
	var line_new = draw.line(colmn2_x0, 5*height_colmn2_p1, colmn2_x2, 5*height_colmn2_p1);
	line_new.stroke({ width: width_line_p, color: color25});
	
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn2_x0+i*w1*steep_risk1, 5*height_colmn2_p1, colmn2_x0+i*w1*steep_risk1, 5*height_colmn2_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color25});
		}
	//Название параметра
	var name_p25 = 'Сумма газов(%) '+d110d[numbs110d-1]["C1C5"];
	var text_name_p25 = draw.text(name_p25)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn2_x0+w1*weight_colmn2/2, colmn2_y0+9*height_colmn2_p1/2)
		.center(colmn2_x0+w1*weight_colmn2/2, colmn2_y0+9*height_colmn2_p1/2)
		.fill(color25)
	//Границы параметра 
	var l_p25 = 0;
	var r_p25 = 1;
	var text_l_p25 = draw.text(String(l_p25))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn2_x0+1*w1*steep_risk1/2, colmn2_y0+4*height_colmn2_p1)
		.cx(colmn2_x0+1*w1*steep_risk1/2)
		.fill(color25)
	var text_r_p25 = draw.text(String(r_p25))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn2_x0+9*w1*steep_risk1/2, colmn2_y0+4*height_colmn2_p1)
		.cx(colmn2_x0+9*w1*steep_risk1/2)
		.fill(color25)
		
	
	//Пол.долота
	var name_p26 = 'Пол.долота '+d110d[numbs110d-1]["Instr"];
	var text_name_p26 = draw.text(name_p26)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn2_x0+2*w1*weight_colmn2/3, colmn2_y0+11*height_colmn2_p1/2)
		.center(colmn2_x0+2*w1*weight_colmn2/3, colmn2_y0+11*height_colmn2_p1/2)
		.fill(color15)
				
	///////////////////////////////////
	

	
	//Шапка Столбец 3 
	var colmn3_x0 = w1*(time_w+2*weight_colmn1);
	var colmn3_y0 = 0;
	var colmn3_x1 = w1*(time_w+2*weight_colmn1);
	var colmn3_y1 = h1*disp_up;
	var colmn3_x2 = w1*(time_w+3*weight_colmn1);
	var colmn3_y2 = h1*disp_up;
	var colmn3_x3 = colmn3_x2;
	var colmn3_y3 = 0;
	var colmn3 = draw.polygon(colmn3_x0+','+colmn3_y0+' '+colmn3_x1+','+colmn3_y1+' '+colmn3_x2+','+colmn3_y2+' '+colmn3_x3+','+colmn3_y3 )
	.fill({ color: '#ffffff' })
	.stroke({ width: 2 });
	
	//Ширина Столбец 3 
	var weight_colmn3 = 23;
	var width_line_p = 2;
	//Число параметров в столбце
	var numbs_colmn3 = 6;
	//Высота одного параметра box
	var height_colmn3_p1 = colmn3_y2 / numbs_colmn3;
	
	//Шкала параметр 1 
	var line_new = draw.line(colmn3_x0, height_colmn3_p1, colmn3_x2, height_colmn3_p1);
	line_new.stroke({ width: width_line_p, color: color31});
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn3_x0+i*w1*steep_risk1, height_colmn3_p1, colmn3_x0+i*w1*steep_risk1, height_colmn3_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color31});
		}
	
	//Название параметра
	var name_p31 = 'Ходы 1 насоса '+d110d[numbs110d-1]["Xn1"];
	var text_name_p31 = draw.text(name_p31)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn3_x0+w1*weight_colmn3/2, colmn3_y0+height_colmn3_p1/2)
		.center(colmn3_x0+w1*weight_colmn3/2, colmn3_y0+height_colmn3_p1/2)
		.fill(color31)
		
	//Границы параметра 
	var l_p31 = 0;
	var r_p31 = 100;
	var text_l_p31 = draw.text(String(l_p31))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn3_x0+1*w1*steep_risk1/2, colmn3_y0)
		.cx(colmn3_x0+1*w1*steep_risk1/2)
		.fill(color31)
	var text_r_p31 = draw.text(String(r_p31))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn3_x0+9*w1*steep_risk1/2, colmn3_y0)
		.cx(colmn3_x0+9*w1*steep_risk1/2)
		.fill(color31)
	
	//Шкала параметр 2
	var line_new = draw.line(colmn3_x0, 2*height_colmn3_p1, colmn3_x2, 2*height_colmn3_p1);
	line_new.stroke({ width: width_line_p, color: color32});
	
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn3_x0+i*w1*steep_risk1, 2*height_colmn3_p1, colmn3_x0+i*w1*steep_risk1, 2*height_colmn3_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color32});
		}
	//Название параметра
	var name_p32 = 'Ходы 2 насоса '+d110d[numbs110d-1]["Xn2"];
	var text_name_p32 = draw.text(name_p32)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn3_x0+w1*weight_colmn3/2, colmn3_y0+3*height_colmn3_p1/2)
		.center(colmn3_x0+w1*weight_colmn3/2, colmn3_y0+3*height_colmn3_p1/2)
		.fill(color32)
	//Границы параметра 
	var l_p32 = 0;
	var r_p32 = 100;
	var text_l_p32 = draw.text(String(l_p32))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn3_x0+1*w1*steep_risk1/2, colmn3_y0+height_colmn3_p1)
		.cx(colmn3_x0+1*w1*steep_risk1/2)
		.fill(color32)
	var text_r_p32 = draw.text(String(r_p32))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn3_x0+9*w1*steep_risk1/2, colmn3_y0+height_colmn3_p1)
		.cx(colmn3_x0+9*w1*steep_risk1/2)
		.fill(color32)
	
	
	//Шкала параметр 3
	var line_new = draw.line(colmn3_x0, 3*height_colmn3_p1, colmn3_x2, 3*height_colmn3_p1);
	line_new.stroke({ width: width_line_p, color: color33});
	
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn3_x0+i*w1*steep_risk1, 3*height_colmn3_p1, colmn3_x0+i*w1*steep_risk1, 3*height_colmn3_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color33});
		}
	//Название параметра
	var name_p33 = 'Темп. на выходе '+d110d[numbs110d-1]["Tbix"];
	var text_name_p33 = draw.text(name_p33)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn3_x0+w1*weight_colmn3/2, colmn3_y0+5*height_colmn3_p1/2)
		.center(colmn3_x0+w1*weight_colmn1/2, colmn3_y0+5*height_colmn3_p1/2)
		.fill(color33)
	//Границы параметра 
	var l_p33 = 0;
	var r_p33 = 70;
	var text_l_p33 = draw.text(String(l_p33))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn3_x0+1*w1*steep_risk1/2, colmn3_y0+2*height_colmn3_p1)
		.cx(colmn3_x0+1*w1*steep_risk1/2)
		.fill(color33)
	var text_r_p33 = draw.text(String(r_p33))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn3_x0+9*w1*steep_risk1/2, colmn3_y0+2*height_colmn3_p1)
		.cx(colmn3_x0+9*w1*steep_risk1/2)
		.fill(color33)
	
	
	//Шкала параметр 4
	var line_new = draw.line(colmn3_x0, 4*height_colmn3_p1, colmn3_x2, 4*height_colmn3_p1);
	line_new.stroke({ width: width_line_p, color: color34});
	
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn3_x0+i*w1*steep_risk1, 4*height_colmn3_p1, colmn3_x0+i*w1*steep_risk1, 4*height_colmn3_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color34});
		}
	//Название параметра
	var name_p34 = 'Поток на выходе '+d110d[numbs110d-1]["Potok"];
	var text_name_p34 = draw.text(name_p34)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn3_x0+w1*weight_colmn3/2, colmn3_y0+7*height_colmn3_p1/2)
		.center(colmn3_x0+w1*weight_colmn3/2, colmn3_y0+7*height_colmn3_p1/2)
		.fill(color34)
	//Границы параметра 
	var l_p34 = 0;
	var r_p34 = 70;
	var text_l_p34 = draw.text(String(l_p34))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn3_x0+1*w1*steep_risk1/2, colmn3_y0+3*height_colmn3_p1)
		.cx(colmn3_x0+1*w1*steep_risk1/2)
		.fill(color34)
	var text_r_p34 = draw.text(String(r_p34))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn3_x0+9*w1*steep_risk1/2, colmn3_y0+3*height_colmn3_p1)
		.cx(colmn3_x0+9*w1*steep_risk1/2)
		.fill(color34)
	
	//Шкала параметр 5
	var line_new = draw.line(colmn3_x0, 5*height_colmn3_p1, colmn3_x2, 5*height_colmn3_p1);
	line_new.stroke({ width: width_line_p, color: color35});
	
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn3_x0+i*w1*steep_risk1, 5*height_colmn3_p1, colmn3_x0+i*w1*steep_risk1, 5*height_colmn3_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color35});
		}
	//Название параметра
	var name_p35 = 'Скор. тальблока '+d110d[numbs110d-1]["Vinstr"];
	var text_name_p35 = draw.text(name_p35)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn3_x0+w1*weight_colmn3/2, colmn3_y0+9*height_colmn3_p1/2)
		.center(colmn3_x0+w1*weight_colmn3/2, colmn3_y0+9*height_colmn3_p1/2)
		.fill(color35)
	//Границы параметра 
	var l_p35 = -5;
	var r_p35 = 5;
	var text_l_p35 = draw.text(String(l_p35))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn3_x0+1*w1*steep_risk1/2, colmn3_y0+4*height_colmn3_p1)
		.cx(colmn3_x0+1*w1*steep_risk1/2)
		.fill(color35)
	var text_r_p35 = draw.text(String(r_p35))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn3_x0+9*w1*steep_risk1/2, colmn3_y0+4*height_colmn3_p1)
		.cx(colmn3_x0+9*w1*steep_risk1/2)
		.fill(color35)
	
	
	
	////////////////////////////////////////////////
	/*
	*/
	
	//Шапка Столбец 4 
	var colmn4_x0 = w1*(time_w+3*weight_colmn1);
	var colmn4_y0 = 0;
	var colmn4_x1 = w1*(time_w+3*weight_colmn1);
	var colmn4_y1 = h1*disp_up;
	var colmn4_x2 = w1*(time_w+4*weight_colmn1);
	var colmn4_y2 = h1*disp_up;
	var colmn4_x3 = colmn4_x2;
	var colmn4_y3 = 0;
	var colmn4 = draw.polygon(colmn4_x0+','+colmn4_y0+' '+colmn4_x1+','+colmn4_y1+' '+colmn4_x2+','+colmn4_y2+' '+colmn4_x3+','+colmn4_y3 )
	.fill({ color: '#ffffff' })
	.stroke({ width: 2 });
	
	
	//Ширина Столбец 4
	var weight_colmn4 = 23;
	var width_line_p = 2;
	//Число параметров в столбце
	var numbs_colmn4 = 7;
	//Высота одного параметра box
	var height_colmn4_p1 = colmn4_y2 / numbs_colmn4;
	
	//Шкала параметр 1 
	var line_new = draw.line(colmn4_x0, height_colmn4_p1, colmn4_x2, height_colmn4_p1);
	line_new.stroke({ width: width_line_p, color: color41});
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn4_x0+i*w1*steep_risk1, height_colmn4_p1, colmn4_x0+i*w1*steep_risk1, height_colmn4_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color41});
		}
	
	//Название параметра
	var name_p41 = 'Объем 1 емкости '+d110d[numbs110d-1]["V1"];
	var text_name_p41 = draw.text(name_p41)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn4_x0+w1*weight_colmn4/2, colmn4_y0+height_colmn4_p1/2)
		.center(colmn4_x0+w1*weight_colmn4/2, colmn4_y0+height_colmn4_p1/2)
		.fill(color41)
		
	//Границы параметра 
	var l_p41 = 0;
	var r_p41 = 100;
	var text_l_p41 = draw.text(String(l_p41))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn4_x0+1*w1*steep_risk1/2, colmn4_y0)
		.cx(colmn4_x0+1*w1*steep_risk1/2)
		.fill(color41)
	var text_r_p41 = draw.text(String(r_p41))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn4_x0+9*w1*steep_risk1/2, colmn4_y0)
		.cx(colmn4_x0+9*w1*steep_risk1/2)
		.fill(color41)
	
	//Шкала параметр 2
	var line_new = draw.line(colmn4_x0, 2*height_colmn4_p1, colmn4_x2, 2*height_colmn4_p1);
	line_new.stroke({ width: width_line_p, color: color42});
	
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn4_x0+i*w1*steep_risk1, 2*height_colmn4_p1, colmn4_x0+i*w1*steep_risk1, 2*height_colmn4_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color42});
		}
	//Название параметра
	var name_p42 = 'Объем 2 емкости '+ d110d[numbs110d-1]["V2"];
	var text_name_p42 = draw.text(name_p42)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn4_x0+w1*weight_colmn4/2, colmn4_y0+3*height_colmn4_p1/2)
		.center(colmn4_x0+w1*weight_colmn4/2, colmn4_y0+3*height_colmn4_p1/2)
		.fill(color32)
	//Границы параметра 
	var l_p42 = 0;
	var r_p42 = 90;
	var text_l_p42 = draw.text(String(l_p42))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn4_x0+1*w1*steep_risk1/2, colmn4_y0+height_colmn4_p1)
		.cx(colmn4_x0+1*w1*steep_risk1/2)
		.fill(color42)
	var text_r_p42 = draw.text(String(r_p42))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn4_x0+9*w1*steep_risk1/2, colmn4_y0+height_colmn4_p1)
		.cx(colmn4_x0+9*w1*steep_risk1/2)
		.fill(color42)
	
	
	//Шкала параметр 3
	var line_new = draw.line(colmn4_x0, 3*height_colmn4_p1, colmn4_x2, 3*height_colmn4_p1);
	line_new.stroke({ width: width_line_p, color: color43});
	
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn4_x0+i*w1*steep_risk1, 3*height_colmn4_p1, colmn4_x0+i*w1*steep_risk1, 3*height_colmn4_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color43});
		}
	//Название параметра
	var name_p43 = 'Объем 3 емкости '+d110d[numbs110d-1]["V3"];
	var text_name_p43 = draw.text(name_p43)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn4_x0+w1*weight_colmn4/2, colmn4_y0+5*height_colmn4_p1/2)
		.center(colmn4_x0+w1*weight_colmn1/2, colmn4_y0+5*height_colmn4_p1/2)
		.fill(color43)
	//Границы параметра 
	var l_p43 = 0;
	var r_p43 = 120;
	var text_l_p43 = draw.text(String(l_p43))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn4_x0+1*w1*steep_risk1/2, colmn4_y0+2*height_colmn4_p1)
		.cx(colmn4_x0+1*w1*steep_risk1/2)
		.fill(color43)
	var text_r_p43 = draw.text(String(r_p43))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn4_x0+9*w1*steep_risk1/2, colmn4_y0+2*height_colmn4_p1)
		.cx(colmn4_x0+9*w1*steep_risk1/2)
		.fill(color43)
	
	
	//Шкала параметр 4
	var line_new = draw.line(colmn4_x0, 4*height_colmn4_p1, colmn4_x2, 4*height_colmn4_p1);
	line_new.stroke({ width: width_line_p, color: color44});
	
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn4_x0+i*w1*steep_risk1, 4*height_colmn4_p1, colmn4_x0+i*w1*steep_risk1, 4*height_colmn4_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color44});
		}
	//Название параметра
	var name_p44 = 'Объем 4 емкости '+d110d[numbs110d-1]["V4"];
	var text_name_p44 = draw.text(name_p44)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn4_x0+w1*weight_colmn4/2, colmn4_y0+7*height_colmn4_p1/2)
		.center(colmn4_x0+w1*weight_colmn4/2, colmn4_y0+7*height_colmn4_p1/2)
		.fill(color44)
	//Границы параметра 
	var l_p44 = 0;
	var r_p44 = 90;
	var text_l_p44 = draw.text(String(l_p44))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn4_x0+1*w1*steep_risk1/2, colmn4_y0+3*height_colmn4_p1)
		.cx(colmn4_x0+1*w1*steep_risk1/2)
		.fill(color44)
	var text_r_p44 = draw.text(String(r_p44))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn4_x0+9*w1*steep_risk1/2, colmn4_y0+3*height_colmn4_p1)
		.cx(colmn4_x0+9*w1*steep_risk1/2)
		.fill(color44)
	
	//Шкала параметр 5
	var line_new = draw.line(colmn4_x0, 5*height_colmn4_p1, colmn4_x2, 5*height_colmn4_p1);
	line_new.stroke({ width: width_line_p, color: color45});
	
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn4_x0+i*w1*steep_risk1, 5*height_colmn4_p1, colmn4_x0+i*w1*steep_risk1, 5*height_colmn4_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color45});
		}
	//Название параметра
	var name_p45 = 'Объем дол.емк. '+d110d[numbs110d-1]["Vdol"];
	var text_name_p45 = draw.text(name_p45)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn4_x0+w1*weight_colmn4/2, colmn4_y0+9*height_colmn4_p1/2)
		.center(colmn4_x0+w1*weight_colmn4/2, colmn4_y0+9*height_colmn4_p1/2)
		.fill(color45)
	//Границы параметра 
	var l_p45 = 0;
	var r_p45 = 30;
	var text_l_p45 = draw.text(String(l_p45))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn4_x0+1*w1*steep_risk1/2, colmn4_y0+4*height_colmn4_p1)
		.cx(colmn4_x0+1*w1*steep_risk1/2)
		.fill(color45)
	var text_r_p45 = draw.text(String(r_p45))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn4_x0+9*w1*steep_risk1/2, colmn4_y0+4*height_colmn4_p1)
		.cx(colmn4_x0+9*w1*steep_risk1/2)
		.fill(color45)
		
	//Шкала параметр 6
	var line_new = draw.line(colmn4_x0, 6*height_colmn4_p1, colmn4_x2, 6*height_colmn4_p1);
	line_new.stroke({ width: width_line_p, color: color46});
	
	for (var i = 1; i < numbs_risk; i++){
		var line_new = draw.line(colmn4_x0+i*w1*steep_risk1, 6*height_colmn4_p1, colmn4_x0+i*w1*steep_risk1, 6*height_colmn4_p1-h1*height_risk);
		line_new.stroke({ width: width_line_p, color: color46});
		}
	//Название параметра
	var name_p46 = 'Cумм. объем емк.'+d110d[numbs110d-1]["Vobj"];
	var text_name_p46 = draw.text(name_p46)
		.font({ family: 'Inconsolata', size: size_text_p  })
		.move(colmn4_x0+w1*weight_colmn4/2, colmn4_y0+11*height_colmn4_p1/2)
		.center(colmn4_x0+w1*weight_colmn4/2, colmn4_y0+11*height_colmn4_p1/2)
		.fill(color46)
	//Границы параметра 
	var l_p46 = 0;
	var r_p46 = 400;
	var text_l_p46 = draw.text(String(l_p46))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn4_x0+1*w1*steep_risk1/2, colmn4_y0+5*height_colmn4_p1)
		.cx(colmn4_x0+1*w1*steep_risk1/2)
		.fill(color46)
	var text_r_p46 = draw.text(String(r_p46))
		.font({ family: 'Inconsolata', size: size_text_p -3})
		.move(colmn4_x0+9*w1*steep_risk1/2, colmn4_y0+5*height_colmn4_p1)
		.cx(colmn4_x0+9*w1*steep_risk1/2)
		.fill(color46)
		
	/////////////////////////////////////	
	////////////////////////////////////
	//Рамка значений
	var rcolmn11_x0 = w1*time_w;
	var rcolmn11_y0 = h1*disp_up;
	var rcolmn11_x1 = w1*(weight_colmn1+time_w);
	var rcolmn11_y1 = h1*disp_up;
	var rcolmn11_x2 = w1*(weight_colmn1+time_w);
	var rcolmn11_y2 = h1*100;
	var rcolmn11_x3 = w1*time_w;
	var rcolmn11_y3 = h1*100;
	
	
		
		
	////////////////////////////////////
	///////////////////////////////////
	
	//Область графика 1 легенда
	var colmn11_x0 = w1*time_w;
	var colmn11_y0 = h1*disp_up;
	var colmn11_x1 = w1*(weight_colmn1+time_w);
	var colmn11_y1 = h1*disp_up;
	var colmn11_x2 = w1*(weight_colmn1+time_w);
	var colmn11_y2 = h1*100;
	var colmn11_x3 = w1*time_w;
	var colmn11_y3 = h1*100;
	//Рамка первого столбца
	var gfx1 = draw.polygon(colmn11_x0+','+colmn11_y0 +' '+colmn11_x1+','+colmn11_y1+' '+colmn11_x2+' '+colmn11_y2+' '+colmn11_x3+' '+colmn11_y3)
	.fill({ color: '#fff' })
	.stroke({ width: width_line_p });
	
	/* var point = path.point(gfx1.click.screenX, gfx1.click.screenY)
	alert (point); */
	//Число засечек
	var numbr_teeth_сolmn1 = 10;
	//Шаг засечек
	var steep_col1 = (colmn11_x1-colmn11_x0)/numbr_teeth_сolmn1;
	//Отступ по вертикале от шапки
	var disp_col1 = colmn11_x0;
	for (var i = 0; i < numbr_teeth_сolmn1; i++) {
		var line = draw.line(disp_col1, colmn11_y0, disp_col1, h1*100);
		line.stroke({ width: 1, color: '#bababa', dasharray: '3,5' });
		disp_col1 = disp_col1 +steep_col1;
	}
	
	//Область графика 2 легенда
	var colmn21_x0 = w1*(weight_colmn1+time_w);
	var colmn21_y0 = h1*disp_up;
	var colmn21_x1 = w1*(2*weight_colmn1+time_w);
	var colmn21_y1 = h1*disp_up;
	var colmn21_x2 = w1*(2*weight_colmn1+time_w);
	var colmn21_y2 = h1*100;
	var colmn21_x3 = w1*(weight_colmn1+time_w);
	var colmn21_y3 = h1*100;
	//Рамка первого столбца
	var gfx2 = draw.polygon(colmn21_x0+','+colmn21_y0 +' '+colmn21_x1+','+colmn21_y1+' '+colmn21_x2+' '+colmn21_y2+' '+colmn21_x3+' '+colmn21_y3)
	.fill({ color: '#fff' })
	.stroke({ width: width_line_p });
	
	//Число засечек
	var numbr_teeth_сolmn2 = 10;
	//Шаг засечек
	var steep_col2 = (colmn21_x1-colmn21_x0)/numbr_teeth_сolmn2;
	//Отступ по вертикале от шапки
	var disp_col2 = colmn21_x0;
	for (var i = 0; i < numbr_teeth_сolmn2; i++) {
		var line = draw.line(disp_col2, colmn21_y0, disp_col2, h1*100);
		line.stroke({ width: 1, color: '#bababa', dasharray: '3,5' });
		disp_col2 = disp_col2 +steep_col2;
	}
	
	//Область графика 3 легенда
	var colmn31_x0 = w1*(2*weight_colmn1+time_w);
	var colmn31_y0 = h1*disp_up;
	var colmn31_x1 = w1*(3*weight_colmn1+time_w);
	var colmn31_y1 = h1*disp_up;
	var colmn31_x2 = w1*(3*weight_colmn1+time_w);
	var colmn31_y2 = h1*100;
	var colmn31_x3 = w1*(2*weight_colmn1+time_w);
	var colmn31_y3 = h1*100;
	//Рамка первого столбца
	var gfx3 = draw.polygon(colmn31_x0+','+colmn31_y0 +' '+colmn31_x1+','+colmn31_y1+' '+colmn31_x2+' '+colmn31_y2+' '+colmn31_x3+' '+colmn31_y3)
	.fill({ color: '#fff' })
	.stroke({ width: width_line_p });
	
	//Число засечек
	var numbr_teeth_сolmn3 = 10;
	//Шаг засечек
	var steep_col3 = (colmn31_x1-colmn31_x0)/numbr_teeth_сolmn3;
	//Отступ по вертикале от шапки
	var disp_col3 = colmn31_x0;
	for (var i = 0; i < numbr_teeth_сolmn3; i++) {
		var line = draw.line(disp_col3, colmn31_y0, disp_col3, h1*100);
		line.stroke({ width: 1, color: '#bababa', dasharray: '3,5' });
		disp_col3 = disp_col3 +steep_col3;
	}
	
	//Область графика 4 легенда
	var colmn41_x0 = w1*(3*weight_colmn1+time_w);
	var colmn41_y0 = h1*disp_up;
	var colmn41_x1 = w1*(4*weight_colmn1+time_w);
	var colmn41_y1 = h1*disp_up;
	var colmn41_x2 = w1*(4*weight_colmn1+time_w);
	var colmn41_y2 = h1*100;
	var colmn41_x3 = w1*(3*weight_colmn1+time_w);
	var colmn41_y3 = h1*100;
	//Рамка первого столбца
	var gfx4 = draw.polygon(colmn41_x0+','+colmn41_y0 +' '+colmn41_x1+','+colmn41_y1+' '+colmn41_x2+' '+colmn41_y2+' '+colmn41_x3+' '+colmn41_y3)
	.fill({ color: '#fff' })
	.stroke({ width: width_line_p });
	
	//Число засечек
	var numbr_teeth_сolmn4 = 10;
	//Шаг засечек
	var steep_col4 = (colmn41_x1-colmn41_x0)/numbr_teeth_сolmn4;
	//Отступ по вертикале от шапки
	var disp_col4 = colmn41_x0;
	for (var i = 0; i < numbr_teeth_сolmn4; i++) {
		var line = draw.line(disp_col4, colmn41_y0, disp_col4, h1*100);
		line.stroke({ width: 1, color: '#bababa', dasharray: '3,5' });
		disp_col4 = disp_col4 +steep_col4;
	}

	
	
	//Первый параметр
	/*
	Wkp=-100.0
	Wdol=-100.0
	Mpot=-100.0
	Npot=-100.0
	Pbx=-100.0
	Qbx=-100.0
	Talblok=-100.0
	C1C5=-100.0
	C1=-100.0
	Xn1=-100.0
	Xn2=-100.0
	Potok=-100.0
	Tbix=-100.0
	V1=-100.0
	V2=-100.0
	V3=-100.0
	V4=-100.0
	Vdol=-100.0
	Vobj=-100.0
	Zaboj=-100.0
	Instr=-100.0
	Vrema=-100
	*/
	
	
	
	//Рамка шкалы времени
	//var group_time_rul = draw.nested();
	var time1 = draw.polygon('0,'+h1*disp_up+' '+w1*time_w + ',' + h1*disp_up+' '+w1*time_w+','+h1*100+' 0,'+h1*100)
	.fill({ color: '#fff' })
	.stroke({ width: width_line_p });
	//Клик!!!!!!
	/*
	time1.click(function() {
	this.fill({ color: '#ff2' });
	alert('OOOO');
	})
	*/
	//group_time_rul.add(time1);
	
	//Линия времени 
	/*var line20 = draw.line(w1*time_w/2, h1*disp_up, w1*time_w/2, height);
	line20.stroke({ width: 2, color: '#000'});
	group_time_rul.add(line20);
	*/
	//Насечка времени 
	/*var employees = [];
	for (var i = 0; i < 10; i++) {
		employees.push({
			Column1: 'column 1 of emp' + i,
			Column2: 'column 1 of emp' + i
		});
	}*/
	//var teeth = [];	
	/* var length = 1;
	var numbr_teeth = 10;
	var steep = (height-h1*disp_up)/numbr_teeth;
	var disp = h1*disp_up;
	alert (steep);
	for (var i = 0; i < numbr_teeth; i++){
		var line_new = draw.line(w1*time_w/2-w1*length, disp, w1*time_w/2+w1*length, disp);
		line_new.stroke({ width: 5, color: '#000'});
		teeth.push({
		line:line_new
		});
		disp = roundPlus((disp + steep),2);
	} 
	*/
	//alert (disp);
	//alert (steep);
	
	//Текущее время
	//Конец времени
	var last_time = d110d[numbs110d-1]["0"]/1;
	var lastday = new Date(last_time*1000);
	var last_hour = lastday.getHours();
	var last_minutes = lastday.getMinutes();
	//Начало времени
	var beg_time = d110d[0]["0"]/1;
	//Текущее время
	var cur_time = beg_time;
	var day = new Date(cur_time*1000);
	var beg_hour = day.getHours();
	var minutes = day.getMinutes();
	//Разница между времени в часах
	var how_hours = (last_time-beg_time)/3600;
	//alert(how_hours);
	//Шаг записей для текстовой глубины долота  и суммы объемов
	var step_txt_numb_rec = Math.round( numbs110d /how_hours);

	//Большие насечки
	//Длина насечки
	var length = 1.5;
	var width_line = 3;
	//Число засечек
	var numbr_teeth = Math.round(how_hours);
	//Шаг засечек
	var steep = Math.round((height-h1*disp_up)/numbr_teeth);
	//Отступ по вертикале от шапки
	var disp = h1*disp_up;
	//Малые насечки
	var length_small = 1;
	var width_line_small = 1;
	var numbr_teeth_small = 5;
	var steep_small = Math.round(steep/numbr_teeth_small);
	var disp_small = h1*disp_up;
	
	for (var i = 0; i < numbr_teeth; i++){
		//Большие насечки
		var line_new = draw.line(0, disp, w1*length, disp);
		line_new.stroke({ width: width_line, color: '#000'});
		//group_time_rul.add(line_new);
		var line_new = draw.line(w1*time_w-w1*length, disp, w1*time_w, disp);
		line_new.stroke({ width: width_line, color: '#000'});
		//group_time_rul.add(line_new);
		disp_small = disp;
			
			//Малые насечки
			for (var j = 0; j < numbr_teeth_small; j++){
				var line_new66 = draw.line(0, disp_small, w1*length_small, disp_small);
				line_new66.stroke({ width: width_line_small, color: '#000'});
				//group_time_rul.add(line_new66);
				var line_new66 = draw.line(w1*time_w-w1*length_small, disp_small, w1*time_w, disp_small);
				line_new66.stroke({ width: width_line_small, color: '#000'});
				//group_time_rul.add(line_new66);
				disp_small = disp_small + steep_small;
				//Маленькие насечки пунктир на все графики
				//Линия пунктирная
				var line = draw.line(w1*time_w, disp_small, w1*99.9, disp_small);
				line.stroke({ width: 1, color: '#bababa', dasharray: '3,5' });
			}
			
		//Текст метки
		//Время
		var day = new Date(cur_time*1000+i*3600000);	
		var hour = day.getHours();
		var minutes = day.getMinutes();
		if (hour<10){hour="0"+hour;}
		if (minutes<10){minutes="0"+minutes;}
		var text_time = draw.text(String(hour)+':'+String(minutes))
		.font({ family: 'Inconsolata', size: size_text_p })
		.move(w1*time_w/2, disp)
		.cx(w1*time_w/2)
		
		//Глубина забоя
		var text_time = draw.text(d110d[i*step_txt_numb_rec]["Zaboj"])
		.font({ family: 'Inconsolata', size: size_text_p })
		.move(colmn1_x0+3*w1*weight_colmn1/4, disp)
		.cx(colmn1_x0+3*w1*weight_colmn1/4)
		
		//Положение долота
		var text_time = draw.text(d110d[i*step_txt_numb_rec]["Instr"])
		.font({ family: 'Inconsolata', size: size_text_p })
		.move(colmn21_x0+3*w1*weight_colmn1/4, disp)
		.cx(colmn21_x0+3*w1*weight_colmn1/4)
		
		//Общий объем
		var text_time = draw.text(d110d[i*step_txt_numb_rec]["Vobj"])
		.font({ family: 'Inconsolata', size: size_text_p })
		.move(colmn41_x0+3*w1*weight_colmn1/4, disp)
		.cx(colmn41_x0+3*w1*weight_colmn1/4)
		
		disp = disp + steep;
		
	}
	//Текущие значения 
	var day = new Date(cur_time*1000+i*3600000);	
	var hour = day.getHours();
	var minutes = day.getMinutes();
	if (hour<10){hour="0"+hour;}
	if (minutes<10){minutes="0"+minutes;}	
	var text_time = draw.text(String(hour)+':'+String(minutes))
		.font({ family: 'Inconsolata', size: size_text_p })
		.move(w1*time_w/2, disp)
		.cx(w1*time_w/2)
	//Глубина забоя
	var text_time = draw.text(d110d[numbs110d-1]["Zaboj"])
	.font({ family: 'Inconsolata', size: size_text_p })
	.move(colmn1_x0+3*w1*weight_colmn1/4, disp)
	.cx(colmn1_x0+3*w1*weight_colmn1/4)
	
	//Положение долота
	var text_time = draw.text(d110d[numbs110d-1]["Instr"])
	.font({ family: 'Inconsolata', size: size_text_p })
	.move(colmn21_x0+3*w1*weight_colmn1/4, disp)
	.cx(colmn21_x0+3*w1*weight_colmn1/4)
	
	//Общий объем
	var text_time = draw.text(d110d[numbs110d-1]["Vobj"])
	.font({ family: 'Inconsolata', size: size_text_p })
	.move(colmn41_x0+3*w1*weight_colmn1/4, disp)
	.cx(colmn41_x0+3*w1*weight_colmn1/4)
	
	
	
	
	
	
	
	//Графики!!!!!!!!!!!!
	//Последняя запись
	var width_gxf_line = 1.5;
	//Последняя дата на рулетке
	
	lastHourRul = cur_time+((i+4)*3600);
	//percent = lastHourRul/d110d[numbs110d-1]["Vrema"];
	//alert (cur_time);
	//alert (beg_time);
	//1513710250 1513710250 
	//1513724650 1513767610 
	//4 минуты
	//1513754440
	//1513768700
	//1513769020 1513768880
	
	//alert (d110d[0]["Vrema"]);

	
	//Последняя запись
	var value='';
	var K_x1=(colmn11_x1 - colmn11_x0)/(r_p4 - l_p4)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul-d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn11_x0 + (d110d[j]["Mpot"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn11_x0) {cur_value_x = colmn11_x0}
	if (cur_value_x > colmn11_x1) {cur_value_x = colmn11_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color14 });
	
	//Последняя запись
	var value='';
	var K_x1=(colmn11_x1 - colmn11_x0)/(r_p3 - l_p3)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul-d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn11_x0 + (d110d[j]["Npot"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn11_x0) {cur_value_x = colmn11_x0}
	if (cur_value_x > colmn11_x1) {cur_value_x = colmn11_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color13 });
	
	//Последняя запись
	var value='';
	var K_x1=(colmn11_x1 - colmn11_x0)/(r_p2 - l_p2)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul-d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d-1;j++){
	cur_value_x = colmn11_x0 + (d110d[j]["Wdol"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn11_x0) {cur_value_x = colmn11_x0}
	if (cur_value_x > colmn11_x1) {cur_value_x = colmn11_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	
	}
	
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color12 });
	
	
	//Последняя запись
	var value='';
	var K_x1=(colmn11_x1 - colmn11_x0)/(r_p1 - l_p1)
	var cur_value_x = 0;
	var cur_value_x = 0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul - d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn11_x0 + (d110d[j]["Wkp"])*K_x1
	if (cur_value_x < colmn11_x0) {cur_value_x = colmn11_x0}
	if (cur_value_x > colmn11_x1) {cur_value_x = colmn11_x1}
	
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color11 });
	//alert(d);
	
	/////////////Второй	 столбик
	//Последняя запись
	var value='';
	var K_x1=(colmn21_x1 - colmn21_x0)/(r_p25 - l_p25)
	var cur_value_x = 0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul - d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn21_x0 + (d110d[j]["C1C5"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn21_x0) {cur_value_x = colmn21_x0}
	if (cur_value_x > colmn21_x1) {cur_value_x = colmn21_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';

	
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color25 });
	
	//Последняя запись
	var value='';
	var K_x1=(colmn21_x1 - colmn21_x0)/(r_p24 - l_p24)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul-d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn21_x0 + (d110d[j]["C1"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn21_x0) {cur_value_x = colmn21_x0}
	if (cur_value_x > colmn21_x1) {cur_value_x = colmn21_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color24 });
	
	//alert(d110d[0]["Talblok"]);
	//Последняя запись
	var value='';
	var K_x1=(colmn21_x1 - colmn21_x0)/(r_p23 - l_p23)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul-d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn21_x0 + (d110d[j]["Qbx"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn21_x0) {cur_value_x = colmn21_x0}
	if (cur_value_x > colmn21_x1) {cur_value_x = colmn21_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color23 });
	
	//Последняя запись
	var value='';
	var K_x1=(colmn21_x1 - colmn21_x0)/(r_p22 - l_p22)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul-d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn21_x0 + (d110d[j]["Talblok"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn21_x0) {cur_value_x = colmn21_x0}
	if (cur_value_x > colmn21_x1) {cur_value_x = colmn21_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color22 });
	
	//Последняя запись
	var value='';
	var K_x1=(colmn21_x1 - colmn21_x0)/(r_p21 - l_p21)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul-d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn21_x0 + (d110d[j]["Pbx"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn21_x0) {cur_value_x = colmn21_x0}
	if (cur_value_x > colmn21_x1) {cur_value_x = colmn21_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';

	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color21 });
	
	
	/////////////Третий	 столбик
	//Последняя запись
	var value='';
	var K_x1=(colmn31_x1 - colmn31_x0)/(r_p35 - l_p35)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul-d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn31_x0 + (colmn31_x1 - colmn31_x0)/2+(d110d[j]["Vinstr"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn31_x0) {cur_value_x = colmn31_x0}
	if (cur_value_x > colmn31_x1) {cur_value_x = colmn31_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color35 });
	
	//Последняя запись
	var value='';
	var K_x1=(colmn31_x1 - colmn31_x0)/(r_p34 - l_p34)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul-d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn31_x0 + (d110d[j]["Potok"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn31_x0) {cur_value_x = colmn31_x0}
	if (cur_value_x > colmn31_x1) {cur_value_x = colmn31_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color34 });
	
	//Последняя запись
	var value='';
	var K_x1=(colmn31_x1 - colmn31_x0)/(r_p33 - l_p33)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul-d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn31_x0 + (d110d[j]["Tbix"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn31_x0) {cur_value_x = colmn31_x0}
	if (cur_value_x > colmn31_x1) {cur_value_x = colmn31_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color33 });
	
	//Последняя запись
	var value='';
	var K_x1=(colmn31_x1 - colmn31_x0)/(r_p32 - l_p32)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul-d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn31_x0 + (d110d[j]["Xn2"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn31_x0) {cur_value_x = colmn31_x0}
	if (cur_value_x > colmn31_x1) {cur_value_x = colmn31_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';	
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color32 });
	
	//Последняя запись
	var value='';
	var K_x1=(colmn31_x1 - colmn31_x0)/(r_p31 - l_p31)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul-d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn31_x0 + (d110d[j]["Xn1"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn31_x0) {cur_value_x = colmn31_x0}
	if (cur_value_x > colmn31_x1) {cur_value_x = colmn31_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color31 });
	
	
	/////////////Четвертый	 столбик
	//Последняя запись
	var value='';
	var K_x1=(colmn41_x1 - colmn41_x0)/(r_p46 - l_p46)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul-d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn41_x0 + (d110d[j]["Vobj"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn41_x0) {cur_value_x = colmn41_x0}
	if (cur_value_x > colmn41_x1) {cur_value_x = colmn41_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color46 });
	
	
	
	//Последняя запись
	var value='';
	var K_x1=(colmn41_x1 - colmn41_x0)/(r_p45 - l_p45)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul-d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn41_x0 + (d110d[j]["Vdol"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn41_x0) {cur_value_x = colmn41_x0}
	if (cur_value_x > colmn41_x1) {cur_value_x = colmn41_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color45 });
	
	//Последняя запись
	var value='';
	var K_x1=(colmn41_x1 - colmn41_x0)/(r_p43 - l_p43)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul-d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn41_x0 + (d110d[j]["V3"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn41_x0) {cur_value_x = colmn41_x0}
	if (cur_value_x > colmn41_x1) {cur_value_x = colmn41_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color43 });
	
	//Последняя запись
	var value='';
	var K_x1=(colmn41_x1 - colmn41_x0)/(r_p44 - l_p44)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul-d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn41_x0 + (d110d[j]["V4"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn41_x0) {cur_value_x = colmn41_x0}
	if (cur_value_x > colmn41_x1) {cur_value_x = colmn41_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color44 });
	
	
	//Последняя запись
	var value='';
	var K_x1=(colmn41_x1 - colmn41_x0)/(r_p42 - l_p42)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul-d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn41_x0 + (d110d[j]["V2"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn41_x0) {cur_value_x = colmn41_x0}
	if (cur_value_x > colmn41_x1) {cur_value_x = colmn41_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color42 });
	
	
	//Последняя запись
	var value='';
	var K_x1=(colmn41_x1 - colmn41_x0)/(r_p41 - l_p41)
	var cur_value_x = 0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/(lastHourRul - d110d[0]["Vrema"]);
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn41_x0 + (d110d[j]["V1"])*K_x1
	cur_value_y = colmn11_y0 + (d110d[j]["Vrema"]-d110d[0]["Vrema"])*cur_value_y_step;
	if (cur_value_x < colmn41_x0) {cur_value_x = colmn41_x0}
	if (cur_value_x > colmn41_x1) {cur_value_x = colmn41_x1}
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: width_gxf_line, color: color41 });
	
	
	//alert(value);
	
	//
	
	gfx1.click(function() {
		//Клик
		//Высота области
		var height_value = 7;
		//Высота области
		var width_value = 14;
		//ЧИсло параметров
		var numb_value =5;
		//Шаг вертикального отступа
		var step_val = height_value/numb_value;
		
		var text_size_value = width_line_p +3;
		//alert(X_cur_mouse_click);
		//console.log(gfx1.attr(''));
		//var b = gfx1.attr('pointers').split(',').map(Number);
		//console.log(b);
		var gfxr = draw.polygon((X_cur_mouse_click-w1*(width_value/2-0.5))+','+(Y_cur_mouse_click -h1*(height_value+0.5)) +' '+(X_cur_mouse_click+w1*(width_value/2+0.5))+','+(Y_cur_mouse_click -h1*(height_value+0.5))+' '+(X_cur_mouse_click+w1*(width_value/2+0.5))+' '+Y_cur_mouse_click+' '+(X_cur_mouse_click-w1*(width_value/2-0.5))+' '+Y_cur_mouse_click)
		.fill({ color: '#ffd080' })
		.stroke({ width: width_gxf_line, dasharray: '3,5' });
		
		var cur_value_y_step_val = (h1*100 - colmn11_y0)/numbs110d;
		var disp_val1 = Math.round((Y_cur_mouse_click - colmn11_y0)/cur_value_y_step_val);
		//Значение1
		var text_value_11 = draw.text( d110d[disp_val1]["Wkp"] )
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value)
		.cx(X_cur_mouse_click)
		.fill(color11)
		
		//Значение2
		var text_value_12 = draw.text( d110d[disp_val1]["Wdol"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val)
		.cx(X_cur_mouse_click)
		.fill(color12)
		
		//Значение3
		var text_value_13 = draw.text(d110d[disp_val1]["Npot"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val*2)
		.cx(X_cur_mouse_click)
		.fill(color13)
		
		//Значение4
		var text_value_14 = draw.text(d110d[disp_val1]["Mpot"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val*3)
		.cx(X_cur_mouse_click)
		.fill(color14)
		
		//Значение4
		var text_value_15 = draw.text(d110d[disp_val1]["Zaboj"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val*4)
		.cx(X_cur_mouse_click)
		.fill(color15)

		
		//Визир
		gfxr.attr({'fill-opacity': 0.6});
		var gfxr_line = draw.line( '0 ,'+ Y_cur_mouse_click +' ' +(w1*100)+',' + Y_cur_mouse_click)
		.stroke({ width: width_gxf_line});
		
		//Группа
		var gfx_group = draw.group();
		gfx_group.add(gfxr);
		gfx_group.add(gfxr_line);
		gfx_group.add(text_value_11);
		gfx_group.add(text_value_12);
		gfx_group.add(text_value_13);
		gfx_group.add(text_value_14);
		gfx_group.add(text_value_15);
		
		//Удаление значения
		text_value_11.click(function() {
			this.remove();
			gfx_group.remove();
			})
		text_value_12.click(function() {
			this.remove();
			gfx_group.remove();
			})
		text_value_13.click(function() {
			this.remove();
			gfx_group.remove();
			})
		text_value_14.click(function() {
			this.remove();
			gfx_group.remove();
			})
			
		text_value_15.click(function() {
			this.remove();
			gfx_group.remove();
			})
			
		gfxr.click(function() {
			this.remove();
			gfx_group.remove();
			})
			
	});
	
	gfx2.click(function() {
		//Клик
		//Высота области
		var height_value = 8;
		//Высота области
		var width_value = 14;
		//ЧИсло параметров
		var numb_value =6;
		//Шаг вертикального отступа
		var step_val = height_value/numb_value;
		
		var text_size_value = width_line_p +3;
		var gfxr = draw.polygon((X_cur_mouse_click-w1*(width_value/2-0.5))+','+(Y_cur_mouse_click -h1*(height_value+0.5)) +' '+(X_cur_mouse_click+w1*(width_value/2+0.5))+','+(Y_cur_mouse_click -h1*(height_value+0.5))+' '+(X_cur_mouse_click+w1*(width_value/2+0.5))+' '+Y_cur_mouse_click+' '+(X_cur_mouse_click-w1*(width_value/2-0.5))+' '+Y_cur_mouse_click)
		.fill({ color: '#ffd080' })
		.stroke({ width: width_gxf_line, dasharray: '3,5' });
		
		var cur_value_y_step_val = (h1*100 - colmn11_y0)/numbs110d;
		var disp_val1 = Math.round((Y_cur_mouse_click - colmn11_y0)/cur_value_y_step_val);
		//Значение1
		var text_value_11 = draw.text( d110d[disp_val1]["Pbx"] )
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value)
		.cx(X_cur_mouse_click)
		.fill(color21)
		
		//Значение2
		var text_value_12 = draw.text( d110d[disp_val1]["Talblok"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val)
		.cx(X_cur_mouse_click)
		.fill(color22)
		
		//Значение3
		var text_value_13 = draw.text(d110d[disp_val1]["Qbx"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val*2)
		.cx(X_cur_mouse_click)
		.fill(color23)
		
		//Значение4
		var text_value_14 = draw.text(d110d[disp_val1]["C1"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val*3)
		.cx(X_cur_mouse_click)
		.fill(color24)
		
		//Значение5
		var text_value_15 = draw.text(d110d[disp_val1]["C1C5"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val*4)
		.cx(X_cur_mouse_click)
		.fill(color25)
		
		//Значение6
		var text_value_16 = draw.text(d110d[disp_val1]["Instr"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val*5)
		.cx(X_cur_mouse_click)
		.fill(color26)

		
		//Визир
		gfxr.attr({'fill-opacity': 0.6});
		var gfxr_line = draw.line( '0 ,'+ Y_cur_mouse_click +' ' +(w1*100)+',' + Y_cur_mouse_click)
		.stroke({ width: width_gxf_line});
		
		//Группа
		var gfx_group = draw.group();
		gfx_group.add(gfxr);
		gfx_group.add(gfxr_line);
		gfx_group.add(text_value_11);
		gfx_group.add(text_value_12);
		gfx_group.add(text_value_13);
		gfx_group.add(text_value_14);
		gfx_group.add(text_value_15);
		gfx_group.add(text_value_16);
		
		//Удаление значения
		text_value_11.click(function() {
			this.remove();
			gfx_group.remove();
			})
		text_value_12.click(function() {
			this.remove();
			gfx_group.remove();
			})
		text_value_13.click(function() {
			this.remove();
			gfx_group.remove();
			})
		text_value_14.click(function() {
			this.remove();
			gfx_group.remove();
			})
		text_value_15.click(function() {
			this.remove();
			gfx_group.remove();
			})
		text_value_16.click(function() {
			this.remove();
			gfx_group.remove();
			})
			
		gfxr.click(function() {
			this.remove();
			gfx_group.remove();
			})
			

	});
	
	
	gfx3.click(function() {
		//Клик
		//Высота области
		var height_value = 7;
		//Высота области
		var width_value = 14;
		//ЧИсло параметров
		var numb_value =5;
		//Шаг вертикального отступа
		var step_val = height_value/numb_value;
		
		var text_size_value = width_line_p +3;
		var gfxr = draw.polygon((X_cur_mouse_click-w1*(width_value/2-0.5))+','+(Y_cur_mouse_click -h1*(height_value+0.5)) +' '+(X_cur_mouse_click+w1*(width_value/2+0.5))+','+(Y_cur_mouse_click -h1*(height_value+0.5))+' '+(X_cur_mouse_click+w1*(width_value/2+0.5))+' '+Y_cur_mouse_click+' '+(X_cur_mouse_click-w1*(width_value/2-0.5))+' '+Y_cur_mouse_click)
		.fill({ color: '#ffd080' })
		.stroke({ width: width_gxf_line, dasharray: '3,5' });
		
		var cur_value_y_step_val = (h1*100 - colmn11_y0)/numbs110d;
		var disp_val1 = Math.round((Y_cur_mouse_click - colmn11_y0)/cur_value_y_step_val);
		//Значение1
		var text_value_11 = draw.text( d110d[disp_val1]["Xn1"] )
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value)
		.cx(X_cur_mouse_click)
		.fill(color31)
		
		//Значение2
		var text_value_12 = draw.text( d110d[disp_val1]["Xn2"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val)
		.cx(X_cur_mouse_click)
		.fill(color32)
		
		//Значение3
		var text_value_13 = draw.text(d110d[disp_val1]["Tbix"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val*2)
		.cx(X_cur_mouse_click)
		.fill(color33)
		
		//Значение4
		var text_value_14 = draw.text(d110d[disp_val1]["Potok"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val*3)
		.cx(X_cur_mouse_click)
		.fill(color34)
		
		//Значение5
		var text_value_15 = draw.text(d110d[disp_val1]["Vinstr"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val*4)
		.cx(X_cur_mouse_click)
		.fill(color35)

		
		//Визир
		gfxr.attr({'fill-opacity': 0.5});
		var gfxr_line = draw.line( '0 ,'+ Y_cur_mouse_click +' ' +(w1*100)+',' + Y_cur_mouse_click)
		.stroke({ width: width_gxf_line});
		
		//Группа
		var gfx_group = draw.group();
		gfx_group.add(gfxr);
		gfx_group.add(gfxr_line);
		gfx_group.add(text_value_11);
		gfx_group.add(text_value_12);
		gfx_group.add(text_value_13);
		gfx_group.add(text_value_14);
		gfx_group.add(text_value_15);
		
		//Удаление значения
		text_value_11.click(function() {
			this.remove();
			gfx_group.remove();
			})
		text_value_12.click(function() {
			this.remove();
			gfx_group.remove();
			})
		text_value_13.click(function() {
			this.remove();
			gfx_group.remove();
			})
		text_value_14.click(function() {
			this.remove();
			gfx_group.remove();
			})
		text_value_15.click(function() {
			this.remove();
			gfx_group.remove();
			})
			
		gfxr.click(function() {
			this.remove();
			gfx_group.remove();
			})
			

	});
	
	gfx4.click(function() {
		//Клик
		//Высота области
		var height_value = 9;
		//Высота области
		var width_value = 14;
		//ЧИсло параметров
		var numb_value =6;
		//Шаг вертикального отступа
		var step_val = height_value/numb_value;
		
		var text_size_value = width_line_p +3;
		var gfxr = draw.polygon((X_cur_mouse_click-w1*(width_value/2-0.5))+','+(Y_cur_mouse_click -h1*(height_value+0.5)) +' '+(X_cur_mouse_click+w1*(width_value/2+0.5))+','+(Y_cur_mouse_click -h1*(height_value+0.5))+' '+(X_cur_mouse_click+w1*(width_value/2+0.5))+' '+Y_cur_mouse_click+' '+(X_cur_mouse_click-w1*(width_value/2-0.5))+' '+Y_cur_mouse_click)
		.fill({ color: '#ffd080' })
		.stroke({ width: width_gxf_line, dasharray: '3,5' });
		
		var cur_value_y_step_val = (h1*100 - colmn11_y0)/numbs110d;
		var disp_val1 = Math.round((Y_cur_mouse_click - colmn11_y0)/cur_value_y_step_val);
		//Значение1
		var text_value_11 = draw.text( d110d[disp_val1]["V1"] )
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value)
		.cx(X_cur_mouse_click)
		.fill(color41)
		
		//Значение2
		var text_value_12 = draw.text( d110d[disp_val1]["V2"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val)
		.cx(X_cur_mouse_click)
		.fill(color42)
		
		//Значение3
		var text_value_13 = draw.text(d110d[disp_val1]["V3"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val*2)
		.cx(X_cur_mouse_click)
		.fill(color43)
		
		//Значение4
		var text_value_14 = draw.text(d110d[disp_val1]["V4"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val*3)
		.cx(X_cur_mouse_click)
		.fill(color44)
		
		//Значение5
		var text_value_15 = draw.text(d110d[disp_val1]["Vdol"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val*4)
		.cx(X_cur_mouse_click)
		.fill(color45)
		
		//Значение6
		var text_value_16 = draw.text(d110d[disp_val1]["Vobj"])
		.font({ family: 'Inconsolata', size: size_text_p +3})
		.move(X_cur_mouse_click, Y_cur_mouse_click -h1*height_value + h1*step_val*5)
		.cx(X_cur_mouse_click)
		.fill(color46)

		
		//Визир
		gfxr.attr({'fill-opacity': 0.5});
		var gfxr_line = draw.line( '0 ,'+ Y_cur_mouse_click +' ' +(w1*100)+',' + Y_cur_mouse_click)
		.stroke({ width: width_gxf_line});
		
		//Группа
		var gfx_group = draw.group();
		gfx_group.add(gfxr);
		gfx_group.add(gfxr_line);
		gfx_group.add(text_value_11);
		gfx_group.add(text_value_12);
		gfx_group.add(text_value_13);
		gfx_group.add(text_value_14);
		gfx_group.add(text_value_15);
		gfx_group.add(text_value_16);
		
		//Удаление значения
		text_value_11.click(function() {
			this.remove();
			gfx_group.remove();
			})
		text_value_12.click(function() {
			this.remove();
			gfx_group.remove();
			})
		text_value_13.click(function() {
			this.remove();
			gfx_group.remove();
			})
		text_value_14.click(function() {
			this.remove();
			gfx_group.remove();
			})
		text_value_15.click(function() {
			this.remove();
			gfx_group.remove();
			})
		text_value_16.click(function() {
			this.remove();
			gfx_group.remove();
			})
			
		gfxr.click(function() {
			this.remove();
			gfx_group.remove();
			})
			

	});
	//Первый параметр
	/*
	Wkp=-100.0
	Wdol=-100.0
	Mpot=-100.0
	Npot=-100.0
	Pbx=-100.0
	Qbx=-100.0
	Talblok=-100.0
	C1C5=-100.0
	C1=-100.0
	Xn1=-100.0
	Xn2=-100.0
	Potok=-100.0
	Tbix=-100.0
	V1=-100.0
	V2=-100.0
	V3=-100.0
	V4=-100.0
	Vdol=-100.0
	Vobj=-100.0
	Zaboj=-100.0
	Instr=-100.0
	Vrema=-100
	*/
	
	/*
	//Последняя запись
	var value='';
	var K_x1=(colmn11_x1 - colmn11_x0)/(r_p1 - l_p1)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/numbs110d;
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn11_x0 + (d110d[numbs110d-1]["Mpot"])*K_x1
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	cur_value_y = cur_value_y + cur_value_y_step;
	
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: 1.5, color: color13 });
	
	//Последняя запись
	var value='';
	var K_x1=(colmn11_x1 - colmn11_x0)/(r_p1 - l_p1)
	var cur_value_x = 0;
	var cur_value_y = colmn11_y0;
	var cur_value_y_step = (h1*100 - colmn11_y0)/numbs110d;
	for (var j=0; j< numbs110d;j++){
	cur_value_x = colmn11_x0 + (d110d[numbs110d-1]["Npot"])*K_x1
	value = value + cur_value_x;
	value = value +',' + cur_value_y+ ' ';
	cur_value_y = cur_value_y + cur_value_y_step;
	
	}
	var polyline = draw.polyline(value).fill('none').stroke({ width: 1.5, color: color14 });
	
	*/
	//alert(value);
	//Mpot=-100.0
	//Npot=-100.0
	//Полилиния
	//#var polyline = draw.polyline('0,0 100,50 50,100').fill('#bababa').stroke({ width: 1 })


	//Сдвиг всех элементов
	//group_time_rul.dmove(100,100);!!!
	

	
	//console.log(teeth);
	//alert (disp);
	//alert (steep);
	
}


function touch_value(){
		var point = path.point(e.screenX, e.screenY)
		alert("MEGA");
		alert("x: "+point+" y:");
	}