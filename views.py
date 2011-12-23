from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(req):
    return render_to_response('index.html', { 'text': 'initial commit' })
