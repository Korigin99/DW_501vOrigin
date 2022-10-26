
var play = new Array();
window.onload =function(){
  while(play.length !=3){
    var r = Math.floor(Math.random()*9)+1;
    if(play.indexOf(r)<0){
      play.push(r);
    }
  }
  var send = document.querySelector("#send");
  send.addEventListener("click", number_input);
};

function number_input(){
  var user = new Array();
  var num = document.getElementsByClassName("num");
  user.push(parseInt(num[0].value));
  user.push(parseInt(num[1].value));
  user.push(parseInt(num[2].value));
  user.push(parseInt(num[3].value));
  user.push(parseInt(num[4].value));
  
  if(input_check(user)){
    alert("잘못된 숫자 입력입니다. 중복없이 1~20중에서 입력하세요");
    return;
  };
  for(var i in num) num[i].value = "";
  num[0].focus();
  number_check(user);
}

function input_check(user){
  for(var i in user){
    if(user[i]<1 && user[i]>20) return true;

  }
  
}

function number_check(u){
  var strike=0, ball = 0;
  if(u[0] == play[0]) strike++;
  if(u[1] == play[1]) strike++;
  if(u[2] == play[2]) strike++;
  if(u[3] == play[3]) strike++;
  if(u[4] == play[4]) strike++;
  if(u[0] == play[1] || u[0] == play[2] || u[0]== play[3] || u[0] == play[4]) ball++;
  if(u[1] == play[0] || u[1] == play[2] || u[1]== play[3] || u[1] == play[4]) ball++;
  if(u[2] == play[0] || u[2] == play[1] || u[2]== play[3] || u[2] == play[4]) ball++;
  if(u[3] == play[0] || u[3] == play[1] || u[3]== play[2] || u[3] == play[4]) ball++;
  if(u[4] == play[0] || u[4] == play[1] || u[4]== play[2] || u[4] == play[3]) ball++;
  print(strike, ball);
}

function print(strike,ball){
  var res = document.querySelector("#result");
  var div = document.createElement("div");
  var out = 3-strike-ball;
  div.appendChild(document.createTextNode(strike+" 스트라이크 " + ball+" 볼 "+out + " 아웃 "));
  res.prepend(div);
}