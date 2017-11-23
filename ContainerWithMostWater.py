'''Problems description:
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water. 
Note: You may not slant the container and n is at least 2. 


I've seen some "proofs" for the common O(n) solution, but I found them very confusing and lacking. Some even didn't explain anything but just used lots of variables and equations and were like "Tada! See?". I think mine makes more sense:

Idea / Proof:
1.The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
2.All other containers are less wide and thus would need a higher water level in order to hold more water.
3.The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration
Further explanation:

Variables i and j define the container under consideration. We initialize them to first and last line, meaning the widest container. Variable water will keep track of the highest amount of water we managed so far. We compute j - i, the width of the current container, and min(height[i], height[j]), the water level that this container can support. Multiply them to get how much water this container can hold, and update water accordingly. Next remove the smaller one of the two lines from consideration, as justified above in "Idea / Proof". Continue until there is nothing left to consider, then return the result.
'''
class Solution:
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        water = 0
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water

