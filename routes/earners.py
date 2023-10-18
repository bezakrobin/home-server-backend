from flask import Blueprint
from func.earners.create_earner import create_earner
from func.earners.get_earner import get_earner
from func.earners.get_all_earners import get_all_earners
from func.earners.delete_earner import delete_earner
from func.earners.update_earner import update_earner
from func.earners.disable_earner import disable_earner
from func.earners.activate_earner import activate_earner

earners_bp = Blueprint('earners', __name__)


@earners_bp.route('/create_earner', methods=['POST'])
def create_earner_route():
    return create_earner()


@earners_bp.route('/get_earner/<int:earner_id>', methods=['GET'])
def get_earner_route(earner_id):
    return get_earner(earner_id)


@earners_bp.route('/get_all_earners', methods=['GET'])
def get_all_earners_route():
    return get_all_earners()


@earners_bp.route('/delete_earner/<int:earner_id>', methods=['DELETE'])
def delete_earner_route(earner_id):
    return delete_earner(earner_id)


@earners_bp.route('/update_earner/<int:earner_id>', methods=['PUT'])
def update_earner_route(earner_id):
    return update_earner(earner_id)


@earners_bp.route('/disable_earner/<int:earner_id>', methods=['PUT'])
def disable_earner_route(earner_id):
    return disable_earner(earner_id)


@earners_bp.route('/activate_earner/<int:earner_id>', methods=['PUT'])
def activate_earner_route(earner_id):
    return activate_earner(earner_id)
