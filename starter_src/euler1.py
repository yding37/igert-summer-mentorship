
def get_all_multiples(number=3, max=1000):
    """
    Return a list of all multiples of [number] up to [max]
    """
    # TOOD: fill in code:

    return None


if __name__="__main__":
    multiples = get_all_multiples(3, 1000)
    multiples.extend(get_all_multiples(5, 1000))

    print sum(multiples)


    
