# MJ_CMS

## CMS server
web & chatbot 's content management server 
```python
├─Demo3
│     ├──
│      offerImage
│        ├── A2OFF0001.jpg
│        ├── A2OFF0002.jpg
│        ├── A2OFF0002.jpg
│        .........
│        .........
│
│     ├── Dockerfile
│     ├── cms_server_v2.py
│     ├── contentDB_ETL.py
│     └── offerData_image.xlsm
│  
└──docker-compose.yml
```

## Usage
### Demo3資料夾
* Dockerfile
* offerImage 資料夾包含所有圖檔(`.jpg`)  -> for web & chatbot channel 使用


### Docker-compose.yml
* 已測試能成功啟動服務: docker-compose up

### Testing
* [Test Document](https://hackmd.io/KwDgnA7ApgTADAQwLQCMJxUgLHAZrpBSKVAZjgBMwA2aimU6qIA=)
