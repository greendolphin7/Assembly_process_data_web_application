var data1= [];
var data2= [];
var data3= [];
var requests = $.get('/Scatter_OP50');  // $. <- 제이쿼리,
   var tm = requests.done(function(result) // 성공하면 result 값을 받아옴
        {
//                var data1= []; // [[[ ]]]  [[ ]]
            data1.push(result[0][0]);
            //console.log(data1)
            data2.push(result[0][1]);
            data3.push(result[0][2]);// 값 업데이트


Highcharts.chart("container", {
title: {
text: "Temperature vs Length",
},
subtitle: {
text: "",
},
credits: {
            enabled: false,
        },
xAxis: {
gridLineWidth: 1,
title: {
  enabled: true,
  text: "Temperature",
},
startOnTick: true,
endOnTick: true,
showLastLabel: true,
},
yAxis: {
title: {
  text: "Length (mm)",
},
},
legend: {
layout: "vertical",
align: "right",
verticalAlign: "middle",
},
series: [
{
  name: "Observations",
  type: "scatter",
  color: "red",
  data: data1[0]
},
],
tooltip: {
headerFormat: "<b>{series.name}</b><br>",
pointFormat: "{point.x} , {point.y} ",
},
responsive: {
rules: [
  {
    condition: {
      maxWidth: 500,
    },
    chartOptions: {
      legend: {
        align: "center",
        layout: "horizontal",
        verticalAlign: "bottom",
      },
    },
  },
],
},
});

Highcharts.chart("container2", {
  title: {
    text: "Temperature vs Width",
  },
  subtitle: {
    text: "",
  },
  credits: {
            enabled: false,
        },
  xAxis: {
    gridLineWidth: 1,
    title: {
      enabled: true,
      text: "Temperature",
    },
    startOnTick: true,
    endOnTick: true,
    showLastLabel: true,
  },
  yAxis: {
    title: {
      text: "Width (mm)",
    },
  },
  legend: {
    layout: "vertical",
    align: "right",
    verticalAlign: "middle",
  },
  series: [
    {
      name: "Observations",
      type: "scatter",
      color: "blue",
      data: data3[0]
    },
  ],
  tooltip: {
    headerFormat: "<b>{series.name}</b><br>",
    pointFormat: "{point.x} , {point.y} ",
  },
  responsive: {
    rules: [
      {
        condition: {
          maxWidth: 500,
        },
        chartOptions: {
          legend: {
            align: "center",
            layout: "horizontal",
            verticalAlign: "bottom",
          },
        },
      },
    ],
  },
});

Highcharts.chart("container3", {
  title: {
    text: "Temperature vs Height",
  },
  subtitle: {
    text: "",
  },
  xAxis: {
    gridLineWidth: 1,
    title: {
      enabled: true,
      text: "Temperature",
    },
    startOnTick: true,
    endOnTick: true,
    showLastLabel: true,
  },
  credits: {
            enabled: false,
        },
  yAxis: {
    title: {
      text: "Height (mm)",
    },
  },
  legend: {
    layout: "vertical",
    align: "right",
    verticalAlign: "middle",
  },
  series: [
    {
      name: "Observations",
      type: "scatter",
      color: "yellow",
      data: data2[0]
    },
  ],
  tooltip: {
    headerFormat: "<b>{series.name}</b><br>",
    pointFormat: "{point.x} , {point.y} ",
  },
  responsive: {
    rules: [
      {
        condition: {
          maxWidth: 500,
        },
        chartOptions: {
          legend: {
            align: "center",
            layout: "horizontal",
            verticalAlign: "bottom",
          },
        },
      },
    ],
  },
});

});
