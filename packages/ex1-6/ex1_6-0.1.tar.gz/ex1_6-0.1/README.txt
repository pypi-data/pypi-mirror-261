1. Создание структуры (и заполнение) проекта
2. Установка twine и wheel
   pip install twine
   pip install wheel
3. Упаковка проекта
   python setup.py sdist bdist_wheel
4. Публиакация на PyPl
   twine upload dist/*
5. Создание виртуального окружения
   python -m venv my_env
6. Активация виртуального окружения
   source my_env/bin/activate  # Для Linux / macOS
   my_env\Scripts\activate      # Для Windows
7. Установка пакета с помощью pip
   pip install my_package
8. Проверка установки пакета

