//const toggleBtn = document.querySelector('.navbar__toggleBtn');
//const menu = document.querySelector('.navbar__menu');
//const icons = document.querySelector('.navbar__Logout');
//
//toggleBtn.addEventListener('click', () => {
//  menu.classList.toggle('active');
//  icons.classList.toggle('active');
//});

// charts = one minute
let UPDATE = 10000;

$(document).ready(function() {
	  var table = $('#coinTable').DataTable( {
             ajax: {
                 url: "http://3.35.208.236:5000/Predict_data",
                 dataSrc: ''
             },
             lengthChange: false,
             order: [ [ 1, "asc" ] ],
             searching: false,
             paging: false,
		    colReorder: {
			realtime: true
		    },
            "aoColumns" : [
                {data : 'product_key'},
                {data : 'body_size_l'},
                {data : 'body_size_w'},
                {data : 'body_size_h'},
                {data : 'wavyfin_size_l'},
                {data : 'wavyfin_size_w'},
                {data : 'wavyfin_size_h'},
                {data : 'op10_machine_data'},
                {data : 'op10_size_l'},
                {data : 'op10_size_w'},
                {data : 'op10_size_h'},

                {data : 'pipe1_size_l'},
                {data : 'pipe1_size_w'},
                {data : 'pipe1_size_h'},
                {data : 'op20_machine_data'},
                {data : 'op20_size_l'},
                {data : 'op20_size_w'},
                {data : 'op20_size_h'},

                {data : 'pipe2_size_l'},
                {data : 'pipe2_size_w'},
                {data : 'pipe2_size_h'},
                {data : 'op30_machine_data'},
                {data : 'op30_size_l'},
                {data : 'op30_size_w'},
                {data : 'op30_size_h'},
                {data : 'predict_result'},
		    ]
	        } );

} );

setInterval( function () {
  console.log('reload');
//    $('#coinTable').DataTable().ajax.reload();
       $('#coinTable').DataTable().ajax.reload(null, true);
}, UPDATE);


function exportTableToCsv(tableId, filename) {
  if (filename == null || typeof filename == undefined) filename = tableId;
  filename += ".csv";

  var BOM = "\uFEFF";

  var table = document.getElementById(tableId);
  var csvString = BOM;
  for (var rowCnt = 0; rowCnt < table.rows.length; rowCnt++) {
    var rowData = table.rows[rowCnt].cells;
    for (var colCnt = 0; colCnt < rowData.length; colCnt++) {
      var columnData = rowData[colCnt].innerHTML;
      if (columnData == null || columnData.length == 0) {
        columnData = "".replace(/"/g, '""');
      } else {
        columnData = columnData.toString().replace(/"/g, '""'); // escape double quotes
      }
      csvString = csvString + '"' + columnData + '",';
    }
    csvString = csvString.substring(0, csvString.length - 1);
    csvString = csvString + "\r\n";
  }
  csvString = csvString.substring(0, csvString.length - 1);

  // IE 10, 11, Edge Run
  if (window.navigator && window.navigator.msSaveOrOpenBlob) {
    var blob = new Blob([decodeURIComponent(csvString)], {
      type: "text/csv;charset=utf8",
    });

    window.navigator.msSaveOrOpenBlob(blob, filename);
  } else if (window.Blob && window.URL) {
    // HTML5 Blob
    var blob = new Blob([csvString], { type: "text/csv;charset=utf8" });
    var csvUrl = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.setAttribute("style", "display:none");
    a.setAttribute("href", csvUrl);
    a.setAttribute("download", filename);
    document.body.appendChild(a);

    a.click();
    a.remove();
  } else {
    // Data URI
    var csvData =
      "data:application/csv;charset=utf-8," + encodeURIComponent(csvString);
    var blob = new Blob([csvString], { type: "text/csv;charset=utf8" });
    var csvUrl = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.setAttribute("style", "display:none");
    a.setAttribute("target", "_blank");
    a.setAttribute("href", csvData);
    a.setAttribute("download", filename);
    document.body.appendChild(a);
    a.click();
    a.remove();
  }
}