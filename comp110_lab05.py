"""
Module: comp110_lab05

Exercises from lab 05, dealing with strings and file reading.
"""

def max_wind_speed(hurricane_filename):
    """
    Finds the maximum wind speed for the hurricane.

    Parameters:
    1. hurricane_filename (type: string) - Name of the file containing the data

    Returns:
    (type: int) The maximum wind speed of the hurricane.
    """

    f = open(hurricane_filename, 'r')
    biggest = 0
    for line in f:
        vals = line.split(',')
        wind = int(vals[-2])
        if wind > biggest:
            biggest = wind
    return biggest
    #print(biggest)


def contains_word(word, review):
    """
    Determines whether the review contains the given word. 

    Note that should ignore the "casing" of letters. For example "ok" is
    considered to be contained in the review "It was an OK movie."

    Parameters:
    1. word (type: string): The word to search for.
    2. review (type: string): The review in which to search.

    Returns:
    (type: boolean) True if word is contained in the review, and false
    otherwise.
    """

    low_word = word.lower()
    low_review = review.lower()

    split_review = low_review.split(' ')

    return low_word in split_review
        
def test_max_wind_speed():
    """ Function that tests the max_wind_speed function. """
    print("Starting test of max_wind_speed")
    result_irma = max_wind_speed('irma.csv')
    if result_irma == 185:
        print('PASSED')
    else:
        print('FAILED')

    result_florence = max_wind_speed('florence.csv')
    if result_florence == 140:
        print('PASSED')
    else:
        print('FAILED')

    result_dorian = max_wind_speed('dorian.csv')
    if result_dorian == 185:
        print('PASSED')
    else:
        print('FAILED')
    
    # To Do: Call your max_wind_speed function on the irma.csv file, using an if
    # statement to indicate whether the result was correct or not.
    # Then repeat the process for the florence.csv and dorian.csv files to check
    # whether your function works for those files.

    #print("FAILED: Not implemented yet.") # remove this line when you finish the to do

    print("Done testing max_wind_speed")


def test_contains_word():
    """ Function that tests the contains_word function. """

    print("\nStarting test of contains word")

    if contains_word('Good', 'the movie was good') != True:
        print("FAILED: contains_word('ok', 'ok')")
    elif contains_word('horrible', 'The movie was Horrible') != True:
        print("FAILED: contains_word('ok', 'OK')")
    elif contains_word('no', 'knowledgeble') != False:
        print("FAILED: contains_word('ok', 'bad')")
    elif contains_word('ok', 'movie ok') != True:
        print("FAILED: contains_word('ok', 'movie ok')")
    # To Do: update the chained conditional to test all of your new test cases.
    else:
        print("All contains_word test cases passed!")


    print("Done testing contains word")


def main():
    """ Calls the tester functions in the code. """
    test_max_wind_speed()
    test_contains_word()

# Do not modify anything after this point.
if __name__ == "__main__":
    main()
