class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = dict()
        for str in strs:
            sort_str = "".join(sorted(str))
            if sort_str in dic:
                dic[sort_str].append(str)
            else:
                dic[sort_str] = []
                dic[sort_str].append(str)
    
        return list(dic.values())


        