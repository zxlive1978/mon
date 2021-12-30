

var chart;
$(function() {
  try{
  //prepare values
  data = []; 
  data10 = [];
  data11 = [];
  data22 = [];
  mdata10 = [];
  mdata11 = [];
  mldata10 = [];
  mldata11 = [];
  t4 =0;
  for (var t = 0; t < numbs916; t++){
    data.push({x: d916[t]["date"]/1, y: d916[t]["value"]});
	if (t>0){
		rx1=100*(Number(d916[t]["tx"])-Number(d916[t-1]["tx"]))/(Number(d916[t]["date"]/1) - Number(d916[t-1]["date"]/1));
		tx1=100*(Number(d916[t]["rx"])-Number(d916[t-1]["rx"]))/(Number(d916[t]["date"]/1) - Number(d916[t-1]["date"]/1));
	} else {rx1=(100*(d916[t]["tx"]))/1; tx1=(100*(d916[t]["rx"]))/1;}
	mrx1=(10000*(d916[t]["mtx"]))/100;
	mtx1=(10000*(d916[t]["mrx"]))/100;
	ml1=(100*(d916[t]["ml"]))/1;
	mlrx1=((d916[t]["mltx"]))/1;
	mltx1=((d916[t]["mlrx"]))/1;
	data10.push({x: d916[t]["date"]/1, y: rx1 });
	data11.push({x: d916[t]["date"]/1, y: tx1 });
	mdata10.push({x: d916[t]["date"]/1, y: mrx1 });
	mdata11.push({x: d916[t]["date"]/1, y: mtx1 });
	mldata10.push({x: d916[t]["date"]/1, y: mlrx1 });
	mldata11.push({x: d916[t]["date"]/1, y: mltx1 });
	data22.push({x: d916[t]["date"]/1, y: ml1 });
	
	}
  
  chart = new JSGadget.Chart($("#chart"), { //create chart
  trends: [new JSGadget.ATrend({color: "green", width: 1}),new JSGadget.ATrend({color: "Violet", width: 1}),new JSGadget.ATrend({color: "orange", width: 1}),new JSGadget.ATrend({color: "IndianRed", width: 1}),new JSGadget.ATrend({color: "teal", width: 1}),new JSGadget.ATrend({color: "blue", width: 1}),new JSGadget.ATrend({color: "Black", width: 1}),new JSGadget.ATrend({color: "Maroon", width: 1})]
 });
 
  chart.trends[0].data = data22;
  chart.trends[1].data = data10;
  chart.trends[2].data = data11;
  chart.trends[3].data = mdata10;
  chart.trends[4].data = mdata11;
  chart.trends[5].data = data;
  chart.trends[6].data = mldata10;
  chart.trends[7].data = mldata11;
  
  chart.bAxis.setMinMax(d916[0]["date"]/1, d916[numbs916-1]["date"]/1); //set x limits
  chart.lAxis.setMinMax(-1.1, 400.1); //set y limits
  chart.draw(); //draw chart  
}catch(e){}});


var chart2;
$(function() {
  try{
  //prepare values
  data2 = []; //data array
  data12 = [];
  data13 = [];
  data23 = [];
  mdata12 = [];
  mdata13 = [];
  mldata12 = [];
  mldata13 = [];
  for (var t = 0; t < numbs4450; t++){
    data2.push({x: d4450[t]["date"]/1, y: d4450[t]["value"]}); 
	if (t>0){
		rx1=100*(Number(d4450[t]["tx"])-Number(d4450[t-1]["tx"]))/(Number(d4450[t]["date"]/1) - Number(d4450[t-1]["date"]/1));
		tx1=100*(Number(d4450[t]["rx"])-Number(d4450[t-1]["rx"]))/(Number(d4450[t]["date"]/1) - Number(d4450[t-1]["date"]/1));
	} else {rx1=(100*(d4450[t]["tx"]))/1; tx1=(100*(d4450[t]["rx"]))/1;}
	mrx1=(10000*(d4450[t]["mtx"]))/100;
	mtx1=(10000*(d4450[t]["mrx"]))/100;
	mlrx1=((d4450[t]["mltx"]))/1;
	mltx1=((d4450[t]["mlrx"]))/1;
	ml1=(100*(d4450[t]["ml"]))/1;
	data12.push({x: d4450[t]["date"]/1, y: rx1 });
	data13.push({x: d4450[t]["date"]/1, y: tx1 });
	mdata12.push({x: d4450[t]["date"]/1, y: mrx1 });
	mdata13.push({x: d4450[t]["date"]/1, y: mtx1 });
	mldata12.push({x: d4450[t]["date"]/1, y: mlrx1 });
	mldata13.push({x: d4450[t]["date"]/1, y: mltx1 });
	data23.push({x: d4450[t]["date"]/1, y: ml1 });
	}
  //create and draw chart
  chart2 = new JSGadget.Chart($("#chart2"), { //create chart
  trends: [new JSGadget.ATrend({color: "green", width: 1}),new JSGadget.ATrend({color: "Violet", width: 1}),new JSGadget.ATrend({color: "orange", width: 1}),new JSGadget.ATrend({color: "IndianRed", width: 1}),new JSGadget.ATrend({color: "teal", width: 1}),new JSGadget.ATrend({color: "blue", width: 1}),new JSGadget.ATrend({color: "Black", width: 1}),new JSGadget.ATrend({color: "Maroon", width: 1})]
  });
 
  chart2.trends[0].data = data23;
  chart2.trends[1].data = data12;
  chart2.trends[2].data = data13;
  chart2.trends[3].data = mdata12;
  chart2.trends[4].data = mdata13;
  chart2.trends[5].data = data2;
  chart2.trends[6].data = mldata12;
  chart2.trends[7].data = mldata13;
  
  chart2.bAxis.setMinMax(d4450[0]["date"]/1, d4450[numbs4450-1]["date"]/1); //set x limits
  chart2.lAxis.setMinMax(-1.1, 400.1); //set y limits
  chart2.draw(); //draw chart  
}catch(e){}});

