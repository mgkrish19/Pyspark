""" tests the jsoncount function

we need to create a HiveContext fixture so that we can read in json files
"""

import pytest 
import jsoncount

# @pytest.mark.usefixtures("spark_context", "hive_context")
# def test_do_json_count(spark_context, hive_context):
#     """ test the json file counting app
    
#     Decorators:
#         pytest.mark.usefixtures -- enable the context for spark and hive
    
#     Arguments:
#         spark_context {SparkContext} -- interface to spark fixture
#         hive_context {HiveContext} -- interface to hive fixture
#     """
#     test_input = [
#         {'name': 'vikas'},
#         {'name': 'vikas'},
#         {'name': 'john'},
#         {'name': 'jane'},
#     ]

#     input_rdd = spark_context.parallelize(test_input, 1)
#     df = hive_context.read.json(input_rdd)
    
#     assert 2 == jsoncount.do_json_counts(df, target_name = 'vikas')
#     assert 1 == jsoncount.do_json_counts(df, target_name = 'john')
#     assert 1 == jsoncount.do_json_counts(df, target_name = 'jane')
#     assert 0 == jsoncount.do_json_counts(df, target_name = 'alice')

#     print ("test_do_json_count finished with SUCCESS")

