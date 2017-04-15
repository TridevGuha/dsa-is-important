class Search(object):
    def __init__(self, array, item):
        self.array = array
        self.item = item

    def search(self):
        sorted_array = sorted(array)
        low = 0
        high = len(sorted_array) - 1
        mid = (high + low) / 2
        while low <= high:
            if sorted_array[mid] == self.item:
                return mid
            elif sorted_array[mid] < self.item:
                low = mid + 1
            else:
                high = mid - 1
        return -1
