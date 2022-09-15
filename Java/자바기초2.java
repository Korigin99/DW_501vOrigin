package 자바0913;

import java.util.Scanner;

public class 자바기초2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		// ctrl + shift + 0 : 자동 임포트
		Scanner s = new Scanner(System.in);
		System.out.print("값을 입력해주세요:");
		int num = s.nextInt();
		System.out.println("값은 " + num);

		if(num%2==0) {
			System.out.println("짝수입니다.");
		}else {
			System.out.println("홀수입니다.");
		}
	}

}
