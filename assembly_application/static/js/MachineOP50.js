var chart;

function requestData() {
    $.ajax({
        url: '/live_Temperature_OP50',
        success: function(point) {
            //console.log(point)
            var series = chart.series[0],
                shift = series.data.length > 30;

            chart.series[0].addPoint(point, true, shift);

            setTimeout(requestData, 10000);
        },
        cache: false
    });
}

$(document).ready(function() {
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'container',
            defaultSeriesType: 'spline',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'Realtime Temperature OP50'
        },
        credits: {
            enabled: false,
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'percent',
                margin: 80
            }
        },
        series: [{
            name: 'Temperature',
            data: []
        }]
    });
});