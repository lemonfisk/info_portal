from django.http import HttpRequest, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from .forms import UserBioForm, UploadFileForm

# Create your views here.

def process_get_view(request: HttpRequest):
    a = request.GET.get("a", "")
    b = request.GET.get("b", "")
    result = a + b
    contex = {
        "a": a,
        "b": b,
        "result": result,
    }
    return render(request, "map_data/map-query-params.html", context=contex)


def user_form(request: HttpRequest) -> HttpResponse:
    context = {
        "form": UserBioForm(),
    }
    return render(request, "map_data/user-bio-form.html", context=context)


def hundle_file_upload(request: HttpRequest) -> HttpResponse:
    if request.method == "POST" :
    # if request.method == "POST" and request.FILES.get("myfile"):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # my_file = request.FILES["myfile"]
            my_file = form.cleaned_data["file"]
            fs = FileSystemStorage()
            filename = fs.save(my_file.name, my_file)
            print("saved filees", filename)
    else:
        form = UploadFileForm()
    context = {
        "form": form,
    }
    return render(request, "map_data/file-upload.html", context=context)
