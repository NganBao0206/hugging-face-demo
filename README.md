# hugging-face-demo

How to Run the Project
Follow these steps to set up and run the project:

Open the Flask Folder in VS Code

Open the folder containing the Flask project in Visual Studio Code.
Create a Virtual Environment

Press Ctrl+Shift+P to open the command palette.
Type and select Python: Create Environment.
Activate the Virtual Environment

Open a terminal in VS Code.
Activate the virtual environment by running the following command:
source {virtual_env_folder_name}/bin/activate

Replace {virtual_env_folder_name} with the name of your virtual environment folder. For example, if your virtual environment is named .venv, you would run source .venv/bin/activate.
Install Required Python Packages

Install all required Python packages by running the following command:
python -m pip install -r requirements.txt

Run the Flask Application

Finally, start the Flask application by running:
python -m flask run
