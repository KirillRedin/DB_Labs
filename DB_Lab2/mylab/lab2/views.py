from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from dbconnect import DataBase

# Create your views here.

db = DataBase()

def flights(request):
    companies = db.get_list_of_companies()
    tracks = db.get_list_of_tracks()
    planes = db.get_list_of_planes()
    flights = db.get_list_of_flights()

    p = Paginator(flights, 20)

    page = request.GET.get('page')
    try:
        flights = p.page(page)
    except PageNotAnInteger:
        flights = p.page(1)
    except EmptyPage:
        flights = p.page(p.num_pages)

    return render(request, 'lab2/flights.html', {'flights': flights, 'companies': companies, 'planes': planes, 'tracks': tracks } )

def make_flight(request):
    if request.method == "POST":
        if request.POST["planename"] != "" and request.POST["track"] != "" \
                and request.POST["companyname"] != "" and request.POST["price"] != "":
            db.make_flight(request.POST)
        return redirect('/lab2')
    elif request.method == "GET":
        companies = db.get_list_of_companies()
        tracks = db.get_list_of_tracks()
        planes = db.get_list_of_planes()
        flights = db.get_list_of_flights()
        return render(request, 'lab2/add.html',
                      {'flights': flights, 'companies': companies, 'planes': planes, 'tracks': tracks})


def edit_flight(request, id):
    if request.method == 'GET':
        companies = db.get_list_of_companies()
        tracks = db.get_list_of_tracks()
        planes = db.get_list_of_planes()
        flight = db.get_flight(id)
        return render(request, 'lab2/edit.html',
                      {'flight': flight, 'companies': companies, 'planes': planes, 'tracks': tracks})

    elif request.method == 'POST':
        if request.POST["newplane"] != "" and request.POST["newtrack"] != "" and \
                        request.POST["newcompany"] != "" and request.POST["newprice"] != "":
            db.edit_flight(request.POST, id)
        return redirect('/lab2')

def delete_flight(request, id):
    db.delete_flight(id)
    return redirect('/lab2')

def top_companies(request):
    companies = db.getTopCompaniesAggregate()
    return render(request, 'lab2/top_companies.html', {'companies': companies})