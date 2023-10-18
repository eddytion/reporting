from celery import shared_task
from .models import ManagedSystemVM, MemoryCpuVM, ManagedSystemCPU, ManagedSystemMemory


@shared_task
def import_data():
    # Your data import logic here
    # E.g., fetch data from IBM HMC and save it to your models
    pass