var chart3;
$(function() {
  try{
  //prepare values
  data3 = []; //data array
  data14 = [];
  data15 = [];
  data24 = [];
  mdata14 = [];
  mdata15 = [];
  mldata14 = [];
  mldata15 = [];
  luchdata14 = [];
  luchdata15 = [];
  for (var t = 0; t < numbs631; t++){
    data3.push({x: d631[t]["date"]/1, y: d631[t]["value"]});
	if (t>0 && (Number(d631[t]["tx"]))>0 && (Number(d631[t]["rx"])>0)&& (Number(d631[t-1]["tx"]))>0 && (Number(d631[t-1]["rx"])>0)){
		rx1=100*(Number(d631[t]["tx"])-Number(d631[t-1]["tx"]))/(Number(d631[t]["date"]/1) - Number(d631[t-1]["date"]/1));
		tx1=100*(Number(d631[t]["rx"])-Number(d631[t-1]["rx"]))/(Number(d631[t]["date"]/1) - Number(d631[t-1]["date"]/1));
	} else {rx1=(100*(d631[t]["tx"]))/1; tx1=(100*(d631[t]["rx"]))/1;}
	mrx1=(10000*(d631[t]["mtx"]))/100;
	mtx1=(10000*(d631[t]["mrx"]))/100;
	mlrx1=((d631[t]["mltx"]))/1;
	mltx1=((d631[t]["mlrx"]))/1;
	//console.log(Number(d631[t]["luchtx"]));
	if (t>0){
		
		if ((Number(d631[t]["luchtx"]))>0) {
			luchtx1=300;}
		else {luchtx1=0;}
		
		if (Number(d631[t]["luchtx"])==-1){
			luchtx1=280;
			//console.log(Number(d631[t]["luchtx"]));
		}
	}else{
		if (Number(d631[t]["luchtx"])>0){
			luchtx1=300;
		} else {luchtx1=0;}
	} 
	luchrx1=((d631[t]["luchtx"])/10);
	ml1=(100*(d631[t]["ml"]))/1;
	data14.push({x: d631[t]["date"]/1, y: rx1 });
	data15.push({x: d631[t]["date"]/1, y: tx1 });
	mdata14.push({x: d631[t]["date"]/1, y: mrx1 });
	mdata15.push({x: d631[t]["date"]/1, y: mtx1 });
	mldata14.push({x: d631[t]["date"]/1, y: mlrx1 });
	mldata15.push({x: d631[t]["date"]/1, y: mltx1 });
	data24.push({x: d631[t]["date"]/1, y: ml1 });
	luchdata14.push({x: d631[t]["date"]/1, y: luchrx1 });
	luchdata15.push({x: d631[t]["date"]/1, y: luchtx1 });
	}
  //create and draw chart
  chart3 = new JSGadget.Chart($("#chart3"), { //create chart
  trends: [new JSGadget.ATrend({color: "green", width: 1}),new JSGadget.ATrend({color: "Violet", width: 1}),new JSGadget.ATrend({color: "orange", width: 1}),new JSGadget.ATrend({color: "IndianRed", width: 1}),new JSGadget.ATrend({color: "teal", width: 1}),new JSGadget.ATrend({color: "blue", width: 1}),new JSGadget.ATrend({color: "Black", width: 1}),new JSGadget.ATrend({color: "Maroon", width: 1}),new JSGadget.ATrend({color: "Red", width: 1}),new JSGadget.ATrend({color: "Red", width: 1})]
  });
 
  chart3.trends[0].data = data24;
  chart3.trends[1].data = data14;
  chart3.trends[2].data = data15;
  chart3.trends[3].data = mdata14;
  chart3.trends[4].data = mdata15;
  chart3.trends[5].data = data3;
  chart3.trends[6].data = mldata14;
  chart3.trends[7].data = mldata15;
  chart3.trends[8].data = luchdata14;
  chart3.trends[9].data = luchdata15;
  
  chart3.bAxis.setMinMax(d631[0]["date"]/1, d631[numbs631-1]["date"]/1); //set x limits
  chart3.lAxis.setMinMax(-1.1, 400.1); //set y limits
  chart3.draw(); //draw chart  
}catch(e){}});

