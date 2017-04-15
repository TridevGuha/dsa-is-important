class MergeSort(object):

    def __init__(self, array):
        self.array = array

    def merge_sort(self):
        if len(self.array) <= 1:
            return self.array
        mid = len(self.array) / 2
        left = self.merge_sort(self.array[:int(mid)])
        right = self.merge_sort(self.array[int(mid):])
        return self.merge(left, right)

    def merge(self, left, right):
        if not left:
            return right
        if not right:
            return right
        if left[0] < right[0]:
            return left[0] + self.merge(left[1:], right)
        return right[0] + self.merge(left, right[1:])


array = [89, 1, 45, 0, 10, 4, 5]
ob = MergeSort(array)
print(ob.merge_sort())
