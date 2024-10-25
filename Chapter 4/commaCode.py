# Take a list value and return a string with all items separated by a comma and a space
spam = ['apples', 'bananas', 'tofu', 'cats']

# Build the list as an argument
def stringify(my_list):
    if len(my_list) == 0: 
        return ''
    elif len(my_list) == 1:
        return my_list[0] # Return the single item if the list has one element
    else:
        result = ', '.join(my_list[:-1]) # Join all items except the last one with ', '
        result += ', and ' + my_list[-1] # Add the last item with ' and ' before it
        return result
        
def main(): # Main program 
    list_string = stringify(spam)
    print(list_string)

main()