# Virtual Environment - Notes

## What is a Virtual Environment?
- A virtual environment is an **isolated Python installation** inside your project folder
- It has its own Python interpreter and its own installed packages
- Anything you install inside it does NOT affect other projects or your system Python

## Why do we need it?
- Project A might need `flask 2.0`, Project B might need `flask 3.0`
- Without virtual environments, they would conflict — only one version can be installed globally
- A virtual environment gives each project its **own separate set of packages**

## How to Create and Use:

```bash
# Step 1: Create the virtual environment
python -m venv myenv

# Step 2: Activate it
# On Windows:
myenv\Scripts\activate
# On Mac/Linux:
source myenv/bin/activate

# Step 3: Now install packages — they go ONLY into this environment
pip install flask

# Step 4: When done, deactivate
deactivate
```

## requirements.txt

### What is it?
- A text file that lists all the packages your project needs, with their versions
- Acts as a **shopping list** for dependencies — anyone can recreate your exact setup

### Format:
```
requests==2.31.0    # exact version (use == for pinning)
flask               # latest version (no version specified)
```

### How to use it:
```bash
# Install all dependencies listed in requirements.txt
pip install -r requirements.txt

# Generate a requirements.txt from currently installed packages
pip freeze > requirements.txt
```

### Why pin versions (`==`)?
- `requests==2.31.0` ensures everyone uses the **exact same version**
- Without pinning, a newer version might install and break your code
- Always pin versions in production projects for consistency

## Best Practice:
1. Always create a virtual environment for every new project
2. Activate it before installing anything
3. Keep a `requirements.txt` updated
4. Add `.venv/` or `myenv/` to `.gitignore` — don't commit the virtual environment itself, only the `requirements.txt`
