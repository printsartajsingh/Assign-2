list1 = ["M", "na", "i", "She"]
list2 = ["y", "me", "s", "lly"]


result = [word1 + word2 for word1, word2 in zip(list1, list2)]
print(result)