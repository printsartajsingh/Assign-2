seq = ['soup', 'dog', 'salad', 'cat', 'great']

# Use filter() with a lambda function to filter words starting with 's'
filtered_words = list(filter(lambda word: word.startswith('s'), seq))

print(filtered_words)