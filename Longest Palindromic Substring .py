'''
Problem description:
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Examples:
Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

Basic thought is simple. when you increase s by 1 character, you could only increase maxPalindromeLen by 1 or 2,
 and that new maxPalindrome includes this new character. 
Proof: if on adding 1 character, maxPalindromeLen increased by 3 or more, say the new maxPalindromeLen is Q, 
and the old maxPalindromeLen is P, and Q>=P+3. Then it would mean, even without this new character, 
there would be a palindromic substring ending in the last character, whose length is at least Q-2.
 Since Q-2 would be >P, this contradicts the condition that P is the maxPalindromeLen without the additional character.

So, it becomes simple, you only need to scan from beginning to the end, adding one character at a time, 
keeping track of maxPalindromeLen, and for each added character, you check if the substrings ending with this new character, 
with length P+1 or P+2, are palindromes, and update accordingly.

Now, this is O(n^2) as taking substrings and checking palindromicity seem O(n) time. We can speed up it by realizing that strings are immutable, 
and there are memory slicing tricks will help to speed these operations up. 
comparing string equality with "==" is O(1), and using slicing to substring and reverse is ̶O(n) (thanks to ChuntaoLu). 
But as slicing is optimized by the interpreter's C code, it should run pretty fast. 
I'm pretty new to Python. Would appreciate you would give more insights or further optimization.

'''
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s)==0:
        	return 0
        maxLen=1
        start=0
        for i in xrange(len(s)):
        	if i-maxLen >=1 and s[i-maxLen-1:i+1]==s[i-maxLen-1:i+1][::-1]:
        		start=i-maxLen-1
        		maxLen+=2
        		continue

        	if i-maxLen >=0 and s[i-maxLen:i+1]==s[i-maxLen:i+1][::-1]:
        		start=i-maxLen
        		maxLen+=1
        return s[start:start+maxLen]


#easy solution to understand
def longestPalindrome(self, s):
    res = ""
    for i in xrange(len(s)):
        # odd case, like "aba"
        tmp = self.helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = self.helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res
 
# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
def helper(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]


#solution based on wiki
class Solution:
    #Manacher algorithm
    #http://en.wikipedia.org/wiki/Longest_palindromic_substring
    
    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
