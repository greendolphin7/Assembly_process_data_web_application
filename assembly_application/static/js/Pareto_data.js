function requestData() {
    var data1=[];
    var requests = $.get('/Pareto');  // $. <- 제이쿼리,
        var tm = requests.done(function (result) // 성공하면 result 값을 받아옴
            {
                data1.push(result);  // 값 업데이트
                console.log(data1)
                console.log(data)
            });
    return data1
};
