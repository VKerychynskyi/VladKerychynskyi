class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()

# Використання контекст-менеджера для читання з файлу
with FileManager("example.txt", "r") as file:
    try:
        content = file.read()
        print(content)
    except Exception as e:
        print(f"Помилка: {e}")