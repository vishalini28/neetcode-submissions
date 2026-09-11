import bisect
class TimeMap:

    def __init__(self):
        self.meta={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.meta:
            self.meta[key]=[]
        self.meta[key].append([timestamp,value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.meta:
            return ""
        arr=self.meta[key]
        idx=bisect.bisect_right(arr,[timestamp,chr(127)])
        if idx==0:
            return ""
        return arr[idx-1][1]

        
