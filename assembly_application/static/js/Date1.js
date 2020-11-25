Highcharts.chart("container1", {
  chart: {
    type: "column",
    styledMode: true,
  },

  title: {
    text: "QUALITY",
  },
  xAxis: {
    categories: ["op10", "op20", "op30", "op40", "op50", "op60"],
  },

  yAxis: {
    className: "highcharts-color-0",
    title: {
      text: "COUNT",
    },
  },

  plotOptions: {
    column: {
      borderRadius: 6,
    },
  },

  series: [
    {
      name: "OK",
      data: [1, 3, 2, 4, 5, 6],
    },
    {
      name: "NOT OK",
      data: [5, 4, 3, 2, 5, 6],
    },
  ],
});
