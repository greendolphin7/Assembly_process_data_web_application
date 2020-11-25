//////$(function () {
//////    $(document).ready(function () {
//////        Highcharts.setOptions({
//////            global: {
//////                useUTC: false
//////            }
//////        });
//////
//////        $('#container').highcharts({
//////            chart: {
//////                type: 'column',
//////                animation: Highcharts.svg, // don't animate in old IE
//////                marginRight: 10,
//////                events: {
//////                    load: function () {
//////                        var requests = $.get('/Pareto');
//////                            var tm = requests.done(function(result)
//////                            {
//////                                console.log(result)
//////                        // set up the updating of the chart each second
//////                                var data1=[];
//////                                data1.push(result);
//////                                var series = this.series[0];
//////                                setInterval(function () {
//////
//////                            series.setData([y,  y*2, y+1, y/2]);
//////                        }, 1000);
//////                                data1.push(result);
//////                                series.setData([1, 3, 4, 5, 6]);
//////                                console.log(result)
//////                        });
//////                    }
//////                }
//////
//////
//////
//////
//////
//////
////    //----------------------------------------------------------------------------------
//////                --------------------------------------
//////                var requests = $.get('/Pareto');  // $. <- 제이쿼리,
//////        var tm = requests.done(function(result) // 성공하면 result 값을 받아옴
//////            {
//////
//////                data1.push(result);  // 값 업데이트
//////                console.log(data1[0])
//////                setTimeout(requestData, 10000);
//////            });
//////               ----------------------------------
////$(function () {
////    $(document).ready(function () {
////        Highcharts.setOptions({
////            global: {
////                useUTC: false
////            }
////        });
////
////        $('#container').highcharts({
////            chart: {
////                type: 'column',
////                animation: Highcharts.svg, // don't animate in old IE
////                marginRight: 10,
////                events: {
////                    load: function () {
////                         var requests = $.get('/Pareto');
////                            var tm = requests.done(function(result)
////                            {
////                        // set up the updating of the chart each second
////                                var series = this.series[0];
////                            setInterval(function () {
////                            series.setData(result);
////                        }, 1000);
////
////                    });
////                }
////            },
////            title: {
////                text: 'Live random data'
////            },
////            xAxis: {
////                type: 'datetime',
////                tickPixelInterval: 150
////            },
////            yAxis: {
////                title: {
////                    text: 'Value'
////                },
////                plotLines: [{
////                    value: 0,
////                    width: 1,
////                    color: '#808080'
////                }]
////            },
////            tooltip: {
////                formatter: function () {
////                    return '<b>' + this.series.name + '</b><br/>' +
////                        Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
////                        Highcharts.numberFormat(this.y, 2);
////                }
////            },
////            legend: {
////                enabled: false
////            },
////            exporting: {
////                enabled: false
////            },
////            series: [{
////                name: 'Random data',
////                data: [0,0,0,0]
////            }]
////    });
//
//$(function () {
//    $(document).ready(function () {
//        Highcharts.setOptions({
//            global: {
//                useUTC: false
//            }
//        });
//            $('#container').highcharts('Barchart',{
//            chart: {
//                type: 'column',
//                animation: Highcharts.svg, // don't animate in old IE
//                marginRight: 10,
//                events: {
//                    load: function () {
//							var requests = $.get('/Pareto');
//                            var tm = requests.done(function(result)
//                            {
//                                var series = this.series[0];
//                                var data1 = [];
//                                data1.push(result);
//                                var y1 = data1[0][0]
//                              var y2 = data1[0][1]
//                               var y3 = data1[0][2]
//                                var y4 = data1[0][3]
//                                var y5 = data1[0][4]
//
//                        // set up the updating of the chart each second
//
//                            setInterval(function () {
//                            var series = series.setData([y1, y2, y3, y4, y5]);
//                        }, 1000);
//                    });
//                }
//                }
//            },
//            title: {
//                text: 'Live random data'
//            },
//            xAxis: {
//                type: 'datetime',
//                tickPixelInterval: 150
//            },
//            yAxis: {
//                title: {
//                    text: 'Value'
//                },
//                plotLines: [{
//                    value: 0,
//                    width: 1,
//                    color: '#808080'
//                }]
//            },
//            tooltip: {
//                formatter: function () {
//                    return '<b>' + this.series.name + '</b><br/>' +
//                        Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
//                        Highcharts.numberFormat(this.y, 2);
//                }
//            },
//            legend: {
//                enabled: false
//            },
//            exporting: {
//                enabled: false
//            },
//            series: [{
//                name: 'Random data',
//                data: [0,0,0,0,0]
//            }]
//        });
//    });
//});
//
//
//
//
//
//
//
//
//

var chart;

$(function () {
    $(document).ready(function () {
        chart = new Highcharts.Chart({
            global: {
                useUTC: false
            }
        });

        $('#container').highcharts({
            chart: {
                type: 'column',
                animation: Highcharts.svg, // don't animate in old IE
                marginRight: 10,
                events: {
                    load: function () {
                                var requests = $.get('/Pareto');
                                   var tm = requests.done(function(result)
                                    {
                                        var series = chart.series[0];
                                         var data1 = [];
                                            data1.push(result);
                                            var y1 = data1[0][0];
                                            var y2 = data1[0][1];
                                            var y3 = data1[0][2];
                                            var y4 = data1[0][3];
                                            var y5 = data1[0][4];
                                            console.log(data1)
                         //set up the updating of the chart each second

                        setInterval(function () {
                          chart.series[0].data([y1, y2, y3, y4, y5]);
                        }, 1000);
                  });
                }
               }
            },
            title: {
                text: 'Live random data'
            },
            xAxis: {
                type: 'datetime',
                tickPixelInterval: 150
            },
            yAxis: {
                title: {
                    text: 'Value'
                },
                plotLines: [{
                    value: 0,
                    width: 1,
                    color: '#808080'
                }]
            },
            tooltip: {
                formatter: function () {
                    return '<b>' + this.series.name + '</b><br/>' +
                        Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                        Highcharts.numberFormat(this.y, 2);
                }
            },
            legend: {
                enabled: false
            },
            exporting: {
                enabled: false
            },
            series: [{
                name: 'Random data',
                data: [0,0,0,0,0]
            }]
        });
    });
});