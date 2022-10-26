// boom.js

var board = new Array(400);
board.fill(0);

for (var i = 0; i < 398;) {
  let pos = Math.floor(Math.random() * 400);
  if (board[pos] != 1) {
    board[pos] = 1;
    i++;
  }
}

window.onload = function () {
  var table = "<table>";
  for (var i = 0; i < 20; i++) {
    table += "<tr>";
    for (var k = 0; k < 20; k++) {
        table += '<td class="bm" data-idx='+(i*20+k)+'></td>'; // data-idx => 데이터 시트 - html에 넣어주면 js에서 사용 가능
    }
    table += "</tr>";
  }
  table += "</table>"
  document.getElementById("wrap").innerHTML = table;

  var bm = document.getElementsByClassName("bm");
  
  // alert(bm.length) 배열로 담아진다
  // bm[0].style.background = 'red';

  for(var i in bm){
    bm[i].addEventListener('click',function(){
      let n = this.dataset.idx;
      if( board[n]== 1){
        // this.innerHTML = '<img src = "../../image/boom.png">'
        this.style.background = 'url(../../image/boom.png) no-repeat center center';
        this.style.backgroundSize = 'cover';
      }else{
        this.style.background = "rgb(230,230,230)";
      }
    }); // 모든 td의 이벤트를 추가 , 동작할 함수의 내용을 직접 생성 or 만든 후 function 자리에 입력
  }
};