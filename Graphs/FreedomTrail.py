"""
In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal 
dial called the "Freedom Trail Ring", and use the dial to spell a specific keyword in order 
to open the door.

Given a string ring, which represents the code engraved on the outer ring and another string 
key, which represents the keyword needs to be spelled. You need to find the minimum number 
of steps in order to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at 12:00 direction. You need to spell 
all the characters in the string key one by one by rotating the ring clockwise or anticlockwise 
to make each character of the string key aligned at 12:00 direction and then by pressing the 
center button. 

At the stage of rotating the ring to spell the key character key[i]:

1. You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. 
The final purpose of the rotation is to align one of the string ring's characters at the 
12:00 direction, where this character must equal to the character key[i].

2. If the character key[i] has been aligned at the 12:00 direction, you need to press 
the center button to spell, which also counts as 1 step. After the pressing, you could 
begin to spell the next character in the key (next stage), otherwise, you've finished 
all the spelling.
"""

def dp(depth, place, end, key, pos, cache):
    if depth == len(key): 
        return 0
    pair = (depth, place)
    if pair not in cache:
        cache[pair] = float('inf')
        nxt = depth + 1
        for p in pos[key[depth]]:
            val = p + end - place if place > p else place + end - p
            steps = min(abs(place - p), val + 1) # +1 for cross over
            cache[pair] = min(cache[pair], steps + dp(nxt, p, end, key, pos, cache))
    return cache[pair]

def findRotateSteps(self, ring, key):
    """
    :type ring: str
    :type key: str
    :rtype: int
    """        
   
    if not ring or not key: return 0
    pos = collections.defaultdict(list)
    for i, c in enumerate(ring):
        pos[c].append(i)
    return dp(int(ring[0] == key[0]), 0, len(ring)-1, key, pos, {}) + len(key)