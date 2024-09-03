import sys
from cx_Freeze import setup, Executable

# Dependencies
build_exe_options = {
    "packages": ["tkinter", "numpy", "matplotlib", "function"],  # Add any packages your script depends on
    "include_files": ["gui/asset/"]  # Add any additional files or data needed by your script
}

# Executable
executable = Executable(
    script="main_gui.py",  # Replace "your_script.py" with the name of your Python script
    base="Win32GUI" if sys.platform == "win32" else None,  # Set the base to None if your script does not use a GUI framework like Tkinter
)

# Setup
setup(
    name="SeizureDetection",  # Replace "YourAppName" with the name of your application
    version="1.0",
    description="Seizure Detection",
    options={"build_exe": build_exe_options},
    executables=[executable]
)
