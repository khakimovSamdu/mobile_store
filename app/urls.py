from django.urls import path
from .views import home, get_add, get_all, brend_item_delete, brend_item_update, get_brend_id
urlpatterns = [
    path('', home),
    path('add/', get_add),
    path('all/', get_all),
    path('delete/<int:id>', brend_item_delete),
    path('update/<int:id>', brend_item_update),
    path('id/<int:id>/', get_brend_id),
]