"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_content = open(file_path).read()
    

    return file_content



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    # chains = { ('hi', 'there') : ['mary', 'juanita'] }

    chains = {}

    # your code goes here
    # splitting our string thats passed in .split() with whitespace
    words = text_string.split()
    # store that in a list so we can iterate. for loop?
    # tracking index using enumerate or range/len
    # as we iterate add to our markov dict. we also want to create a tuple(key) and
    for i in range(len(words)-2): # deal with edge case @ end of list using -2
        # my_dict[key] = value
        if (words[i],words[i+1]) not in chains:
            chains[(words[i],words[i+1])] = [words[i+2]]
            # append to values list if the key-value pair exists already
        else:
            chains[(words[i],words[i+1])].append(words[i+2])
            # else create the key-value pair
        
            # values.append(' the word after that') 
    # add our words to the list as the value. 
    # check out keys to see if they exist
    print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
