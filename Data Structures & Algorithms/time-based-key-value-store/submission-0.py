class TimeMap:

    def __init__(self):
        self.cache = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        vals = self.cache.get(key, [])
        
        l = 0
        r = len(vals) - 1
        while l <= r:
            mid = (l + r) // 2

            if vals[mid][0] <= timestamp:
                result = vals[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return result