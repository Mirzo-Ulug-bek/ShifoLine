from django import template
from apps.hospital.models import Region


register = template.Library()


@register.simple_tag
def navbar():
    return Region.objects.order_by('-id')

print("Navbar templatetag yuklandi!")  # Ishlayotganini tekshirish uchun