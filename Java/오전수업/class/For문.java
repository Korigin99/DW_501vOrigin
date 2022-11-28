package 자바0913;

import java.util.Scanner;

public class For문 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		System.out.print("값을 입력해주세요 :");
		int num = s.nextInt();
		System.out.println("값은 " + num);
		int i;
		if (num >= 3 && num <= 1000) {
			for (i = 1; i < num; i++) {
				if (num % i == 1) {
					System.out.println("가장 작은 자연수는 " + i + "입니다.");
					break;
				}
			}
		}
		int sum = 0;
		for (i = 3; i <= 6; i++) {
			sum += i;
		}
		System.out.println(sum);
	}

}
