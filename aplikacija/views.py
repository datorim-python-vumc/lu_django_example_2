from django.shortcuts import render, HttpResponse


def say_hello(request):

    context = {
        'name': 'Roberts',
        'greeting': 'Čau'
    }

    return render(request,
                  template_name='hello.html',
                  context=context)


def get_time(request):
    from datetime import datetime

    context = {
        'time': datetime.now(),
    }
    return render(request,
                  template_name='time.html',
                  context=context)


def enter_name(request):

    if request.method == 'POST':
        name = request.POST['first_name']
        return HttpResponse(name)

    return render(request,
                  template_name='form.html')