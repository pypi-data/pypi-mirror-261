import os
import shutil
import time

shutil.rmtree("dist")
os.mkdir("dist")
os.system("python -m build")
os.system("twine upload dist/*")
time.sleep(5)
os.system('pip install ragtime --upgrade')