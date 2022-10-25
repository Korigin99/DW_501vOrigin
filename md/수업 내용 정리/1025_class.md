# 10월 25일 수업

### js - 반응형 웹 사이트

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
- meta viewport / content
  - width=device=width -> (문서를 장치의 화면 너비에 일치시킬 것을 지시)

  - initial-scale=1 -> (페이지에 처음 접속 했을 때 보여지는 비율 설정)
    - user-scalable : 사용자의 축소/확대 여부

    - minimum-scale : 뷰포트의 최소 배율값(0~10)

    - maxmum-scale : 뷰포트의 최대 배율값(0~10)

- 미디어 쿼리

  - @media 미디어유형 논리연산자 (특성) {태그 {속성 : 값}}
  ```html
  <style>
    body{background:yellow;}

    @media only screen and (max-width:600px){
      body{background-color: pink;}
    }
  </style>
  ```
-  미디어쿼리에 사용되는 미디어 유형
    
        all : 모든 디바이스
        print : 인쇄결과물 및 인쇄 미리보기
        screen : 화면대상
        tv : 음성과 영상이 동시에 출력되는 TV
        aural : 음성 합성 장치에서 사용할 경우
        hanheld : pad와 같은 기기 (손세 들고 다니는 장치)
        projection : 빔 프로젝트

- 미디어쿼리 구문
          
      only : 미디어쿼리를 지원하지 않는 웹 브라우저에서는 미디어쿼리를 무시하고 실행하지 않는다.
      not : not 다음에 지정하는 미디어 유형 제외
      and : 조건을 여러개 연결
      , : ,(comma) 여러 조건 중 하나라도 해당되면 실행(or 연산자)

- 미디어쿼리 특성

      width, height : 웹페이지의 너비, 높이 조건
      min-width, min-height : 웹페이지의 최소 너비, 높이
      max-width, max-height : 웹페이지의 최대 너비, 높이
      device-width, device-height : 기기의 너비, 높이
      device-min-width, device-min-height : 기기의 최소너비, 높이
      device-max-width, device-max-height : 기기의 최대너비, 높이
      orientation : 모바일의 세로(portarait), 가로(landscape)


- 다른 사용 방법

  ```html
  <!-- 방법 1 -->
  <style>@import url("css파일경로") all and (max-width:500px);</style>
  <!-- 방법 2 -->
  <link rel="stylesheet" media="all and (max-width:900px)" href="">
  ```

- 미디어쿼리 사용 전에 고려해야 할 부분

    - 모바일 우선 적용 일 경우 작은 사이즈 -> 큰 사이즈 순으로 작성
      모바일 크기에서 웹사이트 제작 후 크기별로 반응하도록 제작

    - 모바일 버전으로 제작 완료 후 태블릿 -> 데스크 탑 순으로 제작한다

    - 모바일 우선일 경우는 min을 사용,
      데스크탑 우선일 경우는 max를


- 크기 단위
      
      px : 절대길이, 디스플레이 장치의 픽셀 1개의 크기

      - 반응형에서 많이 사용되는 단위

      % : 상대 길이, 기본 크기에 대해 상대ㅔ적인 크기를 가지는 단위
        100% = 16px;

      rem : 상대길이, 해당 폰트의 대문자 M의 너비를 기준으로 하는 단위
        html 기준
        1rem = 16px;
        2rem = 32px;

      em : 상대길이, 해당 폰트의 대문자 M의 너비를 기준으로 하는 단위 부모 태그의 폰트 크기를 기준으로 배율 설정
        부모태그 기준
        1em = 16px;


------
<br>

# JSON

## JSON이란?
- JSON 는 Douglas Crockford가 널리 퍼뜨린 Javascript 객체 문법을 따르는 문자 기반의 데이터 포맷입니다. JSON이 Javascript 객체 문법과 매우 유사하지만 딱히 Javascript가 아니더라도 JSON을 읽고 쓸 수 있는 기능이 다수의 프로그래밍 환경에서 제공됩니다.

- 쉽게 말 해 프론트엔드와 백엔드가 의사소통 할 때 사용되는 '형식'이 JSON이다.

## JSON 문법 
- json(Java Script Object Notation) 배워보기

- JSON은 Javascript 객체 리터럴 문법을 따르는 문자열입니다.

- JSON은 Key와 Value로 구성 

- Key는 데이터베이스에 PK처럼 중복될 수 없다. Value는 중복 가능!

- json value에 오는 데이터 타입 
  - int, double, string, boolean, array, json 등 json도 데이터 타입!
```js
<script>
    

    var apple = {
      이름: '홍길동',
      나이: 30,
    };

    console.log(apple.이름);
    console.log(apple.나이);

    var data = {
      name: '홍길동',
      money: 400,
      bank: '카카오뱅크',
    };

    var data2 = {
      이름: '홍길동', // string
      나이: 40, // int
      취미: ['등산', '게임', '독서', '헬스'], // array
      결혼여부: false, // boolean
      키: 182.5, // double
      가족: {
        아빠이름: '신형만',
        엄마이름: '봉미선',
      }, // json
    };
```

# JQuery

- Query(제이쿼리)는 HTML의 클라이언트 사이드 조작을 단순화 하도록 설계된 크로스 플랫폼의 자바스크립트 라이브러리다. 존 레식이 2006년 뉴욕 시 바캠프(Barcamp NYC)에서 공식적으로 소개하였다. jQuery는 오늘날 가장 인기있는 자바스크립트 라이브러리 중 하나이다. 

- 제이쿼리를 사용하는 이유

      페이지 내부 요소에 접근하기 쉽다.
      제이쿼리를 사용하지 않으면 DOM 트리를 이용해서 요소(element)에 접근해야 합니다. 이는 배우기도 어렵고 불편한데, 제이쿼리를 사용하면 CSS의 선택자를 이용해서 간편하게 접근할 수 있습니다.

      페이지의 보여지는 모습을 변경하기 쉽다.
      동적으로 페이지의 모습(CSS)를 변경하기 위해서는 자바스크립트를 사용해야 합니다. 이를 제이쿼리를 이용하여 작성하면 코드도 간결해지고 직관적으로 작성할 수 있습니다.
      또, 아작스(AJAX)등에서 페이지를 리로딩하지 않고 동적으로 로딩할 때도 자바스크립트를 이용하는데, 이것 역시 제이쿼리를 이용하면 코드도 간결해지고 더 쉽게 구현할 수 있습니다.

      상호작용 처리가 쉽고 애니메이션을 사용할 수 있다.
      HTML문서의 목적은 페이지의 구조와 데이터를 표현하는 것입니다. 따라서 HTML 태그 속성의 이벤트를 사용하면 이 목적에 어긋난다고 할 수 있습니다. 이벤트를 제이쿼리를 사용해서 핸들링하면 HTML문서를 변경할 필요도 없고 더 쉽습니다.
      또 다양한 애니메이션을 간편하게 사용할 수 있습니다.

      AJAX의 사용이 쉽다.
      제이쿼리를 사용하면 아작스 기술을 사용하는데 매우 편리합니다.