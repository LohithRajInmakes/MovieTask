from django.http import HttpResponse
from django.shortcuts import render, redirect

from moviesapp.forms import MovieForm
from moviesapp.models import Movie


# Create your views here.
def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    movie_detail=Movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie_detail':movie_detail})

def add_movie(request):
    if request.method == "POST":
        movie_title=request.POST.get('title')
        movie_desc=request.POST.get('description')
        movie_year=request.POST.get('year')
        movie_image=request.FILES['image']
        movies_added=Movie(title=movie_title,description=movie_desc,year=movie_year,image=movie_image)
        movies_added.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    movie_update=Movie.objects.get(id=id)
    form_update=MovieForm(request.POST or None,request.FILES,instance=movie_update)
    if form_update.is_valid():
        form_update.save()
        return redirect('/')
    return render(request,'edit.html',{'updatedForm':form_update})

def delete(request,id):
    if request.method == "POST":
        deleteMovie=Movie.objects.get(id=id)
        deleteMovie.delete()
        return redirect('/')
    return render(request,'delete.html')
