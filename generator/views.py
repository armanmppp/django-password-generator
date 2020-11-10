from django.shortcuts import render
from django.shortcuts import redirect
import random
# Create your views here.

def index(request):
    context = {}
    if request.GET.get("error"):
        context["errormsg"] = "Please Write Length Between 0 to 12"
        return render(request,"generator/index.html",context)
    character = list("abcdefghijklmnopqrstuvwxyz")
    if request.GET.get("uppercase"):
        character.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get("number"):
        character.extend(list("0123456789"))
    if request.GET.get("spechial"):
        character.extend(list("!@#$%^&*()_+{}[]><?~"))

    length = int(request.GET.get("length"))
    if 0 <= length <= 12:
        password = ''
        for x in range(length):
            password += random.choice(character)

        context = {
            "password": password,
        }
        return render(request, "generator/index.html", context)
    else:
        redirection = redirect("/?error=true")
        return redirection
