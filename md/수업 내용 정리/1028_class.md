# 10월 28일 수업

## jquery를 이용한 사이트 기능 만들기

- jquery에서 사용가능한 화면 나타내거나 숨기는 함수

      괄호 안에는 시간, fast, slow, 공백 이 들어간다.

      나타내기
      show() 함수를 사용하면 바로 나타남
      show(1000); 안에 넣은 시간 만큼만 나타남
      hide(); - 감추기
      toggle(); show 기능과 hide 기능을 동시에 사용하는 함수

      화면에 표시하는 함수 - 투명도
      fadein(); 
      fadeout();

      슬라이드
      slideup();
      slidedown();
      slideToggle(); - up과 down의 기능을 통합

    ```js
    $(document).ready(function(){
      $(".menu-toggle").on("click", function(){ // on으로 함수 생성
        $(".gnb").stop().slideToggle('fast');
      });
    });
    ```