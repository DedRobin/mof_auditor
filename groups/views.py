from django.shortcuts import render


def create_group(request, username):
    return render(request, "create_group_page.html")
