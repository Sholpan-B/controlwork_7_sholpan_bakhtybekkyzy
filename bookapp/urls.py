from django.urls import path

from bookapp.views import index_view, edit_view, confirm_delete, delete_view, add_view, search_view

urlpatterns = [
    path("", index_view, name='index'),
    path("guest/", index_view, name='index'),
    path("guest/add", add_view, name='guest_add'),
    path('guest/edit/<int:pk>', edit_view, name='guest_edit'),
    path('guest/delete/<int:pk>', delete_view, name='guest_delete'),
    path('guest/confirm_delete/<int:pk>', confirm_delete, name='confirm_delete'),
    path("guest/search", search_view, name='search'),
]