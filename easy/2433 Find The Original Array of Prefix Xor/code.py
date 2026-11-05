class Solution:
    def findArray(self, pref):
        arr = [pref[0]]

        for i in range(1, len(pref)):
            arr.append(pref[i] ^ pref[i - 1])

        return arr

s = Solution()
print(s.findArray([5,2,0,3,1]))



