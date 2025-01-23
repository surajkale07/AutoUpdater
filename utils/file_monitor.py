import yaml
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .git_operations import sync_changes


def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)
    
class ChangeHandler(FileSystemEventHandler):
    def __init__(self, repo):
        self.repo = repo

    def on_modified(self, event):
        print(f"File modified: {event.src_path}")
        sync_changes(self.repo)

    def on_created(self, event):
        print(f"File created: {event.src_path}")
        sync_changes(self.repo)

    def on_deleted(self, event):
        print(f"File deleted: {event.src_path}")
        sync_changes(self.repo)

def start_monitoring(path, repo):

    # First, pull the latest changes from the remote repository
    print("Pulling the latest changes from the remote repository...")
    try:
        config = load_config()
        branch=config["branch"]
        sync_changes(repo, branch)  
        # Pull updates from remote before starting monitoring
        print("Successfully pulled the latest changes.")
    except Exception as e:
        print(f"Failed to pull changes: {e}")
        return  # If pulling fails, stop here


    event_handler = ChangeHandler(repo)
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=True)
    observer.start()
    print(f"Monitoring started on: {path}")
    try:
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
        print("Monitoring stopped.")
