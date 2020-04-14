from django.urls import path

from . import views
# добавление вьюшек т.е. соответствующих им ЮРЛ
urlpatterns = [
    path('', views.home_view, name='home'),
    path('stats/', views.stats_view, name='stats'),
    path('faq/', views.faq_view, name='faq'),
]

# path('index/', views.index, name='index'), # показать вьюшку index_view при переходе на "websitename/index"
