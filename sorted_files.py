import shutil # Модуль для копіювання файлів
from pathlib import Path
from threading import Thread, RLock # Для створення потоків

lock = RLock()

def copy_file(file:Path, destination:Path): # Копіювання одного файлу
    extension = file.suffix[1:] if file.suffix else 'no_extension'

    target_folder = destination / extension # Створюємо нову папку, якщо немає
    with lock:
        target_folder.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file, target_folder / file.name) # Копіюємо файл в нову папку
        print(f'Файл {file.name} скопійовано до папки {target_folder}') # Повідомлення


# Функція з потоками (Основна)
def sorted_files_multithread(source_directory: Path, destination_directory: Path):
    source_directory = Path(source_directory) # Шлях перетворюється на обєект
    destination_directory = Path(destination_directory) # Шлях до папки

    threads = []  # Список потоків

    for file in source_directory.rglob('*'): # Обходимо всі файли рекурсивно
        if file.is_file(): # Перевіряємо чи це файл або ні
            t_file = Thread(target=copy_file, args=(file, destination_directory)) # Потік який копіює цей файл
            t_file.start() # Запускається потік
            threads.append(t_file)  # Додаємо у список

    for t_file in threads: # Чекаємо завершеня
        t_file.join()

# Функція без потоків (для себе тестування)
def sorted_files(source_directory, destination_directory):
    source_directory = Path(source_directory)
    destination_directory = Path(destination_directory)

    for file in source_directory.rglob('*'):
        if file.is_file():
            copy_file(file, destination_directory)

if __name__ == '__main__':
    print('Сортування файлів')
    sorted_files_multithread(
        source_directory=Path.cwd() / 'files_to_sort',
        destination_directory=Path.cwd() / 'sorted_files_out'
    )






