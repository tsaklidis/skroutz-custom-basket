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

    # View Saved lists
    url('^lists/all', views.all_lists, name='all_lists'),

    url('^create/list', views.list_create, name='list_create'),

    url('^add/item/to/list', views.add_item, name='add_item'),


]
