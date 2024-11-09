from django.urls import path
from .views import show_page, submit_comment,comment_form,index
urlpatterns = [
    path('pages/<int:page_number>/', show_page, name='show_page'),
    # path('feedback/', submit_comment, name='feedback'),
    path('comment/', comment_form, name='comment_form'),
    path('submit_comment/', submit_comment, name='submit_comment'),
    path('',index,name='index'),
]
