# 시간복잡도 계산

보편적으로 10^8이 문제의 limit(100,000,000)

O(1) < O(logn) < O(n) < O(nlogn) < O(n^2)
>> 중첩이 아니라면 가장 큰 복잡도로 간주 nlogn + n -> nlogn

ex) 문제의 제약조건 : 1 <= n <= 10^5  

1) n^2으로 문제를 풀면 10^10이 되므로 불가
2) O(nlogn), O(n) 등 O(n^2) 이하의 방식으로 풀어야 함


# 자료구조별 시간복잡도

* dict(set/hashtable) : O(1) 가능 - key로 접근

* heappop() / heappush() : O(logn)

* sort() : O(nlogn)

* deque(양방향 que) : list와 비교해서 양끝 추가/삭제가 효율적(O(1))


# 실행시간

python - timeit 모듈로 실제 실행을 통해서 파악