from pony.orm import Database, PrimaryKey, Required, db_session, commit, select
from datetime import datetime

DB = Database()


class Task(DB.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    description = Required(str)
    status = Required(str)
    due_date = Required(datetime)


DB.bind(provider="sqlite", filename="database.sqlite", create_db=True)
DB.generate_mapping(create_tables=True)


def add_task(name, description, status, due_date):
    try:
        with db_session:
            Task(name=name, description=description, status=status, due_date=due_date)
            commit()
            return {"response": "Success"}
    except Exception as e:
        raise Exception("An error occurred while adding a task: {}".format(str(e)))


def edit_task(task_id, name, description, status, due_date):
    try:
        with db_session:
            task = Task.get(id=task_id)
            if not task:
                return {"response": "Fail"}
            setattr(task, 'name', name)
            setattr(task, 'description', description)
            setattr(task, 'status', status)
            setattr(task, 'due_date', due_date)
            commit()
            return {"response": "Success"}
    except Exception as e:
        raise Exception("An error occurred while editing a task: {}".format(str(e)))


def remove_task(task_id):
    try:
        with db_session:
            task = Task.get(id=task_id)
            if not task:
                return {"response": "Fail"}
            task.delete()
            commit()
            return {"response": "Success"}
    except Exception as e:
        raise Exception("An error occurred while removing a task: {}".format(str(e)))


def get_tasks(status=None, due_date=None):
    try:
        with db_session:
            tasks = Task.select()

            if status:
                tasks = tasks.filter(status=status)
            if due_date:
                tasks = tasks.filter(due_date=due_date)

            tasks_list = [task.to_dict() for task in tasks]
            return tasks_list
    except Exception as e:
        raise Exception("An error occurred while retrieving tasks: {}".format(str(e)))
