from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)
todos = []


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        new_todo = request.form.get('todo')

        if new_todo:
            todos.append({'task': new_todo, 'completed': False})

        return redirect(url_for('home'))
    return render_template('index.html', todos=todos)


@app.route('/complete/<int:todo_index>')
def complete(todo_index):
    if 0 <= todo_index < len(todos):
        todos[todo_index]['completed'] = not todos[todo_index]['completed']
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
