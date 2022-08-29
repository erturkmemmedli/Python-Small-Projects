def heading(string):
    convert_to_list = string.split(' ')
    for i in range(len(convert_to_list)):
        if i != 0 and convert_to_list[i] in ['ON', 'IN', 'AT', 'FOR', 'OF', 'AND', 'THE', 'FROM', 'WITH', 'UNDER']:
            convert_to_list[i] = convert_to_list[i].lower()
        else:
            convert_to_list[i] = convert_to_list[i].capitalize()
    convert_to_string = (' ').join(convert_to_list)
    return convert_to_string
