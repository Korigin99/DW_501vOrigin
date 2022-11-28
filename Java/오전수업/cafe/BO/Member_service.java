package cafe.BO;

import cafe.DAO.Member_DAO;

public class Member_service {
	private Member_DAO mdao = new Member_DAO();

	public boolean login(String id, String pw) {

		boolean chk = mdao.login(id, pw);
		if (chk) {
			System.out.println("아이디 또는 비밀번호 불일치");
			return true;
		} else
			return false; // 성공시 false - 아이디, 비번이 일치한 경우
	}

	public boolean sign_member(String id, String name, String tel, String email) {
		boolean check = mdao.id_check(id, email);

		if (check) {
			System.out.println("아이디 또는 이메일이 중복입니다!");
			return false;
		} else
			mdao.member_insert(id, name, tel, email);
		System.out.println("회원가입 성공");
		return true;
	}

}
