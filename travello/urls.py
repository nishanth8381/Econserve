from django.urls import path

from . import views

urlpatterns = [
	path('Essay',views.essay,name='Essay'),
	path('nuclear',views.essaynuclear,name='nuclear'),
	path('air',views.essayair,name='air'),
	path('',views.index, name='index'),
	path('home',views.index, name='index'),
	path('prototypes',views.prototypes,name='prototypes'),
	path('Smart-Taps',views.Smarttaps,name='Smart-Taps'),
	path('world',views.world,name='world'),
	path('protohome',views.protohome,name='protohome'),
	path('The_U-no_Technique',views.Uno,name='The_U-no_Tehnique')
	]