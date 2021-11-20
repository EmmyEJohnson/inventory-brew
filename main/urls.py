from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    # Authentication routes
    path('registration/login/', views.Login.as_view(), name="login-user"), 
    path('registration/signup/', views.Signup.as_view(), name="signup"),
    # Profile routes
    path('profile/<int:pk>/', views.ProfilePage.as_view(), name="profile"),
    path('profile/<int:pk>/update', views.ProfileUpdate.as_view(), name="profile_update"),
    path('profile/<int:pk>/picture', views.ProfilePictureUpdate.as_view(), name="profile_picture_update"),
    # Post routes
    path('post/<slug:slug>/new', views.ProfilePostCreate.as_view(), name="profile_post_create"),
    path('post/<slug:slug>/update', views.ProfilePostUpdate.as_view(), name="profile_post_update"),
    path('post/<slug:slug>/delete', views.ProfilePostDelete.as_view(), name="profile_post_delete"),
    path('post/<slug:slug>', views.PostDetail.as_view(), name="post_detail"),
    # Comment route
    path('post/<slug:slug>/comments/new', views.CommentCreate.as_view(), name="comment_create"),
    path('post/<slug:post_pk>/comment/<slug:slug>/update', views.CommentUpdate.as_view(), name="comment_update"),
    path('post/<slug:post_pk>/comment/<slug:slug>/delete', views.CommentDelete.as_view(), name="comment_delete"),
    # City routes
    path('city/', views.CityList.as_view(), name="city_list"),
    path('city/<slug:slug>/post/new', views.Post_Create.as_view(), name="post_create"),
    path('city/<slug:city_pk>/post/<slug:slug>/update', views.Post_Update.as_view(), name="post_update"),
    path('city/<slug:city_pk>/post/<slug:slug>/delete', views.Post_Delete.as_view(), name="post_delete"),
    path('city/<slug:slug>', views.CityDetail.as_view(), name="city_detail"),
] 
