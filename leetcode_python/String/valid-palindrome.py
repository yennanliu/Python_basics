"""

Given a string s, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.


Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

"""

# V0 
# IDEA : string + isalpha + isalnum
class Solution(object):
    def isPalindrome(self, s):
        s_ = ""
        for i in s:
            if i.isalpha() or i.isalnum():
                s_ += i.lower()
        return s_ == s_[::-1]

# V1
# https://blog.csdn.net/xiaolewennofollow/article/details/45148577
# IDEA : STACK
def isValid(s):
    matchDict={'(':')','[':']','{':'}'}
    strLen=len(s)
    stackList=[]
    for i in range(strLen):
        if s[i] not in matchDict.keys() and len(stackList)==0:
            return False 
        elif s[i] in matchDict.keys():
            stackList.append(s[i])
        elif s[i]==matchDict[stackList[-1]]:
            stackList.pop()
        else: return False
    if len(stackList)==0:
        return True
    else: return False

# V1' 
# http://bookshadow.com/weblog/2017/09/17/leetcode-valid-parenthesis-string/
# https://blog.csdn.net/fuxuemingzhu/article/details/80680990
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        vset = set([0])
        for c in s:
            nset = set()
            if c == '*':
                for v in vset:
                    nset.add(v + 1)
                    nset.add(v)
                    if v >= 1: nset.add(v - 1)
            elif c == '(':
                for v in vset:
                    nset.add(v + 1)
            elif c == ')':
                for v in vset:
                    if v >= 1: nset.add(v - 1)
            vset = nset
        return 0 in vset

# V2 
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True

# V3 
# Time:  O(n)
# Space: O(1)
class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lower, upper = 0, 0  # keep lower bound and upper bound of '(' counts
        for c in s:
            lower += 1 if c == '(' else -1
            upper -= 1 if c == ')' else -1
            if upper < 0: break
            lower = max(lower, 0)
        return lower == 0  # range of '(' count is valid
