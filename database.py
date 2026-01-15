import sqlite3
import os


def get_db_connection():
    conn = sqlite3.connect('literature.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    if not os.path.exists('literature.db'):
        print("Создание новой базы данных...")

    conn = get_db_connection()
    try:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS literature (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                genre TEXT NOT NULL,
                main_character TEXT NOT NULL,
                romance_line TEXT NOT NULL,
                description TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        print("База данных инициализирована успешно!")

        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM literature')
        count = cursor.fetchone()[0]

        if count == 0:
            add_sample_data()
            print("Добавлены тестовые данные")
        backup.backup_on_startup()

    except Exception as e:
        print(f"Ошибка при инициализации базы данных: {e}")
    finally:
        conn.close()


def add_sample_data():
    sample_books = [
        (
            'война и мир',
            'лев толстой',
            'исторический роман семейная сага военная проза',
            'главный герой: мужчина',
            'романтическая линия: присутствует',
            'эпическое повествование о жизни русского общества во время войны с наполеоном'
        ),
        (
            'преступление и наказание',
            'федор достоевский',
            'психологический роман философский роман детектив',
            'главный герой: мужчина',
            'романтическая линия: присутствует',
            'история бывшего студента родиона раскольникова совершившего убийство'
        ),
        (
            'анна каренина',
            'лев толстой',
            'психологический роман семейный роман реализм',
            'главный герой: женщина',
            'романтическая линия: присутствует',
            'трагическая история замужней женщины влюбившейся в молодого офицера'
        ),
        (
            'мастер и маргарита',
            'михаил булгаков',
            'фантастика сатира философский роман',
            'главные герои: мужчина и женщина',
            'романтическая линия: присутствует',
            'мистическая история о визите дьявола в москву 1930-х годов'
        ),
        (
            'отцы и дети',
            'иван тургенев',
            'социально-психологический роман реализм',
            'главный герой: мужчина',
            'романтическая линия: присутствует',
            'конфликт между поколениями в лице аристократа павла кирсанова'
        ),
        (
            'портрет дориана грея',
            'оскар уайльд',
            'психологический роман философский роман готическая литература',
            'главный герой: мужчина',
            'романтическая линия: присутствует',
            'художник бэзил холлуорд пишет портрет молодого и прекрасного дориана грея'
        ),
        (
            'великий гэтсби',
            'фрэнсис скотт фицджеральд',
            'социальный роман трагедия реализм',
            'главный герой: мужчина',
            'романтическая линия: присутствует',
            'история загадочного миллионера джея гэтсби и его трагической любви'
        ),
        (
            '1984',
            'джордж оруэлл',
            'антиутопия политический роман научная фантастика',
            'главный герой: мужчина',
            'романтическая линия: присутствует',
            'мрачное видение тоталитарного будущего где большой брат следит за каждым'
        ),
        (
            'унесенные ветром',
            'маргарет митчелл',
            'исторический роман любовный роман драма',
            'главный герой: женщина',
            'романтическая линия: присутствует',
            'эпическая сага о скарлетт охара сильной женщине'
        ),
        (
            'гордость и предубеждение',
            'джейн остин',
            'любовный роман социальный роман комедия нравов',
            'главный герой: женщина',
            'романтическая линия: присутствует',
            'история элизабет беннет и мистера дарси'
        ),
        (
            'над пропастью во ржи',
            'джером дэвид сэлинджер',
            'психологический роман роман воспитания реализм',
            'главный герой: мужчина',
            'романтическая линия: присутствует',
            'история подростка холдена колфилда который борется с лицемерием'
        ),
        (
            'три товарища',
            'эрих мария ремарк',
            'психологический роман любовный роман военная проза',
            'главный герой: мужчина',
            'романтическая линия: присутствует',
            'история трех друзей вернувшихся с первой мировой войны'
        ),
        (
            'маленькие женщины',
            'луиза мэй олкотт',
            'семейный роман роман воспитания реализм',
            'главный герой: женщина',
            'романтическая линия: присутствует',
            'трогательная история взросления четырех сестер марч'
        ),
        (
            'джейн эйр',
            'шарлотта бронте',
            'любовный роман готический роман роман воспитания',
            'главный герой: женщина',
            'романтическая линия: присутствует',
            'история сильной и независимой гувернантки джейн эйр'
        ),
        (
            'старик и море',
            'эрнест хемингуэй',
            'психологическая повесть притча реализм',
            'главный герой: мужчина',
            'романтическая линия: отсутствует',
            'история старика сантьяго который выходит в море'
        ),
        (
            'триумфальная арка',
            'эрих мария ремарк',
            'психологический роман любовный роман исторический роман',
            'главный герой: мужчина',
            'романтическая линия: присутствует',
            'история немецкого хирурга-эмигранта в париже'
        ),
        (
            'поющие в терновнике',
            'колин маккалоу',
            'семейная сага любовный роман исторический роман',
            'главный герой: женщина',
            'романтическая линия: присутствует',
            'многоплановая сага о семье клири проживающей в австралии'
        ),
        (
            'граф монте-кристо',
            'александр дюма',
            'приключенческий роман исторический роман месть',
            'главный герой: мужчина',
            'романтическая линия: присутствует',
            'история эдмона дантеса несправедливо осужденного'
        ),
        (
            'тень ветра',
            'карлос руис сафон',
            'мистический роман детектив исторический роман',
            'главный герой: мужчина',
            'романтическая линия: присутствует',
            'загадочная история о книге и ее авторе'
        ),
        (
            'атлант расправил плечи',
            'айн рэнд',
            'философский роман антиутопия социальный роман',
            'главный герой: женщина',
            'романтическая линия: присутствует',
            'монументальное произведение о борьбе талантливых индивидуалистов'
        ),
        (
            'шантарам',
            'грегори дэвид робертс',
            'приключенческий роман автобиографический роман психологический роман',
            'главный герой: мужчина',
            'романтическая линия: присутствует',
            'основанная на реальных событиях история беглого австралийского заключенного'
        ),
        (
            'гарри поттер и философский камень',
            'джоан роулинг',
            'фэнтези роман воспитания приключения',
            'главный герой: мужчина',
            'романтическая линия: отсутствует',
            'первая книга о юном волшебнике гарри поттере'
        )
    ]

    conn = get_db_connection()
    try:
        for book in sample_books:
            conn.execute(
                'INSERT INTO literature (title, author, genre, main_character, romance_line, description) VALUES (?, ?, ?, ?, ?, ?)',
                book
            )
        conn.commit()
        print(f"Добавлено {len(sample_books)} книг в базу данных")
    except Exception as e:
        print(f"Ошибка при добавлении тестовых данных: {e}")
    finally:
        conn.close()


def search_by_tags(tags):
    conn = get_db_connection()
    try:
        tags_lower = tags.lower().strip()
        cleaned_tags = [tag.strip() for tag in tags_lower.split() if tag.strip()]

        if not cleaned_tags:
            return []

        cursor = conn.cursor()
        cursor.execute('SELECT * FROM literature ORDER BY title')
        all_books = cursor.fetchall()

        filtered_books = []

        for row in all_books:
            try:
                title = row['title']
                author = row['author']
                genre = row['genre']
                main_character = row['main_character']
                romance_line = row['romance_line']
                description = row['description']
            except (KeyError, TypeError):
                title = row[1] if len(row) > 1 else ''
                author = row[2] if len(row) > 2 else ''
                genre = row[3] if len(row) > 3 else ''
                main_character = row[4] if len(row) > 4 else ''
                romance_line = row[5] if len(row) > 5 else ''
                description = row[6] if len(row) > 6 else ''

            book_text = f"{title} {author} {genre} {main_character} {romance_line} {description}"

            matches_all_tags = True
            for tag in cleaned_tags:
                if tag not in book_text:
                    matches_all_tags = False
                    break

            if matches_all_tags:
                filtered_books.append({
                    'id': row['id'] if 'id' in row else row[0],
                    'title': title.title(),
                    'author': author.title(),
                    'genre': ' '.join(word.title() for word in genre.split()),
                    'main_character': main_character.title(),
                    'romance_line': romance_line.title(),
                    'description': description.capitalize()
                })

        return filtered_books

    except Exception as e:
        print(f"Ошибка при поиске по тегам: {e}")
        import traceback
        traceback.print_exc()
        return []
    finally:
        conn.close()


def add_literature(title, author, genre, main_character, romance_line, description):
    conn = get_db_connection()
    try:
        title_lower = title.lower()
        author_lower = author.lower()
        genre_lower = genre.lower().replace(',', ' ')
        main_character_lower = main_character.lower()
        romance_line_lower = romance_line.lower()
        description_lower = description.lower()

        conn.execute('''
            INSERT INTO literature (title, author, genre, main_character, romance_line, description)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (title_lower, author_lower, genre_lower, main_character_lower, romance_line_lower, description_lower))
        conn.commit()
        return True
    except Exception as e:
        print(f"Ошибка при добавлении книги: {e}")
        return False
    finally:
        conn.close()