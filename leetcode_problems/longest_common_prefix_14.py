def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for words in strs[1:]:
        while not words.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


if __name__ == "__main__":
    test_strs = ["flower", "flow", "flight"]
    print(longest_common_prefix(test_strs))  # Output: "fl"
