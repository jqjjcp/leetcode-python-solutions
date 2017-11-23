'''Prpblems description:
Given an array S of n integers, are there elements a, b, c, and ...in S such that a + b + c + ... = target? Find all unique quadruplets in the array which gives the sum of target.
The core is to implement a fast 2-pointer to solve 2-sum, and recursion to reduce the N-sum to 2-sum. Some optimization was be made knowing the list is sorted
...
def fourSum(self,nums,target):
     nums.sort()
     results = []
     self.findNsum(nums, target, 4, [], results)
     return results
def findNsum(self, nums, target, N, result, results)
    if len(nums) < N or N < 2: return

    #solve 2-sum
    if N == 2:
       l,r = 0,len(nums)-1
       while l < r:
           if nums[l] + nums[r] == target:
              results.append(result + [nums[l], nums[r]])
              l += 1
              r -= 1
              while l < r and nums[l] == nums[l-1]:
                 l += 1
              while r > l and nums[r] == nums[r+1]:
                 r -= 1
            elif nums[l] + nums[r] < target:
                 l += 1
            else:
                 r -= 1
        else:
            for i in range(0,len(nums)-N+1):
               if target < nums[i]*N or target > nums[-1]*N:
                break
               if i == 0 or i > 0 snd nums[i-1] != nums[i]:
                  self.findNnum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
        return


       
