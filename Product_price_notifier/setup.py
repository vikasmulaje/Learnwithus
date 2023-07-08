from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'product price notifier'

# Setting up
setup(
    name="price_notifier",
    version=VERSION,
    author="vinod",
    author_email="vpmulaje@gmail.com",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=['requests', 'BeautifulSoup', 'python-dotenv', 'pymongo'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests==2.26.0',
        'beautifulsoup4==4.10.0',
        'python-dotenv==0.19.1',
        'pymongo==3.12.0'
    ]
)
