from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView
<<<<<<< HEAD
# Create your views here.
=======
>>>>>>> e97243606961288decdfb0ba8314ac030cbecfff

def news_home(request):
    news=Articles.objects.order_by('-date')
    return render(request,'news/news_home.html',{'news':news})

<<<<<<< HEAD
def NewsDetailView(DetailView):
=======
class NewDetailView(DetailView):
>>>>>>> e97243606961288decdfb0ba8314ac030cbecfff
    model=Articles
    template_name='news/details_view.html'
    context_object_name='article'

<<<<<<< HEAD
    
=======
>>>>>>> e97243606961288decdfb0ba8314ac030cbecfff
def create(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма была не верной'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)