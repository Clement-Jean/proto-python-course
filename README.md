# proto-python-course
[![build main branch](https://github.com/Clement-Jean/proto-python-course/actions/workflows/build.yml/badge.svg)](https://github.com/Clement-Jean/proto-python-course/actions/workflows/build.yml) [![Lint protobuf](https://github.com/Clement-Jean/proto-python-course/actions/workflows/lint.yml/badge.svg)](https://github.com/Clement-Jean/proto-python-course/actions/workflows/lint.yml)

## COUPON: `START_MAR`

## Notes

### `Windows`

- I recommend you use powershell (try to update: [see](https://github.com/PowerShell/PowerShell/releases)) for following this course.
- I recommend you use [Chocolatey](https://chocolatey.org/) as package installer (see [Install](https://chocolatey.org/install))

### Build

#### `Linux/MacOS`

```shell
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
make generate
```

#### `Windows - Chocolatey`
```shell
choco install make
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
make generate
```

#### `Windows - Without Chocolatey`

```shell
python -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
protoc -Iproto --python_out=proto proto/*.proto
```

### Run

```
python main.py
```
