// func2 정답.js

window.onload = function(){
  document.getElementById("bt").addEventListener("click", input);
};

function input(){
  var birth = document.getElementById("birth").value;

  var birth_year = getYear(birth);
  var birth_month = getMonth(birth);
  var age = getAge(birth);
  var info = document.getElementsByTagName("li");
  info[0].innerHTML = birth_year;
  info[1].innerHTML = birth_month;
  info[2].innerHTML = age;

}

function getYear(birth){
  var year = birth.split(".")[0];
  return year;
}

function getMonth(birth){
  var month = birth.splti(".")[1];
  return month;
}

function getAge(birth){
  var year = birth.split(".")[0];
  var age = 2022 - parseInt(year) + 1;
  return age;
}