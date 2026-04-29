# auto-generated-python-suite

## Overview

`auto-generated-python-suite` is a lightweight Python project that provides a simple yet effective TCP port scanner. It allows users to specify a target host (an IP address or domain name) and scan a range of ports to identify which ones are open. This tool was generated as part of an autonomous coding exercise and demonstrates how to create, test, and deploy a Python script within a GitHub repository.

## Features

- Scan a target host for open TCP ports.
- Specify the starting and ending ports for the scan via command-line options.
- Uses only Python’s standard library (`argparse` and `socket`), so there are no external dependencies to install.

## Installation

1. Ensure you have **Python 3.7+** installed on your system. You can verify your Python version by running:

    ```
    python3 --version
    ```

2. Clone this repository using Git:

    ```
    git clone https://github.com/okaloopen/auto-generated-python-suite.git
    cd auto-generated-python-suite
    ```

3. There are no additional packages to install since the project relies exclusively on the standard library. The `requirements.txt` file is included for completeness but lists no dependencies.

## Usage

Run the port scanner from the command line as follows:

```
python3 main.py <target_host> [--start START_PORT] [--end END_PORT]
```

### Arguments

- `<target_host>`: The IP address or domain name of the host you want to scan.
- `--start START_PORT`: Optional. The starting port number to begin scanning from. Defaults to `1`.
- `--end END_PORT`: Optional. The ending port number to finish scanning. Defaults to `1024`.

### Examples

Scan the first 1024 ports of `localhost`:

```
python3 main.py 127.0.0.1
```

Scan ports 20 through 80 of `example.com`:

```
python3 main.py example.com --start 20 --end 80
```

## Contributing

Contributions are welcome! If you find a bug or have an idea for an enhancement, feel free to open an issue or submit a pull request.

## License

This project is provided for educational purposes without any specific licensing terms. You are free to modify and use the code at your own discretion.
