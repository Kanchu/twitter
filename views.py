from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template.context import RequestContext
from forms import TweetForm
from models import Tweet
from django.views.decorators.csrf import csrf_protect

def home(request):
    return render_to_response ('home.html',RequestContext(request))

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

def welcome(request):
    tweets = []
    queryset=Tweet.objects.all()
    for query in queryset:
        if request.user.username == query.name:
            tweets.append(query)
    status = 'abc'
    for tweet in tweets:
        status = tweet.tweet
    return render_to_response('welcome.html', RequestContext(request,{'status':status}))

@csrf_protect
def tweet(request):

    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            twit = Tweet()
            status = twit.tweet = form.cleaned_data['tweet']
            twit.name = request.user.username
            twit.save()
            return render_to_response('tweet.html',{'request':RequestContext(request),'status':status})
        else:
            return render_to_response('tweet.html',{'request':RequestContext(request)})

    else:
        tweets = []
        queryset=Tweet.objects.all()
        for query in queryset:
            if request.user.username == query.name:
                tweets.append(query)
        status = 'abc'
        for tweet in tweets:
            status = tweet.tweet

        form = TweetForm()
        form.name = request.user
        variables = RequestContext(request, {
                'form': form,'status': status
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

def switch_language(request, language):
    request.session['django_language'] = language
    if request.META.has_key('HTTP_REFERER'):
        referer= '/' + '/'.join(request.META['HTTP_REFERER'].split('/')[3:])
    else:
        referer= '/'

    if referer[:4] in ["/en/", "/fr/"]:
        referer = "/%s/%s" % (language, referer[4:])

    return redirect(referer)
