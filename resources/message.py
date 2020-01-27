from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

import models

messages = Blueprint('messages', 'messages')

# Index route
@messages.route('/', methods=["GET"])
@login_required
def get_all_messages():
    try:
        messages = [model_to_dict(message) for message in models.Message.select()]
        print(messages)
        for message in messages:
            message['loggedUser'].pop('password')
        return jsonify(data=messages, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error getting the resources"})

# Create route
@messages.route('/', methods=["POST"])
@login_required
def create_message():
    try:
        payload = request.get_json()
        payload['loggedUser'] = current_user.id
        print(payload, "<<<<hitting post route from React")
        massage = models.Message.create(**payload)
        print(message.__dict__)
        message_dict = model_to_dict(message)

        return jsonify(data = message_dict, status = {"code": 201, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error creating the resources"})

# Show route
@messages.route('/<id>', methods=["GET"])
def get_one_message(id):
    try:
        massage = models.Message.get_by_id(id)
        print(message)
        message_dict = model_to_dict(massage)
        return jsonify(data = message_dict, status={"code": 200, "message": f"Found massage with id {message.id}"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error getting one resource"})

# Update route
@messages.route('/<id>', methods=["PUT"])
def update_dog(id):
    try:
        payload = request.get_json()
        payload['loggedUser'] = current_user.id

        query = models.Message.update(**payload).where(models.Message.id == id)
        query.execute()
        updated_message = model_to_dict(models.Massage.get_by_id(id))
        return jsonify(data=updated_massage, status={"code": 200, "message": f"Resourced updated successfully"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error updating one resource"})

# Delete route
@messages.route('/<id>', methods=["DELETE"])
def delete_massage(id):
    try:
        query = models.Massage.delete().where(models.Massage.id == id)
        query.execute()
        return jsonify(data='Resource successfully deleted', status={"code": 200, "message": "Resource successfully deleted"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error deleting resource"})