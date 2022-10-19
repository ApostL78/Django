from django.shortcuts import render, redirect
from .models import Task, Categories
from .forms import TaskForm
from django.views.generic import ListView, DetailView, CreateView
# from django.urls import  reverse_lazy


class HomeTask(ListView):
    model = Task
    template_name = 'body/task_list.html'
    context_object_name = 'tasks'
    extra_context = {'title': 'Главная'}
    allow_empty = False # если пустой, то выведет 404


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeTask, self).get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):
        return Task.objects.filter(is_published=True).select_related('category')


class ViewTask(ListView):
    model = Task
    context_object_name = 'categories'
    template_name = 'body/list_categories.html'

    def get_queryset(self):
        return Task.objects.filter(category=self.kwargs['pk'])
    # pk_url_kwarg = 'category_id'

class CreateTask(CreateView):
    form_class = TaskForm
    template_name = 'body/add_task.html'
    # success_url = reverse_lazy('home') лучше get_absolute_url в модели чем ето



def about(request):
    return render(request,'body/about.html')

def get_category(request, category_id):
    tasks = Task.objects.filter(category_id=category_id)
    category = Categories.objects.get(pk=category_id)
    return render(request, 'body/category.html', {'tasks': tasks, 'category': category})


# def index(request):
#     task = {
#         'title': 'Главная cтраница сайта',
#             }
#     return render(request,'body/index.html', task)


# def add_task(request):
#     if request.method == "POST":
#         # form = TaskForm(request.POST)
#         # if form.is_valid():
#         #     task = Task.objects.create(**form.cleaned_data)
#         #     return redirect('home')
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save()
#             return redirect('home')
#     else:
#         form = TaskForm()
#     return render(request, 'body/add_task.html', {'form': form})

# merge to master from console

# commit 2
# commit3
# commit3
# commit3
