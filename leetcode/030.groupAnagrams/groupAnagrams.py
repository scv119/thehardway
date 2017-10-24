# leetcode: https://leetcode.com/problems/group-anagrams/description/

  def groupAnagrams(self, strs):
      """
      :type strs: List[str]
      :rtype: List[List[str]]
      """
      hashtable = {}
      for word in strs:
        tempKey = ''.join(sorted(word))
        if tempKey in hashtable:
            hashtable[tempKey].append(word)
        else:
            hashtable[tempKey] = [word]
      return hashtable.values()
