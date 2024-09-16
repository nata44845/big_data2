cd apachespark/
cd hdfs/
sudo docker-compose up -d
docker cp /home/nata44845/BigData/AB_NYC_price.csv hive-server:/
docker exec -it hive-server beeline -u jdbc:hive2://localhost:10000

CREATE TABLE AB_NYC (id int, price int) row format delimited fields terminated by ',';

LOAD DATA LOCAL INPATH '/AB_NYC_price.csv' OVERWRITE INTO TABLE AB_NYC;

select count(*) from AB_NYC;
48895


select AVG(price), VARIANCE(price) from AB_NYC;

+--------------------+---------------------+
|        _c0         |         _c1         |
+--------------------+---------------------+
| 152.7206871868289  | 240.15171391941672  |
+--------------------+---------------------+

