def linear_search(list_of_env:list,key:str) -> bool:
    """
    This function will search if key is present in the list
    args:
    list : list type
    key : str type
    """
    is_found = False
    for env in list_of_env:
        if env == key:
            is_found = True

    return is_found
