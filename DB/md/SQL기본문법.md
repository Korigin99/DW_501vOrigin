# SQL 기본 문법

### 쿼리 순서와 기본적인 쿼리

- 쿼리 순서
  1. FROM 
  2. WHERE 
  3. GROUP BY 
  4. HAVING 
  5. SELECT 
  6. ORDER BY

- SELECT : 조회(READ)
 1. SELECT 컬럼이름 FROM 테이블 이름 WHERE, GROUP BY, HAVING ...
- WHERE, HAVING 차이 - WHERE은 집계함수 사용 시 오류, HAVING은 가능
- ORDER BY 디폴트 값은 오름차순(ASC)
- INSERT : 입력(CREATE)
 1. INSERT INTO 컬럼이름 VALUES 데이터
- UPDATE : 수정
 1. UPDATE 테이블 이름 SET 컬럼이름 = 데이터
 2. 데이터 베이스는 UPDATE를 받으면 DELETE 했다가 INSERT  하는거임
- DELETE : 삭제
 1. DELETE FROM 테이블 이름

 ### DELETE와 truncate
1. DELETE
``` sql
DELETE FROM 테이블이름
DELETE FROM emp where ename = '김기원'
```
- delete 추가 설명
- DELETE FROM EMP  --  emp에 있는 데이터가 모두 삭제 됨
- delete할 때는 where을 사용해서 모든 행이 삭제 되는걸 막아야 한다.

2. truncate
- 테이블 안에 데이터를 모두 지울 때는 delete가 아니라 truncate 사용
```sql
truncate TABLE emp 
truncate TABLE 테이블 이름
```