package cafe.control;

import java.util.Scanner;

import cafe.BO.Member_service;

public class Login implements menu_able {
	
	
	@Override
	public boolean menu_active() {
		Scanner sc = new Scanner(System.in);
		String id = null, pw = null;
		Member_service ms = new Member_service();

		boolean chk = true;
		do {
			System.out.print("아이디 : ");
			id = sc.nextLine();
			System.out.print("비밀번호(연락처) : ");
			pw = sc.nextLine();
			chk = ms.login(id,pw); // 로그인 시도
			
			if(chk) { // 로그인  실패시
				System.out.println("회원가입 하시겠습니까?(y/n)");
				if(sc.nextLine().equals("y")) {
					new Signin().menu_active();
				}
			}
		} while (chk);

		return true;
	}

}
