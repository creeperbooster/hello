import subprocess
import os
subprocess.call(["git", "clone", "https://github.com/creeperbooster/hello"])

#os.system(r"D:\WATCOM\binnt64\cl.exe D:\SkriptGitPul_Institut_2019\hello\hello\main.cpp -o D:\SkriptGitPul_Institut_2019\hello\hello\main.exe")
#os.system(r"D:\InnoSetup6\ISCC.exe D:\SkriptGitPul_Institut_2019\hello\hello\Setup1.iss")
#os.system(r"D:\SkriptGitPul_Institut_2019\hello\hello\mysetup.exe")
#Uncoment me ^^^

#subprocess.call(["git", "pull"])
#subprocess.call(["git", "add", "main.cpp"])
subprocess.call(["git", "commit", "-m", "Commit4"])


subprocess.call(["git", "push", "https://github.com/creeperbooster/hello"])
subprocess.call(["git", "add", "."])


print("Check")

