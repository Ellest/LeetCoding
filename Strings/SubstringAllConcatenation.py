"""
You are given a string, s, and a list of words, words, 
that are all of the same length. Find all starting indices 
of substring(s) in s that is a concatenation of each word 
in words exactly once and without any intervening characters.

For example, given:
s: "barfoothefoobarman"
words: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

"""

def findSubstring(self, s, words):
    """
    :type s: str
    :type words: List[str]
    :rtype: List[int]
    """
    
    if not words: return []
    
    length = len(words[0])
    totalLength = length * len(words)
    indices = [] # result set
    farEast = len(s) - totalLength
    
    for start in range(length):
        left = right = start
        diff = 0
        word = s[right:right+length]
        wordMap = collections.Counter(words)
        while left <= farEast or diff == totalLength:
            if diff == totalLength or not wordMap.get(word, 0):
                if diff == totalLength: 
                    indices.append(left)
                first = s[left:left+length]
                if first not in wordMap: # this means left == right
                    right += length
                    word = s[right:right+length] # grab new word
                else:
                    wordMap[first] += 1
                left += length
            else: # window not satisfied and word count in map > 0
                wordMap[word] -= 1
                right += length 
                word = s[right:right+length] # new word
            diff = right - left # update diff each iteration
    return indices