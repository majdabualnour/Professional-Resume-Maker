
def findMedianSortedArrays( nums1: list[int], nums2: list[int]) -> float:
    pointer1 = 0
    pointer2 = 0
    results = []
    N = 0
    # print(nums1)

    while pointer1 < len(nums1) and pointer2 < len(nums2):
        N +=1 
        if nums1[pointer1] < nums2[pointer2]:
            results.append(nums1[pointer1])
            pointer1 +=1 
        else:
            
            results.append(nums2[pointer2])
            pointer2 +=1  
    results += nums1[pointer1:] 
    results += nums2[pointer2:]
    mid = len(results)//2
    # print(results)
    print(N)
    if len(results) %2 == 0: 
        
        # print(results[mid] + results[mid+1])
        # print(results[mid] , results[mid-1])
        return (results[mid] + results[mid-1])/2
    return results[mid] 


import random
nums1 = [random.randint(1,10) for x in range(10)]
nums2 = [random.randint(1,100000000) for x in range(1000)]
nums1.sort()
nums2.sort()
# print(nums2)


print(findMedianSortedArrays(nums1,nums2))

