import os
import subprocess
import sys

def clear_host():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def print_colored(text, color):
    """
    Prints text in the specified color.
    :param text: The text to print.
    :param color: The color code.
    """
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'reset': '\033[0m'
    }
    print(f"{colors.get(color, colors['reset'])}{text}{colors['reset']}")

def list_virtual_environments():
    """
    Lists all virtual environments in the current directory.
    """
    envs = []
    for item in os.listdir():
        if os.path.isdir(item) and (os.path.exists(os.path.join(item, 'bin', 'activate')) or os.path.exists(os.path.join(item, 'Scripts', 'activate'))):
            envs.append(item)
    return envs

def create_virtual_environment():
    """
    Creates a new virtual environment in the current directory.
    """
    env_name = input("No virtual environments found. Please provide a name for the new virtual environment (default: 'venv'): ").strip()
    if not env_name:
        env_name = 'venv'
    try:
        print_colored(f"Creating a new virtual environment '{env_name}'...", 'yellow')
        subprocess.check_call([sys.executable, '-m', 'venv', env_name])
        print_colored(f"Virtual environment '{env_name}' created successfully.", 'green')
    except subprocess.CalledProcessError:
        print_colored(f"Failed to create virtual environment '{env_name}'. Please try manually.", 'red')
        sys.exit(1)

def activate_virtual_environment(env_name):
    """
    Activates the selected virtual environment.
    :param env_name: Name of the virtual environment to activate.
    """
    activate_script = os.path.join(env_name, 'bin', 'activate') if os.name != 'nt' else os.path.join(env_name, 'Scripts', 'activate')
    if os.path.exists(activate_script):
        print_colored(f"Switching to virtual environment '{env_name}'...", 'yellow')
        command = f"source {activate_script}" if os.name != 'nt' else activate_script
        subprocess.call(command, shell=True, executable="/bin/bash" if os.name != 'nt' else None)
    else:
        print_colored(f"Activation script not found for environment '{env_name}'.", 'red')
        sys.exit(1)

def install_requirements():
    """
    Installs packages from requirements.txt if it exists and user confirms.
    """
    requirements_file = "requirements.txt"
    if os.path.exists(requirements_file):
        user_input = input(f"Found 'requirements.txt'. Do you want to install the dependencies? (yes/no): ").strip().lower()
        if user_input in ["yes", "y"]:
            print_colored("Yes", 'green')
        elif user_input in ["no", "n"]:
            print_colored("No", 'red')
        if user_input in ["yes", "y"]:
            try:
                print_colored(f"Installing dependencies from {requirements_file}...", 'yellow')
                subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", requirements_file])
                print_colored("Dependencies installed successfully.", 'green')
            except subprocess.CalledProcessError:
                print_colored("Failed to install dependencies. Please check the requirements file and try again.", 'red')
    else:
        print_colored("No requirements.txt found.", 'yellow')

if _name_ == "__main__":
    # Clear the terminal screen
    clear_host()

    # Step 1: List virtual environments in the current directory
    virtual_envs = list_virtual_environments()

    # Step 2: Check if there are multiple or no virtual environments
    if not virtual_envs:
        # No virtual environment found, create one
        create_virtual_environment()
        selected_env = 'venv'
    elif len(virtual_envs) == 1:
        # If only one environment is found, activate it
        selected_env = virtual_envs[0]
    else:
        # If multiple environments are found, prompt the user to select one
        print_colored("Multiple virtual environments found:", 'yellow')
        for idx, env in enumerate(virtual_envs):
            print_colored(f"{idx + 1}. {env}", 'blue')

        try:
            choice = int(input("Select the virtual environment to activate (enter the number): ").strip())
            if 1 <= choice <= len(virtual_envs):
                selected_env = virtual_envs[choice - 1]
            else:
                print_colored("Invalid selection. Exiting.", 'red')
                sys.exit(1)
        except ValueError:
            print_colored("Invalid input. Please enter a number. Exiting.", 'red')
            sys.exit(1)

    # Step 3: Activate the selected virtual environment
    activate_virtual_environment(selected_env)

    # Step 4: Check for requirements.txt and install dependencies based on user input
    install_requirements()
