from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lpars/', views.lpars, name='lpars'),
    path('vioses/', views.vioses, name='vioses'),
    path('hmcs/', views.hmcs, name='hmcs'),
    path('<str:server_name>/LiveLparSearch/', views.LiveLparSearch, name='LiveLparSearch'),
    path('<str:mac_addr>/MacAddrSearch/', views.MacAddrSearch, name='MacAddrSearch'),
    path('<str:wwpn>/WWPNSearch/', views.WWPNSearch, name='WWPNSearch'),
    path('<str:serial>/LunSearch/', views.LunSearch, name='LunSearch'),
    path('<str:hmc>/HMCDetails/', views.HMCDetails, name='HMCDetails'),
    path('<str:msname>/MSIoDev/', views.MSIoDev, name='MSIoDev'),
    path('<str:msname>/MSCpuMem/', views.MSCpuMem, name='MSCpuMem'),
    path('<str:msname>/MsFirmware/', views.MsFirmware, name='MsFirmware'),
    path('<str:msname>/GetAllLparsForMS/', views.GetAllLparsForMS, name='GetAllLparsForMS'),
    path('<str:lpar>/<str:lparenv>/getVMDetails/', views.getVMDetails, name='getVMDetails'),
    path('<str:lpar>/getVMStorage/', views.getVMStorage, name='getVMStorage'),
    path('<str:lpar>/getUUID/', views.getUUID, name='getUUID'),
    path('<str:hmc>/getMSListForHMC/', views.getMSListForHMC, name='getMSListForHMC'),
    path('<str:lpar>/getMACAddress/<int:vlan>', views.getMACAddress, name='getMACAddress'),
    path('<str:lpar>/getHMCName/', views.getHMCName, name='getHMCName'),
    path('<str:lpar>/getPostSetupParams/<str:osType>/', views.getPostSetupParams, name='getPostSetupParams'),
    path('reporting/mscounts/', views.get_ms_counts, name='mscount'),
]
