# Flask To-Do List

This is a simple To-Do list web application built with Flask and Python. The app allows users to:
- Add tasks to their to-do list.
- Mark tasks as completed.
- Undo the completion of tasks.
- View a dynamically updated list of tasks.

## Features
- Add new to-dos.
- Toggle the completion status of a to-do (strike-out or fade).
- Simple, clean interface with easy-to-use buttons for completing or undoing tasks.

## Requirements
- Python 3.x
- Flask

## Setup and Installation

1. **Clone the repository**:

   First, clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/todo-flask-app.git
   cd todo-flask-app
    ```

2. **Install dependencies**:

   It is recommended to create a virtual environment before installing the dependencies. If you are using `venv`, you can do the following:

    ```commandline
    python3 -m venv venv
    source venv/bin/activate  # For Windows, use `venv\Scripts\activate`   
   ```

    Then, install the required Python packages

3. Run the app:

    After installing the dependencies, you can run the Flask application:
    ```commandline
   python todo.py
   ```

    The application will be accessible at http://127.0.0.1:5000/ in your web browser.

4. View the App:

    Open a web browser and go to http://127.0.0.1:5000/ to use the To-Do list app.

## File Structure
```text
todo-flask-app/
├── app.py                # The main Flask application file
├── templates/
│   └── index.html        # HTML template for the to-do list
├── requirements.txt      # Required Python packages (Flask)
└── README.md             # This README file
```

## How It Works
1. The app allows users to add new to-dos by typing in the input field and submitting the form.
2. Each to-do item is displayed in a list, with buttons to mark them as "Complete" or "Undo".
3. When a user marks a to-do as complete, the task is visually struck out (or faded, depending on the CSS).
4. The user can also undo the completion, which restores the task's original appearance.

## Technologies Used
* **Python**: Programming language used for the app.
* **Flask**: A lightweight web framework for Python to build the web application.
* **HTML/CSS**: For the structure and styling of the web pages.

## License
This project is licensed under the MIT License.

## Contributions
Feel free to fork the repository, create an issue, or submit a pull request if you'd like to contribute. If you encounter any bugs or have suggestions for new features, please open an issue.