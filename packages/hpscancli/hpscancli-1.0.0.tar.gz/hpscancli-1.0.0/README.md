# HPScanCLI

The HPScanCLI is a command-line interface for interacting with HP scanners through their web interfaces. It allows to search for available printers in the local network, print out printer capabilities, and initiate scans with various parameters.

## Features

- **Search for Printers**: Discover HP printers available in the local network.
- **Print Capabilities**: Retrieve and display the capabilities of a printer.
- **Scan Documents**: Initiate scanning operations with customizable parameters like DPI, height, width, color mode, and output format.

## Requirements

- Python 3.x
- Required Python packages (`bs4`, `requests`)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/prasannareddych/HPScanCLI.git
   ```

2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line with appropriate options:

```
hpscancli [options]
```

### Command-line Options

- `-i, --ip`: IP address of the HP Wireless scanner / InkTank / LaserJet.
- `-s, --searchprinter`: search for available printers in the network.
- `-c, --capabilities`: show capabilities of the printer.
- `--height`: set scan height.
- `--width`: Set scan width.
- `--dpi`: set scan DPI.
- `--colormode`: set scan color mode.
- `--pdf`: set output format to PDF.
- `-o, --output`: set output filename.
- `-b, --bulkscan`: scan in bulk mode.

## Examples

1. Search for available printers:

   ```
   hpscancli -s
   ```

2. Print capabilities of a specific printer:

   ```
   hpscancli -i <printer-ip> -c
   ```

3. Perform a scan with custom parameters:

   ```
   hpscancli -i <printer-ip> --height 1200 --width 800 --dpi 300 --colormode RGB24 --pdf -o scan1
   ```

## Author

Prasanna Reddy. Ch

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
