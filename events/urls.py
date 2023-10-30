from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_event),
    path('get/', views.get_events),
    path('get/<int:pk>', views.get_event),
    path('update/<int:pk>', views.update_event),
    path('delete/<int:pk>', views.delete_event),
    path('register/<int:pk>', views.register_assistant),
    path('unregister/<int:pk>', views.unregister_assistant),
]


