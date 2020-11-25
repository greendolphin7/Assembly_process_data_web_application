const toggleBtn = document.querySelector(".navbar__toggleBtn");
const menu = document.querySelector(".navbar__menu");
const icons = document.querySelector(".navbar__Logout");

toggleBtn.addEventListener("click", () => {
  menu.classList.toggle("active");
  icons.classList.toggle("active");
});
Highcharts.chart("container", {
  chart: {
    type: "spline",
  },
  title: {
    text: "Electric . Temperature",
  },
  subtitle: {
    text: "",
  },
  xAxis: {
    categories: [
      "Jan",
      "Feb",
      "Mar",
      "Apr",
      "May",
      "Jun",
      "Jul",
      "Aug",
      "Sep",
      "Oct",
      "Nov",
      "Dec",
    ],
  },
  yAxis: [
    {
      className: "highcharts-color-0",
      title: {
        text: "Primary axis",
      },
    },
    {
      className: "highcharts-color-1",
      opposite: true,
      title: {
        text: "Secondary axis",
      },
    },
  ],

  tooltip: {
    crosshairs: true,
    shared: true,
  },
  plotOptions: {
    spline: {
      marker: {
        radius: 5,
        lineColor: "#666666",
        lineWidth: 1,
      },
    },
  },
  series: [
    {
      name: "op10",
      marker: {
        symbol: "square",
      },
      data: [
        4.0,
        9.9,
        42.5,
        17.5,
        3.2,
        21.5,
        20.2,
        {
          y: 26.5,
          marker: {
            symbol: "square",
          },
        },
      ],
    },
    {
      name: "op20",
      marker: {
        symbol: "square",
      },
      data: [
        7.0,
        11.9,
        21.5,
        31.5,
        41.2,
        51.5,
        60.2,
        {
          y: 26.5,
          marker: {
            symbol: "square",
          },
        },
      ],
    },
    {
      name: "op30",
      marker: {
        symbol: "square",
      },
      data: [
        3.0,
        9.9,
        9.5,
        9.5,
        9.2,
        9.5,
        10.2,
        {
          y: 26.5,
          marker: {
            symbol: "square",
          },
        },
      ],
    },
    {
      name: "op40",
      marker: {
        symbol: "diamond",
      },
      data: [
        {
          y: 3.9,
          marker: {
            symbol: "diamond",
          },
        },
        4.2,
        5.7,
        8.5,
        11.9,
        15.2,
        17.0,
        16.6,
      ],
      yAxis: 1,
    },
    {
      name: "op50",
      marker: {
        symbol: "diamond",
      },
      data: [
        {
          y: 3.9,
          marker: {
            symbol: "diamond",
          },
        },
        14.2,
        15.7,
        18.5,
        12.9,
        13.2,
        11.0,
        16.6,
      ],
      yAxis: 1,
    },
  ],
});

window.onload = function () {
  var chart = new CanvasJS.Chart("chartContainer", {
    animationEnabled: true,

    title: {
      text: "PROCESSTIME",
    },
    axisX: {
      interval: 1,
    },
    axisY2: {
      interlacedColor: "rgba(1,77,101,.2)",
      gridColor: "rgba(1,77,101,.1)",
      title: "",
    },
    data: [
      {
        type: "bar",
        name: "companies",
        axisYType: "secondary",
        color: "#014D65",
        dataPoints: [
          { y: 24, label: "op10" },
          { y: 24, label: "op20" },
          { y: 24, label: "op30" },
          { y: 24, label: "op40" },
          { y: 24, label: "op50" },
          { y: 24, label: "op60" },
        ],
      },
    ],
  });
  chart.render();
};
