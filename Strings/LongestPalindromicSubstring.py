"""

"""

def longestPalindrome(s):
"""
:type s: str
:rtype: str
"""

"""
Manacher's Algorithm
1. continue until right hits end
    - at this point there can't be any longer palindromes to the right of center
2. set i as center if i + size[i] == right (of current palindrome)
    - this defines a valid prefix 
3. if i + size[i] > right, set size[i] to right-i 
    - if palindrome at i expands beyond the current palindrome window
      it's not gauranteed to be a palindrome
4. if i > right -> set i as new center and try expand. 

"""

if not s: return s
modified = '#'.join('${}^'.format(s))
size = [0 for i in modified]
longest = start = center = right = 0
for i in range(1, len(size)-1):
    
    mirror = size[2 * center - i]
    size[i] = min(max(right - i, 0), mirror)
    
    if i + mirror == right or i > right:
        while modified[i-size[i]-1] == modified[i+size[i]+1]:
            size[i] += 1
            
    if i + size[i] > right:
        if size[i] > longest:
            longest, start = size[i], i
        center, right = i, i + size[i]
        
    #if right >= len(size)-2: break

return s[(start-longest)//2 : (start+longest) // 2]