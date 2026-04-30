def minWindow(s, t):
    from collections import Counter

    if not s or not t:
        return ""

    t_count = Counter(t)
    window = {}
    have = 0
    need = len(t_count)
    left = 0
    res = [-1, -1]
    res_len = float("inf")

    for right in range(len(s)):
        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in t_count and window[char] == t_count[char]:
            have += 1
        while have == need:
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = right - left + 1

            window[s[left]] -= 1
            if s[left] in t_count and window[s[left]] < t_count[s[left]]:
                have -= 1

            left += 1

    l, r = res
    return s[l:r+1] if res_len != float("inf") else ""
s = "ADOBECODEBANC"
t = "ABC"
result = minWindow(s, t)
print("Minimum Window Substring:", result)