var chart4;
$(function() {
  try{
  //prepare values
  data4 = []; //data array
  data16 = [];
  data17 = [];
  data25 = [];
  mdata16 = [];
  mdata17 = [];
  mldata16 = [];
  mldata17 = [];
  for (var t = 0; t < numbs110; t++){
    data4.push({x: d110[t]["date"]/1, y: d110[t]["value"]});
	if (t>0){
		rx1=100*(Number(d110[t]["tx"])-Number(d110[t-1]["tx"]))/(Number(d110[t]["date"]/1) - Number(d110[t-1]["date"]/1));
		tx1=100*(Number(d110[t]["rx"])-Number(d110[t-1]["rx"]))/(Number(d110[t]["date"]/1) - Number(d110[t-1]["date"]/1));
	} else {rx1=(100*(d110[t]["tx"]))/1; tx1=(100*(d110[t]["rx"]))/1;}
	mrx1=(10000*(d110[t]["mtx"]))/100;
	mtx1=(10000*(d110[t]["mrx"]))/100;
	ml1=(100*(d110[t]["ml"]))/1;
	mlrx1=((d110[t]["mltx"]))/1;
	mltx1=((d110[t]["mlrx"]))/1;
	data16.push({x: d110[t]["date"]/1, y: rx1 });
	data17.push({x: d110[t]["date"]/1, y: tx1 });
	mdata16.push({x: d110[t]["date"]/1, y: mrx1 });
	mdata17.push({x: d110[t]["date"]/1, y: mtx1 });
	mldata16.push({x: d110[t]["date"]/1, y: mlrx1 });
	mldata17.push({x: d110[t]["date"]/1, y: mltx1 });
	
	data25.push({x: d110[t]["date"]/1, y: ml1 });
  }
  //create and draw chart
  chart4 = new JSGadget.Chart($("#chart4"), { //create chart
  trends: [new JSGadget.ATrend({color: "green", width: 1}),new JSGadget.ATrend({color: "Violet", width: 1}),new JSGadget.ATrend({color: "orange", width: 1}),new JSGadget.ATrend({color: "IndianRed", width: 1}),new JSGadget.ATrend({color: "teal", width: 1}),new JSGadget.ATrend({color: "blue", width: 1}),new JSGadget.ATrend({color: "Black", width: 1}),new JSGadget.ATrend({color: "Maroon", width: 1})]
  });
 
  chart4.trends[0].data = data25;
  chart4.trends[1].data = data16;
  chart4.trends[2].data = data17;
  chart4.trends[3].data = mdata16;
  chart4.trends[4].data = mdata17;
  chart4.trends[5].data = data4;
  chart4.trends[6].data = mldata16;
  chart4.trends[7].data = mldata17;
  chart4.bAxis.setMinMax(d110[0]["date"]/1, d110[numbs110-1]["date"]/1); //set x limits
  chart4.lAxis.setMinMax(-1.1, 400.1); //set y limits
  chart4.draw(); //draw chart  
}catch(e){}});

var chart5;
$(function() {
  try{
  //prepare values
  data5 = []; //data array
  data18 = [];
  data19 = [];
  data26 = [];
  mdata18 = [];
  mdata19 = [];
  mldata18 = [];
  mldata19 = [];
  luchdata14 = [];
  luchdata15 = [];
  for (var t = 0; t < numbs224; t++) {
    data5.push({x: d224[t]["date"]/1, y: d224[t]["value"]});
	if (t>0){
		rx1=100*(Number(d224[t]["tx"])-Number(d224[t-1]["tx"]))/(Number(d224[t]["date"]/1) - Number(d224[t-1]["date"]/1));
		tx1=100*(Number(d224[t]["rx"])-Number(d224[t-1]["rx"]))/(Number(d224[t]["date"]/1) - Number(d224[t-1]["date"]/1));
	} else {rx1=(100*(d224[t]["tx"]))/1; tx1=(100*(d224[t]["rx"]))/1;}
	mrx1=(10000*(d224[t]["mtx"]))/100;
	mtx1=(10000*(d224[t]["mrx"]))/100;
	mlrx1=((d224[t]["mltx"]))/1;
	mltx1=((d224[t]["mlrx"]))/1;
  
  if (t>0){
		
		if ((Number(d224[t]["luchtx"]))>0) {
			luchtx1=300;}
		else {luchtx1=0;}
		
		if (Number(d224[t]["luchtx"])==-1){
			luchtx1=280;
			//console.log(Number(d631[t]["luchtx"]));
		}
	}else{
		if (Number(d224[t]["luchtx"])>0){
			luchtx1=300;
		} else {luchtx1=0;}
	} 
  luchrx1=((d224[t]["luchtx"])/10);
  ml1=(100*(d224[t]["ml"]))/1;
  
	data18.push({x: d224[t]["date"]/1, y: rx1 });
	data19.push({x: d224[t]["date"]/1, y: tx1 });
	mdata18.push({x: d224[t]["date"]/1, y: mrx1 });
	mdata19.push({x: d224[t]["date"]/1, y: mtx1 });
	mldata18.push({x: d224[t]["date"]/1, y: mlrx1 });
	mldata19.push({x: d224[t]["date"]/1, y: mltx1 });
  data26.push({x: d224[t]["date"]/1, y: ml1 });
  luchdata14.push({x: d224[t]["date"]/1, y: luchrx1 });
	luchdata15.push({x: d224[t]["date"]/1, y: luchtx1 });
  }
  chart5 = new JSGadget.Chart($("#chart5"), { //create chart
  trends: [new JSGadget.ATrend({color: "green", width: 1}),new JSGadget.ATrend({color: "Violet", width: 1}),new JSGadget.ATrend({color: "orange", width: 1}),new JSGadget.ATrend({color: "IndianRed", width: 1}),new JSGadget.ATrend({color: "teal", width: 1}),new JSGadget.ATrend({color: "blue", width: 1}),new JSGadget.ATrend({color: "Black", width: 1}),new JSGadget.ATrend({color: "Maroon", width: 1}),new JSGadget.ATrend({color: "Red", width: 1}),new JSGadget.ATrend({color: "Red", width: 1})]
  });
  chart5.trends[0].data = data26;
  chart5.trends[1].data = data18;
  chart5.trends[2].data = data19;
  chart5.trends[3].data = mdata18;
  chart5.trends[4].data = mdata19;
  chart5.trends[5].data = data5;
  chart5.trends[6].data = mldata18;
  chart5.trends[7].data = mldata19;
  chart5.trends[8].data = luchdata14;
  chart5.trends[9].data = luchdata15;
  
 // chart5.trends[1].data = data6; //set data
  chart5.bAxis.setMinMax(d224[0]["date"]/1, d224[numbs224-1]["date"]/1); //set x limits
  chart5.lAxis.setMinMax(-1.1, 400.1); //set y limits
  chart5.draw(); //draw chart  
}catch(e){}});


