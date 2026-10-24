
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
                          arriveBob: str, leaveBob: str) -> int:

        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

        def toDays(date):
            month = int(date[:2])
            day = int(date[3:])
            return sum(days[:month - 1]) + day

        start = max(toDays(arriveAlice), toDays(arriveBob))
        end = min(toDays(leaveAlice), toDays(leaveBob))

        return max(0, end - start + 1)
