// array.js

// window.onload : 브라우저에 html 문서의 모든 내용이 출력된 후 동작
// window 객체 : 브라우저 실행 시키긱 위한 프로그램 툴
// window에만 onload 있는거 아님, 모든 객체(html 태그포함)에 존재
// load -> 불러오기 즉 onload는 불러오는 작업이 끝났을 때 동작



var item_list = ["핸드폰거치대", "급속충전기", "C타입케이블", "강화유리", "스마트폰 링", "스마트폰 커버"]
window.onload = function () {
  var li = document.getElementsByClassName("item"); // 배열구조로 가져옴
  // var li = document.querySeletorAll(".item");

  for (var i in li) { // 배열구조에서 사용
    li[i].innerHTML = item_list[i];
  }
}

var item = new Array();
var itemP = new Array();
function enroll() {
  var name = document.getElementById("item_name");
  var price = document.getElementById("item_price").value;
  var prop = name.value;
  item.push(prop);
  itemP.push(price);
  var ul = document.getElementById("item_list");
  var li = document.createElement("li"); // li 태그 생성
  li.innerHTML = item[item.length - 1] + " " + itemP[itemP.length - 1]; // li 태그안에 제품명 삽입
  var bt = document.createElement("button");
  bt.setAttribute('class', 'del_bt'); // setAttribute : 기능을 추가할 때 사용 ex) setAttribute('class', 'del_bt) or setAttribute("onclick","del()")
  bt.setAttribute("onclick","del(this)");
  bt.innerHTML = '삭제';
  li.appendChild(bt);
  ul.appendChild(li); // ul 태그 자식으로 li 추가

  // 새 태그(엘리먼트, 요소, 객체)를 생성하는 방법: createElement() 함수

  // 태그(엘리먼트) 내부에 새로운 내용으로 삽입하는 방법 : innerHTML 속성
  // 태그(엘리먼트) 내부에 새로운 내용을 추가하는 방법 : appendChild 함수
  // 태그(엘리먼트) 내부에 텍스트 형식으로 삽입하는 벙법 : appendChild(textnode);
}

function del(obj){
  var parent_li = obj.parentNode;
  var parent_ul = parent_li.parentNode;
  parent_ul.removeChild(parent_li);

  /* 
    document.createElement : 새 태그 생성
    ex) document.createElement("div"); div 생성

    appendChild : 자식 태그로 추가
    ex) p = document.createElement("p");
    body.appendChild(p); : body에 p태그 추가

    setAttribute : 태그에 새속성 추가
    ex) p.setAttribute("id", "ppp") 해당태그에 id="ppp" 삽입

    removeChild : 자식 태그 삭제
    ex) body.removeChild(p); : body 태그에서 해당 태그 삭제
  */
}