## Nezu

[![PyPI version](https://badge.fury.io/py/nezu.svg)](https://pypi.org/project/nezu/)
[![License](https://img.shields.io/badge/license-MIT-teal)](https://opensource.org/license/mit/)
[![Dependencies](https://img.shields.io/badge/dependencies-None-teal)](https://github.com/Nezu-Devs/Nezu/blob/main/pyproject.toml)

### Elegant debugging module

  - **_Python code example_**
    ```py
    # file.py
    from nezu import say
    x = 13
    say('x')  # print debuging info
    ```
  - **_Bash commands to run_**
    ```bash
    export NEZU_SEEK = 1
    $ py file.py
        @4 l x:int  =>  13
    ```

### How to install?

```bash
$ python -m pip install nezu
```

or

```bash
$ python -m poetry add nezu
```

### How to use?

#### Basic usage

Inspect variable using `say` function. Pass name of variable you want to inspect as `str` argument.

- **Note**

  Output of `say` function is hidden by default. If you wannna see what nezu has to say you need to configure it first using `nezu` object. Simplest way is to call it with argument `1`.

```py
# file.py
from nezu import nezu, say
nezu(1)

say('egg')          # works on simple variables
say('ham.spam')     # works on attributes
say('spam["spam"]') # works on keys and indexes
say('print')        # works on functions and build-ins
```

<!--
```bash
$ python file.py
     @4 u egg
     @5 u ham.spam
     @6 u spam["spam"]
     @7 b print:function  =>  Prints the values to a stream, or to sys...
``` -->

### How to interpret output?

```
@7      b  print:function  =>  Prints the values to a stream, or to sys...
 │      │  │     │             │
 │      │  │     │             └───────── Value of inspected variable
 │      │  │     │
 │      │  │     └─────────────── Type of inspected variable.
 │      │  │
 │      │  └───────────── Name of inspected variable.
 │      │
 │      └──────── Scope of inspected variable.
 │                l:local, g:global, b:build-in, u:undefined
 |
 └────── Line number of inspection.
```

### Configuration

By default nezu is configured by _env vars_.
This can be changed in code.

#### Env vars config

If you want to use default configuration method, change your _env vars_ in terminal and than run your Python file.

- **_Bash_**

  ```bash
  export NEZU_SEEK = 1
  export NEZU_COLOR = 1
  export NEZU_LOCK = 0
  python3 file.py
  ```

- **_PowerShell_**
  ```powershell
  $env:NEZU_SEEK = 1
  $env:NEZU_COLOR = $True
  $env:NEZU_LOCK = $True
  py file.py
  ```

#### JSON config

If you dont want to use _env vars_ as configuration you can call `nezu.json()` to read configuration data from json file.
It will search for key `nezu` inside chosen file.

- **_Params_**
  - `path:str = 'nezu.json` - path of configuration file
- **_Example config file_**
  ```json
  "nezu" {
    "seek": 1,
    "color": true,
    "locked": false
  }
  ```

---

#### Hardcoded config

If you dont want to use _env vars_ as configuration you can also call object `nezu` like function to make hardcoded config.

- **_Params_**
  - `seek:int = 0` - debuging level
  - `color:bool = False` - output coloring
  - `lock:bool = False` - lock this config
- **_Example_**

  ```py
  # file.py
  from nezu import nezu, say

  nezu(1, True, False)
  ...
  ```

- **_Tip_**

  There is no build in support for _yaml_, _toml_ or _.env_ in _nezu_
  This is so _nezu_ can stay free of dependencies.
  However you can use hardcoded config to pass data from any config file.

### Coloring output

By default nezu output is monochrome.
If your terminal of choise support coloring you can change that.

#### Env vars coloring

- **_Example Bash command_**
  ```bash
  export NEZU_COLOR = 1
  python3 file.py
  ```
- **_Example PowerShell command_**
  ```powershell
  $env:NEZU_COLOR = $True
  py file.py
  ```

#### JSON coloring

- **_Example config file_**
  ```json
  "nezu" {
    "color": true,
  }
  ```

#### Hardcoded coloring

- **_Example_**

  ```py
  from nezu import nezu, say

  nezu(color = True)
  ...
  ```

### Hiding output

Function `say()` can be can be hidden into deeper levels of debugging via `hide` parameter. Execution argument `--nezu` seeks only for says hidden at level 1. Now if you want to display more, you run your program with `--nezu-seek` integer argument. In example bellow only says hidden up to level 3 are displayed.

```python
#file.py
from nezu import say

say('egg', hide=1)
say('ham', hide=2)
say('spam', hide=3)
say('bacon', hide=4)
say('lobster', hide=5)
```

```
$ python file.py --nezu-seek=3
@4      u  egg
@5      u  ham
@6      u  spam
```

### TO DO

- [x] add class method support?
- [x] add coloring
- [ ] add classes parameter (so you can print only group of logs)
- [ ] indicate shadowing
- [ ] write docstring for say
  - [ ] write test for multiline output
- [ ] write tests for name parser
- [x] write tests for say
- [ ] automate testing with Github actions?
- [ ] automate deployment to PyPI with Github actions?
- [ ] publish to Conda
- [ ] test on different CPython versions
- [ ] test on Pypy
- [ ] test on Anaconda
- [ ] add badges
- [ ] format files with blue
- [ ] remove obsolete tests
- [ ] gitignore .vscode, \_\_pycache, dist
- [ ] write proper documentation
  - [x] How to interpret output
  - [ ] Configuration
  - [ ] Explain arguments
    - [x] Hiding
    - [ ] Notes
    - [ ] args
  - [ ] Note args
  - [ ] brag in readme about being on pypy and and conda
- [ ] make a helper function, that returns dictionary (so it's easier to assert and doesn't require `--nezu`)
  - [ ] write function
  - [ ] write docstring for it
  - [ ] write tests for it
  - [ ] document it in README
- [ ] Write code of conduct
- [ ] Write/generate TOC
- [ ] Update README about configuration
- [ ] Write docstrings to configuration functions
