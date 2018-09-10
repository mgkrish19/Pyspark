""" def. of the wordcount function

it is just like a regular Spark application 
"""

from operator import add 

def do_word_counts(lines):
    """ count the number of words in the @lines
        
    Arguments:
        lines {spark RDD} -- a RDD object containing lines of text
    
    Returns:
        results {dict} -- a dict consisting of {word: count} pairs 
    """

    counts = (lines.flatMap(lambda x: x.split())
                   .map(lambda x: (x, 1))
                   .reduceByKey(add))
    results = {word: count for word, count in counts.collect()}
    return results