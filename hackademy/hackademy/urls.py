from django.contrib import admin
from django.urls import include, path
from activity1 import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('profile/', views.profile, name="profile"),
    path('login/', views.Login.as_view()),
    path('register/', views.registration),
    path('api/', include('api.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)