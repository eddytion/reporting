from django.db import models


class ManagedSystemVM(models.Model):
    hmc_name = models.CharField("HMC Name", max_length=50, null=True, blank=True)
    ms_name = models.CharField("Managed System", max_length=100, null=True, blank=True)
    ms_model = models.CharField("Managed System Model", max_length=50, null=True, blank=True)
    ms_power_type = models.CharField("Managed System Type", max_length=50, null=True, blank=True)
    ms_serial = models.CharField("Managed System Serial", max_length=50, null=True, blank=True)
    lpar_name = models.CharField("Lpar Name", max_length=50, null=True, blank=True)
    lpar_env = models.CharField("Lpar Env", max_length=50, null=True, blank=True)
    lpar_os = models.CharField("Lpar OS", max_length=100, null=True, blank=True)
    lpar_state = models.CharField("Lpar State", max_length=50, null=True, blank=True)
    lpar_ip = models.CharField("Lpar IP Address", max_length=150, null=True, blank=True)
    rmc_state = models.CharField("RMC State", max_length=20, null=True, blank=True)
    curr_lpar_proc_compat_mode = models.CharField("Proc Compat Mode", max_length=20, null=True, blank=True)
    lpar_id = models.CharField("LPAR ID", null=True, blank=True)

    class Meta:
        verbose_name_plural = "LPAR Inventory"
        verbose_name = "LPARS"
        db_table = "lpar_ms"

    def __str__(self):
        return self.lpar_name


class MemoryCpuVM(models.Model):
    profile_name = models.CharField("Profile Name", max_length=150, null=True, blank=True)
    lpar_name = models.CharField("LPAR Name", max_length=150, null=True, blank=True)
    min_mem = models.CharField("Min Memory", null=True, blank=True)
    desired_mem = models.CharField("Desired Memory", null=True, blank=True)
    max_mem = models.CharField("Max Memory", null=True, blank=True)
    mem_mode = models.CharField("Memory Mode", null=True, blank=True)
    proc_mode = models.CharField("CPU Mode", null=True, blank=True)
    min_proc_units = models.CharField("Min Proc Units", null=True, blank=True)
    desired_proc_units = models.CharField("Desired Proc Units", null=True, blank=True)
    max_proc_units = models.CharField("Max Proc Units", null=True, blank=True)
    min_procs = models.CharField("Min Procs", null=True, blank=True)
    desired_procs = models.CharField("Desired Procs", null=True, blank=True)
    max_procs = models.CharField("Max Procs", null=True, blank=True)
    sharing_mode = models.CharField("Sharing Mode", null=True, blank=True)
    uncap_weight = models.CharField("Uncapped Weight", default=128, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Memory / CPU for LPARs"
        verbose_name = "Memory/CPU Config"
        db_table = "mem_cpu_lpars"

    def __str__(self):
        return self.lpar_name


class ManagedSystemCPU(models.Model):
    hmc_name = models.CharField("HMC Name", max_length=150, null=True, blank=True)
    ms_name = models.CharField("Managed System", max_length=150, null=True, blank=True)
    ms_model = models.CharField("Managed System Type", max_length=150, null=True, blank=True)
    ms_power_type = models.CharField("Managed System CPU Type", max_length=150, null=True, blank=True)
    configurable_sys_proc_units = models.CharField("Configurable Proc Units", null=True, blank=True)
    curr_avail_sys_proc_units = models.CharField("Available Proc Units", null=True, blank=True)
    deconfig_sys_proc_units = models.CharField("Deconfigured Proc Units", max_length=150, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Managed System CPU"
        verbose_name = "MS CPU Config"
        db_table = "ms_cpu"

    def __str__(self):
        return self.ms_name


class ManagedSystemMemory(models.Model):
    hmc_name = models.CharField("HMC Name", max_length=150, null=True, blank=True)
    ms_name = models.CharField("Managed System", max_length=150, null=True, blank=True)
    configurable_sys_mem = models.CharField("Configurable Memory", null=True, blank=True)
    curr_avail_sys_mem = models.CharField("Available Memory", null=True, blank=True)
    deconfig_sys_mem = models.CharField("Deconfigured Memory", null=True, blank=True)
    sys_firmware_mem = models.CharField("System Firmware Memory", null=True, blank=True)
    mem_region_size = models.CharField("Memory Region Size", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Managed System Memory"
        db_table = "ms_mem"

    def __str__(self):
        return self.ms_name
