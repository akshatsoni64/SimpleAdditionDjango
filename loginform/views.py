from django.shortcuts import render
from .form import LoginForm


def index(request):
    submit1=request.POST.get("submit")
    a1 = ''
    b1 = ''
    form=LoginForm(request.POST or None)
    if form.is_valid():
        a1 = form.cleaned_data.get("a")
        b1 = form.cleaned_data.get("b")

    context={'form':form,'a1':a1,'b1':b1,'submit1':submit1}
    return render(request,'form.html',context)
def success(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        a1 = form.cleaned_data.get("a")
        b1 = form.cleaned_data.get("b")
        ans = int(a1) + int(b1)
    context = {'ans': ans}
    return render(request, 'success.html', context)