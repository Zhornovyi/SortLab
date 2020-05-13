def partition(xs, start, end):
    follower = leader = start
    while leader < end:
        if xs[leader] <= xs[end]:
            xs[follower], xs[leader] = xs[leader], xs[follower]
            follower += 1
        leader += 1
    xs[follower], xs[end] = xs[end], xs[follower]
    return follower

def _quicksort(xs, start, end, part_size):
    if start >= end:
        return
    p = partition(xs, start, end)
    _quicksort(xs, start, p - 1, part_size)
    if(p<=part_size):
        _quicksort(xs, p + 1, end, part_size)

def quicksort(xs, part_size):
    _quicksort(xs, 0, len(xs) - 1, part_size)
# def main():
#     arr =[
#         2, 10, 24, 2, 10, 11, 27,
#         4, 2, 4, 28, 16, 9, 8,
#         28, 10, 13, 24, 22, 28,
#         0, 13, 27, 13, 3, 23,
#         18, 22, 8, 8]
#
#     n = len(arr)
#
#     quicksort(arr,10)
#     print(arr)
#
#
# if __name__ == '__main__':
#     main()