""" testing the function in wordcount

remember the entry point of spark_context
"""

import pytest
import wordcount

@pytest.mark.usefixtures("spark_context")
def test_do_word_counts(spark_context):
    """ test the do_word_counts function, using a given spark_context
    
    Decorators:
        pytest.mark.usefixtures -- make the local spark_context fixture available to this test function by including this decorator.

    Arguments:
        spark_context {@fixture} -- obejct to holds interface to spark context
    """
    test_inputs = [
        'hello world',
        'hello beautiful world',
        'hello spark spark again'
    ]

    input_rdd = spark_context.parallelize(test_inputs, numSlices = 1)
    results = wordcount.do_word_counts(input_rdd)

    expected_results = {
        'hello': 3, 
        'world': 2, 
        'spark': 2,
        'beautiful': 1,
        'again': 1
    }

    assert expected_results == results











