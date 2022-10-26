

window.onload = function(){
  document.getElementById("bt").addEventListener("click", input);
}

function input(){
  var name = document.getElementById("name");
  var job = document.getElementById("job");

  list_push(name.value, job.value);
  name.value = '';
  job.value = '';
  name.focus();
}
var list = new Array();
function list_push(name, job){
  var out = "<span>"+name+"</span><span>"+job+"</span>";
  list.push(out);
  output_list();
}

function output_list(){
  var div = document.getElementById("output");
  var out = "";
  for(var i in list){
    out += list[i];
  }
  div.innerHTML = out;
}