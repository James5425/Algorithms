import time

nums1 = [4,9,5, 43 ,43, 23, 321, 32,1, 43, 23,4, 234, 1, 2 ,3, 4, 5, 6 ,7, 8, 6, 54, 123 ,123,  32, 123 ,12, 32 ,12, 32,1 ,23, 2,1, 2,3, 2,1, 2,3 ,1, 23, 21, 3,2, 3,12,3]
nums2 = [9,4,9,8,4,  43, 12, 432,123, 32, 1,32, 23, 12, 3,2, 1]


def Github_copilot_verion(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    start = time.time()
    set1 = set(nums1)
    set2 = set(nums2)

    print(f"loop took {time.time() - start} seconds")
    return list(set1 & set2)


def myversion(nums1, nums2):
    start = time.time()
    nums1.sort()
    nums2.sort()

    intersection = []


    for x in nums1:

        left = 0
        right = len(nums2) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums2[mid] < x:
                left = mid + 1

            elif nums2[mid] > x:
                right = mid - 1

            else:
                intersection.append(nums2[mid])
                break
    print(f"loop took {time.time()-start} seconds")


    return intersection


print(f"my loop {myversion(nums1, nums2)}")
print(f"github loop {Github_copilot_verion(nums1, nums2)}")
