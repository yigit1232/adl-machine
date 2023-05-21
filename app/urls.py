from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('urunler/',views.products,name='products'),
    path('kalite/',views.quality,name='quality'),
    path('iletisim/',views.contact,name='contact'),
    path('uretim/',views.production,name='production'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
