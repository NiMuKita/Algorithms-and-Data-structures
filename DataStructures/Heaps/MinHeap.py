class MinHeap:

    def __init__(self, array: list):
        self.h = array
        self.size = len(array)

    @staticmethod
    def parent(i: int) -> int:
        return (i - 1) // 2

    @staticmethod
    def left(i: int) -> int:
        return (2 * i) + 1

    @staticmethod
    def right(i: int) -> int:
        return (2 * i) + 2

    def sift_up(self, i: int):
        while (i > 0) and (self.h[self.parent(i)] > self.h[i]):
            self.h[self.parent(i)], self.h[i] = self.h[i], self.h[self.parent(i)]
            i = self.parent(i)

    def sift_down(self, i: int):
        max_index = i

        left = self.left(i)
        if left < self.size and self.h[left] < self.h[max_index]:
            max_index = left

        right = self.right(i)
        if right < self.size and self.h[right] < self.h[max_index]:
            max_index = right

        if i != max_index:
            self.h[i], self.h[max_index] = self.h[max_index], self.h[i]
            self.sift_down(max_index)

    def build(self) -> list:
        """
        Build heap from list and return list with heap structure.
        """

        for i in range((self.size - 1) // 2, -1, -1):
            self.sift_down(i)

        return self.h


def main():
    my_list = [7, 6, 5, 4, 3, 2]
    min_heap = MinHeap(array=my_list).build()
    print(min_heap)


if __name__ == '__main__':
    main()
