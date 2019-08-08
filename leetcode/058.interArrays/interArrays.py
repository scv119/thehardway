# leetcode: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
# leetcode: https://leetcode.com/problems/intersection-of-two-arrays/description/

1. intersection-of-two-arrays
def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashtable = {}
        res = []
        for i in nums1:
            hashtable[i] = 1
        for i in nums2:
            if i in hashtable and hashtable[i] != 0:
                res.append(i)
                hashtable[i] = 0
        return res

def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
        return list(set(res))
2. intersection-of-two-arrays-ii

def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashtable = {}
        res = []
        for i in nums1:
            if i in hashtable:
                hashtable[i] += 1
            else:
                hashtable[i] = 1
        for j in nums2:
            if j in hashtable and hashtable[j] != 0:
                res.append(j)
                hashtable[j] -= 1
        return res

def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
        return res
