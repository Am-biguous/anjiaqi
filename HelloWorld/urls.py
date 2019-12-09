from django.conf.urls import url
from django.contrib import admin
from novel import views
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$', views.main_Index),
    url(r'select/', views.select),
    url(r'pageSelect/', views.pageSelect),
    url(r'insert/', views.insert),
    url(r'pageInsert/', views.pageInsert),
    url(r'delete/', views.delete),
    url(r'pageDelete/', views.pageDelete),
    url(r'pageUpdate/', views.pageUpdate),
    url(r'update/', views.update),

]
