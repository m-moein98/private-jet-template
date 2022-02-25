import os
import sys
import uvicorn
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


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "runserver":
        uvicorn.run("main:app", host="localhost", port=8000, reload=True)
    elif cmd == "test":
        replace(".env", f'mode="{get_settings().mode}"', 'mode="test"')
        os.system("pytest")