var chart6;
$(function() {
  try{
  //prepare values
  data6 = []; //data array
  data20 = [];
  data21 = [];
  data27 = [];
  mdata20 = [];
  mdata21 = [];
  mldata20 = [];
  mldata21 = [];
  for (var t = 0; t < numbs908; t++){
    data6.push({x: d908[t]["date"]/1, y: d908[t]["value"]}); 
	if (t>0){
		rx1=100*(Number(d908[t]["tx"])-Number(d908[t-1]["tx"]))/(Number(d908[t]["date"]/1) - Number(d908[t-1]["date"]/1));
		tx1=100*(Number(d908[t]["rx"])-Number(d908[t-1]["rx"]))/(Number(d908[t]["date"]/1) - Number(d908[t-1]["date"]/1));
	} else {rx1=(100*(d908[t]["tx"]))/1; tx1=(100*(d908[t]["rx"]))/1;}
	mrx1=(10000*(d908[t]["mtx"]))/100;
	mtx1=(10000*(d908[t]["mrx"]))/100;
	mlrx1=((d908[t]["mltx"]))/1;
	mltx1=((d908[t]["mlrx"]))/1;
	ml1=(100*(d908[t]["ml"]))/1;
	data20.push({x: d908[t]["date"]/1, y: rx1 });
	data21.push({x: d908[t]["date"]/1, y: tx1 });
	mdata20.push({x: d908[t]["date"]/1, y: mrx1 });
	mdata21.push({x: d908[t]["date"]/1, y: mtx1 });
	mldata20.push({x: d908[t]["date"]/1, y: mlrx1 });
	mldata21.push({x: d908[t]["date"]/1, y: mltx1 });
	data27.push({x: d908[t]["date"]/1, y: ml1 });
  }
  //create and draw chart
  chart6 = new JSGadget.Chart($("#chart6"), { //create chart
  trends: [new JSGadget.ATrend({color: "green", width: 1}),new JSGadget.ATrend({color: "Violet", width: 1}),new JSGadget.ATrend({color: "orange", width: 1}),new JSGadget.ATrend({color: "IndianRed", width: 1}),new JSGadget.ATrend({color: "teal", width: 1}),new JSGadget.ATrend({color: "blue", width: 1}),new JSGadget.ATrend({color: "Black", width: 1}),new JSGadget.ATrend({color: "Maroon", width: 1})]
  });
 
  chart6.trends[0].data = data27;
  chart6.trends[1].data = data20;
  chart6.trends[2].data = data21;
  chart6.trends[3].data = mdata20;
  chart6.trends[4].data = mdata21;
  chart6.trends[5].data = data6;
  chart6.trends[6].data = mldata20;
  chart6.trends[7].data = mldata21;
  chart6.bAxis.setMinMax(d908[0]["date"]/1, d908[numbs908-1]["date"]/1); //set x limits
  chart6.lAxis.setMinMax(-1.1, 400.1); //set y limits
  chart6.draw(); //draw chart  
}catch(e){}});


