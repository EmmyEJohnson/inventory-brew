from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = "main"

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    
    path('upload/', views.Upload, name='upload'),
    path('brews/', views.BrewList, name='brew_list'),
    path('brews/upload/', views.UploadBrew, name='upload_brew'),
    path('brews/<int:pk>/', views.DeleteBrew, name='delete_brew'),

    path('vendor/brews/', views.BrewListView.as_view(), name='vendor_brew_list'),
    path('vendor/brews/upload/', views.UploadBrewView.as_view(), name='vendor_upload_brew'),
    # Authentication routes
    # path('registration/login/', views.VendorLogin.as_view(), name="vendor_login"), 
    # path('registration/vendor_signup/', views.VendorSignup.as_view(), name="vendor_signup"),
    # # Profile routes
    # path('profile/<int:pk>/', views.VendorProfilePage.as_view(), name="vendor_profile"),
    # path('profile/<int:pk>/update', views.VendorProfileUpdate.as_view(), name="vendor_profile_update"),
    # path('profile/<int:pk>/picture', views.VendorProfilePictureUpdate.as_view(), name="vendor_profile_picture_update"),
    # Brew routes

    # path('brew/<int:pk>/post/new', views.Post_Create.as_view(), name="post_create"),
    # path('brew/<int:brew_pk>/post/<int:pk>/update', views.Post_Update.as_view(), name="post_update"),
    # path('brew/<int:brew_pk>/post/<int:pk>/delete', views.Post_Delete.as_view(), name="post_delete"),
    # path('brew/<int:pk>', views.BrewDetail.as_view(), name="brew_detail"),
] 
