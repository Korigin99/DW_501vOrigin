package com.example.demo;

import java.util.ArrayList;
import java.util.List;

import org.springframework.stereotype.Service;


// Service : 서비스에서 로직(알고리즘)을 구현한다.
// 비즈니스 구역

@Service
public class ApiService {
	
	/**
	 * @Since : 2022. 11. 23.
	 * @Author : giwon
	 * @Return : List<movie>
	 * @Comment : 영화 만들기
	 */
	public List<movie> makeMovies() {
		
		List<movie> list = new ArrayList<movie>();
		
		movie movie = new movie();
		System.out.println(movie);
		movie.setPoster("/images/intime.png");
		movie.setTitle("Interstellar");
		movie.setYear("2014");
		movie.setRuntime("169min");
		movie.setGenre("SF");

		movie movie2 = new movie();
		System.out.println(movie2);
		movie2.setTitle("TENNET");
		movie2.setYear("2020");
		movie2.setRuntime("150min");
		movie2.setGenre("SF");
		
		movie movie3 = new movie();
		movie3.setTitle("Gravity");
		movie3.setYear("2013");
		movie3.setRuntime("90min");
		movie3.setGenre("SF");
		
		movie movie4 = new movie();
		movie4.setTitle("Ex Machina");
		movie4.setYear("2015");
		movie4.setRuntime("108min");
		movie4.setGenre("SF");
		
		movie movie5 = new movie();
		movie5.setTitle("Passengers");
		movie5.setYear("2017");
		movie5.setRuntime("116min");
		movie5.setGenre("SF");
		
		movie movie6 = new movie();
		movie6.setTitle("In Time");
		movie6.setYear("2011");
		movie6.setRuntime("109min");
		movie6.setGenre("SF");
			
		list.add(movie);
		list.add(movie2);
		list.add(movie3);
		list.add(movie4);
		list.add(movie5);
		list.add(movie6);
		
		return list;
	}
	
}
