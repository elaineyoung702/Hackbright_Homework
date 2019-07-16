"""Print out all the melons in our inventory."""


from young_melons import melons_dict


def print_melon(melons_dict):
    """Print each melon with corresponding attribute information."""

    for melon in melons_dict:
        print(melon.upper())
        for key in melons_dict[melon]:
            print(f'{key}: {melons_dict[melon][key]}')


    ### Solution was created based off of original melon_info.py format
    # for melon in melons_dict:
    #     if melons_dict[melon]["seedlessness"] == True:
    #         have_or_have_not = "have"
    #     elif melons_dict[melon]["seedlessness"] == False:
    #         have_or_have_not = "do not have"
    #     print (f'{melon}s {have_or_have_not} seeds and are ${melons_dict[melon]["price"]}')


print_melon(melons_dict)