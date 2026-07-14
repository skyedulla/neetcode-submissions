class TimeMap:

    def __init__(self):
        self.box_of_keys = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.box_of_keys:
            if timestamp > self.box_of_keys[key][-1][0]:
                self.box_of_keys[key].append((timestamp, value))
            else:
                low = 0 
                high = len(self.box_of_keys[key]) - 1
                
                while low < high:
                    mid = (low + high + 1) // 2
                    if timestamp > self.box_of_keys[key][mid][0]:
                        high = mid - 1
                    else:
                        low = mid
                
                self.box_of_keys[key].insert(low, (timestamp, value))
        else:
            self.box_of_keys[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.box_of_keys:
            #if the timestamp is less than the first key then no key will be valid
            if timestamp >= self.box_of_keys[key][0][0]: 
                low = 0
                high = len(self.box_of_keys[key]) - 1

                while low < high:
                    mid = (low + high + 1) // 2
                    if self.box_of_keys[key][mid][0] <= timestamp:
                        low = mid
                    else:
                        high = mid - 1
                
                return self.box_of_keys[key][low][1]

            else:
                return ""
        
        else:
            return ""
        """this function will perform binary search on a set of numbers attempting to 
        find the largest value that satisfies a condition"""
