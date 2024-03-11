# Импорт недавно установленного пакета setuptools.
import setuptools

# Открытие README.md и присвоение его long_description.
with open("README.md", "r") as fh:
    long_description = fh.read()

# Определение requests как requirements для того, чтобы этот пакет работал. Зависимости проекта.
requirements = ["blinker==1.7.0",
                "certifi==2024.2.2",
                "charset-normalizer==3.3.2",
                "click==8.1.7",
                "colorama==0.4.6",
                "Flask==3.0.2",
                "idna==3.6",
                "itsdangerous==2.1.2",
                "Jinja2==3.1.3",
                "MarkupSafe==2.1.5",
                "requests==2.31.0",
                "urllib3==2.2.1",
                "Werkzeug==3.0.1"]

# with open('requirements.txt') as f:
#     requirements = f.read().splitlines()

# Функция, которая принимает несколько аргументов. Она присваивает эти значения пакету.
setuptools.setup(
    # Имя дистрибутива пакета. Оно должно быть уникальным, поэтому добавление вашего имени пользователя в конце является обычным делом.
    name="simple-weather-api-by-ys",
    # Номер версии вашего пакета. Обычно используется семантическое управление версиями.
    version="0.1.2",
    # Имя автора.
    author="YourShadow",
    # Его почта.
    author_email="rooderuler@gmail.com",
    # Краткое описание, которое будет показано на странице PyPi.
    description="This is a simple Flask API that provides real-time weather information for a specified city. The API is integrated with the Weatherstack service to fetch accurate and up-to-date weather data.",
    # Длинное описание, которое будет отображаться на странице PyPi. Использует README.md репозитория для заполнения.
    long_description=long_description,
    # Определяет тип контента, используемый в long_description.
    long_description_content_type="text/markdown",
    # URL-адрес, представляющий домашнюю страницу проекта. Большинство проектов ссылаются на репозиторий.
    url="https://github.com/Stranger-odua/simple-weather-api-by-ys",
    # Находит все пакеты внутри проекта и объединяет их в дистрибутив.
    packages=setuptools.find_packages(),
    # requirements или dependencies, которые будут установлены вместе с пакетом,
    # когда пользователь установит его через pip.

    install_requires=requirements,
    # Предоставляет pip некоторые метаданные о пакете. Также отображается на странице PyPi.
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # Требуемая версия Python.
    python_requires='>=3.8',
)
