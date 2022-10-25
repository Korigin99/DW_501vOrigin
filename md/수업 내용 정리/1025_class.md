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