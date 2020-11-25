const toggleBtn = document.querySelector('.navbar__toggleBtn');
const menu = document.querySelector('.navbar__menu');
const icons = document.querySelector('.navbar__Logout');

toggleBtn.addEventListener('click', () => {
  menu.classList.toggle('active');
  icons.classList.toggle('active');
});

var chart;

function requestData() {
    $.ajax({
        url: '/live_Electronic_OP10',
        success: function(point) {
            console.log(point)
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
            text: 'Realtime Electronic OP10'
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
            name: 'Electronic',
            data: []
        }]
    });
});