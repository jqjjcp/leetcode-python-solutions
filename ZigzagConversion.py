'''Problems description:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility) 
P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows: 
string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"
/*n=numRows
Δ=2n-2    1                           2n-1                         4n-3
Δ=        2                     2n-2  2n                    4n-4   4n-2
Δ=        3               2n-3        2n+1              4n-5       .
Δ=        .           .               .               .            .
Δ=        .       n+2                 .           3n               .
Δ=        n-1 n+1                     3n-3    3n-1                 5n-5
Δ=2n-2    n                           3n-2                         5n-4
*/


'''


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)

   #another solution:
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
 
'''The idea is to use the remainder (index%period) to determine which line the character at the given index will be. The period is calculated first based on nRows. A dictionary with remainder:line as key:value is then created (this can also be done with a list or a tuple). Once these are done, we simply go through s, assign each character to its new line, and then combine these lines to get the converted string.

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

