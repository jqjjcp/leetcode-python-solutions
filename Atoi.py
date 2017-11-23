'''
Problems description:
Given a 32-bit signed integer, reverse digits of an integer.

Examples:
Input: 123
Output:  321

Input: -123
Output: -321

Input: 120
Output: 21
'''
#Get the sign, get the reversed absolute integer, and return their product if r didn't "overflow".
def reverse(self, x):
    s = cmp(x, 0)
    r = int(`s*x`[::-1])
    return s*r * (r < 2**31)

#another solution
def convert(self, s, nRows):
    if nRows==1:
        return s
    period= 2*(nRows -1)
    lines=["" for i in range(nRows)]
    d={} # dict remainder:line
    for i in xrange(period):
        if i<nRows:
            d[i]=i
        else:
	        d[i]=period-i

    for i in xrange(len(s)):
        lines[ d[i%period] ] +=s[i]

    return "".join(lines)

    '''
    The idea is to use the remainder (index%period) to determine which line the character at the given index will be. The period is calculated first based on nRows. A dictionary with remainder:line as key:value is then created (this can also be done with a list or a tuple). Once these are done, we simply go through s, assign each character to its new line, and then combine these lines to get the converted string.

The code can be further shortened to 8 lines by using dict comprehension:
   d={i:i if i<nRows else (period-i) for i in xrange(period)}

'''
def convert(self, s, nRows):
    if nRows==1:
        return s
    period= 2*(nRows -1)
    lines=["" for i in range(nRows)]
    d={i:i if i<nRows else (period-i) for i in xrange(period)}

    for i in xrange(len(s)):
        lines[ d[i%period] ] +=s[i]

    return "".join(lines)

#solution based on regex
class Solution:
    # @return an integer
    def atoi(self, str):
        str = str.strip()
        str = re.findall('(^[\+\-0]*\d+)\D*', str)

        try:
            result = int(''.join(str))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0