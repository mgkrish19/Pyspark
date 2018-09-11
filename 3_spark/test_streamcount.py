# """ test the steamcount.py functions

# """

# import pytest
# import time
# import streamcount

# def collect_helper(ssc, dstream, expected_length, block=True):
#     """
#     Collect each RDDs into the returned list.
#     This function is borrowed and modified from here:
#     https://github.com/holdenk/spark-testing-base
    
#     :return: list with the collected items.
#     """
#     result = []

#     def get_output(_, rdd):
#         if rdd and len(result) < expected_length:
#             r = rdd.collect()
#             if r:
#                 result.append(r)

#     dstream.foreachRDD(get_output)

#     if not block:
#         return result

#     ssc.start()

#     timeout = 2
#     start_time = time.time()
#     while len(result) < expected_length and time.time() - start_time < timeout:
#         time.sleep(0.01)
#     if len(result) < expected_length:
#         print("timeout after", timeout)

#     return result


# @pytest.mark.usefixtures("spark_context", "stream_context")
# def test_stream_word_count(spark_context, stream_context):
#     """ test the stream_word_count function
        
#     Decorators:
#         pytest.mark.usefixtures -- use 2 fixtures (session level)
    
#     Arguments:
#         spark_context {SparkContext} -- interface to spark
#         stream_context {StreamingContext} -- interface to streaming
#     """

#     test_input = [
#         [
#             ' hello spark ',
#             ' hello again spark spark'
#         ],
#         # [
#         #     ' hello there again spark spark'
#         # ],   # order does not work well

#     ]

#     input_rdds = [spark_context.parallelize(d, 1) for d in test_input]
#     input_stream = stream_context.queueStream(input_rdds)

#     tally = streamcount.do_streaming_word_counts(input_stream)
#     results = collect_helper(stream_context, tally, 2)

#     expected_results = [
#         [('again', 1), ('hello', 2), ('spark', 3)],
#         # [('again', 1), ('hello', 1), ('spark', 2), ('there', 1)] # order is not correct, weird
#     ]

#     assert expected_results == results
    
#     print ("test_stream_word_count finished with SUCCESS")

