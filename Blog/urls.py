from django.urls import path
from Blog.views import index, post_list, post_detail

app_name = "Blog"

urlpatterns = [
    path("", index, name="index"),
    path("posts/", post_list, name="post_list"),
    path("posts/<int:id>", post_detail, name="post_detail")
]