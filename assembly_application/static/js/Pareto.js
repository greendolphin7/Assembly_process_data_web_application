//const toggleBtn = document.querySelector('.navbar__toggleBtn');
//const menu = document.querySelector('.navbar__menu');
//const icons = document.querySelector('.navbar__Logout');
//
//toggleBtn.addEventListener('click', () => {
//  menu.classList.toggle('active');
//  icons.classList.toggle('active');
//});
//var chart;
//var data1=[];
//setInterval(function requestData() {
//    var requests = $.get('/Pareto');  // $. <- 제이쿼리,
//    var tm = requests.done(function(result) // 성공하면 result 값을 받아옴
//        {
//
//            data1.push(result);
//            data1 = data1[0]
//          // 값 업데이트
//            console.log(result)
//            console.log(data1)
//        });
//    }, 5000);
var data1= [];
function requestData() {
    var requests = $.get('/Pareto');  // $. <- 제이쿼리,
        var tm = requests.done(function(result) // 성공하면 result 값을 받아옴
            {

                data1.push(result);  // 값 업데이트
                console.log(data1[0])
                setTimeout(requestData, 10000);
            });
        cache: false
}
//var chart;
//var data2 = [];
//function requestData() {
//    $.ajax({
//        url: '/Pareto',
//        success: function(result) {
//            console.log(result)
//            data2.push(result);
//            data2 = data2[0]
//            setTimeout(requestData, 2000);
//        },
//        cache: false
//    });
//}
var chart;
$(document).ready(function() {
    chart = Highcharts.chart('container4', {
        chart: {
            renderTo: 'container4',
            type: "column",
            events: {
                load: requestData
            }
        },

        title: {
            text: "Pareto"
        },
        tooltip: {
            shared: true
        },
        xAxis: {
            categories: ['OP10','OP20','OP30','OP40','OP50'],
            crosshair: true
        },
        yAxis: [{
        id: "y_axis_0",
        title: {
            text: ''
        }
    }, {
        title: {
            text: ''
        },
        minPadding: 0,
        maxPadding: 0,
        max: 100,
        min: 0,
        opposite: true,
        labels: {
            format: "{value}%"
        }
    }],
        series: [{
            type: 'pareto',
            name: 'Pareto',
            yAxis: 1,
            zIndex: 10,
            baseSeries: 1,
            tooltip: {
                valueDecimals: 2,
                valueSuffix: '%'
            },
        }, {
            name: 'Complaints',
            type: 'column',
            zIndex: 2,
            yAxis: 'y_axis_0',
            data: data1
        }]
         });
    });

//--------------------------------------------------------------------------------

//---------------------------------------------------------------------------------
//function createHighCharts(data){
//    Highcharts.chart("chart",{
//    title:{
//        text: "pareto"
//    },
//    subtitle:{
//        text: "Defective pareto"
//    },
//    xAxis:[
//    }
//        categories:data[0],
//        labels:{
//            rotation:-45
//        }
//    }
//    ],
//    yAxis:[
//    {
//        title:{
//            text:"OP"
//        }
//    }
//    ],
//    series:[
//    {
//        name:"defective",
//        color:"#000000,
//        type:"colum",
//        data:data[1]
//        }
//        ]
//    });
//}