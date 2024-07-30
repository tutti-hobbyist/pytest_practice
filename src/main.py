
import time

from state import State


class Task:
    def __init__(self):
        self.state = State.START

    def process(self):
        sleep_time = 3
        self.state = State.PROCESSING
        for i in range(sleep_time):
            time.sleep(1)
            print(f"{i+1} seconds elapsed")
        self.state = State.FINISHED


def main():
    task = Task()
    print(f"Initial State: {task.state}")

    task.process()
    print(f"State after processing: {task.state}")


if __name__ == "__main__":
    main()
