from flask import Blueprint
from func.services.create_service import create_service
from func.services.get_service import get_service
from func.services.get_all_services import get_all_services
from func.services.delete_service import delete_service
from func.services.update_service import update_service
from func.services.disable_service import disable_service
from func.services.activate_service import activate_service

services_bp = Blueprint('services', __name__)


@services_bp.route('/create_service', methods=['POST'])
def create_service_route():
    return create_service()


@services_bp.route('/get_service/<int:service_id>', methods=['GET'])
def get_service_route(service_id):
    return get_service(service_id)


@services_bp.route('/get_all_services', methods=['GET'])
def get_all_services_route():
    return get_all_services()


@services_bp.route('/delete_service/<int:service_id>', methods=['DELETE'])
def delete_service_route(service_id):
    return delete_service(service_id)


@services_bp.route('/update_service/<int:service_id>', methods=['PUT'])
def update_service_route(service_id):
    return update_service(service_id)


@services_bp.route('/disable_service/<int:service_id>', methods=['PUT'])
def disable_service_route(service_id):
    return disable_service(service_id)


@services_bp.route('/activate_service/<int:service_id>', methods=['PUT'])
def activate_service_route(service_id):
    return activate_service(service_id)
