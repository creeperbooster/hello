import subprocess
#subprocess.call(["git", "clone", "https://github.com/creeperbooster/hello"])
#subprocess.call(["git", "pull"])
subprocess.call(["git", "add", "main.cpp"])
subprocess.call(["git", "commit", "-m", "Commit 1"])
subprocess.call(["git", "add", "."])
print("Check")

