from celery import shared_task
from .models import ManagedSystemVM, MemoryCpuVM, ManagedSystemCPU, ManagedSystemMemory
import configparser
import csv
import logging
from pathlib import Path

import paramiko
from cryptography.fernet import Fernet


@shared_task
def import_data():
    # Your data import logic here
    # E.g., fetch data from IBM HMC and save it to your models
    pass


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
        command = (
            'lssyscfg -r sys -F name,state | '
            'grep Operating | '
            'egrep -v "Authentication|No Connection|Mismatch|Power|HSCL" | '
            'cut -f 1 -d , | '
            'while IFS= read -r ms; do '
            'lshwres -m $ms -r mem --level sys -F configurable_sys_mem,curr_avail_sys_mem,deconfig_sys_mem,sys_firmware_mem,mem_region_size | '
            'while IFS= read -r line; do '
            'echo "$ms,$line"; '
            'done; '
            'done'
        )
        return self.execute_command(command, "No memory information found")

    def get_system_cpu(self, sysname):
        command = (
            'lssyscfg -r sys -F name,state,type_model | '
            'grep Operating | '
            'egrep -v "Authentication|No Connection|Mismatch|Power|HSCL" | '
            'cut -f 1,3 -d , | '
            'while IFS= read -r ms; do '
            'm=$(echo $ms | cut -f1 -d,); '
            'lshwres -m $m -r proc --level sys -F configurable_sys_proc_units,curr_avail_sys_proc_units,deconfig_sys_proc_units | '
            'while IFS= read -r line; do '
            'echo "$ms,$line"; '
            'done; '
            'done'
        )
        return self.execute_command(command, "No CPU information found")

    def get_lpar_memory_cpu(self, sysname):
        self.log.info(f'Getting memory and CPU data for {sysname}')
        command = (
            'lssyscfg -r sys -F name,state | '
            'grep Operating | '
            'egrep -v "Authentication|No Connection|Mismatch|Power|HSCL" | '
            'cut -f 1 -d , | '
            'while IFS= read -r ms; do '
            'lssyscfg -r prof -m $ms -F name,lpar_name,min_mem,desired_mem,max_mem,mem_mode,proc_mode,min_proc_units,desired_proc_units,max_proc_units,min_procs,desired_procs,max_procs,sharing_mode,uncap_weight;'
            'done'
        )
        return self.execute_command(command, "No LPAR memory and CPU information found")

    def get_lpar_list(self, sysname):
        command = """
            lssyscfg -r sys -F name,state,type_model,serial_num | grep Operating | egrep -v "Authentication|No Connection|Mismatch|Power|HSCL" | while IFS=, read -r MSNAME _ MSMODEL MSSERIAL; do
                lssyscfg -r lpar -m $MSNAME -F name,lpar_env,os_version,state,rmc_ipaddr,rmc_state,curr_lpar_proc_compat_mode,lpar_id | while IFS=, read -r LPARNAME LPARENV LPAROS LPARSTATE LPARIP RMCSTATE PROC_COMPAT LPARID; do
                    HMCNAME=$(uname -n | cut -f 1 -d .)
                    LPARNAME=${LPARNAME// /-}
                    LPARENV=${LPARENV// /-}
                    LPAROS=${LPAROS// /-}
                    LPARSTATE=${LPARSTATE// /-}
                    LPARIP=${LPARIP// /-}
                    RMCSTATE=${RMCSTATE// /-}
                    PROC_COMPAT=${PROC_COMPAT// /-}
                    LPARID=${LPARID// /-}
                    echo "$HMCNAME,$MSNAME,$MSMODEL,$MSSERIAL,$LPARNAME,$LPARENV,$LPAROS,$LPARSTATE,$LPARIP,$RMCSTATE,$PROC_COMPAT,$LPARID"
                done
            done
            """
        return self.execute_command(command, "No LPARs found")

    def execute_command(self, command, error_message):
        try:
            output = self.ssh_client.execute_command(command)
            data = [i.rstrip('\n').strip() for i in output]
            if not data:
                self.log.info(error_message)
            return data
        except Exception as e:
            self.log.error(f"Failed to execute command: {command}", exc_info=True)
