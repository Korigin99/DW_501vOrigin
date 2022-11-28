package com.example.demo.vo;

import lombok.Getter;
import lombok.Setter;

// VO 클래스 : Value Object의 줄임말
// VO 클래스에는 필드변수와 getter, setter만 온다.
public class Login {
	
	@Getter
	@Setter
	
	private String userId;
	private String userPw;
	private String userMail;
	
	public String getUserPw() {
		return userPw;
	}
	public void setUserPw(String userPw) {
		this.userPw = userPw;
	}
	public String getUserMail() {
		return userMail;
	}
	public void setUserMail(String userMail) {
		this.userMail = userMail;
	}
	
}
