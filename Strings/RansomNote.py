"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.
"""

def ransome_note(note, magazine):
	magazine_map = collections.Counter(magazine)
	for c in note:
		if c: # skip blanks
			if not magazine_map.get(c, 0): return false
			magazine_map[c] -= 1
	return True  
