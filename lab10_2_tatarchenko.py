import os
import shutil

source = os.getcwd()
destination = r"D:\SIGNAL"

if not os.path.exists(destination):
    os.makedirs(destination)

for filename in os.listdir(source):
    if filename.endswith(".whl"):
        shutil.copy(
            os.path.join(source, filename),
            os.path.join(destination, filename)
        )
        print("Скопійовано:", filename)