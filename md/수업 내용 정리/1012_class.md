# 10워 12일 SQL 수업

## SQL
  
  ### JOIN
  - 2개 이상 테이블 데이터 조회할 때 사용 
  - 교집합 데이터가 있어야 함
  
  ### JOIN 종류

  1. INNER JOIN

  2. SELF JOIN : 본인 테이블을 한번 더 조인 함

  ``` SQL
    SELECT 컬럼이름 FROM 테이블 이름 AS x INNER JOIN 테이블 이름 AS Y ON x.컬럼 = y.컬럼
    -- 데이터에 교집합이 있으면 조회
  ```
  3. LEFT JOIN, RIGHT JOIN
   - 기준이 되는 테이블 이름을 기준으로 LEFT JOIN 또는 RIGHT JOIN을 사용하면 된다.
   - where 조건에 is null을 사용하면 차집합 데이터를 가져올 수 있다.


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

