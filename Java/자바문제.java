package 자바0913;

import java.util.Scanner;

public class 자바문제 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String name[] = { "Brain", "Kim" };

		// 문제 1
		for (int i = 0; i < name.length; i++) {
			// boolean isCheck = name[i].equals("kim"); 이렇게 가능
			// if(isCheck) System.out.println("Kim은" + i + "번에 있습니다.");
			if (name[i].equals("Kim")) {
				System.out.println("Kim은" + i + "번에 있습니다.");
				break;
			}
		}
		Scanner s = new Scanner(System.in);
		// 문제 2
//		String ph = "010-3333-9999";
//		String num[] = ph.split("-");
		
		String ph = "";
		String ph2 = "";
		System.out.printf("번호를 입력하세요 : ");
		ph = s.next();
		String num[] = ph.split("-");
		for (int i = 0; i < num.length; i++) {
			if (i == 0) {
				ph2 += num[0];
			}
			if (i >= 1) {
				ph2 += "-****";
			}
		}
		System.out.println(ph2);
	}

}
