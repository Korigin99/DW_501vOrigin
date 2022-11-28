package cafe.mian;

import java.util.InputMismatchException;
import java.util.Scanner;

import cafe.VO.member;
import cafe.control.Event;
import cafe.control.Exit;
import cafe.control.Login;
import cafe.control.Order;
import cafe.control.Signin;
import cafe.control.menu_able;

public class cafe_main {

	static Scanner sc = new Scanner(System.in);
	public static member user = null;

	public static void main(String[] args) {

		menu_able[] menu = { new Order(), new Login(), new Event(), new Signin(), new Exit() };

		while (menu[main_menu() - 1].menu_active())
			;

	}

	public static int main_menu() { // 클래스 메서드 - 클래스 메서드에만 사용
		int select = 0;
		String[] menu = { "주문", "로그인", "이벤트", "회원가입", "종료" };
		try {
			for (int i = 1; i <= menu.length; i++) {
				if (user != null && (i == 2 || i == 4)) {
					// System.out.println(user);
					continue;
				}
				System.out.println(i + ". " + menu[i - 1]);
			}
			System.out.print("선택 : ");
			select = sc.nextInt();
			if (select < 1 || select > 5) {
				throw new InputMismatchException("잘못 입력 했습니다.");
			}
		} catch (Exception e) {
			System.out.println(e.getMessage());
			sc.nextLine();
			select = main_menu();
		}
		return select;
	}

}
