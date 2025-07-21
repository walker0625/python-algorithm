def two_sum_by_hashtable(nums, target):

    hashtable = {}
    
    for num in nums:
        hashtable[num] = True # value는 아무거나 넣어도 됨(Boolean은 1bit니 추천)

    for num in nums:
        key = target - num # key : target이 되기 위해 필요한 숫자
        
        if key in hashtable: # O(1)으로 탐색 가능한 것이 POINT!(key in nums(list)로 하면 O(n)으로 동작)
            return True

    return False


print(two_sum_by_hashtable(nums = [4, 1, 9, 7, 5, 3, 16], target = 20))