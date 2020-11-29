import re
from flask import Blueprint, make_response, jsonify, request
from flask_jwt_extended import (
    jwt_required, create_access_token, get_jwt_identity)
from werkzeug.exceptions import abort
from ..models import Users
from config import Config

users_bp = Blueprint('users', __name__)

error_pwd_validation_msg = 'Password must contain at least 6 characters, including Upper/Lowercase, special characters and numbers'

# Fetches user profile details based on the username
@users_bp.route(Config.USER_PROFILE, methods=['GET'])
@jwt_required
def user_profile(username):
    if get_jwt_identity() == username:
        user = Users.objects.get(username=username)
        return make_response(jsonify({
            'name': user.name,
            'email': user.email,
            'dob': user.dob
        }), 200)
    else:
        abort(401)

# User can update their user profile based on their username
@users_bp.route(Config.UPDATE_PROFILE, methods=['PUT'])
@jwt_required
def update_profile(username):
    if get_jwt_identity() == username:
        user = Users.objects(username=username).first()
        if 'name' in request.json:
            user.update(name=request.json['name'])

        if 'email' in request.json:
            user.update(name=request.json['email'])

        if 'dob' in request.json:
            user.update(dob=request.json['dob'])

        return make_response(jsonify({
            'success': 'User profile updated successfully'
        }), 200)
    else:
        abort(401)

# User can change password based on their username
@users_bp.route(Config.CHANGE_PASSWORD, methods=['PUT'])
@jwt_required
def change_password(username):
    if get_jwt_identity() == username:
        if 'old_password' in request.json and 'new_password' in request.json:
            user = Users.objects(username=username).first()

            old_password = request.json['old_password']
            new_password = request.json['new_password']

            if old_password == user.password:
                if password_validation(new_password) == None:
                    return make_response(jsonify({"password_validation": error_pwd_validation_msg}), 400)
                user.update(password=new_password)
            else:
                return make_response(jsonify({'success': "Old password doesn't matched with the current password"}), 200)
            return make_response(jsonify({'success': 'Password changed successfully'}), 200)
        else:
            return make_response(jsonify({'error': 'Missing Fields'}), 400)
    else:
        abort(401)

# User can delete their account based on their username
@users_bp.route(Config.DELETE_ACCOUNT, methods=['DELETE'])
@jwt_required
def delete_account(username):
    if get_jwt_identity() == username:
        user = Users.objects(username=username).first()
        # Abort if no movie
        if user == None:
            abort(404)

        user.delete()
        return make_response(jsonify({
            "success": 'Account Deleted Successfully'
        }), 200)
    else:
        abort(401)

# User authenication as per their credentials
@users_bp.route(Config.SIGN_IN, methods=['POST'])
def sign_in():
    try:
        username = request.json['username']
        password = request.json['password']

        user = Users.objects.get(username=username, password=password)
        access_token = create_access_token(identity=username)

        return make_response(jsonify({
            'access_token': access_token,
            'name': user.name,
            'email': user.email,
            'dob': user.dob
        }), 200)
    except Users.DoesNotExist:
        return make_response(jsonify({
            'error': 'Incorrect Username or Password'
        }), 401)

# Create new account with the user details
@users_bp.route(Config.SIGN_UP, methods=['POST'])
def sign_up():
    try:
        username = request.json['username']
        try:
            if Users.objects.get(username=username):
                return make_response(jsonify({"username": username+' username already exists'}), 400)
        except Users.DoesNotExist:
            pass

        email = request.json['email']
        if email_validation(email) == None:
            return make_response(jsonify({"email_validation": email+' is not a valid email address'}), 400)

        password = request.json['password']
        if password_validation(password) == None:
            return make_response(jsonify({"password_validation": error_pwd_validation_msg}), 400)

        users = Users(username=username,
                      password=password,
                      name=request.json['name'],
                      email=email,
                      dob=request.json['dob'])
        users.save()
    except KeyError:
        abort(400)
    return make_response(jsonify({
        "success": 'User Created Successfully'
    }), 201)

@users_bp.errorhandler(400)
def invalid_request(error):
    return make_response(jsonify({'error': 'Invalid Request '+error}), 400)


@users_bp.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Sorry user not found'}), 404)


@users_bp.errorhandler(401)
def unauthorized(error):
    return make_response(jsonify({'error': 'Unauthorized Access'}), 401)

# Utility method to validate the password
def password_validation(password):
    pwd_regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    pwd_pattern = re.compile(pwd_regex)
    password_regex_match = re.search(pwd_pattern, password)
    return password_regex_match

# Utility method to validate the email address
def email_validation(email):
    email_regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    email_pattern = re.compile(email_regex)
    email_regex_match = re.search(email_pattern, email)
    return email_regex_match
