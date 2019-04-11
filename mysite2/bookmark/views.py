from django.shortcuts import render, get_object_or_404
from .models import Bookmark
# Create your views here.
def BookmarkLV(request):
    bookmarks = Bookmark.objects.all()
    for bookmark in bookmarks:
        print("ID : {}, Title : {}, URL : {}".format(bookmark.id, bookmark.title, bookmark.url))
    return render(request, 'bookmark_list.html', {'bookmarks': bookmarks})

def BookmarkDV(request, pk):
    bookmark1 = get_object_or_404(Bookmark, pk=pk)
    bookmark2 = Bookmark.objects.get(pk=pk)

    print("ID : {}, Title : {}, URL : {}".format(bookmark1.id, bookmark1.title, bookmark1.url))
    #print("ID : {}, Title : {}, URL : {}".format(bookmark2.id, bookmark2.title, bookmark2.url))

    return render(request, 'bookmark_detail.html', {'object': bookmark1})
