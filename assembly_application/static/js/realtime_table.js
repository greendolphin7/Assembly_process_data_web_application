const toggleBtn = document.querySelector('.navbar__toggleBtn');
const menu = document.querySelector('.navbar__menu');
const icons = document.querySelector('.navbar__Logout');

toggleBtn.addEventListener('click', () => {
  menu.classList.toggle('active');
  icons.classList.toggle('active');
});

var table;

function requestData() {
    $.ajax({
        url: '/realtime_table',
        success: function(value) {
            console.log(value)



            setTimeout(requestData, 10000);
        },
        cache: false
    });
}

function fillDataTable(dataSet){
  if(document.readyState === "complete") {
    $("#example").DataTable({
        retrieve: true,
        deferRender: true,
        searching: false,
        paging: false,
        "data": [dataSet],
        "columns": [
            {"data": "power"},
            {"data": "mode"},
            {"data": "execution"},
            {"data": "Xact"},
            {"data": "Yact"},
            {"data": "Zact"},
            {"data": "Xcom"},
            {"data": "Ycom"},
            {"data": "Zcom"},
            {"data": "path_feedrate"},
            {"data": "line"},
            {"data": "Block"},
            {"data": "program"}
        ],
    });
  }
}

$(document).ready(function() {
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'container',
            defaultSeriesType: 'spline',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'Realtime Electronic OP10'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'percent',
                margin: 80
            }
        },
        series: [{
            name: 'Electronic',
            data: []
        }]
    });
});