//const toggleBtn = document.querySelector(".navbar__toggleBtn");
//const menu = document.querySelector(".navbar__menu");
//const icons = document.querySelector(".navbar__Logout");
//
//toggleBtn.addEventListener("click", () => {
//  menu.classList.toggle("active");
//  icons.classList.toggle("active");
//});

Highcharts.chart("container", {
  chart: {
    type: "column",
  },

  title: {
    text: "QUALITY",
  },

  xAxis: {
    categories: ["OP10", "OP20", "OP30", "OP40", "OP50"],
  },

  yAxis: {
    allowDecimals: false,
    min: 0,
    title: {
      text: "Count",
    },
  },

  plotOptions: {
    column: {
      stacking: "normal",
    },
  },
  credits: {
    enabled: false,
  },

  series: [
    {
      name: "OK",
      data: [30, 40, 40, 20, 50],
      stack: "male",
    },
    {
      name: "NOT OK",
      data: [3, 1, 4, 4, 3],
      stack: "female",
    },
  ],
});
