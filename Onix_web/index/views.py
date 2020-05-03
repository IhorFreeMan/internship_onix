from django.shortcuts import render
# from django.shortcuts import get_object_or_404
# from blog.models import Post

"""
def index_one(request):
    return render_to_response('index/index.html')
"""
def index_one(request):
    return render(request, 'index/index.html')


