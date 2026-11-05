from typing import List
import os


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return os.path.commonprefix(strs)


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))