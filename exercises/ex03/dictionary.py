"""Practice Dictionary Functions!"""

__author__: str = "730485927"


def invert(invert_dict: dict[str, str]) -> dict[str, str]:
    """The keys and values are inverted"""
    invert_result: dict[str, str] = {}
    for key in invert_dict:
        invert_result[invert_dict[key]] = key
    return invert_result


def count(count_list: list[str]) -> dict[str, int]:
    """Counts the amount of times a value is in the input list"""
    count_dict: dict[str, int] = {}
    for key in count_list:
        if key in count_dict:
            count_dict[key] += 1
        else:
            count_dict[key] = 1
    return count_dict


def favorite_color(count_dict: dict[str, str]) -> str:
    """Returns the most popular color"""
    count_colors: dict[str, int] = {}
    for key in count_dict:
        if count_dict[key] in count_colors:
            count_colors[count_dict[key]] += 1
        else:
            count_colors[count_dict[key]] = 1
    favorite_color_result: str = ""
    most_color: int = 0
    for key in count_colors:
        if count_colors[key] > most_color:
            most_color = count_colors[key]
            favorite_color_result = key
    return favorite_color_result


def bin_len(bin_len_list: list[str]) -> dict[int, set[str]]:
    """Bins strings into a dictionary"""
    bin_len_dict: dict[int, set[str]] = {}

    for string in bin_len_list:
        string_length = len(string)
        if string_length not in bin_len_dict:
            bin_len_dict[string_length] = set()
    return bin_len_dict
