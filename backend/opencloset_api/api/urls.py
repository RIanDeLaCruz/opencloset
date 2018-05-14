from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^users/$', UserList.as_view()),
    url(r'^user/(?P<pk>[0-9]+)$', UserDetail.as_view(), name='user-detail'),
    url(r'^items/$', ItemList.as_view()),
    url(r'^item/(?P<pk>[0-9]+)$', ItemDetail.as_view(), name='item-detail'),
    url(r'^sections/$', ItemSectionList.as_view()),
    url(r'^section/(?P<pk>[0-9]+)$', ItemSectionDetail.as_view(), name='itemsection-detail'),
    url(r'^categories/$', ItemCategoryList.as_view()),
    url(r'^category/(?P<pk>[0-9]+)$', ItemCategoryDetail.as_view(), name='itemcategory-detail'),
    url(r'^login/', Login.as_view())
]
