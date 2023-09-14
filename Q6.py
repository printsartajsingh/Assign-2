def contains_dog(input_string):
    
    input_string = input_string.lower()
    

    return 'dog' in input_string

input_string = "I have a dog and a cat."
if contains_dog(input_string):
    print("The input string contains 'dog'.")
else:
    print("The input string does not contain 'dog'.")