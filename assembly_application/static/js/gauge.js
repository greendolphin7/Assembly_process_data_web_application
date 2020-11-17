const toggleBtn = document.querySelector('.navbar__toggleBtn');
const menu = document.querySelector('.navbar__menu');
const icons = document.querySelector('.navbar__Logout');

toggleBtn.addEventListener('click', () => {
  menu.classList.toggle('active');
  icons.classList.toggle('active');
});


var gaugeOptions = {
    chart: {
        type: 'solidgauge'
    },

    title: null,

    pane: {
        center: ['50%', '85%'],
        size: '140%',
        startAngle: -90,
        endAngle: 90,
        background: {
            backgroundColor:
                Highcharts.defaultOptions.legend.backgroundColor || '#EEE',
            innerRadius: '60%',
            outerRadius: '100%',
            shape: 'arc'
        }
    },

    exporting: {
        enabled: false
    },

    tooltip: {
        enabled: false
    },

    // the value axis
    yAxis: {
        stops: [
            [0.1, '#55BF3B'], // green
            [0.5, '#DDDF0D'], // yellow
            [0.9, '#DF5353'] // red
        ],
        lineWidth: 0,
        tickWidth: 0,
        minorTickInterval: null,
        tickAmount: 2,
        title: {
            y: -70
        },
        labels: {
            y: 16
        }
    },

    plotOptions: {
        solidgauge: {
            dataLabels: {
                y: 5,
                borderWidth: 0,
                useHTML: true
            }
        }
    }
};

// The speed gauge
var chartSpeed = Highcharts.chart('container-speed', Highcharts.merge(gaugeOptions, {
    yAxis: {
        min: 0,
        max: 100,
        title: {
            text: 'OEE'
        }
    },

    credits: {
        enabled: false
    },

    series: [{
        name: 'Speed',
        data: [80],
        dataLabels: {
            format:
                '<div style="text-align:center">' +
                '<span style="font-size:25px">{y:.1f}</span><br/>' +
                '<span style="font-size:12px;opacity:0.4">%</span>' +
                '</div>'
        },
        tooltip: {
            valueSuffix: ' km/h'
        }
    }]

}));

// The RPM gauge
var chartRpm = Highcharts.chart('container-rpm', Highcharts.merge(gaugeOptions, {
    yAxis: {
        min: 0,
        max: 100,
        title: {
            text: 'Availability'
        }
    },

    series: [{
        name: 'RPM',
        data: [1],
        dataLabels: {
            format:
                '<div style="text-align:center">' +
                '<span style="font-size:25px">{y:.1f}</span><br/>' +
                '<span style="font-size:12px;opacity:0.4">' +
                '%' +
                '</span>' +
                '</div>'
        },
        tooltip: {
            valueSuffix: ' revolutions/min'
        }
    }]

}));

var chart1 = Highcharts.chart('container-1', Highcharts.merge(gaugeOptions, {
    yAxis: {
        min: 0,
        max: 100,
        title: {
            text: 'Productivity'
        }
    },

    series: [{
        name: 'RPM',
        data: [1],
        dataLabels: {
            format:
                '<div style="text-align:center">' +
                '<span style="font-size:25px">{y:.1f}</span><br/>' +
                '<span style="font-size:12px;opacity:0.4">' +
                '%' +
                '</span>' +
                '</div>'
        },
        tooltip: {
            valueSuffix: ' revolutions/min'
        }
    }]

}));

var chart2 = Highcharts.chart('container-2', Highcharts.merge(gaugeOptions, {
    yAxis: {
        min: 0,
        max: 100,
        title: {
            text: 'Quality'
        }
    },

    series: [{
        name: 'RPM',
        data: [1],
        dataLabels: {
            format:
                '<div style="text-align:center">' +
                '<span style="font-size:25px">{y:.1f}</span><br/>' +
                '<span style="font-size:12px;opacity:0.4">' +
                '%' +
                '</span>' +
                '</div>'
        },
        tooltip: {
            valueSuffix: ' revolutions/min'
        }
    }]

}));

// Bring life to the dials
setInterval(function () {
    // Speed
    var point,
        newVal,
        inc;
    var requests = $.get('/re_data');  // $. <- 제이쿼리,
        var tm = requests.done(function (result) // 성공하면 result 값을 받아옴
            {
                // Add the Point
                // Time Temperature\
                var data1 = [];
                data1.push(result[0]);  // 값 업데이트
                data1.push(result[1]);  // 첫번째 데이터

                // Add the Point
                // Time Humidity
                var data2 = [];
                data2.push(result[0]);
                data2.push(result[2]);

                var data3 = [];
                data3.push(result[0]);
                data3.push(result[3]);

                // Add the Point
                // Time Humidity
                var data4 = [];
                data4.push(result[0]);
                data4.push(result[4]);

                //setTimeout(requestData, 2000);


    if (chartSpeed) {
        point = chartSpeed.series[0].points[0];
        inc = Math.round(data1[1]);
        newVal = point.y + inc;

        if (newVal < 0 || newVal > 100) {
            newVal = point.y - inc;
        }

        point.update(inc);
    }

    // RPM
    if (chartRpm) {
        point = chartRpm.series[0].points[0];
        inc = Math.round(data2[1]);
        newVal = point.y + inc;

        if (newVal < 0 || newVal > 100) {
            newVal = point.y - inc;
        }

        point.update(inc);
    }

    if (chart1) {
        point = chart1.series[0].points[0];
        inc = Math.round(data3[1]);
        newVal = point.y + inc;

        if (newVal < 0 || newVal > 100) {
            newVal = point.y - inc;
        }

        point.update(inc);
    }

    if (chart2) {
        point = chart2.series[0].points[0];
        inc = Math.round(data4[1]);
        newVal = point.y + inc;

        if (newVal < 0 || newVal > 100) {
            newVal = point.y - inc;
        }

        point.update(inc);
    }
    });
}, 2000);