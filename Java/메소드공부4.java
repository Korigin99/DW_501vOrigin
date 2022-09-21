package 자바0913;

public class 메소드공부4 {

	/*
	 * public static : 접근 제어자 
	 * int : 리턴 타입 
	 * getSum : 메소드 이름 
	 * int x : 파라미터 타입
	 */

	public static int getSum() {
		int sum = 0;
		for (int i = 1; i <= 10; i++) {
			sum += i;
		}
		return sum;
	}

	public static String getWord(String x) {
		return x;
	}

	/*
	 * public static : 접근 제어자 boolean : 리턴 타입 isTrue : 메소드 이름 파라미터 값 없음
	 */
	public static boolean isTrue() {
		return true;
	}

	public static int getCount(int startNum, int endNum) {
		if (startNum > endNum)
			return startNum;
		if (endNum > startNum)
			return endNum;
		return 0;
	}

	public static int 짝수개수구하기() {
		int count = 0;
		for (int i = 1; i <= 20; i++) {
			if (i % 2 == 0)
				count++;
		}
		return count;
	}

	public static int solution(int x) {
		int count = 0;
		long n = x;
		System.out.println(n);
		if (n == 1) {
			return 0;
		}
		while(n != 1){
			if (n % 2 == 0) {
				n = n / 2;	
				count++;
				System.out.println(n);
			} else if (n % 2 == 1) {
				n = n * 3 + 1;
				count++;
				System.out.println(n);
			}
			if (count >= 500) {
				return -1;
			}
		}
		return count;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
//		getCount(1,10);
		System.out.println(getCount(11, 10));
		System.out.println(getSum());
		System.out.println(짝수개수구하기());
		System.out.println("-------------");
		System.out.println(solution(626331)+"번 반복");
	}
}