var chart7;
$(function() {
  try{
  //prepare values
  data7 = []; 
  data8 = [];
  data9 = [];
  data28 = [];
  mdata8 = [];
  mdata9 = [];
  mldata8 = [];
  mldata9 = [];
  for (var t = 0; t < numbs411; t++){
    data7.push({x: d411[t]["date"]/1, y: d411[t]["value"]});
	if (t>0){
		rx1=100*(Number(d411[t]["tx"])-Number(d411[t-1]["tx"]))/(Number(d411[t]["date"]/1) - Number(d411[t-1]["date"]/1));
		tx1=100*(Number(d411[t]["rx"])-Number(d411[t-1]["rx"]))/(Number(d411[t]["date"]/1) - Number(d411[t-1]["date"]/1));
	} else {rx1=(100*(d411[t]["tx"]))/1; tx1=(100*(d411[t]["rx"]))/1;}
	mrx1=(10000*(d411[t]["mtx"]))/100;
	mtx1=(10000*(d411[t]["mrx"]))/100;
	mlrx1=((d411[t]["mltx"]))/1;
	mltx1=((d411[t]["mlrx"]))/1;
	ml1=(100*(d411[t]["ml"]))/1;
	data8.push({x: d411[t]["date"]/1, y: rx1 });
	data9.push({x: d411[t]["date"]/1, y: tx1 });
	mdata8.push({x: d411[t]["date"]/1, y: mrx1 });
	mdata9.push({x: d411[t]["date"]/1, y: mtx1 });
	mldata8.push({x: d411[t]["date"]/1, y: mlrx1 });
	mldata9.push({x: d411[t]["date"]/1, y: mltx1 });
	data28.push({x: d411[t]["date"]/1, y: ml1 });
	}
  
  chart7 = new JSGadget.Chart($("#chart7"), { //create chart
  trends: [new JSGadget.ATrend({color: "green", width: 1}),new JSGadget.ATrend({color: "Violet", width: 1}),new JSGadget.ATrend({color: "orange", width: 1}),new JSGadget.ATrend({color: "IndianRed", width: 1}),new JSGadget.ATrend({color: "teal", width: 1}),new JSGadget.ATrend({color: "blue", width: 1}),new JSGadget.ATrend({color: "Black", width: 1}),new JSGadget.ATrend({color: "Maroon", width: 1})]
 });
 
  chart7.trends[0].data = data28;
  chart7.trends[1].data = data8;
  chart7.trends[2].data = data9;
  chart7.trends[3].data = mdata8;
  chart7.trends[4].data = mdata9;
  chart7.trends[5].data = data7;
  chart7.trends[6].data = mldata8;
  chart7.trends[7].data = mldata9;
  
  chart7.bAxis.setMinMax(d411[0]["date"]/1, d411[numbs411-1]["date"]/1); //set x limits
  chart7.lAxis.setMinMax(-1.1, 400.1); //set y limits
  chart7.draw(); //draw chart  
}catch(e){}});


var chart8;
$(function() {
  try{
  //prepare values
  data29 = []; 
  data30 = [];
  data31= [];
  data32 = [];
  data40 = [];
  for (var t = 0; t < numbsconn; t++){
    data29.push({x: dconn[t]["date"]/1, y: dconn[t]["p8888"]/1});
	data30.push({x: dconn[t]["date"]/1, y: dconn[t]["p6222055149"]/1});
	data31.push({x: dconn[t]["date"]/1, y: dconn[t]["p8084114180"]/1});
	data32.push({x: dconn[t]["date"]/1, y: dconn[t]["p192168773"]/1});
	data40.push({x: dconn[t]["date"]/1, y: dconn[t]["p31173187210"]/1});
	}
  
  chart8 = new JSGadget.Chart($("#chart8"), { //create chart
  trends: [new JSGadget.ATrend({color: "green", width: 1}),new JSGadget.ATrend({color: "Violet", width: 1}),new JSGadget.ATrend({color: "orange", width: 1}),new JSGadget.ATrend({color: "blue", width: 1}),new JSGadget.ATrend({color: "Purple", width: 1})]
 });
 
  chart8.trends[0].data = data29;
  chart8.trends[1].data = data30;
  chart8.trends[2].data = data31;
  chart8.trends[3].data = data32;
  chart8.trends[4].data = data40;
  chart8.bAxis.setMinMax(dconn[0]["date"]/1, dconn[numbsconn-1]["date"]/1); //set x limits
  chart8.lAxis.setMinMax(-1.1, 200.1); //set y limits
  chart8.draw(); //draw chart  
}catch(e){}});

var chart9;
$(function() {
  try{
  //prepare values
  data33 = []; 
  data34 = [];
  data35 = [];
  data36 = [];
  mdata34 = [];
  mdata35 = [];
  mldata34 = [];
  mldata35 = [];
  for (var t = 0; t < numbs89; t++){
    data33.push({x: d89[t]["date"]/1, y: d89[t]["value"]}); 
	if (t>0){
		rx1=100*(Number(d89[t]["rx"])-Number(d89[t-1]["rx"]))/(Number(d89[t]["date"]/1) - Number(d89[t-1]["date"]/1));
		tx1=100*(Number(d89[t]["tx"])-Number(d89[t-1]["tx"]))/(Number(d89[t]["date"]/1) - Number(d89[t-1]["date"]/1));
	} else {rx1=(100*(d89[t]["rx"]))/1; tx1=(100*(d89[t]["tx"]))/1;}
	mrx1=(10000*(d89[t]["mtx"]))/100;
	mtx1=(10000*(d89[t]["mrx"]))/100;
	mlrx1=((d89[t]["mltx"]))/1;
	mltx1=((d89[t]["mlrx"]))/1;
	ml1=(100*(d89[t]["ml"]))/1;
	data34.push({x: d89[t]["date"]/1, y: rx1 });
	data35.push({x: d89[t]["date"]/1, y: tx1 });
	mdata34.push({x: d89[t]["date"]/1, y: mrx1 });
	mdata35.push({x: d89[t]["date"]/1, y: mtx1 });
	mldata34.push({x: d89[t]["date"]/1, y: mlrx1 });
	mldata35.push({x: d89[t]["date"]/1, y: mltx1 });
	data36.push({x: d89[t]["date"]/1, y: ml1 });
	}
  
  chart9 = new JSGadget.Chart($("#chart9"), { //create chart
  trends: [new JSGadget.ATrend({color: "green", width: 1}),new JSGadget.ATrend({color: "Violet", width: 1}),new JSGadget.ATrend({color: "orange", width: 1}),new JSGadget.ATrend({color: "IndianRed", width: 1}),new JSGadget.ATrend({color: "teal", width: 1}),new JSGadget.ATrend({color: "blue", width: 1}),new JSGadget.ATrend({color: "Black", width: 1}),new JSGadget.ATrend({color: "Maroon", width: 1})]
 });
 
  chart9.trends[0].data = data36;
  chart9.trends[1].data = data35;
  chart9.trends[2].data = data34;
  chart9.trends[3].data = mdata34;
  chart9.trends[4].data = mdata35;
  chart9.trends[5].data = data33;
  chart9.trends[6].data = mldata34;
  chart9.trends[7].data = mldata35;
  chart9.bAxis.setMinMax(d89[0]["date"]/1, d89[numbs89-1]["date"]/1); //set x limits
  chart9.lAxis.setMinMax(-1.1, 400.1); //set y limits
  chart9.draw(); //draw chart  
}catch(e){}});

