# backup.py
import sqlite3
import shutil
import os
import datetime
import schedule
import time
import threading
from datetime import datetime as dt


def create_backup():
    try:
        if not os.path.exists('literature.db'):
            print("База данных не найдена, пропускаем резервное копирование")
            return

        backup_dir = 'backups'
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            print(f"Создана папка для бэкапов: {backup_dir}")

        timestamp = dt.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(backup_dir, f"literature_backup_{timestamp}.db")

        shutil.copy2('literature.db', backup_file)

        cleanup_old_backups(backup_dir, keep_last=5)

        print(f"[{dt.now().strftime('%H:%M:%S')}] Резервная копия создана: {backup_file}")
        return True

    except Exception as e:
        print(f"[{dt.now().strftime('%H:%M:%S')}] Ошибка при создании резервной копии: {e}")
        return False


def cleanup_old_backups(backup_dir, keep_last=5):
    try:
        backup_files = [f for f in os.listdir(backup_dir)
                        if f.startswith('literature_backup_') and f.endswith('.db')]

        if len(backup_files) > keep_last:
            backup_files.sort(key=lambda x: os.path.getmtime(os.path.join(backup_dir, x)))

            for old_file in backup_files[:-keep_last]:
                os.remove(os.path.join(backup_dir, old_file))
                print(f"  Удален старый бэкап: {old_file}")

    except Exception as e:
        print(f"Ошибка при очистке старых бэкапов: {e}")


def backup_on_startup():
    print("Создание резервной копии при запуске...")
    create_backup()


def start_backup_scheduler():
    schedule.every().day.at("02:00").do(create_backup)

    schedule.every(12).hours.do(create_backup)

    print("Автоматическое резервное копирование запущено")
    print("Бэкапы будут создаваться:")
    print("  - Каждый день в 02:00")
    print("  - Каждые 12 часов")

    def scheduler_loop():
        while True:
            schedule.run_pending()
            time.sleep(60)

    thread = threading.Thread(target=scheduler_loop, daemon=True)
    thread.start()
    return thread


if __name__ == "__main__":
    print("Создание тестовой резервной копии...")
    create_backup()