'''
Problem description:
Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

Solution (DP, O(n)):
  
  Assume L[i] = s[m...i], denotes the longest substring without repeating
  characters that ends up at s[i], and we keep a hashmap for every
  characters between m ... i, while storing <character, index> in the
  hashmap.
  We know that each character will appear only once.
  Then to find s[i+1]:
  1) if s[i+1] does not appear in hashmap
     we can just add s[i+1] to hash map. and L[i+1] = s[m...i+1]
  2) if s[i+1] exists in hashmap, and the hashmap value (the index) is k
     let m = max(m, k), then L[i+1] = s[m...i+1], we also need to update
     entry in hashmap to mark the latest occurency of s[i+1].
  
  Since we scan the string for only once, and the 'm' will also move from
  beginning to end for at most once. Overall complexity is O(n).
 
  If characters are all in ASCII, we could use array to mimic hashmap.

'''
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength

#another solution 
def lengthOfLongestSubstring2(self, s):
    dic, res, start, = {}, 0, 0
    for i, ch in enumerate(s):
        if ch in dic:
            # update the res
            res = max(res, i-start)
            # here should be careful, like "abba"
            start = max(start, dic[ch]+1)
        dic[ch] = i
    # return should consider the last 
    # non-repeated substring
    return max(res, len(s)-start)