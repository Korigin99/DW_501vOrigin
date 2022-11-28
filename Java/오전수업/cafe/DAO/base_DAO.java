package cafe.DAO;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;

public class base_DAO {

	protected Connection conn = null; // 데이터베이스 연결정보를 저장
	protected Statement st = null; // SQL 질의문을 데이터베이스에 전달
	protected PreparedStatement pt = null; // SQL 질의문을 데이터베이스에 전달
	protected ResultSet rs = null; // SQL 질의문 조회 결과를 저장

	public base_DAO() {
		DriverLoad();
		Connect();
	}

	private void DriverLoad() {
		try {
			Class.forName("com.mysql.cj.jdbc.Driver");
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}

	private void Connect() {
		String url = "jdbc:mysql://localhost:3306/dw_501";
		String user = "root";
		String pass = "9090";
		try {
			conn = DriverManager.getConnection(url, user, pass);
		} catch (Exception e) {
			e.printStackTrace();
			System.out.println("접속 실패");
		}
	}

}
