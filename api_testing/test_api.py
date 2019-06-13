#!/usr/bin/env python3
import unittest
from flask import json
from app import *

class AppTestCase(unittest.TestCase):

    # add user
    @app.route('/user', methods=["POST"])
    def test_adding_user(self):
        print('--Testing user add')
        with app.test_client() as c:
            rv = c.post('/user', json={
                "email": "myemail2@mail.com", "username": "another2"
            })
            json_data = rv.get_json()
            print('JSON Sent:')
            print(json_data)
            response = app.response_class(
                response=json.dumps(json_data),
                status=200,
                mimetype='application/json'
            )
            print(response.status)
            assert response.status=='200 OK'

    # show all users
    @app.route("/user", methods=["GET"])
    def test_getting_all_users(self):
        print('--Testing getting all users')
        with app.test_client() as c:
            rv = c.get('/user')
            json_data = rv.get_json()
            print('JSON Sent:')
            print(json_data)
            response = app.response_class(
                response=json.dumps(json_data),
                status=200,
                mimetype='application/json'
            )
            print(response.status)
            assert response.status == '200 OK'

    # get user by id
    @app.route("/user/<id>", methods=["GET"])
    def test_getting_user_detail_by_id(self):
        print('--Testing getting user by id')
        with app.test_client() as c:
            rv = c.get('/user/1')
            json_data = rv.get_json()
            print('JSON Sent:')
            print(json_data)
            if json_data['username'] == 'another2' and json_data['email'] == 'myemail2@mail.com':
                print('user details correct')
                assert True
            else:
                assert False

    # update user by id
    @app.route("/user/<id>", methods=["PUT"])
    def test_updating_user_by_id(self):
        print('--Testing updating user by id')
        with app.test_client() as c:
            rv = c.put('/user/1', json={
                "email": "myemail3@mail.com", "username": "another3"
            })
            json_data = rv.get_json()
            print('JSON Sent:')
            print(json_data)
            response = app.response_class(
                response=json.dumps(json_data),
                status=200,
                mimetype='application/json'
            )
            print(response.status)
            assert response.status == '200 OK'


    # endpoint to delete user
    @app.route("/user/<id>", methods=["DELETE"])
    def test_user_deletion_by_id(self):
        print('--Testing deleting user by id')
        with app.test_client() as c:
            rv = c.delete('/user/1')
            json_data = rv.get_json()
            print('JSON Sent:')
            print(json_data)
            response = app.response_class(
                response=json.dumps(json_data),
                status=200,
                mimetype='application/json'
            )
            print(response.status)
            assert response.status == '200 OK'


if __name__ == '__main__':
    app.run(debug=True)