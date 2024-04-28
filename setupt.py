from setuptools import setup, find_packages

setup(
    name='chatbotmj',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'nltk',
        'keras',
        # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'chatbot = chatbot.chatbot:main'
        ]
    },
    author='Mohit Janbandhu',
    author_email='vinodjanbandhu3@email.com',
    description='A chatbot package by Mohit Janbandhu',
    url='https://github.com/MJanbandhu/chatbotMJ.git',
    download_url =https://github.com/MJanbandhu/chatbotMJ/archive/refs/tags/ChatbotMJ.tar.gz
    license='MIT',
)
