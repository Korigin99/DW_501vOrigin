# 10월 20일 수업


### javascript

- screen - 화면 정보 제공
        
      screen.width : 화면의 전체 너비 (해상도 너비)
      screen.height : 화면의 전체 높이 (해상도 높이)
      screen.availWidth : 실제 사용 가능한 화면 너비
      screen.availHeight : 실제 사용 가능한 화면 높이
      screen.colorDepth : 사용 가능한 색상 수
      screen.pixelDepth : 한 픽셀당 비트 수

- document 객체
``` js
document.write(" title : " + document.title); // 현재 페이지의 제목
document.write(" 마지막 수정 : " + document.lastModified);
document.write(" 마지막 수정 : " + document.lastModified);
document.write(" 배경색 : " + document.bgColor);
document.write(" 링크색 : " + document.linkColor);
document.write(" 링크색 : " + document.alinkColor);
document.write(" 링크색 : " + document.vlinkColor);
```

- form
```html
  <form name="fm" method="get" action="save.html">
    <input type="text" name="id" id="id">
    <input type="password" name="pw" id="pw">
    <input type="data" name="day" id="day">
    <input type=" checkbox" name="fav" id="fav">
  </form>
```
```JavaScript
  document.fm.id.value // form 태그 안에 있는 input 태그만 가능

  document.write("길이 : " + document.forms.length);
  document.write("첫 번째 form name : " + document.forms[0].name);
  document.write(document.forms.fm.name);
  document.write(document.all.fm.name);
  document.write(document.forms["fm"].name);
  document.write(document.forms[0].elements[0].value);

  function view({
    var forms = document.forms; // 현재 문서의 form을 배열로 받기
    for(var i in forms){
      var tags = forms[i].elements; // 해당 form의 tag를 배열로 받기
      for(var k in tags){
         alert(tags[k].value)
      }
    }
  }
```

- 쿠키 - 사용자가 브라우저 사용 중에 입력하거나 검색한 정보를 저장해 놓은 것
  
      - 특징
      최대 300개까지 사용가능
      하나의 쿠키 크기는 4KB로 제한
      (문자 하나의 크기 - 1byte, 1byte == 8bit)

      쿠키의 정보는 HTTP헤더를 통해 클라이언트 브라우저와 서버가 공유한다.
      사용자에 의해 웹페이작 요청되면 Set_Cookie 필드에 의해 쿠키가 브라우저에 저장됨
      Set-Cookie : 유효기간, 보안정보 등을 포함
      사용자가 다시 같은 페이지를 요청 했을 때 저장 되어있던 쿠키가 발견되면 부라우저는 웹 페이지를 요청하는 헤더에 쿠키필드를 포함하여 전송한다.
      쿠키의 내용은 암호화 되지 않는다.

      Set-Cookie 구조
      - name : 생성될 쿠키의 이름
      - 값 : 쿠키에 저장될 데이터
      - expipres : 유효기간 지정
      - path : 저장된 쿠키와 일치하는 url의 path와 도메인 값이 일치하는 url에 페이지를  요청하게 되면 해당 쿠키가 서버로 전달
      - secure : 데이터 전송시 보안을 위한 프로토콜을 지정할 때 사용

- 쿠키 만드는 법
``` javascript
setCookie("name","kim",1);

setCookie(쿠키이름, 데이터, 유효기간){
  const day = new Date();
  day.setTime(day.getTime() + (유효기간*24*60*60*1000)); // setTime - 시간 설정 함수
  let expires = "expirest="+day.toUTCString();
  document.cookie = 쿠키이름 + "=" + 데이터 + ";" + expires + ";path=/";
}

function getCookie(){
  let decode_cook = decodeURIComponent(document.cookie);
  let temp = decode_cook.split(";");
  for(let i=0; i<temp.length; i++{
    let c = temp[i];
    while(c.charAt(0) == ' '){
      c = c.substring(1);
    }
    if(c.indexOf("name=")==0){
      alert(c.substring("name".length, c.length));
    }
  }
}
```