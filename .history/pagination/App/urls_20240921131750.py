from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls'))
]
