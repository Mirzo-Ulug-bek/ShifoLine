from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from .models import Region, Hospital, Department, Doctor
from django.http import JsonResponse
from django.views.generic import TemplateView, CreateView
import json


class Home(TemplateView):
    template_name = 'index.html'


# **1. Region Views**
# class RegionListView(TemplateView):
#     template_name = 'navbar.html'
#
#     def get_context_data(self,  **kwargs):
#         cnt = super().get_context_data(**kwargs)
#         cnt['regions'] = Region.objects.order_by('id')
#         print("Regions:", cnt['regions'])
#         print('asassasaa')# Konsolga chiqarib ko‘rish
#         return cnt


# **2. Hospital Views**
class HospitalListView(View):
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        region_name = request.GET.get('region')

        if region_name:
            hospitals = Hospital.objects.filter(region__name=region_name)  # Faqat tanlangan regionni olish
        else:
            hospitals = Hospital.objects.all()

        ctx = {
            'hospitals': hospitals,
        }
        return render(request, 'blog.html', ctx)


def hospital_detail(request, slug):
    hospital = get_object_or_404(Hospital, slug=slug)
    context = {
        'hospital': hospital,

    }
    return render(request, 'single-blog.html', context)


# **3. Department Views**
class DepartmentListView(ListView):
    model = Department
    template_name = 'department_list.html'
    context_object_name = 'departments'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'department_detail.html'
    context_object_name = 'department'


# **4. Doctor Views**
class DoctorListView(ListView):
    model = Doctor
    template_name = 'doctor_list.html'
    context_object_name = 'doctors'


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctor_detail.html'
    context_object_name = 'doctor'


class HospitalMapListView(View):
    template_name = 'google_map.html'

    def get_center(self, hospitals):
        """Hospitallar orqali markazni aniqlash"""
        if hospitals.exists():
            first_hospital = hospitals.first()  # Birinchi hospital koordinatasini olish
            if first_hospital.latitude and first_hospital.longitude:
                return {"lat": first_hospital.latitude, "lng": first_hospital.longitude}

        return {"lat": 41.2995, "lng": 69.2401}

    def get(self, request, *args, **kwargs):
        region_name = request.GET.get('region')

        if region_name:
            hospitals = Hospital.objects.filter(region__name=region_name)  # Faqat tanlangan regionni olish
        else:
            hospitals = Hospital.objects.all()
        center = self.get_center(hospitals)  # Markazni aniqlash
        hospitals_data = list(hospitals.values('name', 'latitude', 'longitude', 'address'))  # JSON uchun ma'lumot
        ctx = {
            'map_center': json.dumps(center),  # Markazni JSON sifatida template-ga uzatamiz
            'hospitals_json': json.dumps(hospitals_data, ensure_ascii=False)  # JSON sifatida template-ga uzatamiz
        }
        return render(request, 'google_map.html', ctx)