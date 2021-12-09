def sum_numbers(*args):
    return sum(args)

def get_multiplied_amount(multiplier, *args):
    return multiplier * sum(args)

def word_concatenator(*args):
    return ' '.join(args)

def inverted_word_factory(*args):
    return ''.join(list(" ".join(args))[::-1])

def dictionary_separator(**kwargs):
    return list(kwargs.keys()), list(kwargs.values())

def dictionary_creator(*args, **kwargs):
    return None if len(args) < len(kwargs) else dict(zip(args, list(kwargs.values())))

def purchase_logger(**kwargs):
    return f"Product {kwargs['name']} costs {kwargs['price']} and was bought {kwargs['quantity']}"

def world_cup_logger(country, *args):
    list = ''
    args = sorted(args)
    for index, i in enumerate(args):
        if(index < len(args) - 2):
            list += str(i) + ", "
        elif(index == len(args) - 2):
            list += f"{str(i)} "
        else:
            list += f"e {str(i)}"
    return f"{country} - {list}"