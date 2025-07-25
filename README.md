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


# 실전 풀이 과정

1. 시간복잡도가 만능은 아니지만(DFS/BFS등은 제한 X), 10^8 기준으로 미리 제한 파악

2. 범위수가 작다면 그냥 단순하게 접근해도 문제 없음(M=20, N=20)

3. 제한에 대한 확신 이후에 풀이 접근(풀고나서 제한에 걸리는 시간 낭비 방지)


# Hash Table(Dictionary의 내부 구현 - Hash Function 활용 : O(1))

![alt text](image.png)

if 'key' in 'Dictionary' - O(1)으로 탐색 가능(Memory 활용)