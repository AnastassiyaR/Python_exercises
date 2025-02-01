def findMedianSortedArrays(nums1, nums2):
    num = sorted(nums1 + nums2)
    print(num)
    if len(num) % 2 != 0:
        result = num[int(len(num) / 2)]
    else:
        numb = num[int(len(num) / 2) - 1: int(len(num) / 2) + 1]
        result = sum(numb) / 2

    return result

print(findMedianSortedArrays([1, 3], [2]))  # Output: 2.00000
print(findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.50000