def longestsubstring(str):
    max_length = 0
    curr_length = 0
    substring_set = set()
    start = 0
    end = 0
    while end < len(str):
        if str[end] not in substring_set:
            substring_set.add(str[end])
            curr_length += 1
            end += 1
        else:
            max_length = max(curr_length, max_length)
            substring_set.remove(str[start])
            curr_length -= 1
            start += 1

    return max_length

print(longestsubstring("abcabcbb"))
print(longestsubstring("bbbbb"))
print(longestsubstring("pwwkew"))