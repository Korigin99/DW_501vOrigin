var c = 0;

function doClick() {
  c++;
  var res = document.querySelector("#res_wrap");
  var city = document.querySelector("#city").value;
  var cnt = document.querySelector("#cnt").value;

  var div = document.createElement("div");
  div.setAttribute("class","one");
  var h1 = document.createElement("h4");
  var h2 = document.createElement("h4");
  var h3 = document.createElement("h4");
  let text3 = document.createTextNode(c+".");
  h3.appendChild(text3);
  let text = document.createTextNode(" "+city);
  h1.appendChild(text);
  let text2 = document.createTextNode(" " + cnt + "명");
  h2.appendChild(text2)
  div.appendChild(h3);
  div.appendChild(h1);
  div.appendChild(h2);
  res.prepend(div);
}