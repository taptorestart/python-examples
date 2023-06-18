from algorithms.bubble_sort import sort


def test_sort():
    arr = [2, 3, 1, 5, 4]
    sorted_arr = sort(arr)
    assert sorted_arr == [1, 2, 3, 4, 5]
