class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic={'(':')','{':'}','[':']'}
        i=-1
        k=0
        n=len(s)
        if n%2 !=0 : return False
        for k in range(n):
            if s[k] in dic.keys():
                i=k
            elif (s[k]!= dic[s[i]]) or (i==-1): 
                return False
            else :  
                i -= 1
        return True
        