var chart10;
$(function() {
  try{
  //prepare values
  data33 = []; 
  data34 = [];
  data35 = [];
  data36 = [];
  mdata34 = [];
  mdata35 = [];
  mldata34 = [];
  mldata35 = [];
  for (var t = 0; t < numbs83; t++){
    data33.push({x: d83[t]["date"]/1, y: d83[t]["value"]});
	if (t>0){
		rx1=100*(Number(d83[t]["rx"])-Number(d83[t-1]["rx"]))/(Number(d83[t]["date"]/1) - Number(d83[t-1]["date"]/1));
		tx1=100*(Number(d83[t]["tx"])-Number(d83[t-1]["tx"]))/(Number(d83[t]["date"]/1) - Number(d83[t-1]["date"]/1));
	} else {rx1=(100*(d83[t]["rx"]))/1; tx1=(100*(d83[t]["tx"]))/1;}
	mrx1=(10000*(d83[t]["mtx"]))/100;
	mtx1=(10000*(d83[t]["mrx"]))/100;
	mlrx1=((d83[t]["mltx"]))/1;
	mltx1=((d83[t]["mlrx"]))/1;
	ml1=(100*(d83[t]["ml"]))/1;
	data34.push({x: d83[t]["date"]/1, y: rx1 });
	data35.push({x: d83[t]["date"]/1, y: tx1 });
	mdata34.push({x: d83[t]["date"]/1, y: mrx1 });
	mdata35.push({x: d83[t]["date"]/1, y: mtx1 });
	mldata34.push({x: d83[t]["date"]/1, y: mlrx1 });
	mldata35.push({x: d83[t]["date"]/1, y: mltx1 });
	data36.push({x: d83[t]["date"]/1, y: ml1 });
	}
  
  chart10 = new JSGadget.Chart($("#chart10"), { //create chart
  trends: [new JSGadget.ATrend({color: "green", width: 1}),new JSGadget.ATrend({color: "Violet", width: 1}),new JSGadget.ATrend({color: "orange", width: 1}),new JSGadget.ATrend({color: "IndianRed", width: 1}),new JSGadget.ATrend({color: "teal", width: 1}),new JSGadget.ATrend({color: "blue", width: 1}),new JSGadget.ATrend({color: "Black", width: 1}),new JSGadget.ATrend({color: "Maroon", width: 1})]
 });
 
  chart10.trends[0].data = data36;
  chart10.trends[1].data = data35;
  chart10.trends[2].data = data34;
  chart10.trends[3].data = mdata34;
  chart10.trends[4].data = mdata35;
  chart10.trends[5].data = data33;
  chart10.trends[6].data = mldata34;
  chart10.trends[7].data = mldata35;
  
  chart10.bAxis.setMinMax(d83[0]["date"]/1, d83[numbs83-1]["date"]/1); //set x limits
  chart10.lAxis.setMinMax(-1.1, 400.1); //set y limits
  chart10.draw(); //draw chart  
}catch(e){}});

var chart11;
$(function() {
  try{
  //prepare values
  data33 = []; 
  data34 = [];
  data35 = [];
  data36 = [];
  mdata34 = [];
  mdata35 = [];
  mldata34 = [];
  mldata35 = [];
  for (var t = 0; t < numbs401; t++){
    data33.push({x: d401[t]["date"]/1, y: d401[t]["value"]});
	if (t>0){
		rx1=100*(Number(d401[t]["rx"])-Number(d401[t-1]["rx"]))/(Number(d401[t]["date"]/1) - Number(d401[t-1]["date"]/1));
		tx1=100*(Number(d401[t]["tx"])-Number(d401[t-1]["tx"]))/(Number(d401[t]["date"]/1) - Number(d401[t-1]["date"]/1));
	} else {rx1=(100*(d401[t]["rx"]))/1; tx1=(100*(d401[t]["tx"]))/1;}
	mrx1=(10000*(d401[t]["mtx"]))/100;
	mtx1=(10000*(d401[t]["mrx"]))/100;
	mlrx1=((d401[t]["mltx"]))/1;
	mltx1=((d401[t]["mlrx"]))/1;
	ml1=(100*(d401[t]["ml"]))/1;
	data34.push({x: d401[t]["date"]/1, y: rx1 });
	data35.push({x: d401[t]["date"]/1, y: tx1 });
	mdata34.push({x: d401[t]["date"]/1, y: mrx1 });
	mdata35.push({x: d401[t]["date"]/1, y: mtx1 });
	mldata34.push({x: d401[t]["date"]/1, y: mlrx1 });
	mldata35.push({x: d401[t]["date"]/1, y: mltx1 });
	data36.push({x: d401[t]["date"]/1, y: ml1 });
	}
  
  chart11 = new JSGadget.Chart($("#chart11"), { //create chart
  trends: [new JSGadget.ATrend({color: "green", width: 1}),new JSGadget.ATrend({color: "Violet", width: 1}),new JSGadget.ATrend({color: "orange", width: 1}),new JSGadget.ATrend({color: "IndianRed", width: 1}),new JSGadget.ATrend({color: "teal", width: 1}),new JSGadget.ATrend({color: "blue", width: 1}),new JSGadget.ATrend({color: "Black", width: 1}),new JSGadget.ATrend({color: "Maroon", width: 1})]
 });
 
  chart11.trends[0].data = data36;
  chart11.trends[1].data = data35;
  chart11.trends[2].data = data34;
  chart11.trends[3].data = mdata34;
  chart11.trends[4].data = mdata35;
  chart11.trends[5].data = data33;
  chart11.trends[6].data = mldata34;
  chart11.trends[7].data = mldata35;
  
  chart11.bAxis.setMinMax(d401[0]["date"]/1, d401[numbs401-1]["date"]/1); //set x limits
  chart11.lAxis.setMinMax(-1.1, 400.1); //set y limits
  chart11.draw(); //draw chart  
}catch(e){}});


