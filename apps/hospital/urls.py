from django.urls import path
from .views import (
    Home,
    HospitalListView, HospitalMapListView,
    DepartmentListView, DepartmentDetailView,
    DoctorListView, DoctorDetailView, hospital_detail
)

app_name = 'hospital'

urlpatterns = [
    # **Region URLs**
    path('home/', Home.as_view(), name='home'),
    path('hospital/', HospitalListView.as_view(), name='hospital_list'),
    path('hospital_map/', HospitalMapListView.as_view(), name='hospital_map_list'),
    path('hospital_detail/<slug:slug>/', hospital_detail, name='hospital_detail'),

    # **Hospital URLs**
    # path('hospitals/', HospitalListView.as_view(), name='hospital-list'),
    # path('hospitals/<int:pk>/', HospitalDetailView.as_view(), name='hospital-detail'),
    #
    # # **Department URLs**
    # path('departments/', DepartmentListView.as_view(), name='department-list'),
    # path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department-detail'),
    #
    # # **Doctor URLs**
    # path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    # path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
]