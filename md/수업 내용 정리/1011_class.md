# 10월 11일 수업 내용

### MySQL

### SQL 기본 문법

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


 ###  INNER JOIN

- 조인은 기준 테이블(emp), 조인 테이블(dept)에  조인 컬럼(deptno)에 해당하는 값이 모두  존재하는 경우에만 데이터가 조회된다.
- 조인 (INNER JOIN) : 기준 테이블과 조인 테이블 모두 데이터가 존재해야 조회됨

* 예제1
    ``` sql
    SELECT
    sawon.ename AS "사원 이름",
    sawon.deptno AS "사원 부서 번호",
    d.dname AS "부서 이름",
    boss.ename AS "사수 이름"
    FROM emp AS sawon
    INNER JOIN dept AS d
    ON sawon.deptno = d.deptno
    INNER JOIN emp AS boss
    ON sawon.mgr = boss.empno
    ```

* 예제2
    ```sql
    SELECT sawon.ename AS "부사수 이름", sawon.empno AS "부사수 번호", sawon.mgr AS 
    "사수 번호(사수의 사원번호)", boss.ename AS "사수이름", boss.empno AS "사수 번호"  
    FROM emp AS sawon INNER JOIN emp AS boss ON sawon.mgr = boss.EMPNO 
    ```
