import MySQLdb as mdb
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.code import Code
import random
import redis

class DataBase(object):
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.mydb

    def get_list_of_companies(self):
        companies = [Company for Company in self.db.Companies.find()]
        return companies

    def get_list_of_planes(self):
        planes = [Plane for Plane in self.db.Planes.find()]
        return planes

    def get_list_of_tracks(self):
        tracks = [Track for Track in self.db.Tracks.find()]
        return tracks

    def get_list_of_flights(self):
        flights = [Flight for Flight in self.db.Flights.find()]
        return flights

    def delete_flight(self, id):
        self.db.Flights.delete_one({'_id': ObjectId(id)})

    def make_flight(self, request):
        Plane = self.db.Planes.find_one({'_id': ObjectId(request['planename'])})
        Company = self.db.Companies.find_one({'_id': ObjectId(request['companyname'])})
        Track = self.db.Tracks.find_one({'_id': ObjectId(request['track'])})
        flight = {'Planes' : Plane, 'Companies': Company, 'Tracks': Track, 'Price': request['price']}
        self.db.Flights.insert(flight)

    def get_flight(self, id):
        flight = self.db.Flights.find_one({'_id': ObjectId(id)})
        return flight

    def edit_flight(self,request, id):
        Plane = self.db.Planes.find_one({'_id': ObjectId(request['newplane'])})
        Company = self.db.Companies.find_one({'_id': ObjectId(request['newcompany'])})
        Track = self.db.Tracks.find_one({'_id': ObjectId(request['newtrack'])})
        flight = {'Planes' : Plane, 'Companies': Company, 'Tracks': Track, 'Price': request['newprice']}
        self.db.Flights.update_one({'_id': ObjectId(id)}, {'$set': flight})

    def getTopCompaniesAggregate(self):
        companies = list(self.db.Flights.aggregate(
            [{"$unwind": "$Companies.Name"}, {"$project": {"name": "$Companies.Name", "count": {"$add": [1]}}},
             {"$group": {"_id": "$name", "number": {"$sum": "$count"}}}, {"$sort": {"number": -1}}, {"$limit": 3}]
        ))
        print companies
        return companies

    def mapTopCompany(self):
        mapper = Code("""
                        function() {
                            var key = this.Companies.Name;
                            var value = {count : 1};
                            emit(key, value);
                        };
                        """)
        reducer = Code("""
                        function(key, values) {
                            var count = 0;
                            for(var i in values) {
                                count += values[i].count;
                            }
                            return {count: count};
                        };
                        """)
        result = self.db.Flights.map_reduce(mapper, reducer, 'result')
        res = list(result.find())
        print res

    def generate(self):
        for x in xrange(1, 50000):
            Company = random.choice(self.get_list_of_companies())
            Plane = random.choice(self.get_list_of_planes())
            Track = random.choice(self.get_list_of_tracks())
            flight = {'Planes' : Plane, 'Companies': Company, 'Tracks': Track, 'Price': random.randint(10, 1000)}
            self.db.Flights.insert(flight)




db = DataBase()
#db.mapTopCompany()
#db.generate()