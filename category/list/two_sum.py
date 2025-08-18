# 두수의 합이 target 값이 될 수 있는지 여부에 return
# nums < 10^4 => n^2은 위험할 수 있음

def two_sum_two_pointer(nums, target):
    
    nums.sort() # nlogn
    l = 0
    r = len(nums)-1

    while l < r:
        if nums[l] + nums[r] == target:
            return True
        elif nums[l] + nums[r] > target:
            r = r - 1
        elif nums[l] + nums[r] < target:
            l = l + 1    

    return False

print(two_sum_two_pointer(nums = [4, 1, 9, 7, 5, 3, 16], target = 12))