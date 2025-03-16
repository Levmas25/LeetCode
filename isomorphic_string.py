'''Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.'''
def isIsomorphic(s: str, t: str) -> bool:
    char_index_s = {}
    char_index_t = {}

    for i in range(len(s)):
        if s[i] not in char_index_s:
            char_index_s[s[i]] = i

        if t[i] not in char_index_t:
            char_index_t[t[i]] = i
        
        if char_index_s[s[i]] != char_index_t[t[i]]:
            return False

    return True


print(isIsomorphic("a", "a"))
print(isIsomorphic("badc", "baba"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("egg", "add"))