$(document).ready(function(){
  $(".menu-toggle").on("click", function(){ // on으로 함수 생성
    $(".gnb").stop().slideToggle('fast');
  });
});

/* 
시간설정 가능, fast, slow, 공백

나타내기
show() 함수를 사용하면 바로 나타남
show(1000); 안에 넣은 시간 만큼만 나타남

감추기 
hide();

show 기능과 hide 기능을 동시에 사용하는 함수
toggle();


화면에 표시하는 함수 - 투명도
fadein(); 
fadeout();

slideup();
slidedown();

통합해서 사용 가능한
slideToggle();
*/