# VirtualEnv Manager

**Description**: VirtualEnv Manager is a Python script that simplifies the management of Python virtual environments within a local directory. With this script, users can create, list, activate, and install dependencies in virtual environments, making it ideal for developers who frequently switch between different Python projects.

---

## Features

- **Clear Terminal**: Clears the terminal screen for a clean start.
- **Virtual Environment Listing**: Automatically detects virtual environments within the current directory.
- **Virtual Environment Creation**: If no virtual environments are found, the script prompts the user to create one.
- **Environment Activation**: Activates a selected virtual environment for use in the current session.
- **Dependency Installation**: Installs dependencies from `requirements.txt` if found and user-approved.

## Requirements

- **Python 3.x** is required.
- **Access to a terminal or command line**.
- The script is compatible with **Windows, macOS, and Linux** operating systems.

## Setup

1. Clone or download the script into your desired project directory.
2. Ensure Python 3.x is installed and accessible in your system path.

## Usage

1. **Run the Script**:
   - Execute the script using Python from your command line:
     ```bash
     python virtualenv_manager.py
     ```

2. **Clear Terminal**:
   - The script begins by clearing your terminal screen to provide a clean slate.

3. **List or Create Virtual Environments**:
   - The script checks the current directory for any existing virtual environments. If multiple environments are found, you will be prompted to select one by entering the corresponding number.
   - If no environments are detected, you’ll be prompted to create one.

4. **Activate Virtual Environment**:
   - The selected virtual environment is then activated, ready for use in the current session.

5. **Install Requirements**:
   - If a `requirements.txt` file is found in the directory, you’ll be prompted to install the dependencies listed in it.
   - Enter “yes” or “no” based on your preference.

## Script Walkthrough

- **`clear_host()`**: Clears the terminal screen based on the operating system.
- **`print_colored(text, color)`**: Prints colored text to the terminal, enhancing user interaction.
- **`list_virtual_environments()`**: Scans the directory for virtual environments by checking for `activate` scripts in typical directories.
- **`create_virtual_environment()`**: Prompts the user to create a new virtual environment if none are found. Uses `venv` by default if no name is provided.
- **`activate_virtual_environment(env_name)`**: Attempts to activate the chosen environment by executing the activation script.
- **`install_requirements()`**: Checks for a `requirements.txt` file and installs dependencies if confirmed by the user.

## Example Workflow

```bash
# Run the script
python virtualenv_manager.py

# Follow on-screen prompts:
# - Create or select a virtual environment
# - Activate the chosen environment
# - Optionally install dependencies from requirements.txt
```

## Error Handling

- **Invalid Virtual Environment Name**: If the selected virtual environment name is invalid or the activation script is missing, an error message is displayed.
- **Dependency Installation Failure**: If any dependency fails to install, an error message will be displayed, and the process will halt.
- **Invalid User Input**: For selections and confirmations, if invalid input is provided, the script will exit with an error message.

## Troubleshooting

1. **Activation Not Persisting**: Due to limitations in subprocess calls, the environment activation may not persist in some shells. It’s recommended to activate manually if needed.
2. **Permission Errors**: If you encounter permission errors, ensure you have the necessary permissions to create and modify files in the current directory.

## Future Enhancements

- **Environment Deletion**: Add support to delete old or unused virtual environments.
- **Enhanced Dependency Management**: List installed packages and versioning within the selected environment.

---
