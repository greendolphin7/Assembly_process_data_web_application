# 조립공정 데이터 실시간 모니터링 웹 어플리케이션


**팀원** 

+ 김재우 https://github.com/greendolphin7
+ 정동교 https://github.com/Eliotj-4860  
+ 진익철 https://github.com/jinikcheol  
+ 장규빈 https://github.com/Binsreoun  

## 프로젝트 개요

조립공정에서 생성되는 데이터들을 설계해둔 데이터베이스에 적재한 후 웹 서버에서 실시간으로 모니터링 할 수 있는 웹 애플리케이션을 만든다.


### 개발 계획

1. python으로 flexsim에서 시뮬레이션으로 만들었던 것과 비슷한 수준으로 데이터를 생성할 수 있는 프로그램을 만든다.  
2. DB 모델링을 통해 데이터베이스에 넣을 틀을 만든다. (MySQL)  
3. AWS 서버를 EC2 인스턴스로 만든다. (t2 Micro)  
4. 프로그램으로 생성된 데이터를 Server로 POST 요청을 통해 DB에 적재하거나 GET 요청으로 조회할 수 있다. (Flask or Django)  
5. 데이터를 간단한 홈페이지에서 조회할 수 있다.  
6. 이후 더 다양한 기능들과 복잡한 데이터베이스를 개발한다. (단순 조회, 검색, 예측, OEE 조회 기능)


### 진행해야 할 사항

Local PC에서 Flask -> 프로그램 짜놓고 연결되면 DB만 AWS 연결
확인되면 EC2 올리기 / Django로 GET 방식 만들기, API 만들어서 설계

1. 적재하는 과정에서 machine 테이블에 적재할 데이터가 부실 (makespan, start_time, end_time) 제대로 안넣음
2. DB에 적재된 데이터를 웹으로 가져와야 함
3. API를 좀 더 세부적, 기능들을 다듬을 필요 있음 (단순 조회가 아니라 분석용)
(JOIN활용) -> OEE (makespan필요)
4. AWS 연결
