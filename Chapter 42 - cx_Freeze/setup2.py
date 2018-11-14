from cx_Freeze import setup, Executable

exe = Executable(
    script="sampleApp.py",
    base="Win32GUI",
)

setup(
    name = "wxSampleApp",
    version = "0.1",
    description = "An example wxPython script",
    executables = [exe]
)