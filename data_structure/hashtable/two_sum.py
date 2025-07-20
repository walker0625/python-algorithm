def two_sum_by_hashtable(nums, target):

    hashtable = {}
    
    for num in nums:
        hashtable[num] = True # value는 아무거나 넣어도 됨(Boolean은 1bit니 추천)

    for num in nums:
        key = target - num # key : target이 되기 위해 필요한 숫자
        
        if key in hashtable:
            return True

    return False


print(two_sum_by_hashtable(nums = [4, 1, 9, 7, 5, 3, 16], target = 20))