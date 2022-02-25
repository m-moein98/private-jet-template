import re
import configurations.base_db as base_db


def replace(filePath, text, subs, flags=0):
    with open(filePath, "r+") as file:
        fileContents = file.read()
        textPattern = re.compile(re.escape(text), flags)
        fileContents = textPattern.sub(subs, fileContents)
        file.seek(0)
        file.truncate()
        file.write(fileContents)


def pytest_unconfigure(config):
    replace(".env", f'mode="test"', 'mode="develop"')
