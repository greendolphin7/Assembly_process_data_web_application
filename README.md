# 조립공정 데이터 실시간 모니터링 웹 어플리케이션


**팀원** 

+ 김재우 https://github.com/greendolphin7
+ 정동교 https://github.com/Eliotj-4860  
+ 진익철 https://github.com/jinikcheol  
+ 장규빈 https://github.com/Binsreoun  

## 프로젝트 개요

제조기업에서 항상 중요한 이슈는 원가경쟁력 확보이다. 이를 위해 공정 상황과 생산 결과들을 실시간으로 모니터링할 수 있는 기능들이 필수적이다.

따라서 조립공정에서 생성되는 데이터들을 설계해둔 데이터베이스에 적재한 후 웹 서버에서 실시간으로 모니터링 및 품질예측 할 수 있는 웹 애플리케이션을 만들어본다.  

대상 제품은 EGR Cooler이다.


### 개발 과정

1. 생산할 제품을 선정한 후 제품을 생산할 공정을 설계한다.    
2. 공정과정에서 생성될 데이터들을 선정하고 그에 맞게 데이터베이스 설계를 MySQL로 진행한다.  
3. python으로 데이터를 생성할 수 있는 시뮬레이션 프로그램을 만들고 데이터를 DB에 연결시켜 적재한다.  
4. Flask를 활용해 API를 설계한다. (데이터 생성, OEE 조회, 검색, 분석, 예측 기능)  
5. UI 설계 및 프론트엔드 개발, 대시보드를 만들어 시각적인 부분을 추가한다.  
6. AWS EC2 인스턴스, RDS를 이용해 배포한다.  



### 프로젝트 완료 (2020.11.27) - V. 1.0

완성된 페이지 주소: http://54.180.83.130:5000/



### 프로젝트 시연영상

↓↓↓ 시연영상은 아래 사진 클릭!  
[![Watch the video](https://i9.ytimg.com/vi/d6pkNx7TiYw/mqdefault.jpg?time=1607255700000&sqp=CJSNs_4F&rs=AOn4CLCQUHJQQt0g2Sw-DA8cUIRvQVQxvQ)](https://youtu.be/d6pkNx7TiYw)

