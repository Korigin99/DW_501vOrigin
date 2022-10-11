# 10월 4일 수업


### 오전 수업

- JavaScript로 html 다루기

```js
  var li = document.createElement("li"); // li 태그 생성
  // document.createElement : 새 태그 생성

  ul.appendChild(li); // ul 태그 자식으로 li 추가
  // appendChild : 자식 태그로 추가

  bt.setAttribute('class', 'del_bt');
  // setAttribute : 태그에 새속성 추가

  body.removeChild(p); //body 태그에서 해당 태그 삭제
  // removeChild : 자식 태그 삭제
```

### 오후 수업

- DataBase

``` MySQL  
-- 사원 이름 조회
-- 조회 : select
-- 테이블 선택 : from  
SELECT ename FROM emp

-- 사원번호, 사원이름, 입사날짜 조회
SELECT empno, ename, hiredate FROM emp

-- 사원번호, 사수번호, 사원이름, 급여 조회
SELECT empno, mgr, ename, SAL FROM emp

-- AS : 별칭 주기
SELECT empno AS "사원번호" FROM emp

SELECT empno AS "사원번호" , ename AS "사원이름" FROM emp

-- 필터링 : WHERE 
SELECT empno, ename, job FROM emp WHERE JOB = 'SALESMAN'

SELECT empno, ename, job FROM emp WHERE empno = 7782

-- 급여를 1000 이상 받는 사원 이름 조회
SELECT ename FROM emp WHERE sal >= 1000

-- 급여 2000 이상 받는 사원 이름, 직업, 급여 조회
 
-- SQL 실행 순서 1. FROM 2. WHERE 3. SELECT

-- AND는 모든 조건이 만족해야 한다.
SELECT ename ,job, sal FROM emp WHERE job = 'MANAGER' AND sal >= 2000

-- 입사날짜가 1981-12-03이고 직업이 analyst인 사원의 이름, 입사날짜, 직업조회
SELECT ename, hiredate, job FROM emp WHERE HIREDATE = '1981-12-03' AND job = 'ANALYST'

SELECT sum(sal) FROM emp

-- 직업이 MANAGER인 사원 급여 총합 조회
SELECT sum(sal) FROM emp WHERE job = 'MANAGER'

-- avg : 평균 , MIN, max(
SELECT avg(sal) FROM emp WHERE deptno = 20

-- 날짜 함수 (입사날짜 년도만 나오게 
SELECT date_format(hiredate, "%Y") AS '입사 년도' FROM emp
-- 날짜 함수 (입사날짜 월만 나오게) M : 영어 , m : 숫자 로 월이 나옴
SELECT date_format(hiredate, "%m") AS '입사 월' FROM emp
```




