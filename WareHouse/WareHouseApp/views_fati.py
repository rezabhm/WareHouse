from django.shortcuts import render, HttpResponse
from django.template import loader

# Create your views here.


def main(request):

    """
    this is main & primary page
    """

    # load main.html for render
    main_template = loader.get_template('WareHouseApp/main.html')

    return HttpResponse(main_template.render())


def contact(request):

    """
    this is show how people contact to us
    """

    # load contact.html for render
    contact_template = loader.get_template('WareHouseApp/contact.html')

    return HttpResponse(contact_template.render())


def about(request):

    """
    this is give some information about our's work
    """

    # load about.html for render
    about_template = loader.get_template('WareHouseApp/about.html')

    return HttpResponse(about_template.render())
