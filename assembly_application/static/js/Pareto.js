const toggleBtn = document.querySelector(".navbar__toggleBtn");
const menu = document.querySelector(".navbar__menu");
const icons = document.querySelector(".navbar__Logout");

toggleBtn.addEventListener("click", () => {
  menu.classList.toggle("active");
  icons.classList.toggle("active");
});


    var requests = $.get('/Pareto');  // $. <- 제이쿼리,
        var tm = requests.done(function(result) // 성공하면 result 값을 받아옴
            {
//                var data1= []; // [[[ ]]]  [[ ]]
                data1.push(result);  // 값 업데이트
                console.log(data1)
            });

Highcharts.chart("container4", {
  chart: {
    renderTo: "container4",
    type: "column",
  },
  title: {
    text: "Pareto",
  },
  tooltip: {
    shared: true,
  },
  xAxis: {
    categories: ["OP 10", "OP 20", "OP 30", "OP 40", "OP 50"],
    crosshair: true,
  },
  yAxis: [
    {
      title: {
        text: "",
      },
    },
    {
      title: {
        text: "",
      },
      minPadding: 0,
      maxPadding: 0,
      max: 100,
      min: 0,
      opposite: true,
      labels: {
        format: "{value}%",
      },
    },
  ],
  series: [
    {
      type: "pareto",
      name: "Pareto",
      yAxis: 1,
      zIndex: 10,
      baseSeries: 1,
      tooltip: {
        valueDecimals: 2,
        valueSuffix: "%",
      },
    },
    {
      name: "Defective Product",
      type: "column",
      zIndex: 2,
      data: [data1],
    },
  ],
});
