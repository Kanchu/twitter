from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from forms import TweetForm
from models import Tweet

def home(request):
    return render_to_response ('home.html',RequestContext(request))

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def welcome(request):
    return render_to_response('welcome.html', RequestContext(request))

def tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            twit = Tweet()
            twit.tweet = form.cleaned_data['tweet']
            twit.name = request.user.username
            twit.save()
            return render_to_response('tweet.html',request)
    else:
        form = TweetForm()
        form.name = request.user
        variables = RequestContext(request, {
                'form': form
            })

        return render_to_response('tweet.html',RequestContext(request),variables)

def list_tweet(request):
    tweets = []
    queryset=Tweet.objects.all()
    for query in queryset:
        if request.user.username == query.name:
            tweets.append(query)
            variables = RequestContext(request,{'list_tweet': tweets})
    return render_to_response("list_tweet.html",variables)