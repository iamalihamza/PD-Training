''' You work at a company that receives daily data files from external partners. These files need to be processed and analyzed, but first, they need to be transferred to the company's internal network.

The goal of this project is to automate the process of transferring the files from an external FTP server to the company's internal network.

Here are the steps you can take to automate this process:

    Use the ftplib library to connect to the external FTP server and list the files in the directory.

    Use the os library to check for the existence of a local directory where the files will be stored.

    Use a for loop to iterate through the files on the FTP server and download them to the local directory using the ftplib.retrbinary() method.

    Use the shutil library to move the files from the local directory to the internal network.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the files that have been transferred and any errors that may have occurred during the transfer process. '''

import ftplib
import os
import shutil
import logging
import schedule
import time

# Define FTP server details
ftp_server = "ftp.example.com"
ftp_user = "username"
ftp_password = "password"
ftp_directory = "/directory"

# Define local directory where files will be stored
local_directory = "info"

# Create log file for storing log
logging.basicConfig(filename='file_transfer.log', level=logging.INFO)


def transfer_files():
    try:
        # Connect to FTP server
        ftp = ftplib.FTP(ftp_server)
        ftp.login(ftp_user, ftp_password)

        # Change directory
        ftp.cwd(ftp_directory)

        # List files in directory
        files = ftp.nlst()

        # Check for existence of local directory
        if not os.path.exists(local_directory):
            os.mkdir(local_directory)

        # Download and transfer files
        # Loop through each file in the list of files on the FTP server
        for file in files:
            # Create a local file path by joining the local directory with the filename
            local_file = os.path.join(local_directory, file)
            # Open the local file in write binary mode
            with open(local_file, 'wb') as f:
                # Use the FTP object to retrieve the file from the server and write its contents to the local file
                ftp.retrbinary(f'RETR {file}', f.write)
            # Copy the local file to a network directory
            shutil.copy(local_file, "/internal/network/")
            # Log a message indicating that the file was successfully transferred
            logging.info(f"{file} transferred successfully.")

        # Disconnect from FTP server
        ftp.quit()
    except Exception as e:
        logging.error(f"Error transferring file: {str(e)}")


# Schedule script to run daily at 9 AM
schedule.every().day.at("09:00").do(transfer_files)

while True:
    schedule.run_pending()
    time.sleep(1)
