https://leetcode.com/problems/group-anagrams/discuss/

Group Anagrams
This question is to group all anagrams in a given list.
Most straight forward thought is to use a hash table to store the keys. Then check following words. If found anagram, then append it to the list. Otherwise store this new key into hash table and create a list for this key.

But regarding to how to create and store keys, there are some ideas:
1. What I got at first is to split the word and store it in a list. Then sort the list and store it in dict as a key. Pseudocode is as below:
for word in wordList:
    key = split the word (use list() function)
    sort this list key.sort()
    if this list is in hashtable:
        hashtable[key].append(word)
    else:
        hashtable[key] = [word] 
return hashtable.values()

But the problem is that dict in python do not accept list as a key as it can be updated through index. So I have to combine them into a string again, where we can use join function
Besides, it is not necessary to list(word) as when I use sorted() function, it will be split into a list.
a = ''.join(key)

time complexity: O(mnlgn) m is the length of wordList, n is the length of the word
memory complexity: O(mn)


2. the second idea is from discussion area, it uses prime number as multiplication of prime numbers are unique. So if we use prime numbers we can save time for sorting. The time complexity is O(mn), m is the length of wordList, n is the length of the word. But multiplication of prime numbers will be a problem as it will trigger some overflow problems.  




