### 11월 28일 수업


### java

- java collection

- Collection (인터페이스)

  1. List (인터페이스)

      1. ArrayList (클래스)

          장점 : 속도 (access)

          단점 : 추가 삽입, 삭제 속도가 느림

      2. LinkedList (클래스)

          데이터가 연속적으로 저장되어 있지 않다.

          데이터가 저장된 공간들끼리 연결시켜 놓았다.

          메모리 주소로 각각 연결

          데이터를 삭제 후 나머지 데이터끼리 연결이 된다.

          추가, 삭제 속도가 빠름

      3. vector

          방향을 사용

      4. stack 

          FILO - first in last out

          LIFO - last in first out

          네비게이션에서 길 찾는 방식 - 너비 우선

      5. queue

          FIFO - first in first out

          LILO - last in last out

          네비게이션에서 길 찾는 방식 - 깊이 우선

  2.  Set (인터페이스)

  - 중복x, 순차x 
  - 값 -> Hash 함수 -> 또 다른 값

    1. HashSet

        집합

    2. TreeSet

        이진트리
        
        출력 방식

            전위 : 왼쪽에서 오른쪽 <

            중위 : 가장 왼쪽부터 아래부터 정렬되어 출력 ^

            후위 : 왼쪽부터 시작해서 오른쪽이 마지막 >


- Map (인터페이스)

  map 인터페이스는 키와 값의 쌍을 하나의 데이터로 저장한다.

  데이터 접근은 키를 찾아 데이터를 리턴한다.

  그래ㅔ서 키는 중복으로 사용하지 않는 데이터로 지정해야한다.
  (회원의 고유번호, 도서관의 책번호)

  Map 인터페이스의 메서드

  V put(k key, V value) - k, v는 제네릭 타입이고 <키, 값>으로 저장된다.

  boolean containsKey(Object k) 맵에 키가 있다면 true 없다면 false

  boolean containsValue(Object v) 맵에 value가 있다면 true 없다면 false

  V get(Object k) - 키에 대칭되는 값을 리턴

  ``` java
  // 예시
  Map<String, member> m = new HashMap<String, member>();

  m. put("10가1234", new member("김유신"));
    V put(k key, V value)
    k - String, V - member

  m.containsKey("20사1234");
    boolean containsKeyt(Object k)
    Object - String

  ```

  1. Hash Map


  2. HashTable


  3. TreeMap


  4. Properties


------------


- java를 이용해서 DB랑 연동하려면 JDBC.jar이 필요

- 문제점)

      1. JDBC.jar(디비연동 드라이버) 없으면 DB연동 불가능
      JDBC.jar 어디서 구함? => 구글링
      버전도 알아야 함.

      2. SQL문 작성을 변수로 함
      ex) String sql = "select * from emp";
      SQL 재활용 불가능

- Spring workframe


- ORM : 내가 작성한 SQL을 JAVA로 변환
- Mybatis or JPA


- 추상클래스와 인터페이스 차이점

      추상클래스
      - 정의, 구현 가능

      인터페이스
      - 메소드 정의만 가능
      - 인터페이스는 객체화가 불가능
      - 누군가에게 상속을 해주면 상속 받은 클래스를 이용해 객체화가 가능하다.