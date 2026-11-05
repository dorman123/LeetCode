from collections import defaultdict
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> dict:
        alerts = []
        start_pos = 0
        converted_times = list(map(lambda x: int(x[:2]) * 60 + int(x[3:]), keyTime))

        dict_of_times = defaultdict(list)

        for name, time in zip(keyName, converted_times):
            dict_of_times[name].append(time)

        for name in dict_of_times:
            uses = sorted(dict_of_times[name])
            if any(third - first <= 60 for third, first in zip(uses[2:], uses)):
                alerts.append(name)

        return sorted(alerts)


# Example Usage
keyName = ["john","john","john"]
keyTime = ["23:58","23:59","00:01"]
s = Solution()
print(s.alertNames(keyName, keyTime))
