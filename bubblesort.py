class BubbleSort(object):
    def __init__(self, array):
        self.array = array

    def bubble_sort(self):
        for num in range(len(self.array) - 1, 0, -1):
            for i in range(num):
                if self.array[i] > self.array[i + 1]:
                    self.array[i], self.array[i + 1] = self.array[i + 1], self.array[i]
        return self.array

mylist = [10, 2, 67, 4, 6, 1]
ob = BubbleSort(mylist)
print(ob.bubble_sort())
