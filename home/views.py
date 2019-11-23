from django.shortcuts import render


# Create your views here.
def test(request):
    user=request.user

    
    name = request.GET['text']

    print(name)

    import emojis
    
    text=emojis.decode('{}'.format(name))
    text=text.replace(":"," ")
    print(text)
    

    #if request.method =='POST':
        #text=request.POST.get('msgbox','None')
        #print(text)

    return render(request,'index.html',{'name':text})
