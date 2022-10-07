
var x =new Array();
window.onload = function(){
  
  while(x.length!=3){
    var r = Math.floor(Math.random()*9)+1;
    if(x.indexOf(r) < 0){
      x.push(r);
    }
  }
  console.log(x);
  var click = document.querySelector("#send");
  click.addEventListener("click",function(){
    var num1 = document.querySelector("#num1").value;
    var num2 = document.querySelector("#num2").value;
    var num3 = document.querySelector("#num3").value;
    console.log(num1,num2,num3);
    num_check(num1, num2, num3);
  });

  function num_check(n1,n2,n3){
    
    n1 = parseInt(n1);
    n2 = parseInt(n2);
    n3 = parseInt(n3);
    console.log(n1,n2,n3);
    var cnt = 0;
    for(var i=0; i<x.length; i++){
      if(x[i] == n1 || x[i] == n2 || x[i] == n3){
        cnt++;
      }
    }
    document.querySelector("#result").innerHTML = "일치하는 값 : "+cnt+"개";
  }
};



