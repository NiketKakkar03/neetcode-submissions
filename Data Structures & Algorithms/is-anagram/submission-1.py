class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        for i in range(max(len(s),len(t))):
            try:
                a,b = s.count(s[i]),t.count(s[i])
                if a != b:
                    raise ValueError
            except:
                return False
        return True        
        
        # flag = True
        # for i in str1:
        #     try:
        #         if str1[i] == str2[i]:
        #             pass
        #         else:
        #             flag = False
        #     except:
        #         flag = False
        # return flag

        