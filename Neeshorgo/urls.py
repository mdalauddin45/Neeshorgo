from django.contrib import admin
from django.urls import path,include
from core.views import HomeView, AboutView, RoomView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('rooms/', RoomView.as_view(), name='rooms'),
    path('accounts/', include('accounts.urls')),
    path('room/', include('room.urls')),
    path('transactions/', include('transactions.urls')),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)