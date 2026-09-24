class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(can):
            ships, currcan = 1, can
            for w in weights:
                if currcan - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currcan = can

                currcan -= w
            return True

        while l <= r:
            can = (l + r) // 2
            if canShip(can):
                res = min(res, can)
                r = can - 1
            else:
                l = can + 1

        return res
        