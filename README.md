# Micrograd: A learning repo based on [Andrej Karpathy's lecture](https://www.youtube.com/watch?v=VMj-3S1tku0)

### Create a virtual environment for the project

1. Open the terminal through PyCharm, this will automatically open at the root for the current project.

2. Create a virtual environment called ```.venv```
    The `.` denotes a hidden folder.

    The command below will create a new folder called ```.venv```

        python3 -m venv .venv

    In my system the Python3 installation was not pointed to by the system `python` so I have used `python3` for the above command. Alternatively use the following:

        python -m venv .venv

---

### Activate the new virtual environment ```.venv```

In the PyCharm terminal type in the following command to activate the virtual environment ```.venv ```:

    source .venv/bin/activate

---

### Configure PyCharm current Project Interpreter

Go to (Cmd + ",") to open Python Interpreter and add a new interpreter from existing (under virtual environments).