# CI/CD AutoUpdater Tool

This tool automatically monitors changes in a local project folder, pushes updates to a GitHub repository, and pulls updates from the remote repository. It is designed to simplify version control and automate synchronization between local and remote repositories.

## Features

- Monitors a specified directory for changes (file creation, modification, deletion).
- Automatically commits and pushes changes to a remote GitHub repository.
- Periodically fetches updates from the remote repository and applies them locally.
- Configurable repository URL, branch, and other settings via a `config.yml` file.

---

## Requirements

- Python 3.9 or higher
- Git installed and configured on your system

### Python Dependencies

- `PyYAML`
- `GitPython`
- `watchdog`

Install the dependencies using:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```
cicd_tool/
├── main.py                 # Entry point of the application
├── config.yaml             # Configuration file for the tool
├── utils/
│   ├── git_operations.py   # Git-related operations
│   ├── file_monitor.py     # Folder monitoring logic
│   ├── webhook_handler.py  # Webhook handling logic
│   └── logger.py           # Logging utility
├── requirements.txt        # Required Python packages
└── README.md               # Project documentation
```

---

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/ci-cd-tool.git
cd ci-cd-tool
```

### 2. Configure the Tool

Update the `config.yaml` file with your repository details:

```yaml
repo_url: "https://github.com/your-username/your-repo.git"
repo_path: "path/to/your/local/repo"
branch: "main"
```

- `repo_url`: URL of your remote GitHub repository.
- `repo_path`: Path to your local repository directory.
- `branch`: The branch to sync with (default is `main`).

### 3. Set Up Git Authentication

Ensure that Git is configured for authentication using one of the following methods:

#### a. Personal Access Token (Recommended)

Generate a [Personal Access Token](https://github.com/settings/tokens) and configure it in your Git credentials manager.

#### b. SSH Keys

Set up SSH keys for authentication. Refer to the [GitHub SSH documentation](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) for instructions.

### 4. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

---

## Running the Tool

### 1. Start the Tool

Run the tool using:

```bash
python main.py
```

This will:

- Clone the repository (if not already cloned).
- Fetch updates from the remote repository.
- Start monitoring the local directory for changes.

### 2. Stop Monitoring

To stop monitoring, press `Ctrl+C` in the terminal.

---

## Example Workflow

1. **Local Changes**:

   - Make changes to the files in the specified directory.
   - The tool will detect changes, commit them, and push them to the remote repository.

2. **Remote Changes**:

   - If changes are made in the remote repository, the tool will automatically pull and apply them locally.

---

## Logs

Logs are printed to the console, showing:

- Detected changes (file creation, modification, deletion).
- Push and pull operations.
- Any errors encountered during execution.

---

## Contribution

Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

