"""run unit test on Spark-related functions using pytest

Follow tutorial: https://engblog.nextdoor.com/unit-testing-apache-spark-with-py-test-3b8970dc013b

This module includes pytest fixtures and util. functions that can be reused across tests. The filename has to be "conftest.py"
"""

# make sure that env variables are set correctly, run the following two lines if pyspark cannot be imported
# import findspark
# findspark.init()

import logging
import pytest

from pyspark import SparkConf
from pyspark import SparkContext
from pyspark import HiveContext
from pyspark.streaming import StreamingContext


def quiet_py4j():
    """ turn down spark logging for the test context
    """
    logger = logging.getLogger('py4j')
    logger.setLevel(logging.WARN)


@pytest.fixture(scope='session') 
def spark_context(request):
    """ the fixture to create a Spark Context for organizing stuff
        
    Decorators:
        pytest.fixture -- it is slow to create spark context, so reuse it for all the test sessions, use the session scope

    Arguments:
        request {pytest.FixtureRequest} -- it can add the teardown function for this fixture to properly close the spark context that was created. 
    
    Returns: 
        sc -- the constructed SparkContext object
    """
    appName = "pytest-pyspark-local-wordcount"
    conf = (SparkConf().setMaster("local[2]")
                       .setAppName(appName)
                       .set("spark.driver.host", "localhost")) # avoid the network shiftting issue, hostname = 127.0.0.1
    sc = SparkContext(conf = conf)
    print ("Creating SparkContext for app: %s" % appName)

    def close_sc():
        print ("Terminating SparkContext for app: %s" % appName)
        sc.stop()

    request.addfinalizer(close_sc)
    quiet_py4j()
    return sc 


@pytest.fixture(scope='session')
def hive_context(spark_context):
    """ the fixture to interface with hive context
        
    Decorators:
        pytest.fixture -- on a session scale
    
    Arguments:
        spark_context {SparkContext} -- enable proper init. from SparkContext
    
    Returns: 
        hc -- the constructed HiveContext object
    """
    hc = HiveContext(spark_context)
    return hc 


@pytest.fixture(scope='session')
def stream_context(spark_context):
    """ create fixture of spark streaming context
        
    Decorators:
        pytest.fixture -- session scope
    
    Arguments:
        spark_context {SparkContext} -- interface to sc

    Returns:
        ssc -- the construced StreamingContext object
    """
    ssc = StreamingContext(spark_context, 1)
    return ssc 









