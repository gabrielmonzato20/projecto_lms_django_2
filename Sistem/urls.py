from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('password_reset',views.reset,name='password_reset'),
    path('cadastra/funcionario/',views.cadastra_funcionario,name='cadastra_funcionario'),
    path('delete',views.deleta_tudo,name='cadastra_funcionario')
]
