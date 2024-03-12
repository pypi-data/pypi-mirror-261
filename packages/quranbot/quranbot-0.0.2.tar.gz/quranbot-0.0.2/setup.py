from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'A package developed by SaudiBits to facilitate the process of making a quran bot'
LONG_DESCRIPTION = 'A package developed by SaudiBits to facilitate the process of making a quran bot'

# Setting up
setup(
    name="quranbot",
    version=VERSION,
    author="Ahmed Alnasser",
    author_email="itzzmega2005@gmail.com",
    license="MIT",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['python-telegram-bot', 'Pillow', 'requests'],
    keywords=['Quran', 'Bot'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: MIT License"
    ]
)