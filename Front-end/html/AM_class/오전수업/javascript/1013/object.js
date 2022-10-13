// object.js

/* 
1. 각 인풋 클릭시 라벨의 위치 이동
2. 등록 버튼

*/

// 내가 한 거
/* window.onload = function(){
  var info = document.querySelectorAll(".movie");
  for(var i=0; i<info.length; i++){
    info[i].addEventListener("focus", function(){
      this.setAttribute('class','movie active');
    });
    info[i].addEventListener("blur",function(){
      this.setAttribute('class', 'movie');
    });
  }
} */

// 다른 답안
window.onload = function(){
  var input = document.getElementsByClassName("movie");
  for(var i in input){
    input[i].addEventListener("focus",function(){
      this.classList.add("active");
    });
    input[i].addEventListener("blur",function(){
      this.classList.remove("active");
    })
  }
}

// 객체 : 사물, 사람, 동물 등 대표성을 지닌 독립적인 존재
/* 
    모든 객체는 자신만의 속성(특성)을 가지며, 자신만의 행동을 갖는다.
    객체는 자신만의 속성을 가진다 -> 변수
    객체는 자신만의 행동을 가진다 -> 함수
*/

/* 
  객체 정의 : 추상화 시켜 놓은 것
  - 추상화란 불필요한 정보의 노출을 최소화하고 꼭 필요한 정보만 노출하는 기법
  차상화의 기본 : 속성과 행동을 나열하고 구성한다.
  멤버변수 : 객체의 속성을 구성
  멤버함수 : 객체의 속성을 기반으로 행동을 구현 해놓은 코드
  멤버변수 : 객체의 속성을 구성
  멤버함수 : 객체의 속성을 기반으로 행동을 구현 해놓은 코드

*/

