package cafe.DAO;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import cafe.VO.member;
import cafe.mian.cafe_main;

public class Member_DAO extends base_DAO{

	public Member_DAO() {

		table_check();
	}

	public boolean info_check(String tel, String email) {
		String[] t = tel.split("-");

		if (!(t[0].equals("010")) || tel.length() != 13) {
			System.out.println("연락처 형식이 옳바르지 않습니다!");
			return true;
		}

		return false;
	}

	public boolean login(String id, String pw) {
		String sql = "select * from member where id=? and tel =?";
		try {
			pt = conn.prepareStatement(sql);
			pt.setString(1, id);
			pt.setString(2, pw);
			rs = pt.executeQuery();
			if (rs.next()) {
				cafe_main.user = new member(rs.getString(1), rs.getString(2), rs.getString(3), rs.getString(4),
						rs.getInt(5));
				return false;
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}
		return true;
	}

	public boolean id_check(String id, String email) {
		String sql = "select * from member where id=? or email=?";
		try {
			pt = conn.prepareStatement(sql);
			pt.setString(1, id);
			pt.setString(2, email);
			rs = pt.executeQuery();
			if (rs.next()) {
				return true;
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}

		return false;
	}

	public boolean member_insert(String id, String name, String tel, String email) {
		String sql = "insert into member(id, name, tel, email) values(?,?,?,?)";
		try {
			pt = conn.prepareStatement(sql);
			pt.setString(1, id);
			pt.setString(2, name);
			pt.setString(3, tel);
			pt.setString(4, email);
			pt.executeUpdate(); // query - 조회하는 경우 사용, update - 변경, 추가, 삭제인 경우 삭제
			return true;
		} catch (SQLException e) {
			e.printStackTrace();
			return false;
		}
	}

	private void tablemake() {
		String sql = "create table member( member_seq int auto_increment primary key, id varchar(50) not null, name varchar(20) not null, tel varchar(20) not null, email varchar(255) not null)";
		try {
			st = conn.createStatement();
			int result = st.executeUpdate(sql);
			System.out.println("member 테이블 생성");
		} catch (SQLException e) {
			e.printStackTrace();
		}

	}

	private void table_check() {

		String sql = "select COUNT(*) as cnt from information_schema.tables where table_schema ='dw_501' and table_name='member'";
		try {
			st = conn.createStatement(); // 접속 정보로 질의문 저장할 수 있는 객체 생성
			rs = st.executeQuery(sql); // 만들어 놓은 질의문을 저장해서 연결 돼 데이터베아스에 전달하고 결과 받기
			if (rs.next()) { // rs.next() : rs에 결과값이 있는가? 없는가? 확인하고 rs에서 값 가져오기 해야한다.
				int cnt = rs.getInt("cnt");
				if (cnt == 0) {
					tablemake();
				}
				rs.close();
				st.close();
			}
		} catch (SQLException e) {
			e.printStackTrace();
		}

	}

}

/*
 * 자바 - 데이터베이스 연결
 * 
 * 1. 연결할 데이터베이스의 드라이버 로드 - 많이 사용되는 데이터베이스의 드라이버는 해당 데이터베이스 웹사이트에서 얻을 수 있다,
 * 
 * 2. 드라이버 로드를 하면 데이터베이스와 자바프로그램간의 연결이 이루어진다.
 * 
 * 3. 데이터베이스와 연결을 하였다면 데이터베이스에 로그인을 시도한다.
 * 
 * 4. 데이터베이스 계정을 가지고 로그인을 해야한다.
 * 
 * 5. 데이터베이스 주소와 계정명, 비밀번호가 필요하다.
 * 
 */