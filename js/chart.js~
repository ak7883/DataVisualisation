$(document).ready(function(){

InitChart();  //initialising the axis via default data (declaring function)
	$("#btnSearch").click(function(){
		var a = document.getElementById("txtSearchKeyword");
		$.ajax({
		'url':'getdata',
		'type':'post',
		'data':{'param1':a.value},
		'beforeSend':function(){
			$('#imgloader').show();
		},
		'success':function(response){
			console.log(JSON.parse(response))
			var data = JSON.parse(response); 
			CreateChart(data); 
			$('#imgloader').hide();  
		},
		'error':function(error){
			console.log(error);
			$('#imgloader').hide();
		}
		});
	});
});

function CreateChart(data) {
var color = d3.scale.category20();
    var vis = d3.select("svg"),
        WIDTH = 800,
        HEIGHT = 500,
        MARGINS = {
            top: 20,
            right: 20,
            bottom: 20,
            left: 50
        },
        xScale = d3.scale.linear().range([MARGINS.left, WIDTH - MARGINS.right]).domain([d3.min(data, function(d) {
                return (parseInt(d.corpus_date, 10) - 5);
            }),
            d3.max(data, function(d) {
                return parseInt(d.corpus_date, 10);
            })
        ]),
        yScale = d3.scale.linear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([d3.min(data, function(d) {
                return (parseInt(d.word_count, 10) - 5);
            }),
            d3.max(data, function(d) {
                return parseInt(d.word_count, 10);
            })
        ]),
        xAxis = d3.svg.axis() 
        .scale(xScale), 
 
        yAxis = d3.svg.axis() 
        .scale(yScale)
        .orient("left");
 
 
 
 
   var hasAxis = vis.select('.axis')[0][0];
 
if (!hasAxis) {
    
    vis.append("svg:g") 
        .attr("class", "x axis") 
        .attr("transform", "translate(0," + (HEIGHT - MARGINS.bottom) + ")") 
        .call(xAxis); 
 
    vis.append("svg:g")
        .attr("class", "y axis")
        .attr("transform", "translate(" + (MARGINS.left) + ",0)")
        .call(yAxis);
}

var transition = vis.transition().duration(2000);
            transition.select(".x.axis").call(xAxis);
            transition.select(".y.axis").call(yAxis);


            var circles = vis.selectAll("circle").data(data);
            circles.enter()
                .append("svg:circle")
                .attr("stroke", "black")
                .attr("r", 10)
                .attr("cx", function(d) {
                    return xScale(d.corpus_date);
                })
                .attr("cy", function(d) {
                    return yScale(d.word_count);
                })
                .style("fill", function(d, i) {
                    return color(i);
                });
            circles.transition().duration(1000)
                .attr("cx", function(d) {
                    return xScale(d.corpus_date);
                })
                .attr("cy", function(d) {
                    return yScale(d.word_count);
                })
                .attr("r", 10);
            circles.exit()
                .transition().duration(1000)
                .remove();

$('svg circle').tipsy({
    gravity: 'w',
    title: function() {
        var d = this.__data__;
 
        return d.word_count + ' occurrences found in ' + d.corpus;
    }
});
 
}


function InitChart() {
    var data = [{
        "count": "202",
        "year": "1590"
    }, {
        "count": "215",
        "year": "1592"
    }, {
        "count": "179",
        "year": "1593"
    }, {
        "count": "199",
        "year": "1594"
    }, {
        "count": "134",
        "year": "1595"
    }, {
        "count": "176",
        "year": "1596"
    }, {
        "count": "172",
        "year": "1597"
    }, {
        "count": "161",
        "year": "1598"
    }, {
        "count": "199",
        "year": "1599"
    }, {
        "count": "181",
        "year": "1600"
    }, {
        "count": "157",
        "year": "1602"
    }, {
        "count": "179",
        "year": "1603"
    }, {
        "count": "150",
        "year": "1606"
    }, {
        "count": "187",
        "year": "1607"
    }, {
        "count": "133",
        "year": "1608"
    }, {
        "count": "190",
        "year": "1609"
    }, {
        "count": "175",
        "year": "1610"
    }, {
        "count": "91",
        "year": "1611"
    }, {
        "count": "150",
        "year": "1612"
    }];
 
 
    var color = d3.scale.category20();
    var vis = d3.select("svg"),
        WIDTH = 800,
        HEIGHT = 500,
        MARGINS = {
            top: 20,
            right: 20,
            bottom: 20,
            left: 50
        },
        xScale = d3.scale.linear().range([MARGINS.left, WIDTH - MARGINS.right]).domain([d3.min(data, function(d) {
                return (parseInt(d.year, 10) - 5);
            }),
            d3.max(data, function(d) {
                return parseInt(d.year, 10);
            })
        ]),
        yScale = d3.scale.linear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([d3.min(data, function(d) {
                return (parseInt(d.count, 10) - 5);
            }),
            d3.max(data, function(d) {
                return parseInt(d.count, 10);
            })
        ]),
        xAxis = d3.svg.axis() 
        .scale(xScale), 
 
        yAxis = d3.svg.axis()
        .scale(yScale)
        .orient("left");
 
 
 
 
    vis.append("svg:g") 
        .attr("class", "x axis") 
        .attr("transform", "translate(0," + (HEIGHT - MARGINS.bottom) + ")")
        .call(xAxis); 
 
    vis.append("svg:g")
        .attr("class", "y axis")
        .attr("transform", "translate(" + (MARGINS.left) + ",0)")
        .call(yAxis);
}
