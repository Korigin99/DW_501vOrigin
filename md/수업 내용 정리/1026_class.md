# 10월 26일

## HTML + css : 반응형 웹사이트

- 가변적 계산식 - 너비에만 적용된다.

      (가변길이 적용 할 길이 값 / 적용할 박스를 감싸고 있는 박스의 가로너비) * 100

- 위 식을 사용하기 위해 순서가 있다.
  1. 최대 너비값 정하기
  2. 요소별 너비값 px로 길이 값 구하기
  3. 가변 길이 값 구하는 식으로 % 로 변환하여 작성

- 가변 폰트 단위

      vw - view width : 너비 기준
      vh - view height : 높이 기준
      vmin - 브라우저의 높이, 너비 중 가장 작은 것을 기준
      vmax - 브라우저의 높이, 너비 중 가 작 큰 값 기준

- 가변 폰트 예시
  ```css
  .imgb1{
   font-size: 5vw;
  }

  .imgb2{
    font-size : 5vmin;
  }
  ```

- 플레서블 박스 - flex
  
      display에 flex가 적용된 박스는 부모박스
      부모박스 하위 태그들은 자식박스(플렉스 아이템)

      플럭서블 박스이 방향
      플렉스의 방향은 축에 따라 다르다. (주축, 교차축)
      주축이 가로일 경우 플렉스 아이템들은 왼쪽에서 오른쪽으로 배치
      주축이 세로일 경우 플렉스 아이템들은 위에서 아래로 배치

- 플렉스 속성

      display - flex, inline-flex (모든 태그 적용)
        flex - 박스를 블록 수준의 플렉서블 박스로 작동
        inline-flex - 박스를 인라인 수준의 플렉서블 박스로 작동

- 아이템 배치 방향

      flex-direction - row(기본), row-reverse, column, column-reverse
        row : 박스를 왼쪽에서 오른쪽으로 배치
        row-reverse : 박스를 가로로 배치하되 역방향으로 배치
        column : 박스를 위에서 아래로 배치
        column-reverse : 박스를 세로로 배치하되 역방향으로 배치

- 아이템 배치 방식

      flex-wrap - nowrap(기본 값), wrap, wrap-reverse (플렉서블 박스에 적용)
        nowrap : 박스를 한 줄로 배치
        wrap : 박스를 여러줄로 배치
        wrap-reverse : 박스를 여러줄로 배치하되 역방향 배치 
                      주축이 가로일 때(direction : row) 아래에서 위로
                      주축이 세로일 때(driection : column) 오른쪽에서 왼쪽으로

- 아이템 배치 방식

      flex-flow - flex-flow:row wrap;


-----

## 인터넷

- URL : 페이지 주소

      ex) https://entertain.naver.com/read?oid=076&aid=0003931625


      ? : 쿼리스트링
      ? 는 프로그래밍에서 파라미터와 같은 역할을 함
      -> 쿼리 스트링이라고 부른다.

      & 연산자 : 콤마를 의미한다.

      = : 대입 연산자

      oid=076 -> oid라는 변수에 076을 대입

      메소드와 비슷한 구조
      메소드이름 (oid, aid){

      }

      

