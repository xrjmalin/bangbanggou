from django.http import HttpResponse
from django.shortcuts import render
from django import forms
 
def serach_form(request):
    return render(request,"serach_form.html")


# class StuMform(forms.Form):
#     stuid = forms.CharField(label=u'',max_length=12)
#     password = forms.CharField(label=u'',widget=forms.PasswordInput())
#     name = forms.CharField(label=u'',max_length=30)
#     address = forms.CharField(label=u'',max_length=40)
#     phonenum = forms.CharField(label=u'',max_length=11)

# def regist(request):
#     if request.method =='POST':
#         stumform = StuMform(request.POST)
#         if stumform.is_valid():
#             stuid = stumform.cleaned_data['stuid']
#             password = stumform.cleaned_data['password']
#             name = stumform.cleaned_data['name']
#             address = stumform.cleaned_data['address']
#             phonenum = stumform.cleaned_data['phonenum']

#             StuM.objects.create(stuid=stuid,password=password,name=name,address=address,phonenum=phonenum)
#             StuM.save()
#             return HttpResponse('regist success!!!')
#     else:
#         stumform = StuMform()
#     return render(request,'bbg2.html')

# def login(request):
#     if request.method =='POST':
#         stumform = StuMform(request.POST)
#         if stumform.is_valid():
#             stuid = stumform.clean_data['stuid']
#             password = stumform.clean_data['password']

#             stum = StuM.object.filter(stuid_exact=stuid,password_exact=password)

#             if stum:
#                 return render(request,'frirstcontent.html')
#             else:
#                 return HttpResponse('')
    
#     else:
#         stumform = StuMform()

#     return render(request,'bbg2.html')

# def index(request):
#     return render(request,'index.html')

# def firstcontent(request):
#     return render(request,'frirstcontent.html')

def serach(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = 'content: ' + request.GET['q']
    else:
        message = ''
    return HttpResponse(message)