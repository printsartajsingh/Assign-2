def count_dog_occurrences(input_string):
   
    input_string = input_string.lower()
    
    words = input_string.split()
    

    count = 0
    
    for word in words:
        if word == 'dog':
            count += 1
    
    return count

# Example usage:
input_string = "I have a dog, and my neighbor has a dog too. My dog is a friendly dog."
dog_count = count_dog_occurrences(input_string)
print("The word 'dog' appears", dog_count, "times in the input string.")