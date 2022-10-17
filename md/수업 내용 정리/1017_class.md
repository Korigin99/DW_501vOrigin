# 10월 17일 수업





## 오후 수업

### SQL
 
- 데이터베이스 모델링
  - 테이블들은 자식과 부모 관계를 가진다.

-  관계 종류
        
        1. 1 : 1 관계 (One to One)  
        ex) 군인 <-> 총기, 사람 <-> 주민
        
        2. 1 : N (One to Many)
        ex) 부서(1) <-> 사원(N), 축구팀(1) <-> 선수(N)
        
        3. N : M 관계 (Many to Many) : 테이블 3개 이상
        ex) 과목(N) <-> 수강신청 <-> 학생(M)


----

- 💡 모델링 Tip 💡

    1. 자주 조회하는 컬럼은 위쪽으로 배치

    2. 테이블에 컬럼이 많으면 좋은게 아님 - 테이블을 나누자(객체화)

    3. 자주 조회하는 테이블은 **역정규화** 하자
      
  
---

#### 정규화와 역정규화
- **정규화** : 관계형 데이터베이스의 설계에서 중복을 최소화하게 데이터를 구조화하는 프로세스를 정규화(Normalization)라고 한다.
    - Data Model 과정에서 Entity 사이의 관계(Level, Depth 등)를 분석하여 다수의     Relation으로 분리하는 과정을 말한다.

  정규화는 이렇게 함으로써 데이터의 일관성(Consistency)과 모델의 응집도(Cohesion)를 높이는 것을 지향한다.  
    - 정규화는 일관성(Consistency)을 향상시킨다.

          정규화는 하나의 논리적 Database에서 여러 테이블에 동일한 데이터(column)가 관리되지 않도록 설계하는 과정이다.

          만약, 여러 테이블에서 필요한 데이터라면 해당 Entity의 Level은 최상위 Level에 속하게 될  것이고, 데이터의 값(value)이 아닌 데이터의 구분자(일반적으로 index)로 관계를 맺어주면  된다.

          즉, 데이터가 한 곳에서 관리되는 것은 데이터의 변경(INSERT / UPDATE / DELETE)이 있을 때,   특정 테이블의 특정 row만 수정하면 된다.

          여러 곳에 데이터가 산재해 있을 경우, 해당 데이터의 값을 일관되게 관리하는

          즉, 데이터의 Sync 이슈를 최소화 시킬 수 있기 위해서는 정규화 과정이 중요하다.

          정규화는 데이터 조회의 비용을 향상시킨다.
          정규화를 통해 데이터를 Entity 단위로 분리하고, 각 데이터 간의 Relation을 만들었다면,  필요한 데이터가 하나의 테이블에 있지 않은 경우가 많다.

          즉 필요한 정보가 해당 테이블에 없기 때문에 다른 테이블과 JOIN을 통해 정보를 가져와야  하며, 이는 연산 시간과 비용을 증가시킬 수 있다.


- **역정규화** : 정규화된 데이터베이스에서 성능을 개선하기 위해 사용되는 전략을 역정규화(Denormalization)라고 한다
                    
      정규화의 단점으로 언급되었던 것이 '비용(Cost)'이다.

      역정규화는 데이터베이스의 비용을 최소화하기 위해 중복을 허용하며 Entity를 다시 통합하거나 분할하여 정규화 과정을 통해 도출된 DB 구조를 재조정하는 과정이다.

      Join이 너무 많아지는 DB 설계와 쿼리는 요청을 처리하는 시간을 증가시키는 문제가 있기 때문에 모든 주요 Entity를 분리하는 것이 좋은 것이 아니라 DB의 전반적인 성능을 향상시킬 수 있는 구조화 과정을 거치는 것이 필요하다.

----

### 테이블 만들기

- 테이블 생성, 삭제와 데이터 삽입
  
  ```sql
  -- INSERT, SELECT, UPDATE, DELETE : DML
  -- CREATE(테이블 생성), DROP(테이블 삭제), ALTER(테이블 수정) : DDL
  -- 상품 테이블 만들기
  -- 데이터 베이스는 카멜 표기법이 불가능
  -- 컬럼 이름 데이터타입(바이트 수)
  -- AUTO_INCREMENT 는 자동으로 PK값을 증가 시켜줌
  -- comment '설명'
  CREATE TABLE products(
  	product_id int(4) AUTO_INCREMENT PRIMARY KEY,
  	product_price int(4) comment '물품가',
  	create_at datetime comment '입고 날짜',
  	shipment_price int(4) comment '출하가',
  	a_brand_name varchar(30) comment 'A 브랜드 이름',
  	b_brand_name varchar(30) comment 'B 브랜드 이름',
  	c_brand_name varchar(30) comment 'C 브랜드 이름'
  )

  -- 상품 테이블에 데이터 넣기

  INSERT into products (product_price, create_at, shipment_price, a_brand_name)
  VALUES (3000,now(),5000, '나이키 에어포스')

  INSERT into products (product_price, create_at, shipment_price, b_brand_name)
  VALUES (3000,now(),5000, '아디다스')


  INSERT into products (product_price, create_at, shipment_price, a_brand_name,b_brand_name,c_brand_name)
  VALUES (3000,now(),5000, '나이키', '아디다스', '코닥')

  -- 테이블 삭제 (안에 있는 데이터도 모두 사라짐)
  DROP TABLE products

  CREATE TABLE brand(
  	brand_id int(4) AUTO_INCREMENT PRIMARY KEY,
  	brand_name varchar(30) comment '브랜드 이름'
  );

  -- 상품 테이블 다시 만들기
  CREATE TABLE products(
  	product_id int(4) AUTO_INCREMENT PRIMARY KEY,
  	product_price int(4) comment '물품가',
  	create_at datetime comment '입고 날짜',
  	shipment_price int(4) comment '출하가',
  	brand_id int(4) comment '브랜드 번호',
  	FOREIGN KEY (brand_id) REFERENCES brand(brand_id) ON DELETE CASCADE
  );

  INSERT INTO brand (brand_name) VALUES ('나이키')
  INSERT INTO brand (brand_name) VALUES ('아디다스')
  INSERT INTO brand (brand_name) VALUES ('코닥')
  INSERT INTO brand (brand_name) VALUES ('톰브라운')
  INSERT INTO brand (brand_name) VALUES ('버버리')

  INSERT INTO products (product_price, create_at, shipment_price, brand_id)
  values(5000, now(),3000, 1)
  INSERT INTO products (product_price, create_at, shipment_price, brand_id)
  values(6000, now(),4000, 2)
  INSERT INTO products (product_price, create_at, shipment_price, brand_id)
  values(7000, now(),5000, 3)
  INSERT INTO products (product_price, create_at, shipment_price, brand_id)
  values(5000, now(),3000, 4)
  INSERT INTO products (product_price, create_at, shipment_price, brand_id)
  values(9000, now(),7000, 5)

  SELECT p.product_price, p.shipment_price, p.create_at, b.brand_name FROM products AS p INNER JOIN brand AS b ON p.brand_id = b.brand_id  
  ORDER BY p.create_at
  ```