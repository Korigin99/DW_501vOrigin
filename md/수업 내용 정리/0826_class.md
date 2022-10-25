
# 2022.08.26 수업


##  HTML + css

=======================================================

### 갤러리 만들기

1. 이미지를 표현할 때 max-width, max-height를 사용한다.  
    이미지의 크기에 맞게 조절된다.
 ```css
    /* ex */
    img{max-width: 380px; height: 295px;}
 ```
2. 이미지를 표현할 때 img태그가 아닌 div의 background 영역에 삽입이 가능하다.
 ```css
    .img_area{
        background: url(/img/m2.png) no-repeat center center;
        background-size: cover;
    }
    
    .img_area{background: url(이미지의 경로) 반복의 여부 | div의 x축 | div의 y축}
 ```
 3. Javascript - split 함수 분리 할때 사용
 ```Javascript
        var url = location.href; // 데이터타입 변수이름 = location.가져올거
        var params = url.split('?')[1];
        var 변수이름 = 분리할 변수 이름.split('기준')[가져오고 싶은 인덱스 번호]; 
 ```
   - '?'를 기준으로 0번째 인덱스와 1번째 인덱스로 나눔 
   - [1]을 뒤에 쓰면 1번째 주소에 있는 내용을 가져옴