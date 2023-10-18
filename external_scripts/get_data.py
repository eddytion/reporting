import configparser
import csv
import logging
from pathlib import Path

import paramiko
from cryptography.fernet import Fernet


def returnMsPowerType(ms):
    types = {
        "8233-E8B": "Power_7",
        "9179-MHD": "Power_7",
        "8246-L2T": "Power_7",
        "8286-42A": "Power_8",
        "8284-22A": "Power_8",
        "9119-MME": "Power_8",
        "9009-22A": "Power_9",
        "9009-42A": "Power_9",
        "9080-M9S": "Power_9",
        "9080-HEX": "Power_10",
        "9043-MRX": "Power_10"
    }
    if types.get(ms) is not None:
        return types[ms]
    else:
        return "Unknwon"


class HMCDataFetcher(object):
    def __init__(self, ssh_client):
        self.ssh_client = ssh_client
        self.log = logging.getLogger(__name__)

    def get_system_memory(self, sysname):
        command = f"lshwres -m {sysname} -r mem --level sys -F configurable_sys_mem,curr_avail_sys_mem"
        return self.execute_command(command, "No memory information found")

    def get_system_cpu(self, sysname):
        command = f"lshwres -m {sysname} -r proc --level sys -F configurable_sys_proc_units,curr_avail_sys_proc_units"
        return self.execute_command(command, "No CPU information found")

    def get_lpar_memory(self, sysname):
        self.log.info(f'Getting memory data for {sysname}')
        command = f"lshwres -m {sysname} -r mem --level lpar -F lpar_name,curr_mem"
        return self.execute_command(command, "No LPAR memory information found")

    def get_lpar_cpu(self, sysname):
        self.log.info(f'Getting CPU data for {sysname}')
        command = f"lshwres -m {sysname} -r proc --level lpar -F lpar_name,curr_proc_units"
        return self.execute_command(command, "No LPAR CPU information found")

    def execute_command(self, command, error_message):
        try:
            output = self.ssh_client.execute_command(command)
            data = [i.rstrip('\n').strip() for i in output]
            if not data:
                self.log.info(error_message)
            return data
        except Exception as e:
            self.log.error(f"Failed to execute command: {command}", exc_info=True)


class SSHClient:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self, hostname):
        try:
            self.ssh_client.connect(hostname, username=self.username, password=self.password)
        except Exception as e:
            logging.error(f"Failed to connect to {hostname}: {str(e)}")

    def execute_command(self, command):
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            return stdout.readlines()
        except Exception as e:
            logging.error(f"Failed to execute command {command}: {str(e)}")


def setup_logging():
    log_file = 'reporting.log'
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)-1s]: %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S',
        handlers=[logging.FileHandler(log_file), logging.StreamHandler()]
    )
    logging.getLogger("paramiko").setLevel(logging.WARNING)


def read_config():
    config_file = Path("settings.cfg")
    config = configparser.ConfigParser()
    config.read(config_file)
    return {
        'sysuser': config['system']['username'],
        'syspass': config['system']['password'],
        'sshtimeout': int(config['system']['timeout'])
    }


def load_systems(filename):
    systems = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=':')
        for row in reader:
            systems[row[0]] = row[1]
    return systems


def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password.encode())
    return decrypted_password.decode()


def main():
    setup_logging()
    config_values = read_config()
    key_file = Path("secret.key")
    key = key_file.read_bytes()
    decrypted_password = decrypt_password(config_values['syspass'], key)

    ssh_client = SSHClient(config_values['sysuser'], decrypted_password)

    systems = load_systems('systems.txt')

    reporting = HMCDataFetcher(ssh_client)
    for hmc_name, sysname in systems.items():
        ssh_client.connect(hmc_name)
        reporting.combine_and_output_db(hmc_name, sysname)


if __name__ == "__main__":
    main()
