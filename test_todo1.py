import pytest
import todo
import json
@pytest.fixture(autouse=True )
def reset_tasks():
    """Reset tasks before every test"""
    todo.tasks = []
    
    
    
#test adding a task
def test_add_task(monkeypatch):
    monkeypatch.setattr("builtins.input",lambda _:"STUDY PYTHON")
    monkeypatch.setattr(todo, "save_task", lambda: None)
    
    todo.add_task()
    
    assert len(todo.tasks) == 1
    assert todo.tasks[0] == {
        "task": "STUDY PYTHON",
        "done":False 
    }
    
#test adding a empty task
def test_add_empty_task(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "   ")
    
    todo.add_task()
    
    assert len(todo.tasks) == 0
    
    
#test viewing task
def test_view_task(capsys):
    todo.tasks = [
        {"task": "STUDY PYTHON", "done":False }
    ]
    
    todo.view_task()
    
    captured = capsys.readouterr()
    assert "STUDY PYTHON" in captured.out
    assert "✘" in captured.out
    
    
#test viewing an empty task list
def test_view_empty_task(capsys):
    todo.view_task()
    
    
    captured = capsys.readouterr()
    assert "no tasks yet!" in captured.out
    
    
#test marking a task as done
def test_mark_done(monkeypatch):
    todo.tasks = [
        {"task": "STUDY PYTHON", "done": False }
    ]
    
    monkeypatch.setattr("builtins.input", lambda _: "1")
    monkeypatch.setattr(todo, "save_tasks", lambda: None)
    
    todo.mark_done()
    
    assert todo.tasks[0]["done"] is True
    
    
#test invalid task number when marking done
def test_mark_done_invalid_number(monkeypatch, capsys):
    todo.tasks = [
        {"task": "STUDY PYTHON", "done": False }
        ]
    
    monkeypatch.setattr("builtins.input", lambda _: "5")
    
    todo.mark_done()
    
    
    captured  = capsys.readouterr()
    assert "Invalid number" in captured.out
    assert todo.tasks[0]["done"] is False
    
    
#test invalid input when marking done
def test_mark_done_invalid_input(monkeypatch, capsys):
    todo.tasks = [
        {"task": "STUDY PYTHON", "done": False }
    ]
    
    
    monkeypatch.setattr("builtins.input", lambda _: "abc")
    
    todo.mark_done()
    
    captured = capsys.readouterr()
    assert "Please enter a valid number." in captured.out
    
    
#test deleting a task
def test_delete_task(monkeypatch):
    todo.tasks = [
        {"task": "STUDY PYTHON", "done": False }
    ]
    
    monkeypatch.setattr("builtins.input", lambda _: "1")
    monkeypatch.setattr(todo, "save_tasks", lambda: None )
    
    
    todo.delete_task()
    
    assert len(todo.tasks) == 0
    
    
    
#test deleting an invalid task number
def test_delete_invalid_number(monkeypatch, capsys):
    todo.tasks = [
        {"task": "STUDY PYTHON", "done": False }
    ]
    
    monkeypatch.setattr("builtins.input", lambda _: "5")
    
    todo.delete_task()
    
    captured = capsys.readouterr()
    assert "Invalid number!" in captured.out
    assert len(todo.tasks) == 1
    
    
#test deleting with invalid input
def test_delete_invalid_input(monkeypatch, capsys):
    todo.tasks = [
        {"task": "STUDY PYTHON", "done": False }    
    ]
    
    monkeypatch.setattr("builtins.input", lambda _: "abc")
    
    todo.delete_task()
    
    captured = capsys.readouterr()
    assert "Please enter a valid number." in captured.out
    assert len(todo.tasks) == 1
    
    
#test saving task
def test_save_tasks(tmp_path, monkeypatch):
    file_path = tmp_path / "tasks.json"
    
    monkeypatch.setattr(todo, "open", open, raising=False )
    monkeypatch.chdir(tmp_path)
    
    todo.tasks = [
         {"task": "STUDY PYTHON", "done": False }   
    ]
    
    todo.save_tasks()
    
    with open(file_path, "r") as file:
        saved_tasks = json.load(file)
        
        
    assert saved_tasks == todo.tasks
    
    
#test loading tasks
def test_load_tasks(tmp_path, monkeypatch):
    file_path = tmp_path / "tasks.json"
    
    with open(file_path, "w") as file:
        json.dump(
            [{"task": "STUDY PYTHON", "done": False }],
            file
            
        )
        
    monkeypatch.chdir(tmp_path)
    
    todo.load_tasks()
    
    
    assert len(todo.tasks) == 1
    assert todo.tasks[0]["task"] == "STUDY PYTHON"
    
    
#TEST loading when file does not exist
def test_load_tasks_file_not_found(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    
    todo.load_tasks()
    
    assert todo.tasks == []
    
                        
    