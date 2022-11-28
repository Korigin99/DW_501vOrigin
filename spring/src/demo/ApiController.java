package com.example.demo;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import javax.servlet.http.HttpServletRequest;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.vo.Login;
import com.example.demo.vo.Login2;

/*
 *  RestController 와 Controller 차이점
 *  
 *  Controller는 페이지(html) 이동
 *  RestController는 데이터(JSON) 전송
 *  
 *  Controller는 사용자 요쳥(URL 요청)을 처리하는 class
 */

// Rest : 자원 (==데이터)
@RestController
public class ApiController {
	
	// @Autowired : Spring에서 객체를 관리함 (IoC : Inversion of Control 제어 역전)
	// Autowired가 사용되긴 위해선 클래스 위에 annotation이 있어야 함
	@Autowired
	ApiService apiService; 
	
	@GetMapping("/api/v1/sample")
	public List<String> callData() {
		List<String> list = new ArrayList<>();
		list.add("삼겹살");
		list.add("항정살");
		list.add("오리고기");
		list.add("목살");
		return list;
	}

	// Get : 조회
	// Mapping : URL 연결
	@GetMapping("/api/v1/movie")
	public movie callMovie() {
		movie movie = new movie();
		movie.setTitle("Interstellar");
		movie.setYear("2014");
		movie.setRuntime("169min");
		movie.setGenre("SF");
		return movie;
	}

	@GetMapping("/api/v1/movies")
	public List<movie> callMovies() {
		
		return apiService.makeMovies();
	}

	// URL을 이용하여 데이터 받는 방법

	@GetMapping("/api/v1/sports/qatar2022/article/{articleNumber}")
	public int callArticle(@PathVariable int articleNumber) {
		return articleNumber;
	}
	
	// 쿼리 스트링으로 데이터 받기
	// /api/v1/webtoon/list?titleId=75837&weekday=mon
	// Request(요청) + Param(파라미터)
	@GetMapping("/api/v1/webtoon/list")
	public Map<String, Object> callWebtoon(@RequestParam int titleId, @RequestParam String weekday){
		Map<String, Object> map = new HashMap<String, Object>();
		map.put("titleId", titleId);
		map.put("weekday", weekday);
		return map;
	}
	
	@GetMapping("/api/v1/webtoon/list/titleId/{titleId}/weekday/{weekday}")
	public Map<String, Object> callWebtoon2(@PathVariable int titleId, @PathVariable String weekday){
		Map<String, Object> map = new HashMap<String, Object>();
		map.put("titleId", titleId);
		map.put("weekday", weekday);
		return map;
	}
	
	// Post : 데이터블 받아서 생성할 때 사용
	@PostMapping("/api/v1/join")
	public boolean callJoin(@RequestBody Login login) {
		System.out.println("HTML에서 서버로 받아온 데이터");
		System.out.println("아이디 : "+login.getUserId());
		System.out.println("이메일 : "+login.getUserMail());
		System.out.println("비밀번호 : "+login.getUserPw());
		return true;
	}
	
	@PostMapping("/api/v1/join2")
	public boolean callJoin(@RequestBody Login2 login, HttpServletRequest request) {
		
		String ip = request.getRemoteAddr();
		System.out.println("요청받은 IP : " + ip);
		
		System.out.println("HTML에서 서버로 받아온 데이터");
		System.out.println("회사명 : "+login.getCompanyName());
		System.out.println("사용자 명 : "+login.getUserName());
		System.out.println("사용자 번호 : "+login.getPhone());
		return true;
	}
	
	/*
	 * CRUD = Create Read Update Delete
	 * Get : 데이터 조회 == select
	 * Post : 데이터 생성 = insert
	 * Patch : 데이터 업데이트 == update
	 * Delete : 데이터 삭제 == delete
	 */
	
}









