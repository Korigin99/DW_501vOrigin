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


function movie(title, dir, year, genre){ // 생성자 함수
  this.movie_title = title;
  this.movie_dir = dir;
  this.movie_year = year;
  this.movie_genre = genre;
}

movie.prototype.out=function(){
  return this.movie_title + " " + this.movie_dir + " " + this.movie_year + " " + this.movie_genre;
}

var movie_list = new Array(); // movie 객체 저장된 배열

// 다른 답안
window.onload = function () {
  var input = document.getElementsByClassName("movie");
  for (var i in input) {
    input[i].addEventListener('focus', function () {
      this.classList.add("active");
    });
    input[i].addEventListener("blur", function () {
      if(this.value == ''){
      this.classList.remove("active");
      }
    })
  }
};

function enroll(){
  var val_temp = document.getElementsByClassName("movie");
  var data = new movie(val_temp[0].value, val_temp[1].value, val_temp[2].value, val_temp[3].value);
  movie_list.push(data);
  print();
}

function print(){
  var li = document.createElement("li");
  li.innerText = movie_list[movie_list.length-1].out();

  document.getElementById("movie_list").append(li);
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

  객체 생성 : new 연산을 통해서 생성
  생성된 객체는 변수에 저장하여 사용하는데 이떄 변수를 참조 변수라고 한다.
  참조변수는 ram의 주소를 저장하는 변수이다.

  var obj = new Object();

  도형 객체
  도형.모양 = 사각형
  도형.위치x축 = 120
  도형.위치y축 = 50
  도형.그리기(함수)
  도형.지우기(함수)

  도형.모양 = 삼각형
  도형.위치x축 = 200
  도형.위치y축 = 120
  도형.그리기(함수)
  도형.지우기

  객체의 멤버로 접근하기 위한 연산자 (.) - access 연산자 접근연산자
  접근연산자는 +, -, ++, &&, || 등 보다 우선순위가 높음
  도형.위치X축 + 10; 접근연산자 순위 약 4위
  1순위 (), 2순위 [], 3순위 ->


*/

// 객체 생성방법

// javascript에서는 key와 value로 구분 됨
/* var shape = {
  모양 : "사각형",
  x축 : 120,
  y축 : 23,
  draw:function(){  // 익명 함수 : 이름이 없는 함수
    return "x축 : " + this.x축 + "y축 : " + this.y축 + "위치에 "+this.모양+" 그리기";
  }
};
 */
// 객체 내부에서 함수 생성시, 변수(key)의 사용은 this로 접근한다.
// 객체의 값 출력 -> 객체.key -- >key의 value가 출력 됨
/* document.write("모양 "+ shape.모양);
document.write(shape.draw()); */
// key는 문자열로만 가능
// 객체 생성 방법 1. 객체 리터럴 방식 : 변수처럼 객체를 생성하는 방식

// 학생 객체 생성 (학년, 반, 번호, 이름)

/* var name = "김춘추" // 객체에서는 외부 데이터를 가져다 쓰는 것을 지양함
var student = {
  학년 : 3, 반 : 3, 번호 : 202210327, 이름 : name // 중앙선 표시된 것은 권장하지 않는 방식이라는 의미
};

document.write("<br>" + student.이름); */

// 객체 생성 방법 2. 생성자 방식 -> new 연산자로 생성하는 방식
// 생성자 방식 1) Object 객체로 생성
// 생성자 방식 2) 함수를 통한 생성

/* var music = new Object();
music.title = "Hype boy";
music['가수'] = "뉴진스";
music.link = '<iframe width="1280" height="753" src="https://www.youtube.com/embed/NcJo-T5Wo3U?list=RDMMNcJo-T5Wo3U" title="[릴레이댄스] NewJeans(뉴진스) - Hype Boy (4K)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>';

document.write( "<a href='javascript:open();'>"+ music['title']+" - "+music.가수 +"</a>");
// 함수를 통한 생성은 외부 데이터를 사용해도 된다.

function open(){
  document.getElementById("play").innerHTML= music.link;
} */

/* var 제목 = 'tomboy';
music.title = 제목;
document.write(music.title); */

/* function movie(제목, 감독, 년도, 장르){
  this.영화제목=제목;
  this.감독=감독;
  this.개봉년도=년도;
  this.장르=장르;
}

movie.prototype.view = function(){
  return this.영화제목 + " " + this.감독;
} */

// 메모리 최적화
/* 
    javascript의 모든 객체는 prototype을 가지고 있다.
    prototype으로 만든 거는 객체의 수 상관 없이 하나만 존재한다.
    그만큼 메모리가 절약 된다.
*/

/* var m1 = new movie('한산','김**',2022,'전쟁');
document.write(m1.영화제목);

var m2 = new movie('공조2',"이**",2022,"탐정");
document.write(m2.개봉년도);
document.write(m2.view()); */




