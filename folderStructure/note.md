# Folder Structure - Notes

## How Python Projects are Organized

### Modules
- A **module** is simply a **single `.py` file**
- Any Python file can be a module — when you write `import chai`, Python looks for `chai.py`
- Modules help break code into separate files so each file has one responsibility

```
chai_shop/
    run.py     → this is a module (starts the app)
    chai.py    → this is a module (contains chai logic)
```

### Packages
- A **package** is a **folder that contains Python modules** and a special `__init__.py` file
- `__init__.py` tells Python "this folder is a package, you can import from it"
- It can be empty or contain initialization code for the package

```
chai_shop/
    utils/              → this is a package (folder with __init__.py)
        __init__.py     → makes this folder importable
        helpers.py      → a module inside the package
    processing/         → another package/folder
```

### Why this structure matters:
- **Modules** keep your code organized — one file per purpose
- **Packages** group related modules together — like folders for files
- You can import from packages: `from utils.helpers import some_function`

### Module vs Package:
| Module | Package |
|---|---|
| A single `.py` file | A folder with `__init__.py` |
| `import chai` | `from utils import helpers` |
| Contains functions, classes, variables | Contains multiple modules |

### `run.py` as entry point:
- Typically one file serves as the **entry point** (the file you actually run)
- `run.py` starts the app and imports what it needs from other modules
