# 10월 14일 수업


### JavaScript
  1. 객체 정의

    - 추상화 시켜 놓은 것 
    -> 추상화란 불필요한 정보의 노출을 최소화하고 꼭 필요한 정보만 노출하는 기법

    - 차상화의 기본 : 속성과 행동을 나열하고 구성한다.
      멤버변수 : 객체의 속성을 구성
      멤버함수 : 객체의 속성을 기반으로 행동을 구현 해놓은 코드
    
    - JavaScript에서는 key와 value로 구분이 된다.

  2. 객체 생성 방법
    
      - 객체 리터럴 방식 : 변수처럼 객체를 생성하는 방식
      ```javascript
      var shape = {
        모양 : "사각형",
        x축 : 120,
        y축 : 23,
        draw:function(){  // 익명 함수 : 이름이 없는 함수
          return "x축 : " + this.x축 + "y축 : " + this.y축 + "위치에 "+this.모양+" 그리기";
        }
      };
      
      // 객체 내부에서 함수 생성시, 변수(key)의 사용은 this로 접근한다.
      // 객체의 값 출력 -> 객체.key -- >key의 value가 출력 됨
      document.write("모양 "+ shape.모양);
      document.write(shape.draw());
      // key는 문자열로만 가능

      // 학생 객체 생성 (학년, 반, 번호, 이름)
      var name = "김춘추" // 객체에서는 외부 데이터를 가져다 쓰는 것을 지양함
      var student = {
      학년 : 3, 반 : 3, 번호 : 202210327, 이름 : name // 중앙선 표시된 것은 권장하지 않는 방식이라는 의미
      };
      document.write("<br>" + student.이름);
      ```
      
      - 객체 생성 방법 2. 생성자 방식 -> new 연산자로 생성하는 방식

        1. 생성자 방식 1) Object 객체로 생성

        2. 생성자 방식 2) 함수를 통한 생성

        
      - Object 객체로 생성
        ```JavaScript
        var music = new Object();
        music.title = "Hype boy";
        music['가수'] = "뉴진스";
        music.link = '<iframe width="1280" height="753" src="https://www.youtube.com/embed/NcJo-T5Wo3U?list=RDMMNcJo-T5Wo3U" title="[릴레이댄스] NewJeans(뉴진스) - Hype Boy (4K)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';
        
        document.write( "<a href='javascript:open();'>"+ music['title']+" - "+music.가수 +"</a>");
        // 함수를 통한 생성은 외부 데이터를 사용해도 된다.
        
        function open(){
          document.getElementById("play").innerHTML= music.link;
        } */
        
        var 제목 = 'tomboy';
        music.title = 제목;
        document.write(music.title);
        ```
      - 함수를 통한 생성
        ```javaScript
        function movie(제목, 감독, 년도, 장르){
          this.영화제목=제목;
          this.감독=감독;
          this.개봉년도=년도;
          this.장르=장르;
        }
        // 함수 객체 사용 방법
        var m1 = new movie('한산','김**',2022,'전쟁');
        document.write(m1.영화제목);

        var m2 = new movie('공조2',"이**",2022,"탐정");
        document.write(m2.개봉년도);
        ```

      3. Prototype
       - javascript의 모든 객체는 prototype을 가지고 있다.
       - prototype으로 만든 거는 객체의 수 상관 없이 하나만 존재한다.
       - 그만큼 메모리가 절약 된다.
          ```JavaScript
          movie.prototype.view = function(){
            return this.영화제목 + " " + this.감독;
          }
          ```
    
--------


### MySQL
    ERWin => 데이터베이스 테이블 모델링 프로그램

    엔티티(객체, object) => 테이블

    ****관계형 테이터베이스
    종류 : MySQL, Oracle, MariaDB ...

    ****비관계형 데이터베이스(NoSQL)
    종류 : MongoDB, DynamoDB

    ****시계열 데이터베이스

    관계형 데이터베이스는 부모와 자식 관계를 가진다.

    다른 테이블 Primary Key를 사용하는 테이블을 자식 테이블이라 하고 Primary Key를 제공하는 테이블을 부모 테이블이라고 한다.

    관계형 데이타베이스에서 테이블에 최소 하난 이상 PK가 존재해야 한다.
    
Primary Key(PK)
- 주 식별자키로 테이블의 모든 데이터를 식별하는 컬럼
- 중복 불가, NULL 불가
- 함수적 종속관계

Foreign Key(FK)
- 부모 테이블에서 받아온 PK를 FK라고 한다.
- 외부 식별자키로 테이블 간의 관계 의미
- 두 테이블 간의 종속이 필요한 관계이면 그 접점이 되는 컬럼을 FK로 지정하여 서로 참조할 수 있도록 관계를 맺어준다.
- 테이블 간 잘못된 매핑을 방지하는 역할

    
      