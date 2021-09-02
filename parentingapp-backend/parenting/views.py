from django.shortcuts import render, redirect
from .models import Kid, Todo
from .forms import KidForm



# Create your views here.
def kid_form(request):
    if request.method == "POST":
        form = KidForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            return render(request, "parenting/kid_form.html", {"obj": obj})
    else:
        form = KidForm()
    img = Kid.objects.all()

    return render(request, "parenting/kid_form.html", {"img": img, "form": form})


def todo_list(request):
    todo = Todo.objects.all()
    return render(request, 'nostaldja/fad_list.html', {'fads': fads})

 

