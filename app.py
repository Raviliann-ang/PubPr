from flask import Flask, render_template, request, jsonify
from database import init_db, search_by_tags, add_literature
import backup

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query', '').strip()
    if query:
        results = search_by_tags(query)
        return jsonify(results)
    return jsonify([])

@app.route('/add', methods=['POST'])
def add_book():
    title = request.form.get('title', '').strip()
    author = request.form.get('author', '').strip()
    genre = request.form.get('genre', '').strip()
    main_character = request.form.get('main_character', '').strip()
    romance_line = request.form.get('romance_line', '').strip()
    description = request.form.get('description', '').strip()

    if title and author and genre and main_character and romance_line and description:
        add_literature(title, author, genre, main_character, romance_line, description)
        return jsonify({'success': True, 'message': 'Книга добавлена успешно!'})

    return jsonify({'success': False, 'message': 'Заполните все обязательные поля!'})


@app.route('/create-backup', methods=['POST'])
def create_manual_backup():
    if request.method != 'POST':
        return jsonify({'error': 'Метод не поддерживается'}), 405

    try:
        success = backup.create_backup()
        if success:
            return jsonify({'status': 'success', 'message': 'Резервная копия создана'})
        else:
            return jsonify({'status': 'error', 'message': 'Ошибка при создании бэкапа'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    backup_thread = backup.start_backup_scheduler()
    app.run(debug=True)