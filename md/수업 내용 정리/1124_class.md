## 11월 24일

### java

- MVC

      M : model
      V : view
      C : control

- model

      데이터를 다루는 클래스들이 들어간다


- view 

      웹페이지

- control

      클라이언트 요청

      control - 클라이언트 요청

      login
      sign
      order
      event

      ->

      BO - 클라이언트가 보낸 데이터를 가공(확인하는 작업)

      login
      service

      ->

      DAO - 데이터 저장

      login
      DAO

      
      VO - 데이터가 저장되기 위한 클래스
      -> 로그인 한 사람의 데이터를 저장하기 위한 공간


