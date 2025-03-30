

def camel_to_snake(para):

    result = ''

    for char in para:
        if char.isupper():
            result = result + '_' + char.lower()
        else:
            result += char
    return result

camel_case = input("camelcase: name")
snake_case = camel_to_snake(camel_case)
print(snake_case)



