import re

from pytest import Config


def replace(filePath: str, text: str, subs: str, flags: int = 0) -> None:
    with open(filePath, "r+") as file:
        fileContents = file.read()
        textPattern = re.compile(re.escape(text), flags)
        fileContents = textPattern.sub(subs, fileContents)
        file.seek(0)
        file.truncate()
        file.write(fileContents)


def pytest_unconfigure(config: Config) -> None:
    replace(".env", 'mode="test"', 'mode="develop"')
