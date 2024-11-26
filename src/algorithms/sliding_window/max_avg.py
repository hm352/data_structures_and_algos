
from typing import List

nums = [1,12,-5,-6,50,3]
k = 4
single_case = [5]
v = 1 
def find_max_avg(nums, k):
    """
    Find the maximum average of a subarray of size k in the given array
    :param nums: The given array
    :type nums: list
    :param k: The size of the subarray
    :type k: int
    :returns: The maximum average of a subarray of size k
    :rtype: int
    """
    n = len(nums)
    max_avg = None
    i = 0
    j = i + k
    while j <= n:
        arr = nums[i:j]
        s = sum(arr)
        print(s)
        if not max_avg or s > max_avg:
            max_avg = s
        print(max_avg)
        i += 1 
        j += 1
    return max_avg / k

def find_max_avg_optimal(nums, k):
    left = 0
    right = k
    n = len(nums)
    max_sum = prev_sum = sum(nums[left:right])
    while (right < n):
        prev_sum = prev_sum + nums[right] - nums[left]
        if prev_sum > max_sum:
            max_sum = prev_sum
        left += 1
        right += 1
    return max_sum / k

def findMaxAverage(nums: List[int], k: int) -> float:
        
        # initialize and instantiate variables
        left = 0
        right = k
        
        # sum the array and save the max for now
        prevSum = sum(nums[left:right])
        maxSum = prevSum

        # iterate using sliding window
        while(right < len(nums)):

            # only sum the ends since the middle is the same
            prevSum = prevSum - nums[left] + nums[right]
            
            # save the max sum if the new sum (prevSum) is greater
            if prevSum > maxSum:
                maxSum = prevSum
                
            # increment the window
            right += 1 
            left += 1
            
        # return the average
        return maxSum / k

if __name__ == "__main__":
    print(find_max_avg(nums, k))
    print(find_max_avg(single_case, v))
    print(find_max_avg_optimal(nums, k))
    print(find_max_avg_optimal(single_case, v))
    print(findMaxAverage(nums, k))
    print(findMaxAverage(single_case, v))