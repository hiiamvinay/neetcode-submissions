class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i]+=1
            else:
                s_dict[i] =1
        for j in t:
            if j in s_dict:
                s_dict[j]-=1
            else:
                return False
        
        for i in s_dict:
            if s_dict[i]!=0:
                return False
        return True
        
        
        
        