## 11월 14일 수업

## java

- 제네릭과 컬렉션즈

  - <> : 제네릭
  - List : 컬렉션즈

  - 컬렉션즈 : 자료구조 (스택, 힙, 맵, 셋 ...)

  - 생성 방법
  
  ```java
  // List
  List<Integer> list = new ArrayList<Integer>(); // 정수형을 담는 리스  
  list.add(10);
  list.add(20)  
  System.out.println("0번째 값 : " + list.get(0));
  System.out.println("1번째 값 : " + list.get(1)) 
  // List 길이 출력
  System.out.println(list.size()) 
  list.remove(1); // 1번째 요소 삭제
  System.out.println(list.size()) 
  List<Integer> numberList = new ArrayList<Integer>() 
  numberList.add(5);
  numberList.add(7);
  numberList.add(13);
  numberList.add(15)  
  for (int i = 0; i < numberList.size(); i++) {
  	int n = numberList.get(i);
  	if (n % 5 == 0) {
  		System.out.println(n);
  	}
  }

  // 향상된 for문을 이용한 로직구현 (for each)
  for(int i : numberList) {
  	if (i % 5 == 0) {
  		System.out.println(i);
  	}
  }

  numberList = new ArrayList<Integer>();
  numberList.add(50);
  numberList.add(100);
  numberList.add(300);
  int sum, cnt;
  sum = cnt = 0;
  for (int i : numberList) {
  	sum += i;
  	if (i >= 100) {
  		cnt++;
  	}
  }
  System.out.printf("총합 : %d, 100이상인 요소 개수 : %d \n", sum, cnt);

  List<String> wordList = new ArrayList<String>();
  wordList.add("아이스 아메리카노");
  wordList.add("카페라떼");
  wordList.add("카페모카");
  wordList.add("아이스 아메리카노");
  wordList.add("아이스 아메리카노");
  wordList.add("아이스 아메리카노"); 

  for(String item : wordList) {
  	if(item.equals("아이스 아메리카노"))
  	System.out.println(item);
  }
  ```

  - add로 값을 추가하고 get으로 값을 불러온다.