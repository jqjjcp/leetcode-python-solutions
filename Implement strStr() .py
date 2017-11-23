Problems description:
Implement strStr(). 

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. 


Examples:
Input: haystack = "hello", needle = "ll"
Output: 2

'''
class Solution(object):
def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    for i in range(len(haystack) - len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1