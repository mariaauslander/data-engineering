## Data Engineering Project: Streaming and Querying Game-Related Events 
### Using Tools Such as Kafka, Spark, HDFS/Parquet, and Apache Bench

This is a simple data engineering project that utilizes multiple tools to emulate game-related events. It consists of the following tasks:

- Instrumenting API server to log events to Kafka

- Creating a data pipeline to catch the following events: filter
  select event types from Kafka using Spark streaming, landing these event types into HDFS/parquet to make them
  available for analysis using Presto

- Using Apache Bench to generate test data for the pipeline

- Producing an analytics report where a description of the pipeline and basic analysis is provided 

The notebook to presents queries and findings. It's understood that events in this pipeline are _generated_ events which make
them hard to connect to _actual_ business decisions, but the project is meant to demonstrate the ability to stand up a data pipeline and query results accordingly.
