# WI machine learning microservice
---

### Start app with docker
#### Prerequisites
* Os: Linux (can run without container)
* MongoDB
* Sentry
* Flask / Restplus

#### Start app for development
* Copy .env.example => .env
* Edit mapping port, or environment if need
* Run
```bash
$ pipenv install
$ pipenv sync -d
$ flask run
```
* Open http://localhost:5000/api/v1/docs . Enjoy!
* For testing
```bash
$ pytest
```

#### Deployment
* Copy .env.example => .env
* Edit mapping port, or environment if need
* Run
```bash
$ pipenv install
$ gunicorn -c etc/gunicorn.conf.py main:app
```

#### Viewing the app
Open the following url on your browser to view swagger documentation http://127.0.0.1:5000/api/v1/docs

### Structures application folder
* etc: chứa các file config
* wipm thư mục code service
    * api: chứa các định nghĩa api
        * _requests: định nghĩa cấu trúc các request theo openapi
        * _responses: định nghĩa cấu trúc các response theo openapi
	* services: chứa các hàm chức năng
* tests: thư mục chứa các test case



### Resource
* Flask - python micro web framework [http://flask.pocoo.org/](http://flask.pocoo.org/)
* Flask-Restplus - extension of flask for implement restful api [https://flask-restplus.readthedocs.io/en/stable/](https://flask-restplus.readthedocs.io/en/stable/)
* Pytest - python testing framework [https://docs.pytest.org/en/latest/](https://docs.pytest.org/en/latest/)
* mongoengine - python ORMs database framework for Mongo [http://mongoengine.org/](http://mongoengine.org/)
* GridFS in MongoDB for store large binary files - [https://www.mongodb.com/blog/post/storing-large-objects-and-files-in-mongodb](https://www.mongodb.com/blog/post/storing-large-objects-and-files-in-mongodb)
