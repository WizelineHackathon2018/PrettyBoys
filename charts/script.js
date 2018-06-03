var w = 400, h = 400; // Size

var colorscale = d3.scale.category10();

//Legend titles
//var LegendOptions = ['Smartphone'];
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
       var response = JSON.parse(xhttp.responseText);
       //Call function to draw the Radar chart
       //Will expect that data is in %'s
       RadarChart.draw("#chart", response, mycfg);
    }
};
xhttp.open("GET", "probe.json", true);
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

var svg = d3.select('#body')
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
