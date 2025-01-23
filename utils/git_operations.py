import yaml
from git import Repo, GitCommandError


def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)


def init_repo(local_path, remote_url):
    try:
        return Repo(local_path)
    except:
        print("Cloning repository...")
        return Repo.clone_from(remote_url, local_path)

def sync_changes(repo, branch=None):
    try:
        if not branch:
            config = load_config()  # Load the config from the YAML file
            branch = config['branch']

        print(f"Pulling latest changes from branch {branch}...")
        origin = repo.remotes.origin
        # Pull latest changes from the specific branch
        origin.pull(branch)
        print(f"Successfully pulled changes from {branch}.")

        # Stage all changes
        print("Staging changes...")
        repo.git.add(A=True)

        # Commit the changes
        print("Committing changes...")
        repo.index.commit(f"Automated commit to {branch} by CI/CD tool")

        # Push the changes to the specific branch
        print(f"Pushing changes to {branch} branch...")
        origin.push(refspec=f"HEAD:{branch}")  # Push the current HEAD to the specified branch
        print(f"Changes pushed successfully to {branch} branch.")

    except GitCommandError as e:
        print(f"Error during Git operation: {e}")


def pull_changes(repo):
    try:
        repo.remotes.origin.pull()
        print("Changes pulled from remote repository.")
    except GitCommandError as e:
        print(f"Error during pull: {e}")
