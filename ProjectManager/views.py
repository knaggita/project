# Create your views here.
from django.http import HttpResponse
from django.template import loader, Context
from ProjectManager.models import ActionPlan, Contact


def tasks(request):
    entries = ActionPlan.objects.all()
    t = loader.get_template('tasks.html')
    c = Context({
        'ActionPlan': entries
    })

    return HttpResponse(t.render(c))


def contact(request):
    entries = Contact.objects.all()
    t = loader.get_template('contacts.html')
    c = Context({
        'Contacts': entries
    })

    return HttpResponse(t.render(c))


def index(request):
    t = loader.get_template('index.html')

    return HttpResponse(t.render())
