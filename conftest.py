import re
from settings import get_settings


def replace(filePath, text, subs, flags=0):
    with open(filePath, "r+") as file:
        fileContents = file.read()
        textPattern = re.compile(re.escape(text), flags)
        fileContents = textPattern.sub(subs, fileContents)
        file.seek(0)
        file.truncate()
        file.write(fileContents)


def pytest_configure(config):
    replace(".env", f'mode="{get_settings().mode}"', 'mode="test"')


def pytest_unconfigure(config):
    replace(".env", f'mode="test"', 'mode="develop"')
