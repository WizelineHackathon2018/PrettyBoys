var w = 400, h = 400; // Size

var colorscale = d3.scale.category10();

//Legend titles
//var LegendOptions = ['Smartphone'];

//Data
var data = [
		  [
			{axis:"Work Ability",value:0.8},
			{axis:"Technical Ability",value:0.8},
			{axis:"Charisma",value:0.42},
			{axis:"Grit/Determination",value:0.6},
			{axis:"Teaching Ability",value:0.48},
			{axis:"Hustle Ability",value:0.35},
			{axis:"Honesty & Sincerity",value:0.11}
		  ]
		];

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

//Call function to draw the Radar chart
//Will expect that data is in %'s
RadarChart.draw("#chart", data, mycfg);

////////////////////////////////////////////
/////////// Initiate legend ////////////////
////////////////////////////////////////////

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

/*
//Initiate Legend
var legend = svg.append("g")
	.attr("class", "legend")
	.attr("height", 100)
	.attr("width", 200)
	.attr('transform', 'translate(90,20)')
	;

	//Create colour squares
	legend.selectAll('rect')
	  .data(LegendOptions)
	  .enter()
	  .append("rect")
	  .attr("x", w - 65)
	  .attr("y", function(d, i){ return i * 20;})
	  .attr("width", 10)
	  .attr("height", 10)
	  .style("fill", function(d, i){ return colorscale(i);})
	  ;
	//Create text next to squares
	legend.selectAll('text')
	  .data(LegendOptions)
	  .enter()
	  .append("text")
	  .attr("x", w - 52)
	  .attr("y", function(d, i){ return i * 20 + 9;})
	  .attr("font-size", "11px")
	  .attr("fill", "#737373")
	  .text(function(d) { return d; })
	  ; */
