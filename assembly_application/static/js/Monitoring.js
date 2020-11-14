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
var chartspeed = Highcharts.chart('container-speed', Highcharts.merge(gaugeOptions, {
  yAxis: {
    min: 0,
    max: 200,
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
        '<span style="font-size:25px">{y}</span><br/>' +
        '<span style="font-size:12px;opacity:0.4">km/h</span>' +
        '</div>'
    },
    tooltip: {
      valueSuffix: ' km/h'
    }
  }]

}));

// The speed gauge
var chartrpm = Highcharts.chart('container-rpm', Highcharts.merge(gaugeOptions, {
  yAxis: {
    min: 0,
    max: 200,
    title: {
      text: 'TIME'
    }
  },

  credits: {
    enabled: false
  },

  series: [{
    name: 'rpm',
    data: [80],
    dataLabels: {
      format:
        '<div style="text-align:center">' +
        '<span style="font-size:25px">{y}</span><br/>' +
        '<span style="font-size:12px;opacity:0.4">km/h</span>' +
        '</div>'
    },
    tooltip: {
      valueSuffix: ' km/h'
    }
  }]

}));

// The speed gauge
var chart1 = Highcharts.chart('container-1', Highcharts.merge(gaugeOptions, {
  yAxis: {
    min: 0,
    max: 200,
    title: {
      text: 'PRODUCTIVITY'
    }
  },

  credits: {
    enabled: false
  },

  series: [{
    name: '1',
    data: [80],
    dataLabels: {
      format:
        '<div style="text-align:center">' +
        '<span style="font-size:25px">{y}</span><br/>' +
        '<span style="font-size:12px;opacity:0.4">km/h</span>' +
        '</div>'
    },
    tooltip: {
      valueSuffix: ' km/h'
    }
  }]

}));

// The RPM gauge
// The speed gauge
var chart2 = Highcharts.chart('container-2', Highcharts.merge(gaugeOptions, {
  yAxis: {
    min: 0,
    max: 200,
    title: {
      text: 'QUALITY'
    }
  },

  credits: {
    enabled: false
  },

  series: [{
    name: '2',
    data: [80],
    dataLabels: {
      format:
        '<div style="text-align:center">' +
        '<span style="font-size:25px">{y}</span><br/>' +
        '<span style="font-size:12px;opacity:0.4">km/h</span>' +
        '</div>'
    },
    tooltip: {
      valueSuffix: ' km/h'
    }
  }]

}));

// Bring life to the dials
setInterval(function () {
  // Speed
  var point,
    newVal,
    inc;

  if (chartspeed) {
    point = chartspeed.series[0].points[0];
    inc = Math.round((Math.random() - 0.5) * 100);
    newVal = point.y + inc;

    if (newVal < 0 || newVal > 200) {
      newVal = point.y - inc;
    }

    point.update(newVal);
  }

  // RPM
  if (chartrpm) {
    point = chartrpm.series[0].points[0];
    inc = Math.round((Math.random() - 0.5) * 100);
    newVal = point.y + inc;

    if (newVal < 0 || newVal > 200) {
      newVal = point.y - inc;
    }

    point.update(newVal);
  }

  if (chart1) {
    point = chart1.series[0].points[0];
    inc = Math.round((Math.random() - 0.5) * 100);
    newVal = point.y + inc;

    if (newVal < 0 || newVal > 200) {
      newVal = point.y - inc;
    }

    point.update(newVal);
  }

  if (chart2) {
    point = chart2.series[0].points[0];
    inc = Math.round((Math.random() - 0.5) * 100);
    newVal = point.y + inc;

    if (newVal < 0 || newVal > 200) {
      newVal = point.y - inc;
    }

    point.update(newVal);
  }

}, 2000);


setInterval(function() {
    $.ajax({
        url: 'data_temps.php',
        success: function(json) {
            var chart0 = $('#gauge0').highcharts();
            var chart1 = $('#gauge1').highcharts();

            // add the point
            chart0.series[0].setData(json[3]['data'],true);
            chart1.series[0].setData(json[8]['data'],true);
        },
         cache: false
    })
}, 1000)