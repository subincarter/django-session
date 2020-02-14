from django.shortcuts import render
from .form import  *
def home(request):
    form=session1
    if request.method=='POST':
        print("posted")
        form = session1(request.POST)
        if form.is_valid():
             request.session['id']=form.cleaned_data['name']
             print('created')
        return render(request, 'newhome.html', {'sess': form})



    return render(request,'newhome.html',{'sess':form})

def about(request):
      uid=request.session.get('id')
      return render(request,'newhome.html',{'data':uid})
def session(request):
    del request.session['id']
    return render(request, 'newhome.html')