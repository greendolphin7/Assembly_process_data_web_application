setInterval(function ()
{
    // Ajax call to get the Data from Flask
    var requests = $.get('/real_value');
    var tm = requests.done(function (result)
    {
        var data1 = [],
        process = [];
        data1.push(result[0]);
        data1.push(result[1]);
        process.push(Math.round(result[1]/8640*100))
        //console.log(data1)
        $(".sensor2").text("");
        $(".sensor2").text(Math.round(data1[1]) );
        $(".sensor0").text("");
        $(".sensor0").text(process +'%');
        $(".sensor1").val(process);
        //console.log(process)
        // call it again after one second
        //setTimeout(requestData, 2000);
    });
}, 10000);


