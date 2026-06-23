#
# @lc app=leetcode id=2960 lang=python3
#
# [2960] Count Tested Devices After Test Operations
#

# @lc code=start
from typing import *


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested_devices = 0
        for i in range(len(batteryPercentages)):
            device_battery = batteryPercentages[i]
            if device_battery == 0:
                continue
            if device_battery > 0:
                tested_devices += 1
                for j in range(i + 1, len(batteryPercentages)):
                    batteryPercentages[j] = max(0, batteryPercentages[j] - 1)
        return tested_devices


# @lc code=end
