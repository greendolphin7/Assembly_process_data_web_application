$(function () {
    $.get('http://127.0.0.1:5126/Pareto', function (data) {


        var Serie_data_1 = [],
            Serie_data_2 = [],
            Serie_data_3 = [],
            dataLength = data.length,


            i = 0;

        for (i; i < dataLength; i += 1) {
            Serie_data_1.push([
                data[i][0], // the date
                data[i][1], //data
            ]);

            Serie_data_2.push([
                data[i][0], // the date
                data[i][2] // data
            ]);

            Serie_data_3.push([
                data[i][0], // the date
                data[i][3] // data
            ]);
        }


        // create the chart
        $('#container').highcharts('pareto', {

            rangeSelector: {
                selected: 1
            },

            yAxis: [{
                title: {
                    text: 'Serie 1'
                },
            }, {
                title: {
                    text: 'Serie 2'
                }
            }, {
                title: {
                    text: 'Serie 3'
                }
            }],

            series: [{
                name: 'Serie 1',
                data: Serie_data_1,
            }, {
                name: 'Serie 2',
                data: Serie_data_2,
                yAxis: 1,
            },{
                name: 'Serie 3',
                data: Serie_data_3,
                yAxis: 2,
            }]
        });
    });
});