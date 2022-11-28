package 자바0913;

import java.util.Scanner;

public class 메소드공부3 {
	
	public static void 캐릭터생성() {
		Scanner s = new Scanner(System.in);
		System.out.println("캐릭터 이름을 입력 해주세요.");
		System.out.print("캐릭터 이름 => ");
		String 캐릭터이름 = s.next();
		System.out.println("캐릭터 이름은 : "+캐릭터이름);
	}
	
	public static void 직업선택() {
		Scanner s = new Scanner(System.in);
		System.out.println("[1] 전사 [2] 마법사 [3] 궁수");
		System.out.print("직업 선택 => ");
		int 직업 = s.nextInt();
		String[] 직업배열 = {"전사", "마법사", "궁수"};
		System.out.println(직업배열[직업-1]+"을(를) 선택하셨습니다!");
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		System.out.println("### 게임 프로그램 시작 ###");
		
		while(true) {
			System.out.println("[1] 캐릭터 생성 [2] 직업 선택 [3] 프로그램 종료");
			System.out.print("이용하실 서비스를 선택해주세요 : ");
			String menu = s.next();
			switch(menu) {
				case "1": 
					System.out.println("### 캐릭터 생성 선택");
					캐릭터생성();
					break;
				case "2": 
					System.out.println("### 직업 선택"); 
					직업선택();
					break;
				case "3": 
					System.out.println("프로그램 종료"); 
					System.exit(0);
					break;
			}
		}
	}
}
