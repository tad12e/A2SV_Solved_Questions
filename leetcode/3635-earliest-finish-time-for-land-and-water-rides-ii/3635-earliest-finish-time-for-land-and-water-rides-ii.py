from bisect import bisect_right
from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        def build(starts, durations):
            rides = sorted(zip(starts, durations))
            s = [x for x, _ in rides]
            d = [y for _, y in rides]
            n = len(rides)

            pref_min_d = [0] * n
            pref_min_d[0] = d[0]
            for i in range(1, n):
                pref_min_d[i] = min(pref_min_d[i - 1], d[i])

            INF = 10**18
            suf_min_sd = [INF] * (n + 1)
            for i in range(n - 1, -1, -1):
                suf_min_sd[i] = min(suf_min_sd[i + 1], s[i] + d[i])

            return s, pref_min_d, suf_min_sd

        water_s, water_pref_d, water_suf_sd = build(
            waterStartTime, waterDuration
        )

        land_s, land_pref_d, land_suf_sd = build(
            landStartTime, landDuration
        )

        INF = 10**18
        ans = INF

        # land -> water
        for sL, dL in zip(landStartTime, landDuration):
            A = sL + dL

            idx = bisect_right(water_s, A)
            best = INF

            if idx > 0:
                best = min(best, A + water_pref_d[idx - 1])

            best = min(best, water_suf_sd[idx])

            ans = min(ans, best)

        # water -> land
        for sW, dW in zip(waterStartTime, waterDuration):
            B = sW + dW

            idx = bisect_right(land_s, B)
            best = INF

            if idx > 0:
                best = min(best, B + land_pref_d[idx - 1])

            best = min(best, land_suf_sd[idx])

            ans = min(ans, best)

        return ans