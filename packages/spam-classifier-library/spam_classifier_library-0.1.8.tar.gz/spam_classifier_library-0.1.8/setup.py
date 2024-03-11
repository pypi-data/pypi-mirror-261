from setuptools import setup, find_packages

# Чтение README.md с явным указанием кодировки UTF-8
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    include_package_data=True,
    name='spam_classifier_library',  # Имя вашего пакета
    version='0.1.8',  # Версия вашего пакета
    packages=find_packages(),  # Список пакетов для включения в ваш пакет
    author='Кирилл',  # Ваше имя
    author_email='totoshkus@gmail.com',  # Ваш адрес электронной почты
    description='A library for spam classification',  # Краткое описание вашего пакета
    long_description=long_description,  # Длинное описание вашего пакета (из файла README.md)
    long_description_content_type='text/markdown',  # Тип содержимого вашего длинного описания
    url='https://github.com/CodeNeuralist/SpamLib',  # URL-адрес вашего репозитория на GitHub
    install_requires=[
        'torch>=1.9.0',
        'scikit-learn>=0.24.2',
        'GitPython>=3.1.42',
    ],  # Список зависимостей вашего пакета
    classifiers=[  # Классификаторы, которые описывают ваш пакет
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
