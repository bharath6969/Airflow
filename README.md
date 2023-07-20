#Architecture 


SQS --------> Lambda ---------->   S3   <---------Crawler<-----------  AWS GLUE  ------------->RDS(POSTGRES)
-----------------STEP1----------------  -------------------------------STEP2------------------------------

#Step1

A message is published in SQS we need to do some transformation for that we need to store the data into s3 bucket either in csv or parquet format.
To do this we need to trigger lambda functions where we work on writing data into s3 bucket 

#Step2

We are using AWS GLUE to write spark jobs and save the results in Postgres 
we are using crawler to get the schema from s3 and store it in Data Catalog 
finally i can use either glue functionality or pyspark functions for transforming the data and store it in postgres 

#In our project i need to work with images and try to test the data
The mentioned docker-compose.yaml

Lets look into this yaml file and i could see we are pulling two images localstack and for postgres

docker-compose up 

docker ps-> helps me to see if the containers are up 

docker exec -it container_id /bin/bash -> helps to work with test data 








