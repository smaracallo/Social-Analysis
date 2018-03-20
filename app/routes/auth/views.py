import requests
from requests_oauthlib import OAuth1
from flask import Blueprint, request, make_response, jsonify, current_app
from flask.views import MethodView

# from project.server import bcrypt, db
import os
from os.path import join, dirname
from dotenv import load_dotenv
from app.models.user_model import User

dotenv_path = join(dirname(__file__), '../../.env')
load_dotenv(dotenv_path)

auth_blueprint = Blueprint('auth', __name__)

class RegisterAPI(MethodView):
    """
    User Registration Resource
    """

    def post(self):
        # get the post data
        responseObject = {}
        post_data = request.get_json()
        # check if user already exists
        user = User.query.filter_by(email=post_data.get('email')).first()
        if not user:
            try:
                user = User(
                    email=post_data.get('email'),
                    password=post_data.get('password')
                )
                # insert the user
                db.session.add(user)
                db.session.commit()
                # generate the auth token
                auth_token = user.encode_auth_token(user.id)
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                    'auth_token': auth_token.decode()
                }
                return make_response(jsonify(responseObject)), 201
            except Exception as e:
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occurred. Please try again.'
                }
                return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
        return make_response(jsonify(responseObject)), 202


class LoginAPI(MethodView):
    """
    User Login Resource
    """
    def post(self):
        # get the post data
        responseObject = {}
        # post_data = request.get_json()
        try:
            # fetch the user data
            user = User.query.filter_by(
                email=post_data.get('email')
            ).first()
            if user and bcrypt.check_password_hash(
                user.password, post_data.get('password')
            ):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    responseObject = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'auth_token': auth_token.decode()
                    }
                    return make_response(jsonify(responseObject)), 200
            else:
                responseObject = {
                    'status': 'fail',
                    'message': 'User does not exist.'
                }
                return make_response(jsonify(responseObject)), 404
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
        return make_response(jsonify(responseObject)), 500


class UserAPI(MethodView):
    """
    User Resource
    """
    def get(self):
        responseObject = {}
        # get the auth token
        auth_header = request.headers.get('Authorization')
        if auth_header:
            try:
                auth_token = auth_header.split(" ")[1]
            except IndexError:
                responseObject = {
                    'status': 'fail',
                    'message': 'Bearer token malformed.'
                }
                return make_response(jsonify(responseObject)), 401
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                user = User.query.filter_by(id=resp).first()
                responseObject = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'admin': user.admin,
                        'registered_on': user.registered_on
                    }
                }
                return make_response(jsonify(responseObject)), 200
            responseObject = {
                'status': 'fail',
                'message': resp
            }
            return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
        return make_response(jsonify(responseObject)), 401


class LogoutAPI(MethodView):
    """
    Logout Resource
    """
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                blacklist_token = BlacklistToken(token=auth_token)
                try:
                    # insert the token
                    db.session.add(blacklist_token)
                    db.session.commit()
                    responseObject = {
                        'status': 'success',
                        'message': 'Successfully logged out.'
                    }
                    return make_response(jsonify(responseObject)), 200
                except Exception as e:
                    responseObject = {
                        'status': 'fail',
                        'message': e
                    }
                    return make_response(jsonify(responseObject)), 200
            else:
                responseObject = {
                    'status': 'fail',
                    'message': resp
                }
                return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
        return make_response(jsonify(responseObject)), 403

class AuthMeApi(MethodView):
    """
    Logout Resource
    """
    def get(self):
        responseObject = {}

        return make_response(jsonify(responseObject)), 200

class AuthTwitterReverseApi(MethodView):
    """
    Logout Resource
    """
    def post(self):
        # Post to twitter
        # twitter_response = requests.post(
        #     'https://api.twitter.com/oauth/request_token',

        # )
        current_app.logger.info("this is a test!!!")
        twitter_oauth = OAuth1(os.environ.get('CONSUMER_KEY'),
            client_secret=os.environ.get('CONSUMER_SECRET'),
        )
        r = requests.post(url='https://api.twitter.com/oauth/request_token',
            auth=twitter_oauth)
        # Send response back
        current_app.logger.info("r!!!")
        current_app.logger.info(r)

        responseObject = {}
        # user = User(email='foobar@example.com').save()
        return make_response(jsonify(responseObject)), 200

class AuthTwitterApi(MethodView):
    """
    Logout Resource
    """
    def post(self):
        responseObject = {}
        # user = User(email='foobar@example.com')
        return make_response(jsonify(responseObject)), 200

class HealthCheckApi(MethodView):
    """
    Health Check API 
    """
    def get(self):
        responseObject = {'message': 'Health Check Complete'}
        return make_response(jsonify(responseObject)), 200

# define the API resources
# registration_view = RegisterAPI.as_view('register_api')
# login_view = LoginAPI.as_view('login_api')
# user_view = UserAPI.as_view('user_api')
# logout_view = LogoutAPI.as_view('logout_api')

# '/health-check'
# '/auth/twitter/reverse'
# '/auth/twitter'
# '/auth/me'

health_check_view = HealthCheckApi.as_view('healh_check_api')
auth_twitter_reverse_view = AuthTwitterReverseApi.as_view('auth_twitter_reverse_api')
auth_twitter_view = AuthTwitterApi.as_view('auth_twitter_api')
auth_me_view = AuthMeApi.as_view('auth_me_api')
# add Rules for API Endpoints
# auth_blueprint.add_url_rule(
#     '/auth/register',
#     view_func=registration_view,
#     methods=['POST']
# )
# auth_blueprint.add_url_rule(
#     '/auth/login',
#     view_func=login_view,
#     methods=['POST']
# )
# auth_blueprint.add_url_rule(
#     '/auth/status',
#     view_func=user_view,
#     methods=['GET']
# )
# auth_blueprint.add_url_rule(
#     '/auth/logout',
#     view_func=logout_view,
#     methods=['POST']
# )
auth_blueprint.add_url_rule(
    '/api/v1/health-check',
    view_func=health_check_view,
    methods=['GET']
)
auth_blueprint.add_url_rule(
    '/api/v1/auth/twitter/reverse',
    view_func=auth_twitter_reverse_view,
    methods=['POST']
)
auth_blueprint.add_url_rule(
    '/api/v1/auth/twitter',
    view_func=auth_twitter_view,
    methods=['POST']
)
auth_blueprint.add_url_rule(
    '/api/v1/auth/me',
    view_func=auth_me_view,
    methods=['GET']
)
auth_blueprint.add_url_rule(
    '/',
    view_func=lambda: 'foobar',
    methods=['GET']
)