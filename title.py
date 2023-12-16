def title(input:str):
    sentense = input.split()  
    first_char_upper = [word[0].upper() + word[1:] for word in sentense]
    return ' '.join(first_char_upper)

input_string = "F a cA fa Ac"
result = title(input_string)
print(result)
