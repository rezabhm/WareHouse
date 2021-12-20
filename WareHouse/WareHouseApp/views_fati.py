from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from . import models

# Create your views here.

