import yaml
from utils.git_operations import init_repo
from utils.file_monitor import start_monitoring
from utils.webhook_handler import app, secret
from utils.logger import setup_logger

logger = setup_logger()

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    config = load_config()
    repo = init_repo(config["local_repo_path"], config["repository_url"])
    secret = config["webhook_secret"]

    # Start file monitoring
    start_monitoring(config["local_repo_path"], repo)

    # Start Flask server for webhooks
    app.run(host="0.0.0.0", port=5000)
