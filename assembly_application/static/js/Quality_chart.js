Highcharts.chart('container', {
  data: {
    table: 'datatable'
  },
  credits: {
            enabled: false,
        },
  chart: {
    type: 'column'
  },
  title: {
    text: 'Product Quality'
  },
  yAxis: {
    allowDecimals: false,
    title: {
      text: 'Quality'
    }
  },
  tooltip: {
    formatter: function () {
      return '<b>' + this.series.name + '</b><br/>' +
        this.point.y + ' ' + this.point.name.toLowerCase();
    }
  }
});