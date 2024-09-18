from django.urls import path
from .views import *

urlpatterns = [

    path('', CarViewSet.as_view({'get': 'list', 'post': 'create'}), name='car_list'),
    path('<int:pk>/', CarViewSet.as_view({'get': 'retrieve',
                                          'put': 'update',
                                          'delete': 'destroy'}), name='car_detail'),
    path('user', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}), name='user_list'),
    path('user/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve',
                                                       'put': 'update',
                                                       'delete': 'destroy'}), name='user_detail'),

    path('category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('category/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve',
                                                        'put': 'update',
                                                        'delete': 'destroy'}), name='category_detail'),

    path('car_make/', CarMakeViewSet.as_view({'get': 'list', 'post': 'create'}), name='car_make_list'),
    path('car_make/<int:pk>/', CarMakeViewSet.as_view({'get': 'retrieve',
                                                       'put': 'update',
                                                       'delete': 'destroy'}), name='car_make_detail'),

    path('model/', ModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='model_list'),
    path('model/<int:pk>/', ModelViewSet.as_view({'get': 'retrieve',
                                                  'put': 'update',
                                                  'delete': 'destroy'}), name='model_detail'),

    path('bet/', BetViewSet.as_view({'get': 'list', 'post': 'create'}), name='bet_list'),
    path('bet/<int:pk>/', BetViewSet.as_view({'get': 'retrieve',
                                              'put': 'update',
                                              'delete': 'destroy'}), name='bet_detail'),

    path('comment/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment_list'),
    path('comment/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve',
                                                      'put': 'update',
                                                      'delete': 'destroy'}), name='comment_detail'),

]
