# 10월 21일

### window 객체

- history 객체 - 사용자의 웹사이트 사용 내역
    
      history.length : 히스토리 목록에 포함된 url의 수
      histroy.back() : 뒤로 이동
      history.forward() : 앞으로 이동
      history.go( 2 ) : 현재 url 위치에서 2만큼 앞으로 이동, 음수라면 뒤로, 양수라면 앞으로
    - 예시
    ```js
    if(미로그인 상태){
    alert("로그인 후 이용해주세요");
    history.back();
    }

    if(로그인시 아이디 비번 틀리다면){
      alert("아이디 또는 비밀번호가 올바르지 않습니다.");
      history.back();
    }
    ```

- location 객체 
  -> 현재 윈도우의 url 주소에 대한 정보 제공 객체

      location.host : 호스트 이름과 포트번호(url로부터 분리하여 제공)
      ex) www.naver.com:80
      location.hostname : url 주소에 대한 호스트 이름
      location.href : 하이퍼 링크로 주소 지정
      location.pathname : 디렉토리 위치 (호스트)
      location.port : 호스트 포트번호
      location.protocol : 프로토콜 종류
      location.reload() : 문서 다시 읽기 (새로고침)
      window.loaction.assign(url 주소) : url로 이동(방문기록 저장)
      window.location.replace(url) : url로 이동(방문기록 덮어씀)

  - 사용 예시
    ```js
    if(미로그인 상태){
      alert("로그인 후 이용해주세요");
      location.href = 'login.html';
    }

    if(로그인시 아이디 비번 틀렸다면){
      var move = confirm("아이디 또는 비밀번호가 올바르지 않습니다. 회원가입 하시겠습니까?");
      if(move){
        location.href = 'join.html';
      }else{
        history.back();
      }
    }
    ```


- navigator 객체
  -> 웹 브라우저의 특성 정보를 가지는 객체

      navigator.appName : 사용중인 브라우저 종류
      navigator.appCodeName : 사용중인 웹브라우저 이름
      navigator.appVersion : 브라우저 버전 및 os 이름
      navigator.plaform : 운영체제 환경
      navigator.userAgent : 웹브라우저 종류와 버전
      navigator.pluguns : 설치된 플러그인 정보
      navigator.mimeTypes : 브라우저에서 지원되는 MIME 타입
      MIME 타입 종류 : text, image, audio, video, application, message, multiport

      image - gif, jpeg
      video - mpeg
      application - stream, script

    - 예시
    ```js
    document.write("appName : " + navigator.appName);
    document.write("appCodeName : " + navigator.appCodeName);
    document.write("appVersion : " + navigator.appVersion);
    document.write("plaform : " + navigator.plaform);
    document.write("uesrAgent : " + navigator.userAgent);

    var os = navigator.userAgent;
    if(os.toLowerCase().indexOf("windows")){
      alert("현재 접속기기는 pc입니다.");
    }else if(os.toLowerCase().indexOf("android")){
      alert("현재 접속 기기는 모바일(안드로이드)입니다.");
    }else if(os.toLowerCase().indexOf("iphone")){
      alert("현재 접속 기기는 아이폰입니다.");
    }

     var orient = window.orientation;
    if(orient != undefined){
      if(orient == 0){
        alert("세로 방향");
      }else if(orient == -90 || orient == 90){
        alert("가로방향");
      }
    }
    ```