var chart12;
$(function() {
  try{
  //prepare values
  data33 = []; 
  data34 = [];
  data35 = [];
  data36 = [];
  mdata34 = [];
  mdata35 = [];
  mldata34 = [];
  mldata35 = [];
  for (var t = 0; t < numbs610; t++){
    data33.push({x: d610[t]["date"]/1, y: d610[t]["value"]});
	if (t>0){
		rx1=100*(Number(d610[t]["rx"])-Number(d610[t-1]["rx"]))/(Number(d610[t]["date"]/1) - Number(d610[t-1]["date"]/1));
		tx1=100*(Number(d610[t]["tx"])-Number(d610[t-1]["tx"]))/(Number(d610[t]["date"]/1) - Number(d610[t-1]["date"]/1));
	} else {rx1=(100*(d610[t]["rx"]))/1; tx1=(100*(d610[t]["tx"]))/1;}
	mrx1=(10000*(d610[t]["mtx"]))/100;
	mtx1=(10000*(d610[t]["mrx"]))/100;
	mlrx1=((d610[t]["mltx"]))/1;
	mltx1=((d610[t]["mlrx"]))/1;
	ml1=(100*(d610[t]["ml"]))/1;
	data34.push({x: d610[t]["date"]/1, y: rx1 });
	data35.push({x: d610[t]["date"]/1, y: tx1 });
	mdata34.push({x: d610[t]["date"]/1, y: mrx1 });
	mdata35.push({x: d610[t]["date"]/1, y: mtx1 });
	mldata34.push({x: d610[t]["date"]/1, y: mlrx1 });
	mldata35.push({x: d610[t]["date"]/1, y: mltx1 });
	data36.push({x: d610[t]["date"]/1, y: ml1 });
	}
  
  chart12 = new JSGadget.Chart($("#chart12"), { //create chart
  trends: [new JSGadget.ATrend({color: "green", width: 1}),new JSGadget.ATrend({color: "Violet", width: 1}),new JSGadget.ATrend({color: "orange", width: 1}),new JSGadget.ATrend({color: "IndianRed", width: 1}),new JSGadget.ATrend({color: "teal", width: 1}),new JSGadget.ATrend({color: "blue", width: 1}),new JSGadget.ATrend({color: "Black", width: 1}),new JSGadget.ATrend({color: "Maroon", width: 1})]
 });
 
  chart12.trends[0].data = data36;
  chart12.trends[1].data = data35;
  chart12.trends[2].data = data34;
  chart12.trends[3].data = mdata34;
  chart12.trends[4].data = mdata35;
  chart12.trends[5].data = data33;
  chart12.trends[6].data = mldata34;
  chart12.trends[7].data = mldata35;
  chart12.bAxis.setMinMax(d610[0]["date"]/1, d610[numbs610-1]["date"]/1); //set x limits
  chart12.lAxis.setMinMax(-1.1, 400.1); //set y limits
  chart12.draw(); //draw chart  
}catch(e){}});

