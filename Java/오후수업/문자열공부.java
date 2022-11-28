package 자바0913;

public class 문자열공부 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String name = "황정민";
		String name2 = "황정민";
		
		boolean isCheck = name.equals(name2);
		/** 
		 * 자바에서 문자끼리 비교 할 때 equals를 사용하는 이유는 자바에서 문자열은 클래스이기 때문에
		 * == 연산자로 비교하게 되면 문자를 비교하는게 아니라 클래스를 비교하는 것 이다. 
		 */
		
		System.out.println("name하고 name2를 비교한 결과 => "+isCheck);
		//boolean은 true or false만 표현할 수 있다.
		
		// 문자 길이 알아내기
		String password = "12341234";
		int str_length = password.length();
		System.out.println("문자 길이는 =>"+str_length);
		
		// 3.문자 자르기
		String pn = "010-8888-1222";
		String array[] = pn.split("-");
		System.out.println(array[0]);
		System.out.println(array[1]);
		System.out.println(array[2]);
		
		// 4.특정 문자만 추출하기
		String title = "어벤져스 인피니티 워";
		String result = title.substring(0,2);
		String result2 = title.substring(0,4);
		System.out.println(result2);
		
	}

}
