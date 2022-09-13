package 자바0913;

public class 자바기초 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int 돈 = 100;
		돈 = 50;

		int 고기 = 3;

		고기 = 1;
		고기 = 고기 + 3; // 값 4
		고기 = 고기 + 고기; // 값 8

		int 초밥 = 5;
		초밥 = 초밥 * 2; // 10

		int 내지갑 = 50000;
		int 만원 = 0;
		만원 = 내지갑 / 10000;
		System.out.println(만원);

		int 국어 = 80;
		int 수학 = 15;
		int 영어 = 65;
		int 평균 = 0;
		평균 = (국어 + 수학 + 영어) / 3;
		System.out.println(평균);
		
		String 이름 = "홍길동";
		이름 = 이름 + "철수"; // 문자와 문자 사이를 더해준다.
		System.out.println(이름);
		
		// 문자를 숫자로 변환
		String num = "10";
		int num2 = 0;
		
		num2 = Integer.parseInt(num);
		System.out.println("문자에서 숫자로 변환된 값은 : "+num2);
	}

}