var chart13;
$(function() {
  try{
  //prepare values
  data33 = []; 
  data34 = [];
  data35 = [];
  data36 = [];
  mdata34 = [];
  mdata35 = [];
  mldata34 = [];
  mldata35 = [];
  for (var t = 0; t < numbs627; t++){
    data33.push({x: d627[t]["date"]/1, y: d627[t]["value"]});
	if (t>0){
		rx1=100*(Number(d627[t]["rx"])-Number(d627[t-1]["rx"]))/(Number(d627[t]["date"]/1) - Number(d627[t-1]["date"]/1));
		tx1=100*(Number(d627[t]["tx"])-Number(d627[t-1]["tx"]))/(Number(d627[t]["date"]/1) - Number(d627[t-1]["date"]/1));
	} else {rx1=(100*(d627[t]["rx"]))/1; tx1=(100*(d627[t]["tx"]))/1;}
	mrx1=(10000*(d627[t]["mtx"]))/100;
	mtx1=(10000*(d627[t]["mrx"]))/100;
	mlrx1=((d627[t]["mltx"]))/1;
	mltx1=((d627[t]["mlrx"]))/1;
	ml1=(100*(d627[t]["ml"]))/1;
	data34.push({x: d627[t]["date"]/1, y: rx1 });
	data35.push({x: d627[t]["date"]/1, y: tx1 });
	mdata34.push({x: d627[t]["date"]/1, y: mrx1 });
	mdata35.push({x: d627[t]["date"]/1, y: mtx1 });
	mldata34.push({x: d627[t]["date"]/1, y: mlrx1 });
	mldata35.push({x: d627[t]["date"]/1, y: mltx1 });
	data36.push({x: d627[t]["date"]/1, y: ml1 });
	}
  
  chart13 = new JSGadget.Chart($("#chart13"), { //create chart
  trends: [new JSGadget.ATrend({color: "green", width: 1}),new JSGadget.ATrend({color: "Violet", width: 1}),new JSGadget.ATrend({color: "orange", width: 1}),new JSGadget.ATrend({color: "IndianRed", width: 1}),new JSGadget.ATrend({color: "teal", width: 1}),new JSGadget.ATrend({color: "blue", width: 1}),new JSGadget.ATrend({color: "Black", width: 1}),new JSGadget.ATrend({color: "Maroon", width: 1})]
 });
 
  chart13.trends[0].data = data36;
  chart13.trends[1].data = data35;
  chart13.trends[2].data = data34;
  chart13.trends[3].data = mdata34;
  chart13.trends[4].data = mdata35;
  chart13.trends[5].data = data33;
  chart13.trends[6].data = mldata34;
  chart13.trends[7].data = mldata35;
  chart13.bAxis.setMinMax(d627[0]["date"]/1, d627[numbs627-1]["date"]/1); //set x limits
  chart13.lAxis.setMinMax(-1.1, 400.1); //set y limits
  chart13.draw(); //draw chart  
}catch(e){}});

var chart14;
$(function() {
  try{
  //prepare values
  data33 = []; 
  data34 = [];
  data35 = [];
  data36 = [];
  mdata34 = [];
  mdata35 = [];
  mldata34 = [];
  mldata35 = [];
  for (var t = 0; t < numbs544; t++){
    data33.push({x: d544[t]["date"]/1, y: d544[t]["value"]});
	if (t>0){
		rx1=100*(Number(d544[t]["rx"])-Number(d544[t-1]["rx"]))/(Number(d544[t]["date"]/1) - Number(d544[t-1]["date"]/1));
		tx1=100*(Number(d544[t]["tx"])-Number(d544[t-1]["tx"]))/(Number(d544[t]["date"]/1) - Number(d544[t-1]["date"]/1));
	} else {rx1=(100*(d544[t]["rx"]))/1; tx1=(100*(d544[t]["tx"]))/1;}
	mrx1=(10000*(d544[t]["mtx"]))/100;
	mtx1=(10000*(d544[t]["mrx"]))/100;
	mlrx1=((d544[t]["mltx"]))/1;
	mltx1=((d544[t]["mlrx"]))/1;
	ml1=(100*(d544[t]["ml"]))/1;
	data34.push({x: d544[t]["date"]/1, y: rx1 });
	data35.push({x: d544[t]["date"]/1, y: tx1 });
	mdata34.push({x: d544[t]["date"]/1, y: mrx1 });
	mdata35.push({x: d544[t]["date"]/1, y: mtx1 });
	mldata34.push({x: d544[t]["date"]/1, y: mlrx1 });
	mldata35.push({x: d544[t]["date"]/1, y: mltx1 });
	data36.push({x: d544[t]["date"]/1, y: ml1 });
	}
  
  chart14 = new JSGadget.Chart($("#chart14"), { //create chart
  trends: [new JSGadget.ATrend({color: "green", width: 1}),new JSGadget.ATrend({color: "Violet", width: 1}),new JSGadget.ATrend({color: "orange", width: 1}),new JSGadget.ATrend({color: "IndianRed", width: 1}),new JSGadget.ATrend({color: "teal", width: 1}),new JSGadget.ATrend({color: "blue", width: 1}),new JSGadget.ATrend({color: "Black", width: 1}),new JSGadget.ATrend({color: "Maroon", width: 1})]
 });
 
  chart14.trends[0].data = data36;
  chart14.trends[1].data = data35;
  chart14.trends[2].data = data34;
  chart14.trends[3].data = mdata34;
  chart14.trends[4].data = mdata35;
  chart14.trends[5].data = data33;
  chart14.trends[6].data = mldata34;
  chart14.trends[7].data = mldata35;
  chart14.bAxis.setMinMax(d544[0]["date"]/1, d544[numbs544-1]["date"]/1); //set x limits
  chart14.lAxis.setMinMax(-1.1, 400.1); //set y limits
  chart14.draw(); //draw chart  
}catch(e){}});

//function tick() {

  //var t2 = new Date(), tz = tz = t2.getTimezoneOffset() * 60;

  //t2 = t2.getTime() / 1000 - tz;

  //var t1 = t2 - i, t = (t2 / c) % (Math.PI * 2);

  //v.push([t2, Math.sin(t), Math.cos(t)]);

  //if (v.length > i)

    //delete v.shift();

  //if (!chart.lAxis.zoom && !chart.bAxis.zoom) {

    //chart.bAxis.setMinMax(t1, t2);
	//<?php echo 'var d1 = '.json_encode($xy_value).';'; ?>;

    //chart.draw();

 // } 