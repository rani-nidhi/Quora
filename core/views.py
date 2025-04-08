from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from .models import Question, Answer
from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def home(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'questions': questions})

@login_required
def post_question(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Question.objects.create(user=request.user, title=title, description=description)
        return redirect('home')
    return render(request, 'post_question.html')

@login_required
def question_detail(request, pk):
    question = Question.objects.get(pk=pk)
    if request.method == 'POST':
        content = request.POST['content']
        Answer.objects.create(question=question, user=request.user, content=content)
        return redirect('question_detail', pk=pk)
    return render(request, 'question_detail.html', {'question': question})

@login_required
def like_answer(request, answer_id):
    answer = Answer.objects.get(id=answer_id)
    answer.likes.add(request.user)
    return redirect('question_detail', pk=answer.question.id)