const toggleBtn = document.querySelector('.navbar__toggleBtn');
const menu = document.querySelector('.navbar__menu');
const icons = document.querySelector('.navbar__icons');

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
var chartAvailability = Highcharts.chart('container-Availability', Highcharts.merge(gaugeOptions, {
    yAxis: {
        min: 50,
        max: 100,
        title: {
            text: 'Availability'
        }
    },

    credits: {
        enabled: false
    },

    series: [{
        name: 'Availability',
        data: [1],
        dataLabels: {
            format:
                '<div style="text-align:center">' +
                '<span style="font-size:25px">{y:.1f}</span><br/>' +
                '<span style="font-size:12px;opacity:0.4">%</span>' +
                '</div>'
        },
        tooltip: {
            valueSuffix: '%'
        }
    }]

}));

// The RPM gauge
var chartProductivity = Highcharts.chart('container-Productivity', Highcharts.merge(gaugeOptions, {
    yAxis: {
        min: 50,
        max: 100,
        title: {
            text: 'Productivity' 
        }
        
    },

    series: [{
        name: 'Productivity',
        data: [1],
        dataLabels: {
            format:
                '<div style= "text-align:center">' +
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

var chartQuality = Highcharts.chart('container-Quality', Highcharts.merge(gaugeOptions, {
    yAxis: {
        min: 50,
        max: 100,
        title: {
            text: 'Quality'
        }
    },

    series: [{
        name: 'Quality',
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

var chartOEE = Highcharts.chart('container-OEE', Highcharts.merge(gaugeOptions, {
    yAxis: {
        min: 50,
        max: 100,
        title: {
            text:'OEE'
        }
    },

    series: [{
        name: 'OEE',
        data: [80],
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
        inc1,
        inc2,
        inc3,
        inc4
        ;
		inc1 = Math.round((Math.random() - 0.5) * 100);
        inc2 = Math.round((Math.random() - 0.5) * 100);
        inc3 = Math.round((Math.random() - 0.5) * 100);
        inc4 = (inc1 * inc2 * inc3) / 10000;



    if (chartAvailability) {
        point = chartAvailability.series[0].points[0];       
        newVal = point.y + inc1;
				//inc1 = Math.round((Math.random() - 0.5) * 100);
        //if (newVal < 0 || newVal > 100) {
           //newVal = point.y - inc1;
        //}

        point.update(newVal);
    }

    // RPM
    if (chartProductivity) {
        point = chartProductivity.series[0].points[0];
        //nc = Math.round((Math.random() - 0.5) * 100);
        newVal = point.y + inc2;

       // if (newVal < 0 || newVal > 100) {
           // newVal = point.y - inc2;
       // }

        point.update(newVal);
    }
    if (chartQuality) {
        point = chartQuality.series[0].points[0];
        //inc = Math.round((Math.random() - 0.5) * 100);
        newVal = point.y + inc3;

        if (newVal < 0 || newVal > 100) {
            newVal = point.y - inc3;
        }

        point.update(newVal);
    }
    if (chartOEE) {
        point = chartOEE.series[0].points[0];
        //inc = Math.round((Math.random() - 0.5) * 100);
        newVal = point.y + inc4;

        //if (newVal < 0 || newVal > 100) {
            //newVal = point.y - inc4;
       //}
        point.update(newVal);
    }
}, 1000);
