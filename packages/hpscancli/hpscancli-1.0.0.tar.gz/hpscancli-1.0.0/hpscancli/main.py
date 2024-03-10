from pathlib import Path
from hpscancli.schema import scan_xml_schema

import argparse
import bs4
import datetime
import re
import requests
import socket
import sys
import time

class HPScanner:
    def __init__(self, ip: str = None):
        if ip:
            self.host = ip
            if not self.check_printer(ip):
                print(f"Error. counldn't connect to the printer. please check the ip: {ip}")
                exit()
            self.session = requests.Session()

    def check_printer(self, ip: str) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.01)
            result = sock.connect_ex((ip, 9100))
            if result == 0:
                return True 
            sock.close()
        except:
            return False

    def get_capabilities(self):
        URL_SCANNER_CAPABILITY  = f'http://{self.host}/eSCL/ScannerCapabilities'
        response = self.session.get(URL_SCANNER_CAPABILITY)
        soup = bs4.BeautifulSoup(response.text,"xml")
        class Capability:       
            make_and_model = soup.find('pwg:MakeAndModel').text
            serial_number = soup.find('pwg:SerialNumber').text
            manufacturer = soup.find('scan:Manufacturer').text
            firmware_version = soup.find('pwg:Version').text
            platen_info = soup.find('scan:Platen')
            min_width = int(platen_info.find('scan:MinWidth').text)
            max_width = int(platen_info.find('scan:MaxWidth').text)
            min_height = int(platen_info.find('scan:MinHeight').text)
            max_height = int(platen_info.find('scan:MaxHeight').text)
            color_modes = [mode.text for mode in platen_info.find_all('scan:ColorMode')]
            document_formats = [format.text for format in platen_info.find_all('pwg:DocumentFormat')]
            supported_resolutions = [int(res.find('scan:XResolution').text) for res in platen_info.find_all('scan:DiscreteResolution')]
        return Capability()

    def print_capabilities(self):
        capabilities = self.get_capabilities()
        print(f"Make and Model: {capabilities.make_and_model}")
        print(f"Serial Number: {capabilities.serial_number}")
        print(f"Manufacturer: {capabilities.manufacturer}")
        print(f"Firmware Version: {capabilities.firmware_version}")
        print()
        print(f"Min/Max Width: {capabilities.min_width}/{capabilities.max_width}")
        print(f"Min/Max Height: {capabilities.min_height}/{capabilities.max_height}")
        print(f"Supported Color Modes: {', '.join(capabilities.color_modes)}")
        print(f"Supported Resolutions: {', '.join([str(x) for x in capabilities.supported_resolutions])}")

        
    def get_job(self,retry_count: int = 0):
        URL_SCANNER_STATUS = f'http://{self.host}/eSCL/ScannerStatus'
        response = self.session.get(URL_SCANNER_STATUS)
        soup = bs4.BeautifulSoup(response.text,"xml")
        job_infos = soup.find_all('scan:JobInfo')
        for job_info in job_infos:
            job_uri = job_info.find('pwg:JobUri').text.strip()
            job_state = job_info.find('pwg:JobState').text.strip()
            if job_state == "Processing":
                return job_uri
        if retry_count < 5:
            time.sleep(0.2)
            return self.get_job(retry_count=retry_count+1)
     
    def perform_scan(self, dpi: int = 0, h: int  = 0, w: int = 0, cm: str = "RGB24",pdf: bool = False, out_file_name: str = None):
        URL_CREATE_SCAN = f'http://{self.host}/eSCL/ScanJobs'
        capability = self.get_capabilities()
        height = h if h else capability.max_height
        width = w if w else capability.max_width
        if not dpi: dpi = 300
        dpi = dpi if dpi in capability.supported_resolutions else capability.supported_resolutions[0]
        xdpi, ydpi  = dpi, dpi
        format = "application/pdf" if pdf else "image/jpeg"  
        colormode = cm if cm in capability.color_modes else capability.color_modes[-1]
        print(f"scan parameters:: h: {height}, w: {width}, dpi: {dpi}, cm: {colormode}, format: {format}")
        data = scan_xml_schema.format(
            height = height,
            width = width,
            xdpi = xdpi,
            ydpi = ydpi,
            format = format,
            colormode = colormode
        )
        res = self.session.post(URL_CREATE_SCAN,data = data)
        if res.status_code != 201:
            http_code = -1
            description = "scanner may be busy. please wait."
            try:
                soup = bs4.BeautifulSoup(res.text,"xml")
                http_code = soup.find("httpcode").text
                description = soup.find("description").text
            except:
                pass
            print(f"scan error! code: {http_code}, reason: {description}.")
            time.sleep(5)
            return
        job = self.get_job()
        if job:
            url = f'http://{self.host}{job}/NextDocument'
            print("scan started. please wait...")
            data = self.session.get(url).content
            file_name =out_file_name if out_file_name else datetime.datetime.now().strftime("SCAN_%Y%m%d_%H%M%S")
            file_name += ".pdf" if pdf else ".jpg"
            file = Path(file_name)
            suffix = 1
            temp = file
            while file.exists():
                file = temp.parent.joinpath(f"{temp.stem}_{suffix}{temp.suffix}")
                suffix += 1
            file.write_bytes(data)
            print(f"scan complete. saved {file}")
    
    def get_ip_address(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip_address = s.getsockname()[0]
            s.close()
            return ip_address
        except socket.error as e:
            return
         
    def scan_network(self):
        printers = []
        machine_ip = self.get_ip_address()
        if not machine_ip:
            return printers
        _ip = re.findall("\d+.\d+.\d+.",machine_ip)[0]
        ip_range = [_ip+str(i) for i in range(2,255) if _ip+str(i) != machine_ip]
        total_ips = len(ip_range)
        scanned_ips = 0
        for ip in ip_range:
            if self.check_printer(ip):
                printers.append(ip)
            time.sleep(0.01)
            scanned_ips += 1
            progress = scanned_ips / total_ips
            sys.stdout.write('\rScanning Network: [{:<50}] {:.2%}'.format('=' * int(progress * 50), progress))
            sys.stdout.flush()
        print()
        return printers

    def search_printers(self):
        print("Searching for printers. Please wait...")
        printers = self.scan_network()
        if not printers:
            print("No printers found!")
            return
        for printer in printers:
            print(f"Found {printer}")

def parse_command_line():
    parser = argparse.ArgumentParser(description='HPScanCLI')
    parser.add_argument('-i','--ip', help='IP address of the HP Wireless scanner / InkTank / LaserJet', metavar='')
    parser.add_argument('-s','--searchprinter', action='store_true', help='search for available printers in the network')
    parser.add_argument('-c','--capabilities', action='store_true', help='show capabilities of the printer')
    parser.add_argument('--height', help='set scan height',metavar='')
    parser.add_argument('--width', help='set scan width',metavar='')
    parser.add_argument('--dpi', help='set scan dpi',metavar='')
    parser.add_argument('--colormode', help='set scan colormode',metavar='')
    parser.add_argument('--pdf',action='store_true', help='set output format to pdf')
    parser.add_argument('-o','--output', help='set output filename',metavar='')
    parser.add_argument('-b','--bulkscan', action='store_true', help='scan in bulk mode')
    
    args = parser.parse_args()
    return args

def main_process():
    args = parse_command_line()
    if args.searchprinter:
        hpscanner = HPScanner()
        hpscanner.search_printers()
        return
    
    if args.ip:
        dpi,h,w = 0,0,0
        hpscanner = HPScanner(args.ip)
        try:
            if args.dpi:
                dpi = int(args.dpi)
        except:
            raise Exception(f"invalid dpi value: {args.dpi}")
        try:
            if args.height:
                h = int(args.height)
        except:
            raise Exception(f"invalid height value: {args.height}")
        try:
            if args.width: 
                w = int(args.width)
        except:
            raise Exception(f"invalid width value: {args.width}")
        
        
        def do_scan():
            hpscanner.perform_scan(
                dpi = dpi,
                h   = h,
                w   = w,
                cm  = args.colormode,
                pdf = args.pdf,
                out_file_name=args.output
            )
        
        if args.capabilities:
            hpscanner.print_capabilities()
            return
        if args.bulkscan:
            do_scan()
            while True:
                choice = input("Continue scan? y/n: ")
                if choice.lower() not in ["y","n"]:
                    print("enter correct choice")
                    continue
                if choice.lower() == "y": 
                    do_scan()
                    continue
                print("bulk scan complete.")
                return
        do_scan()
    else:
        print("usage: hpscancli -i <ip-address>")

def main():
    try:
        main_process()
    except KeyboardInterrupt:
        print("\nscan cancelled. exiting...")
    except Exception as e:
        print(f"\nexception occurred: {e}")