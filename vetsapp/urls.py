from django.urls import path
from django.conf.urls.static import static
from . import views

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_DIR)

urlpatterns = [
    path('', views.index, name='home'),
    path('record', views.record, name='record'),
    path('accounts/profile/', views.profile_user, name='profile')
]
