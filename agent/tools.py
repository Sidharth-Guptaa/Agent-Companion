def get_current_tasks():
    return ["Buy groceries", "Call Mom", "Review proposal"]

def get_tools():
    return {
        "task_manager": get_current_tasks
    }