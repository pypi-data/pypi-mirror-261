from setuptools import setup, find_packages

setup(
    name='stock-chat',
    version='1.1.0',
    packages=find_packages(),
    author='xshanzhu2024',
    author_email='xshanzhu2024@gmail.com',
    description='agent for stock with gptchat',
    long_description='agent for stock with gptchat。you can search stock trends .',
    long_description_content_type='text/markdown',
    url='https://github.com/xshanzhu2024/stock-chat',
    install_requires=[
        # List of dependencies
		'flask>=2.0.2',
		'flask-cors>=4.0.0',
		'llm-chat-openapi>1.0.5'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
