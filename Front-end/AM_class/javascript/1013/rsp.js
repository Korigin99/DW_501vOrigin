// rsp.js


/* window.onload = function(){ 
  docu
};


function userInput(){
  var user = document.getElementById("ipt");
  decision(user.value, comRandom());
}

function comRandom(){
  var comR = Math.floor(Math.random()*3)+1;
  return comR;
}

function decision(user, com){
  var out = "";
  if(user == 3){
    user == com ? out = "DRAW" : com == 1 ? out = "DEFEAT" : out = "WIN"; // user - 보
  }else if(user == 2){
    user == com ? out = "DRAW" : com == 1 ? out = "WIN" : out = "DEFEAT"; // user - 바위
  }else{
    user == com ? out = "DRAW" : com == 2 ? out = "DEAFEAT" : out = "WIN"; // user - 가위
  }
} */

// rsp.js

user();

function user(){
  var u = parseInt(prompt("1.가위 2.바위 3.보"));
  var c =com();
  result(u, c);
}

function com(){
  var c = Math.floor(Math.random()*3)+1;
  return c;
}

function result(u, c){
  if(u==c){
    alert("비김");
  }else if((u==1 && c==3) || (u==2 && c==1) || (u==3 && c==2)){
    alert("이김");
  }else{
    alert("패배");
  }
}