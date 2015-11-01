// queue()
//     // .defer(d3.csv)
//     .await(makeGraphs);

d3.csv('/static/wtf.csv', function makeGraphs(data) {
	
//Start Transformations
	var dataSet =data ;
	// var dateFormat = d3.time.format("%m/%d/%Y");
	dataSet.forEach(function(d) {
		// d.week = dateFormat.parse(d.week);
				// d.transaction_date.setDate(1);
		d.week= +d.week;
		d.sales_price = +d.sales_price;
		d.sales_count = +d.sales_count;
	});

	//Create a Crossfilter instance
	var ndx = crossfilter(dataSet);

	//Define Dimensions
	var all = ndx.groupAll();	
	var weekNum = ndx.dimension(function(d) { return d.week; });
	var custStatus = ndx.dimension(function(d) { return d.cust_new_or_return; });

	var custNew=weekNum.group().reduceSum(function(d) 
   {if (d.cust_new_or_return==='new') {return d.sales_count;}else{return 0;}});
	var custReturn=weekNum.group().reduceSum(function(d) 
   {if (d.cust_new_or_return==='return') {return d.sales_count;}else{return 0;}});


	//Define threshold values for data
	var minDate = weekNum.bottom(1)[0].week;
	var maxDate = weekNum.top(1)[0].week;


    //Charts

	var newcustChart = dc.lineChart("#newcust-chart");


	newcustChart
		//.width(600)
		.height(300)
		.margins({top: 10, right: 50, bottom: 30, left: 50})
		.dimension(weekNum)
		.group(custReturn, 'Returning Customers')
		.stack(custNew,'New Customers')
		.renderArea(true)
		.transitionDuration(500)
		.x(d3.time.scale().domain([minDate, maxDate]))
		.elasticY(true)
		.renderHorizontalGridLines(true)
    	.renderVerticalGridLines(true)
		.xAxisLabel("2015 Week Number#")
		.legend(dc.legend().x(60).y(10).itemHeight(13).gap(5))
		.elasticX(true)
        .brushOn(false)
        .ordinalColors(["#56B2EA","#E064CD","#F8B700","#78CC00","#7B71C5"])
		.yAxis().ticks(6);	

    dc.renderAll();

});