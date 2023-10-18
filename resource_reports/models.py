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
    lpar_ip = models.GenericIPAddressField("Lpar IP Address", null=True, blank=True)
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
    min_mem = models.FloatField("Min Memory", null=True, blank=True)
    desired_mem = models.FloatField("Desired Memory", null=True, blank=True)
    max_mem = models.FloatField("Max Memory", null=True, blank=True)
    mem_mode = models.FloatField("Memory Mode", null=True, blank=True)
    proc_mode = models.FloatField("CPU Mode", null=True, blank=True)
    min_proc_units = models.FloatField("Min Proc Units", null=True, blank=True)
    desired_proc_units = models.FloatField("Desired Proc Units", null=True, blank=True)
    max_proc_units = models.FloatField("Max Proc Units", null=True, blank=True)
    min_procs = models.FloatField("Min Procs", null=True, blank=True)
    desired_procs = models.FloatField("Desired Procs", null=True, blank=True)
    max_procs = models.FloatField("Max Procs", null=True, blank=True)
    sharing_mode = models.CharField("Sharing Mode", null=True, blank=True)
    uncap_weight = models.FloatField("Uncapped Weight", default=128, null=True, blank=True)

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
    configurable_sys_proc_units = models.FloatField("Configurable Proc Units", null=True, blank=True)
    curr_avail_sys_proc_units = models.FloatField("Available Proc Units", null=True, blank=True)
    deconfig_sys_proc_units = models.FloatField("Deconfigured Proc Units", null=True, blank=True)

    class Meta:
        verbose_name_plural = "Managed System CPU"
        verbose_name = "MS CPU Config"
        db_table = "ms_cpu"

    def __str__(self):
        return self.ms_name


class ManagedSystemMemory(models.Model):
    hmc_name = models.CharField("HMC Name", max_length=150, null=True, blank=True)
    ms_name = models.CharField("Managed System", max_length=150, null=True, blank=True)
    configurable_sys_mem = models.FloatField("Configurable Memory", null=True, blank=True)
    curr_avail_sys_mem = models.FloatField("Available Memory", null=True, blank=True)
    deconfig_sys_mem = models.FloatField("Deconfigured Memory", null=True, blank=True)
    sys_firmware_mem = models.CharField("System Firmware Memory", null=True, blank=True)
    mem_region_size = models.FloatField("Memory Region Size", default=256, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Managed System Memory"
        db_table = "ms_mem"

    def __str__(self):
        return self.ms_name
