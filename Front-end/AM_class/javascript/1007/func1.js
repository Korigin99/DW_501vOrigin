
// return -> 반환값은 1개만 가능
// 다 수의 값을 리턴하려면 배열로 리턴 해야한다.


function scroe_input(){
  var kor = 99;
  var mat = 89;
  var eng = 79;
  total(kor,mat,eng);
  return [kor, mat, eng];
}

function total(k,m,e){
  var tot = k + m + e;
  avg(tot);
}

function avg(tot){
  var res = tot/3;
  result_print(res);
}

function result_print(res){
  document.write("평균 : "+ res);
}