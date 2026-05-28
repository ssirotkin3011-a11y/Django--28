from django.contrib import admin
from django.urls import path

from app.views import home_view, current_time_view, workdir_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_view),
    path('current_time/', current_time_view),
    path('workdir/', workdir_view),
]