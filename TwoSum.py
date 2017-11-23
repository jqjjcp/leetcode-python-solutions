'''
Problem description:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice

Example:
Given nums = [2, 7, 11, 15]'target = 9'
Beacause nums[0]+ nums[1] = 2 + 7 = 9'
return [0, 1].

'''
##solution in O(n) time
##Python dict is HashTable, so looking up a key is O(1).
class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}  
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

##soluton using hash
class Solution(object):
	#return a tuple
	def twoSum(self, num,target):
		map = {}
		for i in range(len(num)):
			if num[i] not in map:
				map[target - num[i]] = i + 1
		    else:
		    	return map[num[i]], i + 1

		return -1, -1
