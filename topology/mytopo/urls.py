from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home, name='home'),
    path('Topology/', views.showTopology, name='showTopology'),
    path('Topologyy/',views.Topologyy,name='Topologyy'),
    path('NewTopology/', views.NewTopology,name='NewTopology'),
    path('Station/', views.Station, name='Station'),
    path('Company/', views.Company_Emp, name ='Company_Emp'),
]
