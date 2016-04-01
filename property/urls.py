from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^add-property/', views.addProperty),
    url(r'^insert-property/', views.insertProperty),
    url(r'^edit-property/(\d+)/$', views.editProperty),
    url(r'^delete-property/(\d+)/$', views.deleteProperty),
    url(r'^update-property/', views.updateProperty),
    url(r'^list-properties/$', views.listProperties),
    url(r'^list-properties-crud/$', views.listPropertiesCRUD),
    url(r'^list-property/(\d+)/$', views.listProperty),
    url(r'^search/', views.search),

]
