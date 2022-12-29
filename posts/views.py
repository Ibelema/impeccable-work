from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Article

# Create your views here.

#to show homepage
class ArticleListView(ListView):
    model = Article
    template_name = 'homepage.html'

#to show all posts we do this
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'post_article.html'

#to create a post
class PostCreateView(CreateView):
    model = Article
    template_name = 'new_post.html'
    fields = ['title', 'author', 'body', 'date_added']

#to edit a post
class EditPostView(UpdateView):
    """Edit an existing article."""
    model = Article
    template_name = 'edit.html'
    fields = ['title', 'body']
   
class DeletePostView(DeleteView):
    model = Article
    template_name = 'delete.html'
    sucess_url = reverse_lazy('home')

#to create a signup message in the email
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
    
        user = User.objects.create_user(
                username = username,
                password = password,
                email = email,
            )
        login(request, user)
        subject = 'welcome to my world'
        message = f"Hi {user.username}, thank you for registering with ibelema's newsletter."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email,]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('/dashboard/')
    return render(request, 'signup.html')


