


<div>

# 2022.08.25 수업 내용

## HTML + css  

div 태그를 이용하여 게시판 제작  
diplay:flex를 이용하여 게시판을 제작  
```css
    display:flex;
```
form 태그
```css
<form method=" " action=" "></form>
<form method="전송방식(GET, POST)"  action="전송위치(uri)"></form>
```
form : 데이터를 전달하기 위한 영역  
전달 방법 : GET , POST  
GET : 데이터를 가공하지 않고 전달  
POST : 데이터를 암호화 하여 전달  


## Javascript

if문을 활용하여 회원가입에 영향을 주는 함수를 만들었다.
```javascript
     function doJoin(){

        var data = document.getElementById('userId').value;
        var pw1 = document.getElementById('userPw1').value;
        var pw2 = document.getElementById('userPw2').value;
        var email = document.getElementById('userEmail').value;

        if(data == ''){
            alert("고객님 아이디를 입력해주세요.");
            document.getElementById('userId').focus();
            return false;
        }

        if(pw1 == '' || pw2 == ''){
            alert("고객님 비밀번호를 입력해주세요.");
            document.getElementById('userPw1').focus();
            return false;
        }

        if(pw1.length<6){
            console.log('비밀번호는 6자리 이상 입력해야 합니다.');
            document.getElementById('userPw1').focus();
            return false;
        }
        if(pw1 != pw2){
            console.log('비밀번호 불일치');
            document.getElementById('userPw1').focus();
            return false;
        }else{
            console.log('비밀번호 일치');
        }

        if(email == ''){
            alert("고객님 이메일을 입력해주세요.");
            document.getElementById('userEmail').focus();
            return false;
        }

        alert('회원가입 완료')
    }
```

</div>