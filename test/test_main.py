
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import Task
from state import State


task = Task()

def test_check_initial_state():
    assert task.state == State.START

def test_check_after_process_state():
    task.process()
    assert task.state == State.FINISHED
