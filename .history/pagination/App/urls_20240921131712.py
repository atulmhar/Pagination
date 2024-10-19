urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('App.urls'))
]