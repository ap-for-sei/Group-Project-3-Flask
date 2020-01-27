from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

import models

boards = Blueprint('boards', 'boards')

# Index route
@boards.route('/', methods=["GET"])
@login_required
def get_all_boards():
    try:
        boards = [model_to_dict(board) for board in models.Board.select().where(models.Board.loggedUser_id == current_user.id)]
        print(boards)
        for board in boards:
            board['loggedUser'].pop('password')
        return jsonify(data=boards, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error getting the resources"})

# Create route
@boards.route('/', methods=["POST"])
@login_required
def create_board():
    try:
        payload = request.get_json()
        payload['loggedUser'] = current_user.id
        board = models.Board.create(**payload)
        print(board.__dict__)
        board_dict = model_to_dict(board)

        return jsonify(data = board_dict, status = {"code": 201, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error creating the resources"})

# Show route
@boards.route('/<id>', methods=["GET"])
def get_one_board(id):
    try:
        board = models.Board.get_by_id(id)
        print(board)
        board_dict = model_to_dict(board)
        return jsonify(data = board_dict, status={"code": 200, "message": f"Found board with id {board.id}"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error getting one resource"})

# Update route
@boards.route('/<id>', methods=["PUT"])
def update_dog(id):
    try:
        payload = request.get_json()
        payload['loggedUser'] = current_user.id

        query = models.Board.update(**payload).where(models.Board.id == id)
        query.execute()
        updated_board = model_to_dict(models.Board.get_by_id(id))
        return jsonify(data=updated_board, status={"code": 200, "message": f"Resourced updated successfully"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error updating one resource"})

# Delete route
@boards.route('/<id>', methods=["DELETE"])
def delete_board(id):
    try:
        query = models.Board.delete().where(models.Board.id == id)
        query.execute()
        return jsonify(data='Resource successfully deleted', status={"code": 200, "message": "Resource successfully deleted"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 400, "message": "Error deleting resource"})
