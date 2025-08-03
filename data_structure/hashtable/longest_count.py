# 1. dictionary로 탐색 복잡도 낮추기
# 2. 시작점이 dictionary에 있는지 확인하여 중복 count 제거(n^2 => 2n))

def longest_count(nums):
    
    longest = 0

    # nums_dict = {}
    
    # for num in nums:
    #     nums_dict[num] = True

    # 값 중복을 고려할 필요가 없으면, set으로 구현하는 것이 value에 대한 고려를 할 필요가 없음
    nums_set = set(nums)    

    for num in nums:

        # 처음 시작점이 아니면 중복 count가 발생하니, 바로 이전 숫자가 있는지 파악
        if num - 1 not in nums_set: 

            count = 1
            target = num + 1

            while target in nums_set:
                count += 1
                target += 1

            longest = max(longest, count)    

    return longest

print(longest_count([1,2,3,4,5]))

