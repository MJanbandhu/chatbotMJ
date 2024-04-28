from setuptools import setup, find_packages

setup(
    name='0.05',
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
    author_email='mojanbandhu@email.com',
    description='A chatbot package',
    url='https://github.com/MJanbandhu/chatbotMJ.git',
    license='MIT',
)
