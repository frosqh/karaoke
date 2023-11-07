from django.shortcuts import render, get_object_or_404, redirect
from .models import Theme, Song
from django.http import HttpResponseNotFound
import random

# Create your views here.
def choose_theme(request):
    theme1, theme2 = random.sample(list(Theme.objects.filter(used=False)), 2)
    return render(request, 'kara/choose_theme.html', {'theme1': theme1, 'theme2': theme2, 'unusedthemes': len(list(Theme.objects.filter(used=False))), 'allthemes':len(Theme.objects.all())})

def choose_song(request, pk):
    songs = Song.objects.filter(theme=pk)
    theme = Theme.objects.filter(pk=pk)[0]
    theme.used = True
    theme.save()
    if len(songs) == 2:
        return render(request, 'kara/choose_song_2.html', {'song1':songs[0], 'song2':songs[1], 'theme':theme})
    elif len(songs) == 3:
        return render(request, 'kara/choose_song_3.html', {'song1':songs[0], 'song2':songs[1], 'song3':songs[2], 'theme':theme})
    elif len(songs) == 4:
        return render(request, 'kara/choose_song_4.html', {'song1':songs[0], 'song2':songs[1], 'song3':songs[2], 'song4': songs[3], 'theme':theme})
    return HttpResponseNotFound(songs)

def reset(request):
    Theme.objects.all().update(used=False)
    return redirect('choose_theme')