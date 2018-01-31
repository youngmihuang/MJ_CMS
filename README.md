# MJ_CMS (POC)

## CMS server
web & chatbot 's content management server 

### Structure
```python
├─Demo3
│     ├──
│      adjust                    #all the images that cms server needed
│        ├── A2OFF0001.jpg
│        ├── A2OFF0002.jpg
│        ├── A2OFF0002.jpg
│        .........
│        .........
│
│     ├── Dockerfile             #dockerfile
│     ├── cms_server_v2.py       #flask server
│     ├── contentDB_ETL.py       #content raw metadata to redis
│     └── offerData_image.xlsm   #content raw metadata
│
│
├─CMS_Test                       #stress test and unit test 
│     ├── cms_test_aws.jmx       #jmeter scipt for stress testing (aws)
│     ├── cms_test_azure.jmx     #jmeter scipt for stress testing (azure)
│     ├── cms_test_gcp.jmx       #jmeter scipt for stress testing (gcp)
│     ├── cms_test_test.csv      #test data for jmeter
│     └── unittest.py            #unit test
│
└──docker-compose.yml
```

## Usage
### Demo3 
use docker to build images & container.
``` 
$ docker-compose up
```

### CMS_test
* stress test and unittest were included
* stress test: jmeter 
* [Test Document](https://hackmd.io/KwDgnA7ApgTADAQwLQCMJxUgLHAZrpBSKVAZjgBMwA2aimU6qIA=)
