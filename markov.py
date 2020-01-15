"""Generate Markov text from text files."""

import random
import sys


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_path)
    long_string = file.read()
    string_list = long_string.split()

    return string_list




def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    for i, word in enumerate(text_string):
        if i == len(text_string)-n+1:
            break

        # create tuple of bi-gram at each iteration:
        mark_list = []

        for index in list(range(n)):
            # print(index)
            mark_list.append(text_string[i+index])
            mark_tup = tuple(mark_list)

        
        if i == len(text_string)-n:
            break
        # store the next word that follows the bi-gram:       
        next_word = text_string[i+n]

        #in the chains dictionary, itstores an empty list as 
        # a value for each key element (bi-gram):
        chains[mark_tup] = chains.get(mark_tup, [])

        # print(mark_tup, chains[mark_tup])

        chains[mark_tup].append(next_word) # sets list to third word
        # chains[mark_tup] = [third_word]
        # for chain in chains[mark_tup].keys():
        # print(chains[mark_tup])
    # print(' ')
    # for k,v in chains.items():
    #     print(k,v)


    return chains





def make_text(chains):
    """Return text from chains."""
    key_list = list(chains.keys())
    
    #print(key_list)

    # first_word = key_list[0][0]
    # second_word = key_list[0][1]
    
    words = list(key_list[0])
    #print(words)

    current_tuple = key_list[0]

    n = len(current_tuple)

    while chains.get(current_tuple) != None:

         current_list = chains[current_tuple]
         random_word = random.choice(current_list)
         words.append(random_word)
         new_tuple= current_tuple + (random_word,)
         current_tuple = tuple(list(new_tuple)[-n:])



    return " ".join(words)



# input_path = sys.argv[1]

# Open the file and turn it into one long string


# Get a Markov chain
# chains = make_chains(input_text)

# Produce random text
#

#print(random_text)

# print(make_text(chains))

input_path = "green-eggs.txt"
# input_text = open_and_read_file(input_path)
string_list = open_and_read_file(input_path)
chains = make_chains (string_list,4)
random_text = make_text(chains)
print(random_text)