
var chart10;
$(function() {
  //prepare values
  data37 = []; 
  data38 = [];
  data39 = [];
  data40 = [];
  data41 = [];
  data42 = [];
  data43 = [];
  data44 = [];
  data45 = [];
  data46 = [];
  data47 = [];
  for (var t = 0; t < numbs110d; t++){
    data37.push({x: d110d[t]["Vrema"]/1, y: d110d[t]["Wkp"]});
	data38.push({x: d110d[t]["Vrema"]/1, y: d110d[t]["Wdol"] });
	Mpot=(10*( d110d[t]["Mpot"]))/1;
	data39.push({x: d110d[t]["Vrema"]/1, y: Mpot });
	data40.push({x: d110d[t]["Vrema"]/1, y: d110d[t]["Npot"] });
	data41.push({x: d110d[t]["Vrema"]/1, y: d110d[t]["Pbx"] });
	data42.push({x: d110d[t]["Vrema"]/1, y: d110d[t]["Qbx"] });
	data43.push({x: d110d[t]["Vrema"]/1, y: d110d[t]["Talblok"] });
	data44.push({x: d110d[t]["Vrema"]/1, y: d110d[t]["Xn1"] });
	data45.push({x: d110d[t]["Vrema"]/1, y: d110d[t]["Xn2"] });
	Potok=(10*( d110d[t]["Potok"]))/1;
	data46.push({x: d110d[t]["Vrema"]/1, y: Potok });
	data47.push({x: d110d[t]["Vrema"]/1, y: d110d[t]["Tbix"] });
	}
  
  chart10 = new JSGadget.Chart($("#chart10"), { //create chart
  trends: [new JSGadget.ATrend({color: "red", width: 1}),new JSGadget.ATrend({color: "Indigo", width: 1}),new JSGadget.ATrend({color: "Teal", width: 1}),new JSGadget.ATrend({color: "DarkGreen", width: 1}),new JSGadget.ATrend({color: "Tomato", width: 1}),new JSGadget.ATrend({color: "DarkRed", width: 1}),new JSGadget.ATrend({color: "Blue", width: 1}),new JSGadget.ATrend({color: "Brown", width: 1}),new JSGadget.ATrend({color: "DarkSlateGray", width: 1}),new JSGadget.ATrend({color: "DarkOrange", width: 1}),new JSGadget.ATrend({color: "Magenta", width: 1})]
 });
 
  chart10.trends[0].data = data37;
  chart10.trends[1].data = data38;
  chart10.trends[2].data = data39;
  chart10.trends[3].data = data40;
  chart10.trends[4].data = data41;
  chart10.trends[5].data = data42;
  chart10.trends[6].data = data43;
  chart10.trends[7].data = data44;
  chart10.trends[8].data = data45;
  chart10.trends[9].data = data46;
  chart10.trends[10].data = data47;
  chart10.bAxis.setMinMax(d110d[0]["Vrema"]/1, d110d[numbs110d-1]["Vrema"]/1); //set x limits
  chart10.lAxis.setMinMax(-1.1, 100.1); //set y limits
  chart10.draw(); //draw chart  
});


var chart11;
$(function() {
  //prepare values
  data48 = []; 
  data49 = [];
  data50 = [];
  data51 = [];
  data52 = [];
  data53 = [];
  data54 = [];
  data55 = [];
  for (var t = 0; t < numbs110d; t++){
    data48.push({x: d110d[t]["Vrema"]/1, y: d110d[t]["V1"]});
	data49.push({x: d110d[t]["Vrema"]/1, y: d110d[t]["V2"] });
	data50.push({x: d110d[t]["Vrema"]/1, y: d110d[t]["V3"] });
	data51.push({x: d110d[t]["Vrema"]/1, y: d110d[t]["V4"] });
	data52.push({x: d110d[t]["Vrema"]/1, y: d110d[t]["Vdol"] });
	data53.push({x: d110d[t]["Vrema"]/1, y: d110d[t]["Vobj"] });
	C1=(100*( d110d[t]["C1"]))/1;
	C1C5=(100*( d110d[t]["C1C5"]))/1;
	data54.push({x: d110d[t]["Vrema"]/1, y: C1 });
	data55.push({x: d110d[t]["Vrema"]/1, y: C1C5 });
	}
  
  chart11 = new JSGadget.Chart($("#chart11"), { //create chart
  trends: [new JSGadget.ATrend({color: "red", width: 1}),new JSGadget.ATrend({color: "Indigo", width: 1}),new JSGadget.ATrend({color: "Teal", width: 1}),new JSGadget.ATrend({color: "DarkGreen", width: 1}),new JSGadget.ATrend({color: "Tomato", width: 1}),new JSGadget.ATrend({color: "DarkRed", width: 1}),new JSGadget.ATrend({color: "Blue", width: 1}),new JSGadget.ATrend({color: "Brown", width: 1})]
 });
 
  chart11.trends[0].data = data48;
  chart11.trends[1].data = data49;
  chart11.trends[2].data = data50;
  chart11.trends[3].data = data51;
  chart11.trends[4].data = data52;
  chart11.trends[5].data = data53;
  chart11.trends[6].data = data54;
  chart11.trends[7].data = data55;
  chart11.bAxis.setMinMax(d110d[0]["Vrema"]/1, d110d[numbs110d-1]["Vrema"]/1); //set x limits
  chart11.lAxis.setMinMax(-1.1, 150.1); //set y limits
  chart11.draw(); //draw chart  
});



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