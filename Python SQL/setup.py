import sys
from cx_Freeze import setup, Executable


build_exe_options = {"packages": ["os"], "includes": ["tkinter", "pyodbc"]}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Gerenciamento de banco de dados",
    version="0.1",
    description="Aplicação",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py", base=base)]
)