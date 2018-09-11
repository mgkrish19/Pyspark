* conftest (common entry point for all tests)
* SparkContext
* HiveContext
* StreamingContext
* solve network issue => .set("spark.driver.host", "localhost")), or alternatively, do sudo hostname -s 127.0.0.1
* request.addfinalizer(close_sc)
* @pytest.mark.usefixtures
* hive read json files
