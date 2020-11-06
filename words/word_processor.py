from functools import reduce


def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    """
    Converts a sentence to a list of words.
    :param text: A sentence with punctuation spaces between words.
    :return: a list of all words in lower case
    and punctuation removed.
    """
    
    punctuation = [",",".","?",";",":"]
    word_list = "".join([letter for letter in text if letter not in punctuation])
    word_list = split(" ", word_list.lower())
    return list(filter(lambda word: word != "", word_list))


def words_longer_than(length, text):
    """
    Converts a sentence to a list of words with len(word) larger than length.
    :param length: int for words larger than length.
    :param text: A sentence with punctuation spaces between words.
    :return: a list of all words in lower case that len is larger than length
    with punctuation removed.
    """

    word_list = convert_to_word_list(text)
    return list(filter(lambda word: len(word) > length, word_list))


def words_lengths_map(text):
    """
    Converts a sentence to a list of len(word) creates dict with count of 
    each length occurance.
    :param text: A sentence with punctuation spaces between words.
    :return: a dictionary with value for each occurance of key or length of word.
    """

    length_list = list(map(lambda word: len(word), convert_to_word_list(text)))
    return {k: length_list.count(k) for k in length_list}


def letters_count_map(text):
    """
    Converts a sentence to a dict with value of each occurance of 
    letter of the alphabet.
    :param text: A sentence with punctuation spaces between words.
    :return: a dictionary with value for each occurance of key or length of letter.
    """

    alpha = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    word_list = "".join(convert_to_word_list(text))
    return {k: word_list.count(k) for k in alpha}


def most_used_character(text):
    """
    Returns letter with highest occurance in a sentence.
    :param text: A sentence with punctuation spaces between words.
    :return: a str of the caracter with highest occurance.
    """
    
    if not text:
        return None
    else:
        word_dict = letters_count_map(text)
        largest = reduce(lambda x,y: x if (word_dict[x] > word_dict[y]) else y, word_dict)
        return largest


