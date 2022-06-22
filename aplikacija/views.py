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


def university(request):

    if request.method == 'POST':

        name = request.POST['full_name']

        math = int(request.POST['mat'])
        latvian = int(request.POST['lat'])
        foreign = int(request.POST['for'])

        can_apply = 'cannot'
        if math >= 40 and latvian >= 40 and foreign >= 40:
            can_apply = 'can'

        context = {
            'name': name,
            'can_apply': can_apply
        }

        return render(request,
                      template_name='uni.html',
                      context=context)

    return render(request,
                  template_name='uni_form.html')


def add_post(request):
    from datetime import datetime

    if request.method == 'POST':

        context = {
            'title': request.POST['title'],
            'content': request.POST['content'],
            'time': datetime.now(),
        }

        return render(request,
                      template_name='post.html',
                      context=context)

    return render(request,
                  template_name='add_post.html')
