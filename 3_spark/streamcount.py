""" def. of streaming word count

Spark streaming’s key abstraction is a discretized stream or a DStream, which is basically a sequence of RDDs. Here is a streaming version of our word counting example that operates on a DStream and returns a stream of counts.
"""

from operator import add

def do_streaming_word_counts(lines):
    """ count the number of words in a dstream of lines (stream of RDDs)

    Arguments:
        lines {DStream} -- a stream of RDD objects

    Returns:
        counts_stream {a stream of ???} -- 
    """
    counts_stream = (lines.flatMap(lambda x: x.split())
                          .map(lambda x: (x, 1))
                          .reduceByKey(add)) 
    return counts_stream