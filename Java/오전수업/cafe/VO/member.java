package cafe.VO;

public class member {
	private String id;
	private String name;
	private String tel;
	private String email;
	private int money;

	public member() {}
	public member(String id, String name, String tel, String email, int money) {
		this.id = id;
		this.name = name;
		this.tel = tel;
		this.email = email;
		this.money = money;
	}
	
	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getTel() {
		return tel;
	}

	public void setTel(String tel) {
		this.tel = tel;
	}

	public String getEmaill() {
		return email;
	}

	public void setEmaill(String emaill) {
		this.email = emaill;
	}

}
