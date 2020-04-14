from django.urls import path

from . import views
# добавление вьюшек т.е. соответствующих им ЮРЛ
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'), # показать вьюшку index_view при переходе на "websitename/index"
    path('home/', views.home_view, name='home')
]