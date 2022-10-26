// js_object.js

function tb(col, row, wd, hg) {
  this.col = col;
  this.row = row;
  this.width = wd;
  this.height = hg;
}

var bt_cnt = 0;
var bt_check = false;
var tb_list = new Array();

window.onload = function () {
  var add_bt = document.getElementById("bt");
  add_bt.addEventListener("click", add_button);

  var T_put = document.getElementsByClassName("T_put");
  for (var i in T_put) {
    T_put[i].addEventListener("keyup", function () {
      if (!bt_check) {
        alert("새 세팅버튼을 추가하세요");
        this.value = '';
      }
    });
  }
};

function add_button() {

  if(bt_check){  // 새 버튼 생성 후 값등록 안되었으면 새버튼 생성 금지
    alert("값 먼저 등록해주세요");
    return;
  }

  var bt = document.createElement("button");
  bt.appendChild(document.createTextNode("세팅" + (++bt_cnt)));
  bt.setAttribute("data-value","0");
  bt.addEventListener("click", function(){
    if(this.dataset.value == 0){
      value_save(this);
    }else{
      table_draw(this);
    }
    
  });
  document.getElementsByClassName("new_bt")[0].appendChild(bt);
  bt_check = true;
}

function value_save(obj) {
  var input_label = ["행", "열", "너비", "높이"];
  var T_put = document.getElementsByClassName("T_put");
 
  for (var i in T_put) {
    if (T_put[i].value == '') {
      alert(input_label[i] + "값을 입력하세요.");
      T_put[i].focus();
      return;
    }
  }

  var temp = new tb(T_put[0].value, T_put[1].value, T_put[2].value, T_put[3].value);
  tb_list.push(temp);  

  obj.dataset.value = bt_cnt;

  bt_check = false;
  for (var i = 0; i < T_put.length; i++) {
    T_put[i].value = '';
  }
}

function table_draw(obj){
  var draw = document.getElementById("draw");
  var data = tb_list[parseInt(obj.dataset.value-1)];
  
  var tab = "<table border='1'>"
  for(var i=0; i<data.col; i++){
    tab += "<tr>";
    for(var j=0; j<data.row; j++){
      tab += "<td width="+data.width+" height="+data.height+"></td>";
    }
    tab += "</tr>";
  }
    tab += "</table>"
  draw.innerHTML = tab;

}