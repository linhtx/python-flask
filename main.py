
from flask import Flask
from google.cloud import datastore

app = Flask(__name__)
project_id = 'python-flask-tokyo-15482'

# import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "15482-5682fbe0bf33.json"

@app.route("/")
def home():
    return "home"

@app.route("/users", methods=['POST'])
def add_user():
    # Instantiates a client
    datastore_client = datastore.Client(project_id)

    # The kind for the new entity
    kind = 'User'
    # The name/ID for the new entity
    name = 'user_id'
    # The Cloud Datastore key for the new entity
    task_key = datastore_client.key(kind, name)

    # Prepares the new entity
    task = datastore.Entity(key=task_key)
    task['email'] = 'test@yopmail.com'
    task['country_code'] = 100000

    # Saves the entity
    datastore_client.put(task)

    return task.key
    
if __name__ == '__main__':
    app.run(port = 80, debug = True)
    
