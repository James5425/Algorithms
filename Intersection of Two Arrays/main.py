def linear():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    both = []
    for x in nums1:
        for j in nums2:
            if x == j:
                if x not in both:
                    both.append(x)

    print(both)

