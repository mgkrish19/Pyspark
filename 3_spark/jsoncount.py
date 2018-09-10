""" def. of the json count function

which uses DataFrames API (also used in Spark SQL). This function counts the occurrences of a name in a dataframe (read from a bunch of json files)
"""

def do_json_counts(df, target_name):
    """ count of records where name = 'target_name' where name is a column in df
        
    Arguments:
        df {Spark DataFrame} -- needs to contain column "name" and its string
        target_name {string} -- the target string to search for
    
    Returns:
        count {int} -- the number of occurances of target_name in column 'name' of DataFrame 'df'
    """
    count = df.filter(df.name == target_name).count()
    return count