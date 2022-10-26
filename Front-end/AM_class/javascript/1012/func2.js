// func2.js

window.onload = function(){
  document.getElementById("bt").addEventListener("click", input);
}

function input(){
  var born = document.getElementById("ipt").value;
  var li = document.getElementsByTagName("li");
  li[0].innerHTML = getYear(born);
  li[1].innerHTML = getMonth(born);
  li[2].innerHTML = getAge(born);
}

function getYear(born){
  var info = born.split(".")[0];
  return "출생년도 : " + parseInt(info) + "년";
}

function getMonth(born){
  var info = born.split(".")[1];
  return "출생 월 : " + parseInt(info) + "월";
}

function getAge(born){
  var info = born.split(".")[0];
  info = 2022 - parseInt(info) + 1;
  return "올해 나이 : "+info+"살";
}