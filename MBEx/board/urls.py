from django.urls.conf import path
from board import views

app_name = "board"
urlpatterns = [
    path( "list", views.ListView.as_view(), name="list" ),
    path( "write", views.WriteView.as_view(), name="write" ),
    path( "content", views.ContentView.as_view(), name="content" ),
    path( "delete", views.DeleteView.as_view(), name="delete" ),
    path( "update", views.UpdateView.as_view(), name="update" ),
    path( "updatepro", views.UpdateProView.as_view(), name="updatepro" ),
    
    path( "image", views.ImageView.as_view(), name="image" ),
    path( "imagedown", views.ImageDownView.as_view(), name="imagedown" ),
    ]