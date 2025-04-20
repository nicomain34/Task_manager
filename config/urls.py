from django.contrib import admin
from django.urls import path
from tasks import views  # 🟢 додай це

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.task_list, name='task_list'),  # 🟢 тут ми викликаємо task_list
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
]
