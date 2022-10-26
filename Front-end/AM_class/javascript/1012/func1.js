// func1.js

/* 
html 작업
1. input 2개 생성 - 너비 150, 높이 35, 둥근 모서리
2. 버튼 1개 생성 -> text - 입력, 너비 80, 높이 35 검정바탕, 흰색 글씨, 글씨 크기 15px
3. div 생성 -> id - output


java script 작업
*/

window.onload = function(){
  var bt = document.getElementById("bt1");
  bt.addEventListener("click", input);
};

function input(){
  var v1 = document.getElementById("v1").value;
  var v2 = document.getElementById("v2").value;
  list_push(v1,v2);
}


function list_push(v_1, v_2){
  var arr = new Array();
  arr.push(v_1);
  arr.push(v_2);
  output_list(arr)
}

function output_list(n){
  var r_out = document.getElementById("output");
  var div1 = document.createElement("div");
  var div2 = document.createElement("div");
  div1.setAttribute('style','width:150px; height:30px');
  div1.appendChild(document.createTextNode("이름 : " + n[0]));
  r_out.appendChild(div1);
  r_out.setAttribute('style', 'display : flex;');
  div2.setAttribute('style','width:150px; height:30px');
  div2.appendChild(document.createTextNode("직업 : " + n[1]));
  r_out.appendChild(div2);
}