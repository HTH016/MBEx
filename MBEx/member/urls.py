from django.urls.conf import path
from member import views

urlpatterns = [
    path( "main", views.MainView.as_view(), name="main" ),
    path( "input", views.InputView.as_view(), name="input" ),
    path( "login", views.LoginView.as_view(), name="login" ),
    path( "logout", views.LogoutView.as_view(), name="logout" ),
    path( "confirm", views.ConfirmView.as_view(), name="confirm" ),
    path( "delete", views.DeleteView.as_view(), name="delete" ),
    path( "update", views.UpdateView.as_view(), name="update" ),
    path( "updatepro", views.UpdateProView.as_view(), name="updatepro" ), 
    ]
