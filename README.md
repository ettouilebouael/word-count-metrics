# word-count-metrics 
Outils big data - Master 2 SEP

Ouael ETTOUILEB et Jacob Dembele

## Description
Ce code compare le temps d'éxécution entre spark et pandas d'une fonction de comptage de mots dans différents jeux de données.

## Requirements
* Python 3.6+
* Java 8
* Spark 3.2.0
* PySpark 3.2.0
* Pandas
* Linux

## Pour tester sur linux
```sh
1 - Intaller pyspark
pip install pyspark

2 - Cloner le dépot github
git clone https://github.com/ettouilebouael/word-count-metrics.git

3- Accèder au dossier du code
cd word-count-metrics

4- Executer le code
spark-submit  run.py --path <liste des chemins des jeux de données> --api <liste des API à tester>

Exemple:
spark-submit run.py --path 1M.data 10.data --api pandas spark
```
## Screenshot


![alt text](https://github.com/ettouilebouael/word-count-metrics/blob/fd27b46d9a9cd43c8e575bb921d897b3f890910e/imgs/Capture%20d%E2%80%99e%CC%81cran%202021-12-11%20a%CC%80%2009.33.01.png)
