# **_Lab 1 _**

# Jenkins Installation

[Installing Jenkins](https://www.jenkins.io/doc/book/installing/linux/)

CREATE EXTERNAL TABLE s3_bucket_inventory(
'bucket' string,
key string,
size bigint,
last_modified_date string,
storage_class string
)
ROW FORMAT SERDE 'org. apache.hadoop.hive.serde2.OpenCSVSerde'
STORED AS INPUTFORMAT 'org.apache. hadoop.hive.ql.io.SymlinkTextInputFormat'
OUTPUTFORMAT 'org.apache.hadoop.hive.ql.io. IgnoreKeyTextOutputFormat'
LOCATION s3://inventory-fraud-archive/fraud-logs-archive/fraud-archive-inventory-config/hive/dt=2023-08-05-01-00/ ;
