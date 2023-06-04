from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('urunler/',views.products,name='products'),
    path('iletisim/',views.contact,name='contact'),
    path('uretim/',views.production,name='production'),
    path('kurumsal/hakkimizda/',views.about,name='about'),
    path('kurumsal/vizyonumuz-misyonumuz/',views.vision,name='vision'),
    path('kurumsal/kalite/', views.quality, name='quality'),
    path('kurumsal/tezgah-parkuru/', views.bench, name='bench'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
