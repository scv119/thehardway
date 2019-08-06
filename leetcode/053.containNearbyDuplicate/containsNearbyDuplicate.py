# leetcode: https://leetcode.com/problems/contains-duplicate-ii/description/

def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # time: O(n), space O(n)
        hashtable = {}
        for i in xrange(len(nums)):
            if nums[i] not in hashtable:
                hashtable[nums[i]] = [i]
            else:
                if i - hashtable[nums[i]][-1] <= k:
                    return True
                else:
                    hashtable[nums[i]].append(i)
        return False

def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # time O(n^2), space O(1)
        for i in xrange(len(nums)):
            for j in xrange(len(nums)):
                if nums[i] == nums[j] and i - j != 0 and abs(i - j) <= k:
                    return True
        return False
