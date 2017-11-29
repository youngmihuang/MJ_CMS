FROM python:2
MAINTAINER Youngmi-huang <cyeninesky3@gmail.com>
COPY . /src
WORKDIR /src
RUN pip install -r requirements.txt
EXPOSE 6020
CMD python contentDB_ETL.py && python cms_server_v2.py

# docker build -t cms_api:1.0 .
# docker run -itd --name redis redis:latest
# docker run -itd --name cmsserver --link redis:redis cms_api:1.0
