from django.conf.urls import url
from skroutzbasket.public import views

urlpatterns = [
    # Home page
    url('^$', views.home, name='home'),
    # Add item with ajax
    url('^item/add/', views.item_add, name='item_add'),
    # View spacific list
    url('^list/(?P<list_name>[\w.@+-]+)',
        views.list_view, name='list_view'),

    url('^create/list', views.list_create, name='list_create'),


]
