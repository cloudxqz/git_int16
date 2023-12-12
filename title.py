def title(input:str):
    sentense = input.split()  
    first_char_upper = [word.lower().capitalize() for word in sentense] 
    result = ' '.join(first_char_upper) 
    return result

input_string = "F a cA fa Ac"
result = title(input_string)
print(result)
