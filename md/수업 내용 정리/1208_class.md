### 12월 8일 수업

### python - list 기본 문법


- list 생성
- 1. memo = ["a", "b", "c"]
- 2. memo = list(("a","b","c"))
- 데이터 추가 memo.append("abc")
- 데이터 삽입 memo.insert(2, "abc")
- 데이터 삭제
- 삭제 데이터 지정 memo,remove("c")
- 마지막 데이터 삭제 memo.pop()
- 인덱스로 삭제 del memo[3]
- 배열 합치기 memo.extend(리스트 이름)
- 리스트 크기 len(리스트 이름)
- 갯수 구하기 memo.count("a") - a 라는 데이터의 개수를 찾을 떄 사용
- 인덱스 찾기 memo.index("a") - a 라는 데이터는 몇번 인덱스에 있는지 찾을 때 사용
- 정렬 memo.sort() - 오름차순, memo.sort(reverse=True) - 내림차순
- 반전 memo.reverse()