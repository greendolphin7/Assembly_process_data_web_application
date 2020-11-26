// charts = one minute
let UPDATE = 10000;

function() {
	  var table = $('#coinTable').DataTable( {
             ajax: {
                 url: "http://3.35.208.236:5000/Search_data",
                 dataSrc: ''
             },
		    colReorder: {
			realtime: true
		    },
            "aoColumns" : [
                {data : 'product_key'},
                {data : 'op60_timestamp'},
                {data : 'body_l'},
                {data : 'body_w'},
                {data : 'body_h'},
                {data : 'wavyfin_l'},
                {data : 'wavyfin_w'},
                {data : 'wavyfin_h'},
                {data : 'op10_machine_data'},
                {data : 'op10_process_time'},
                {data : 'op10_product_size_l'},
                {data : 'op10_product_size_w'},
                {data : 'op10_product_size_h'},

                {data : 'pipe1_l'},
                {data : 'pipe1_w'},
                {data : 'pipe1_l'},
                {data : 'op20_machine_data'},
                {data : 'op20_process_time'},
                {data : 'op20_product_size_l'},
                {data : 'op20_product_size_w'},
                {data : 'op20_product_size_h'},

                {data : 'pipe2_l'},
                {data : 'pipe2_w'},
                {data : 'pipe2_l'},
                {data : 'op30_machine_data'},
                {data : 'op30_process_time'},
                {data : 'op30_product_size_l'},
                {data : 'op30_product_size_w'},
                {data : 'op30_product_size_h'},

                {data : 'flange1_l'},
                {data : 'flange1_w'},
                {data : 'flange1_h'},
                {data : 'op40_machine_data'},
                {data : 'op40_process_time'},
                {data : 'op40_product_size_l'},
                {data : 'op40_product_size_w'},
                {data : 'op40_product_size_h'},

                {data : 'flange2_l'},
                {data : 'flange2_w'},
                {data : 'flange2_h'},
                {data : 'op50_machine_data'},
                {data : 'op50_process_time'},
                {data : 'op50_product_size_l'},
                {data : 'op50_product_size_w'},
                {data : 'op50_product_size_h'},

		    ]
	        } );

setInterval( function () {
  console.log('reload');
    //$('#coinTable').DataTable().ajax.load();
     //$('#coinTable').DataTable().ajax.reload(null, true);
}, UPDATE  );
