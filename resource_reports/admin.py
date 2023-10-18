from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy
import csv
from django.http import HttpResponse
from .models import *
from django.contrib import admin


class ExportToCSV:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected Rows as CSV"


class VMViewAdmin(admin.ModelAdmin, ExportToCSV):
    list_display = ['lpar_name', 'hmc_name', 'ms_name', 'lpar_os', 'lpar_ip', 'rmc_state']
    search_fields = ['lpar_name', 'ms_serial', 'hmc_name']
    readonly_fields = ['lpar_id']
    actions = ['export_as_csv']


class ManagedSystemCPUViewAdmin(admin.ModelAdmin, ExportToCSV):
    list_display = ['ms_name', 'ms_model', 'ms_power_type', 'configurable_sys_proc_units', 'curr_avail_sys_proc_units',
                    'deconfig_sys_proc_units']
    search_fields = ['ms_name', 'ms_model', 'hmc_name']
    actions = ['export_as_csv']


class ManagedSystemMemoryViewAdmin(admin.ModelAdmin, ExportToCSV):
    list_display = ['ms_name', 'configurable_sys_mem', 'curr_avail_sys_mem', 'deconfig_sys_mem', 'sys_firmware_mem',
                    'mem_region_size']
    search_fields = ['ms_name', 'hmc_name']
    actions = ['export_as_csv']


class MemoryCpuVMViewAdmin(admin.ModelAdmin, ExportToCSV):
    list_display = ['lpar_name', 'min_mem', 'desired_mem', 'max_mem', 'mem_mode', 'proc_mode',
                    'min_proc_units', 'desired_proc_units', 'max_proc_units', 'min_procs', 'desired_procs', 'max_procs',
                    'sharing_mode', 'uncap_weight']
    search_fields = ['lpar_name']
    actions = ['export_as_csv']


admin.site.register(ManagedSystemVM, VMViewAdmin)
admin.site.register(MemoryCpuVM, MemoryCpuVMViewAdmin)
admin.site.register(ManagedSystemCPU, ManagedSystemCPUViewAdmin)
admin.site.register(ManagedSystemMemory, ManagedSystemMemoryViewAdmin)

AdminSite.site_title = gettext_lazy('SAP Inventory')
AdminSite.site_header = gettext_lazy('Admin Interface')
AdminSite.index_title = gettext_lazy('Resource Administration')
