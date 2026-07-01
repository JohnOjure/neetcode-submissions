class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t): return False

        # # if set(list(s)) == set(list(t)): return True
        # # return False
        s_list, t_list = list(s), list(t)
        s_list.sort(), t_list.sort()

        if s_list == t_list: return True
        return False

