from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from todoapp.models import TodoContent
from . forms import ToDoForm


@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo-home')
        else:
            form = ToDoForm()
    context = {
        'todos': TodoContent.objects.all().order_by('-date_posted')
    }
    return render(request, 'todoapp/home.html', context)


class PostListView(LoginRequiredMixin, ListView):
    model = TodoContent
    template_name = 'todoapp/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'todos'
    ordering = ['-date_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = context['todos'].filter(author=self.request.user)
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = TodoContent
    form_class = ToDoForm
    template_name = 'todoapp/home.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        if form.is_valid():
            form.save()
            return redirect('todo-home')
        else:
            form = TodoContent()


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = TodoContent
    form_class = ToDoForm
    template_name = 'todoapp/update.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            return redirect('todo-home')
        else:
            form = TodoContent()


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = TodoContent
    template_name = 'todoapp/delete.html'
    success_url = '/'
