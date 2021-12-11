import argparse
import pandas as pd
import time
from pyspark import SparkConf, SparkContext

parser = argparse.ArgumentParser()
parser.add_argument('--path', action='store', dest='path',
                    type=str, nargs='*', required=True)
parser.add_argument('--api', action='store', dest='api',
                    type=str, nargs='*', required=True)

args = parser.parse_args()
apis = args.api
paths = args.path

if "spark" in apis:
    conf = SparkConf().setMaster("local")
    sc = SparkContext(conf = conf)

def pandas_count_word(paths):
  
    dbs = [db.split("/")[-1] for db in paths]

    dict_res = {"Data": dbs}
    if "pandas" in apis:
        dict_res["pandas"] = []
    if "spark" in apis:
        dict_res["spark"] = []

    for i,db in enumerate(paths):
        if "pandas" in apis:
            
            start = time.time()
            data = pd.read_csv(db, sep = "\t", header= None)
            data[0] = data[0].str.lower()
            new_df = data[0].str.split(expand=True).stack().value_counts().reset_index()
            new_df.columns = ['Word', 'Frequency']
            end = time.time()
            print(f"======= pandas - {dbs[i]} - word count =======")
            print(new_df)
            exe_time = end - start
            dict_res["pandas"].append(exe_time)
        
        if "spark" in apis:
            
            start = time.time()
            lines = sc.textFile(db)
            words = lines.flatMap(lambda x: x.split())
            wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b : a + b)
            end = time.time()
            print(f"======= spark - {dbs[i]} - word count =======")
            for word in wordCounts.collect():
                print(word)
            exe_time = end - start
            dict_res["spark"].append(exe_time)
    
    return dict_res

df = pd.DataFrame(pandas_count_word(paths))

print(df.to_string(index=False))

