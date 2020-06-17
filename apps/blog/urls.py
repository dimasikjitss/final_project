from django.urls import path
from . import views
# app_name = 'blog'
urlpatterns = [ 
    # post views
    path('', views.CategoryList.as_view(), name='categories'), 
    path('<slug:slug>/', views.PostCategory.as_view(), name='post_category' ),
    path('<slug:category>/<slug:slug>/', views.PostDetail.as_view(), name='post_detail' ),
    #   path('about/',views.About.as_view(), name='about'),

]
