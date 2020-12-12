from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import HttpResponseRedirect
from recipe2.forms import AddAuthorForm, AddRecipeForm, AddLoginForm, AddSignupForm
from recipe2.models import Author, Recipe
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from recipe2.models import Recipe, Author, Favorites


def index(request):
    # my_title = Recipe.objects.all()
    return render(
        request,
        "index.html",
        {"Recipes": Recipe.objects.all(), "Authors": Author.objects.all()},
    )


def recipe_detail(request, recipe_id):
    my_recipe = Recipe.objects.get(id=recipe_id)
    return render(request, "recipe_detail.html", {"Recipe": my_recipe})


def author_detail(request, author_id):
    my_author = Author.objects.filter(id=author_id).first()
    return render(request, "author_detail.html", {"Author": my_author})


@login_required(login_url="/login/")
def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                username=data.get("username"), password=data.get("password")
            )
            Author.objects.create(
                name=data.get("name"), bio=data.get("bio"), user=request.user
            )
            return HttpResponseRedirect(request.GET.get("next", reverse("homepage")))
    form = AddAuthorForm()
    return render(request, "add_author.html", {"form": form})


@login_required(login_url="/login/")
def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            add_recipe = Recipe.objects.create(
                title=data.get("title"),
                time_required=data.get("time_required"),
                description=data.get("description"),
                instruction=data.get("instruction"),
                author=request.user.author,
            )
            return HttpResponseRedirect(reverse("homepage"))
    form = AddRecipeForm()
    return render(request, "add_recipe.html", {"form": form})


def author_favorite(request, author_id):
    author = Author.objects.get(id=author_id)
    favorite = Favorites.objects.filter(author=Author)
    return render(
        request, "favorites.html", {"favorites": favorite, "Author": author.name}
    )


@login_required
def favorite_recipe(request, recipe_id):
    Favorites.objects.create(
        author=Author.objects.get(user=request.user),
        recipe=Recipe.objects.get(id=recipe_id),
    )
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def login_view(request):
    if request.method == "POST":
        form = AddLoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data.get("username"), password=data.get("password")
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get("next", reverse("homepage"))
                )
    form = AddLoginForm()
    return render(request, "generic_form.html", {"form": form})


@login_required(login_url="/login/")
def edit_recipe_view(request, recipe_id):
    edit_recipe = Recipe.objects.get(id=recipe_id)
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            edit_recipe.title = data["title"]
            edit_recipe.description = data["description"]
            edit_recipe.time_required = data["time_required"]
            edit_recipe.instruction = data["instruction"]
            edit_recipe.save()
        return HttpResponseRedirect(reverse("homepage"))
    data = {
        "title": edit_recipe.title,
        "description": edit_recipe.description,
        "time_required": edit_recipe.time_required,
        "instruction": edit_recipe.instruction,
    }
    form = AddRecipeForm(initial=data)
    return render(request, "generic_form.html", {"form": form})


def signup_view(request):
    if request.method == "POST":
        form = AddSignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = User.objects.create_user(
                username=data.get("username"), password=data.get("password")
            )
            Author.objects.create(name=data.get("username"), user=new_user)
            login(request, new_user)
            return HttpResponseRedirect(reverse("homepage"))
    form = AddSignupForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))