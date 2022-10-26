

// addEventListener 는 태그에 이벤트 설정하는 함수
// addEventListener("이벤트", 이벤트발생시동작함수)
// 함수는 직접 괄호 안에서 직접 만들거나 미리 만든 함수를 호출할 수 있다.

window.onload = function () {
  var add = document.querySelector('#add');
  add.addEventListener("click", tag_add);

};

var add_check = false;

function tag_add() {
  if (add_check) {
    return;
  }
  add_check = true;
  var Pdiv = document.querySelector("#score_wrap");
  var div = document.createElement("div");
  var ipt = document.createElement('input');
  ipt.setAttribute('type', 'text');
  ipt.setAttribute('id', 'name');
  ipt.setAttribute('placeholder', '이름');
  div.appendChild(ipt);

  var course = [["국어", "kor"], ["수학", "mat"], ["영어", "eng"]];
  for (let i = 0; i < 3; i++) {
    ipt = document.createElement("input");
    ipt.setAttribute("type", "number");
    ipt.setAttribute("id", course[i][1]);
    ipt.setAttribute("placeholder", course[i][0]);
    div.appendChild(ipt);
  }
  var bt = document.createElement("button");
  bt.addEventListener("click", enroll);
  var text = document.createTextNode('등록');
  bt.appendChild(text);
  div.appendChild(bt); // input 태그들을 새 div에 넣고 score_wrap에 추가하기
  Pdiv.appendChild(div); // score_wrap div에 추가
}

function enroll() {
  add_check = false;
  var name = document.querySelector("#name").value;
  var kor = document.querySelector("#kor").value;
  var mat = document.querySelector("#mat").value;
  var eng = document.querySelector("#eng").value;
  var Pdiv = document.querySelector("#score_wrap");

  // socre_wrap div에 추가하는 작업

  var div = document.createElement("div");
  div.setAttribute("class", "score");
  var data = [name, kor, mat, eng];
  for (let i in data) {
    let h = document.createElement("h3");
    let text = document.createTextNode(data[i]);
    h.appendChild(text);
    div.appendChild(h);
  }
  var input = Pdiv.lastChild;
  Pdiv.removeChild(input); // input태그 삭제
  Pdiv.appendChild(div); // input 태그값 div 에 삽입
}