from flask import Blueprint
from func.tasks.create_task import create_task
from func.tasks.get_task import get_task
from func.tasks.get_all_tasks import get_all_tasks
from func.tasks.delete_task import delete_task
from func.tasks.update_task import update_task
from func.tasks.disable_task import disable_task
from func.tasks.activate_task import activate_task

tasks_bp = Blueprint('tasks', __name__)


@tasks_bp.route('/create_task', methods=['POST'])
def create_earner_route():
    return create_task()


@tasks_bp.route('/get_task/<int:task_id>', methods=['GET'])
def get_earner_route(task_id):
    return get_task(task_id)


@tasks_bp.route('/get_all_earners', methods=['GET'])
def get_all_earners_route():
    return get_all_tasks()


@tasks_bp.route('/delete_earner/<int:task_id>', methods=['DELETE'])
def delete_earner_route(task_id):
    return delete_task(task_id)


@tasks_bp.route('/update_earner/<int:task_id>', methods=['PUT'])
def update_earner_route(task_id):
    return update_task(task_id)


@tasks_bp.route('/disable_earner/<int:task_id>', methods=['PUT'])
def disable_earner_route(task_id):
    return disable_task(task_id)


@tasks_bp.route('/activate_earner/<int:task_id>', methods=['PUT'])
def activate_earner_route(task_id):
    return activate_task(task_id)
