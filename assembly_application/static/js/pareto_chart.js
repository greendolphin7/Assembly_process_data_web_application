var data4= [];
var requests = $.get('/Pareto');  // $. <- 제이쿼리,
   var tm = requests.done(function(result) // 성공하면 result 값을 받아옴
        {
//                var data1= []; // [[[ ]]]  [[ ]]
            data4.push(result[0][0]);
            //console.log(data1)

Highcharts.chart('container4', {
    chart: {
        renderTo: 'container4',
        type: 'column'
    },
    title: {
        text: 'Quality Pareto'
    },
    tooltip: {
        shared: true
    },
    xAxis: {
        categories: [
            'OP 10',
            'OP 20',
            'OP 30',
            'OP 40',
            'OP 50'
        ],
        crosshair: true
    },
    credits: {
            enabled: false,
        },
    yAxis: [{
        title: {
            text: ''
        }
    }, {
        title: {
            text: ''
        },
        minPadding: 0,
        maxPadding: 0,
        max: 100,
        min: 0,
        opposite: true,
        labels: {
            format: "{value}%"
        }
    }],
    series: [{
        type: 'pareto',
        name: 'Pareto',
        yAxis: 1,
        zIndex: 10,
        baseSeries: 1,
        tooltip: {
            valueDecimals: 2,
            valueSuffix: '%'
        }
    }, {
        name: 'Machine',
        type: 'column',
        zIndex: 2,
        data: data4[0]
    }]
});

});