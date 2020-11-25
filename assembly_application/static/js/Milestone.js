Highcharts.chart('container', {
    chart: {
        type: 'timeline'
    },
    accessibility: {
        screenReaderSection: {
            beforeChartFormat: '<h5>{chartTitle}</h5>' +
                '<div>{typeDescription}</div>' +
                '<div>{chartSubtitle}</div>' +
                '<div>{chartLongdesc}</div>' +
                '<div>{viewTableButton}</div>'
        },
        point: {
            valueDescriptionFormat: '{index}. {point.label}. {point.description}.'
        }
    },
    credits: {
            enabled: false,
    },
    xAxis: {
        visible: false
    },
    yAxis: {
        visible: false
    },
    title: {
        text: '마일스톤 일정'
    },
    subtitle: {
        text: '프로젝트 개발 기간 : 2020.08.01~2020.12.03'
    },
    colors: [
        '#4185F3',
        '#427CDD',
        '#406AB2',
        '#3E5A8E',
        '#3B4A68',
        '#363C46'
    ],
    series: [{
        data: [{
            name: '공정 설계 계획',
            label: '08/23: 공정 설계 시작',
            description: '공정에 필요한 BOM 선정, FlexSim 가상 시뮬레이션'
        }, {
            name: '설비 프로세스',
            label: '09/15: 공정, 설비, 품질 Data 생성 프로세스',
            description: 'Python으로 Data 생성'
        }, {
            name: 'DB 구축',
            label: '10/15: ERD 설계 및 DB 구축',
            description: 'MySQL DB 사용, 공정,설비,품질 Data 적재'
        }, {
            name: '머신 러닝 학습',
            label: '10/15: 공정 제품의 불량률 예측 및 분석',
            description: 'Python RandomForest 머신러닝 기법 사용, OEE(설비종합효율) 개선'
        }, {
            name: 'API 서버 구축',
            label: '11/18: Flask 프론트 엔트 설계, 웹 페이지 구성',
            description: 'flask를 이용한 웹 페이지 구축 및 java, highchatrs 시각화, 실시간 Data 모니터링 서비스'
        }, {
            name: 'AWS 배포',
            label: '12/03: 모니터링 서비스 시작',
            description: 'AWS 서비스 연결 및 배포'
        }]
    }]
});