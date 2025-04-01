# Write a function to find the longest common prefix string amongst an array of strings.
def longest_common_prefix(strs: list[str]) -> str:
    pref = min(strs, key=len)
    end = len(pref)

    while pref:
        if all(x.startswith(pref[:end]) for x in strs):
            return pref[:end]
        end -= 1

    return pref


print(longest_common_prefix(["flower","flow","flight"]))
print(longest_common_prefix(["dog","racecar","car"]))