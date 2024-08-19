from django.shortcuts import render,redirect
from web1.models import FrontEnd,BackEnd,Skill,Resume,Contact
from django.contrib import messages

# Create your views here.
def home(request):
    frontend = FrontEnd.objects.all()
    backend = BackEnd.objects.all()
    skill = Skill.objects.all()
    file = Resume.objects.all()


    contaxt = {
        'frontend':frontend,
        'backend':backend,
        'skill':skill,
        'file':file,
    }
    return render(request,'web1/home.html',contaxt)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        messages.success(request,'Submitted',name)
        query = Contact(name=name,email=email,subject=subject,message=message)
        query.save()
    return redirect('home')


def redirect2lms(request):
    return render(request,'web3/lms.html')

def redirect2curd(request):
    return render(request,'web2/curd.html')

def redirect2todo(request):
    return render(request,'web1/todo.html')

def redirect2cmd(request):
    return render(request,'web3/cmd.html')




