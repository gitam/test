In here we have following files:
- app.py - our api application we are testing
- crud.sqlite - our db used for testing
- test_api.py - our tests to test application api
- requirements.txt and .circleci is required so that CircleCI is run with tests on every commit

To run tests use following command line:

```python3 -m unittest test_api```

Pre-requesites for tests are **python3** and these libraries:

```pip3 install flask```

```pip3 install unittest```

```pip3 install flask_sqlalchemy```

```pip3 install flask_marshmallow```

To generate sqlite db launch python interactive shell:

```$ python3```

Use following code afterwards:

```>>> from app import db```

```>>> db.create_all()```
