import os
import logging
import filetype
import pandas as pd
from PyPDF2 import PdfReader
from zipfile import ZipFile, BadZipFile

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

def check_file(file_path):
    # Check if file exists
    if not os.path.isfile(file_path):
        logging.error(f"File {file_path} does not exist.")
        return

    # Check file size
    file_size = os.path.getsize(file_path)
    if file_size > MAX_FILE_SIZE:
        logging.warning(f"File {file_path} is too large: {file_size} bytes.")
        return
    logging.info(f"File Size: {file_size} bytes")

    # Check file type
    file_type = filetype.guess(file_path)
    if file_type is None:
        logging.error(f"Cannot guess the file type for {file_path}")
        return
    logging.info(f"File Type: {file_type.mime}")

    # Check if file is password protected
    if is_password_protected(file_path, file_type.mime):
        logging.warning(f"File {file_path} is password protected.")
        return
    
     # Handle ZIP files separately
    if file_type.mime == 'application/zip':
        if not handle_zip_file(file_path):
            return
    
    # Check if file can be read
    if not file_type.mime == 'application/zip':
        if not can_read_file(file_path, file_type.mime):
            logging.error(f"File {file_path} cannot be read.")
            return

        logging.info(f"File {file_path} passed all checks.")

def is_password_protected(file_path, mime_type):
    try:
        if mime_type == 'application/pdf':
            with open(file_path, 'rb') as file:
                pdf = PdfReader(file)
                if pdf.is_encrypted:
                    return True
        elif mime_type == 'application/zip':
            with ZipFile(file_path, 'r') as zip_file:
                if zip_file.testzip() is not None:
                    return True
        # Add checks for other file types if needed
        return False
    except Exception as e:
        logging.error(f"Error checking if file is password protected: {e}")
        return False

def can_read_file(file_path, mime_type):
    try:
        if mime_type.startswith('text'):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                logging.info("File can be read. Sample content:")
                logging.info(content[:100])  # Print first 100 characters as a sample
        elif mime_type == 'application/pdf':
            with open(file_path, 'rb') as file:
                pdf = PdfReader(file)
                if pdf.is_encrypted:
                    logging.warning(f"File {file_path} is encrypted and cannot be read.")
                    return False
                content = ''
                for page_num in range(min(5, len(pdf.pages))):  # Read first 5 pages as sample
                    page = pdf.pages[page_num]
                    content += page.extract_text()
                logging.info("File can be read. Sample content:")
                logging.info(content[:100])  # Print first 100 characters as a sample
        elif mime_type in ['application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'application/vnd.ms-excel']:
            df = pd.read_excel(file_path)
            logging.info("File can be read. Sample content:")
            logging.info(df.head())  # Print first few rows as sample
        else:
            logging.warning(f"Unsupported file type: {mime_type}")
            return False
        return True
    except UnicodeDecodeError:
        logging.error(f"File {file_path} has encoding issues.")
        return False
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {e}")
        return False

def check_files(file_paths):
    for file_path in file_paths:
        logging.info(f"Checking file: {file_path}")
        check_file(file_path)



def handle_zip_file(zip_path, file_paths):
    try:
        with ZipFile(zip_path, 'r') as zip_file:
            for file_info in zip_file.infolist():
                logging.info(f"Extracting file from ZIP: {file_info.filename}")
                extracted_path = zip_file.extract(file_info, "/tmp")
                file_paths.append(extracted_path)
    except BadZipFile:
        logging.error(f"Bad ZIP file: {zip_path}")
    except Exception as e:
        logging.error(f"Error handling ZIP file {zip_path}: {e}")
        


# Example usage
file_paths = ['trial_files/raga ai.zip']
check_files(file_paths)



