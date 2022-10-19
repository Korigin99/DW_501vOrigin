# 10월 18일 수업

## 오전 수업

### *window* 와 *brower*

    window 객체 - 최상위 객체

      location 객체 (주소)
      document 객체 (출력 화면)
      history 객체 (방문 내역)
      screen 객체 (브라우저와 브라우저가 표시되는 모니터 화면 전체)
      navigator (브라우저 정보)

  - location 객체를 이용하여 주소를 이동할 수 있다.
  ```js
  <script>
    function move(){
      location.href = "https://www.google.com"; // location 객체의 href를 활용
    }
  </script>
  <body>
    <a href="https://www.naver.com">네이버</a> // a태그도 location 객체의 일부이다.
    // location 객체의 href를 이용
    <button onclick="move()">구글</button>
    <button onclick="location_object()">location 객체 보기</button>
    <script>
      function location_object(){
        window.close();
      }
    </script>
  <body>
  ```

- window 객체 종류
<img src="../image/brower Object.jpg" width="600px">

## window 객체 - 최상위 객체
    window 객체 : 브라우저를 열었을 때 생성되는 항상 존재하는 객체
    석상 : classes, defaultStatus, document, frame, history, legnth, location, navigator 등

    - classes : HTML 문서에서 정의된 모든 스타일 시트
    - defaultStatus : 상태바에 표시될 문자열 지정
    - frame : window에 포함된 프레임수 반환
      -> 여러 프레임이 존재할 경우 배열 형태로 표현 가능
        (window.frames[0])
    - history : window가 방문한 URL 정보
    - innerHeight : 현재 브라우저의 document 영역의 높이
    - innerWidth : 현재 브라우저의 document 영역의 너비
    - location : 현재 문서의 URL 정보
    - menubar : 메뉴바 표시 여부 지정
    - opener : open() 함수로 생성한 윈도우 이름
              -> 부모를 의미함
    - name : window 이름
    - outerHeight : 윈도우 밖 테두리 높이
    - outerWidth : 윈도우 밖 테두리 너비
    - pageXOffset : window에 표시되는 X 위치
    - pageYOffset : window에 표시되는 Y 위치
    - scroll

## window 객체 메서드
    - alert() : 메세지와 OK 버튼을 가진 메시지 박스
    - setInterval : 지정된 시간만큼 반복
    - setTimeout : 지정된 시간 이후에 실행
    - clearInertval : setInterval 해제
    - clearTimeout : setTimeout 해재
    - close() : 윈도우 닫기
    - confirm : 질문 다이얼로그 확인과 취소 버튼을 가진 박스
    - back, forward : 뒤, 앞으로 이동
    - moveBy(x, y) : 윈도우 이동(상대적)
    - moveTo(x, y) : 윈도우 이동(절대적)
    - resizeBy(x, y) : 윈도우 크기 변경(상대적)
    - resizeTo(x, y) : 윈도우 크기 변경(절대적)
    - open : 새 윈도우 생성
      -> open( url, window_name, property)
      -> url : 페이지 주소
      -> window_name : _blank(새창에 열린다.)
      -> _parent (부모 프레임에 열린다.)
      -> _self (현재 페이지를 대체한다.)
         _top (로드된 프레임셋 대체)
      -> prooerty : 새 window의 옵션 부여 
                    height 새창의 높이 지정
                    width 새창의 너비 지정
                    left 모니터 화면 왼쪽에서부터 위치
                    top 모니터 화면 위쪽에서부터 위치
                    channelmode : 전체화면 (yes, NO)
                    fullscreen : 전체화면 (yes, no)
                    location : 주소 표지줄 표시여부 (yes, no)
                    menubar : 메뉴바 표시 여부 (yes, no)
                    scrollbars : 스크롤바 표시여부 (yes, no)
                    status : 상태바 표시여부 (yes, no)
                    resizable : window 크기 변경 가능 여부 (yes, no)
                    toobat : 툴바 표시여부 (yes, no)





-----

## 오후 수업

### DB
* 관계형 데이터 베이스

  * 관계 1:1(주민번호)

  * 부모 자식 관계를 가진 관계형 데이터 베이스는 자식테이블에서 부모테이블 PK를 사용하고 있다면, 부모 테이블에 있는 PK는 지울 수 없다.

- 삭제 방법
  - **ON DELETE CASCADE** : 부모테이블에 있는 데이터를 지우면 자식테이블에 있는 데이터도 삭제 - 자주 사용
  ```sql
  --자식 테이블을 생성할 때 입력
  CREATE TABLE products(
	product_id int(4) AUTO_INCREMENT PRIMARY KEY,
	product_price int(4) comment '물품가',
	create_at datetime comment '입고 날짜',
	shipment_price int(4) comment '출하가',
	brand_id int(4) comment '브랜드 번호',
	FOREIGN KEY (brand_id) REFERENCES brand(brand_id) ON DELETE CASCADE
  );
  ```
  - ON DELETE SET NULL : 부모테이블에 있는 데이터를 지우면 자식테이블에 있는 데이터에 NULL.
  - ON DELETE NO ACTION : 부모테이블에 있는 데이터를 지우면 자식테이블에 데이터에는 변화가 없다.
  - ON DELETE SET DEFAULT : 부모테이블에 있는 데이터를 지우면 자식테이블 데이터 DEFAULT 값으로 변경
  - *ON DELETE RESTRICT(기본값) : 자식테이블에서 부모테이블 사용하고 있으면 삭제 불가능


          

