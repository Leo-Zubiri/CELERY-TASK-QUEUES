from celery import Celery
from time import sleep

app = Celery('tasks', broker='redis://localhost:6379', backend='redis://localhost:6379')

@app.task
def my_task(x):
    print("Hello, World!")
    sleep(5)
    print(f"Processed value: {x}")
    return x