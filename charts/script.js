var w = 400, h = 400; // Size

var colorscale = d3.scale.category10();

//Legend titles
//var LegendOptions = ['Smartphone'];
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var response1 = JSON.parse(xhttp.responseText);
      var team1 = [[{axis:"sentinel",value:response1[0].sentinel},{axis:"seniority",value:response1[0].seniority},{axis:"diplomat",value:response1[0].diplomat},{axis:"analyst",value:response1[0].analyst},{axis:"explorer",value:response1[0].explorer}]]
      var team2 = [[{axis:"sentinel",value:response1[1].sentinel},{axis:"seniority",value:response1[1].seniority},{axis:"diplomat",value:response1[1].diplomat},{axis:"analyst",value:response1[1].analyst},{axis:"explorer",value:response1[1].explorer}]]
      var team3 = [[{axis:"sentinel",value:response1[2].sentinel},{axis:"seniority",value:response1[2].seniority},{axis:"diplomat",value:response1[2].diplomat},{axis:"analyst",value:response1[2].analyst},{axis:"explorer",value:response1[2].explorer}]]
       //Call function to draw the Radar chart
       //Will expect that data is in %'s
       //console.log(team
       RadarChart.draw("#chart1", team1, mycfg);
       RadarChart.draw("#chart2", team2, mycfg);
       RadarChart.draw("#chart3", team3, mycfg);
    }
};
xhttp.open("GET", "http://54.71.144.166/api/staff-requirements/1/teams", true);
//xhttp.open("GET", "probe.json", true);
xhttp.send();

/*// Example, how to change content
data[0][1].axis = 'Vales M!!!'
data[0][1].value = 0
*/

//Options for the Radar chart, other than default
var mycfg = {
  w: w,
  h: h,
  maxValue: 0.7,
  levels: 10,      // Number of axis
  ExtraWidthX: 300
}

/////////// Initiate legend ////////////////

var svg = d3.select('#body1')
	.selectAll('svg')
	.append('svg')
	.attr("width", w+300)
	.attr("height", h)

  var svg = d3.select('#body2')
  	.selectAll('svg')
  	.append('svg')
  	.attr("width", w+300)
  	.attr("height", h)

    var svg = d3.select('#body3')
    	.selectAll('svg')
    	.append('svg')
    	.attr("width", w+300)
    	.attr("height", h)

//Create the title for the legend
var text = svg.append("text")
	.attr("class", "title")
	.attr('transform', 'translate(90,0)')
	.attr("x", w - 60)
	.attr("y", 20)
	.attr("font-size", "20px")
	.attr("fill", "#404040")
	.text("Profile team"); // Tittle
