// charts = one minute
let UPDATE = 10000;

$(document).ready(function() {
	  var table = $('#coinTable').DataTable( {
             ajax: {
                 url: "http://localhost:5000/realtime_table_OP30",
                 dataSrc: ''
             },
		    colReorder: {
			realtime: true
		    },
            "aoColumns" : [
                {data : 'product_key'},
                {data : 'machine_code'},
                {data : 'process_time'},
                {data : 'start_time'},
                {data : 'end_time'},
                {data : 'product_test'},
                {data : 'product_size_l'},
                {data : 'product_size_w'},
                {data : 'product_size_h'}
		    ]
	        } );


} );

setInterval( function () {
  console.log('reload');
    //$('#coinTable').DataTable().ajax.reload();
       $('#coinTable').DataTable().ajax.reload(null, true);
}, UPDATE  );