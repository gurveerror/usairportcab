from django.shortcuts import render, get_object_or_404
from .models import Car, Car_fare, Site, Common_detail, Sites_common_detail
from django.http import HttpResponse
from django.http import *
from django.contrib import auth
from django.contrib.auth import REDIRECT_FIELD_NAME
import decimal
import datetime

# Create your views here.
def index(request):

    time_sloat1 = ("00:00 AM","00:15 AM","00:30 AM","00:45 AM","01:00 AM","01:15 AM","01:30 AM","01:45 AM","02:00 AM","02:15 AM","02:30 AM","02:45 AM","03:00 AM","03:15 AM","03:30 AM","03:45 AM","04:00 AM","04:15 AM","04:30 AM","04:45 AM","05:00 AM","05:15 AM","05:30 AM","05:45 AM","06:00 AM","06:15 AM","06:30 AM","06:45 AM","07:00 AM","07:15 AM","07:30 AM","07:45 AM","08:00 AM","08:15 AM","08:30 AM","08:45 AM","09:00 AM","09:15 AM","09:30 AM","09:45 AM","10:00 AM","10:15 AM","10:30 AM","10:45 AM","11:00 AM","11:15 AM","11:30 AM","11:45 AM","12:00 PM","12:15 PM","12:30 PM","12:45 PM","01:00 PM","01:15 PM","01:30 PM","01:45 PM","02:00 PM","02:15 PM","02:30 PM","02:45 PM","03:00 PM","03:15 PM","03:30 PM","03:45 PM","04:00 PM","04:15 PM","04:30 PM","04:45 PM","05:00 PM","05:15 PM","05:30 PM","05:45 PM","06:00 PM","06:15 PM","06:30 PM","06:45 PM","07:00 PM","07:15 PM","07:30 PM","07:45 PM","08:00 PM","08:15 PM","08:30 PM","08:45 PM","09:00 PM","09:15 PM","09:30 PM","09:45 PM","10:00 PM","10:15 PM","10:30 PM","10:45 PM","11:00 PM","11:15 PM","11:30 PM","11:45 PM")
    time_sloat2 = (
        "00:00:00", "00:15:00", "00:30:00", "00:45:00", "01:00:00", "01:15:00", "01:30:00", "01:45:00", "02:00:00",
        "02:15:00", "02:30:00", "02:45:00", "03:00:00", "03:15:00", "03:30:00", "03:45:00", "04:00:00", "04:15:00",
        "04:30:00", "04:45:00", "05:00:00", "05:15:00", "05:30:00", "05:45:00", "06:00:00", "06:15:00", "06:30:00",
        "06:45:00", "07:00:00", "07:15:00", "07:30:00", "07:45:00", "08:00:00", "08:15:00", "08:30:00", "08:45:00",
        "09:00:00", "09:15:00", "09:30:00", "09:45:00", "10:00:00", "10:15:00", "10:30:00", "10:45:00", "11:00:00",
        "11:15:00", "11:30:00", "11:45:00", "12:00:00", "12:15:00", "12:30:00", "12:45:00", "13:00:00", "13:15:00",
        "13:30:00", "13:45:00", "14:00:00", "14:15:00", "14:30:00", "14:45:00", "15:00:00", "15:15:00", "15:30:00",
        "15:45:00", "16:00:00", "16:15:00", "16:30:00", "16:45:00", "17:00:00", "17:15:00", "17:30:00", "17:45:00",
        "18:00:00", "18:15:00", "18:30:00", "18:45:00", "19:00:00", "19:15:00", "19:30:00", "19:45:00", "20:00:00",
        "20:15:00", "20:30:00", "20:45:00", "21:00:00", "21:15:00", "21:30:00", "21:45:00", "22:00:00", "22:15:00",
        "22:30:00", "22:45:00", "23:00:00", "23:15:00", "23:30:00", "23:45:00")
    time_sloat = zip(time_sloat1, time_sloat2)
    return render(request, "index.html", {'range': range(0, 9), 'time': time_sloat})

def isNowInTimePeriod(startTime, endTime, nowTime):
        return nowTime > startTime or nowTime < endTime

def getfare(request):
    time_sloat1 = (
    "00:00 AM", "00:15 AM", "00:30 AM", "00:45 AM", "01:00 AM", "01:15 AM", "01:30 AM", "01:45 AM", "02:00 AM",
    "02:15 AM", "02:30 AM", "02:45 AM", "03:00 AM", "03:15 AM", "03:30 AM", "03:45 AM", "04:00 AM", "04:15 AM",
    "04:30 AM", "04:45 AM", "05:00 AM", "05:15 AM", "05:30 AM", "05:45 AM", "06:00 AM", "06:15 AM", "06:30 AM",
    "06:45 AM", "07:00 AM", "07:15 AM", "07:30 AM", "07:45 AM", "08:00 AM", "08:15 AM", "08:30 AM", "08:45 AM",
    "09:00 AM", "09:15 AM", "09:30 AM", "09:45 AM", "10:00 AM", "10:15 AM", "10:30 AM", "10:45 AM", "11:00 AM",
    "11:15 AM", "11:30 AM", "11:45 AM", "12:00 PM", "12:15 PM", "12:30 PM", "12:45 PM", "01:00 PM", "01:15 PM",
    "01:30 PM", "01:45 PM", "02:00 PM", "02:15 PM", "02:30 PM", "02:45 PM", "03:00 PM", "03:15 PM", "03:30 PM",
    "03:45 PM", "04:00 PM", "04:15 PM", "04:30 PM", "04:45 PM", "05:00 PM", "05:15 PM", "05:30 PM", "05:45 PM",
    "06:00 PM", "06:15 PM", "06:30 PM", "06:45 PM", "07:00 PM", "07:15 PM", "07:30 PM", "07:45 PM", "08:00 PM",
    "08:15 PM", "08:30 PM", "08:45 PM", "09:00 PM", "09:15 PM", "09:30 PM", "09:45 PM", "10:00 PM", "10:15 PM",
    "10:30 PM", "10:45 PM", "11:00 PM", "11:15 PM", "11:30 PM", "11:45 PM")
    time_sloat2 = (
        "00:00:00", "00:15:00", "00:30:00", "00:45:00", "01:00:00", "01:15:00", "01:30:00", "01:45:00", "02:00:00",
        "02:15:00", "02:30:00", "02:45:00", "03:00:00", "03:15:00", "03:30:00", "03:45:00", "04:00:00", "04:15:00",
        "04:30:00", "04:45:00", "05:00:00", "05:15:00", "05:30:00", "05:45:00", "06:00:00", "06:15:00", "06:30:00",
        "06:45:00", "07:00:00", "07:15:00", "07:30:00", "07:45:00", "08:00:00", "08:15:00", "08:30:00", "08:45:00",
        "09:00:00", "09:15:00", "09:30:00", "09:45:00", "10:00:00", "10:15:00", "10:30:00", "10:45:00", "11:00:00",
        "11:15:00", "11:30:00", "11:45:00", "12:00:00", "12:15:00", "12:30:00", "12:45:00", "13:00:00", "13:15:00",
        "13:30:00", "13:45:00", "14:00:00", "14:15:00", "14:30:00", "14:45:00", "15:00:00", "15:15:00", "15:30:00",
        "15:45:00", "16:00:00", "16:15:00", "16:30:00", "16:45:00", "17:00:00", "17:15:00", "17:30:00", "17:45:00",
        "18:00:00", "18:15:00", "18:30:00", "18:45:00", "19:00:00", "19:15:00", "19:30:00", "19:45:00", "20:00:00",
        "20:15:00", "20:30:00", "20:45:00", "21:00:00", "21:15:00", "21:30:00", "21:45:00", "22:00:00", "22:15:00",
        "22:30:00", "22:45:00", "23:00:00", "23:15:00", "23:30:00", "23:45:00")
    time_sloat = zip(time_sloat1, time_sloat2)

    if request.method == 'POST':
        pickup = request.POST['from']
        dropoff = request.POST['to']
        ride_time = request.POST['time']
        ride_date = request.POST['datepicker']
        pax = int(request.POST['pax'])
        lugg = int(request.POST['lugg'])
        distance = decimal.Decimal(request.POST['key'])
        result = {}
        car_details = Car.objects.filter(pax__gte=pax, large_luggage__gte=lugg).first()
        #return HttpResponse(str(car.car_name))
        common_details = get_object_or_404(Common_detail, id=1)
        carfare = Car_fare.objects.filter(car_name__car_name__contains=car_details.car_name)
        i = 1
        for car in carfare:

            sitecommondetails = get_object_or_404(Sites_common_detail,company_name=car.site_name, booking_active="1.00")
            if distance <= common_details.distance_slab1:
                miles_price = (car.base_fare + car.fare1 * distance)
            elif (distance > common_details.distance_slab1) and (distance <= common_details.distance_slab2):
                miles_price = (car.base_fare + (car.fare2 * distance))
            elif (distance > common_details.distance_slab2) and (distance <= common_details.distance_slab3):
                miles_price = (car.base_fare + (car.fare3 * distance))
            elif (distance > common_details.distance_slab3) and (distance <= common_details.distance_slab4):
                miles_price = (car.base_fare + (car.fare4 * distance))
            elif (distance > common_details.distance_slab4) and (distance <= common_details.distance_slab5):
                miles_price = (car.base_fare + (car.fare5 * distance))
            elif (distance > common_details.distance_slab5) and (distance <= common_details.distance_slab6):
                miles_price = (car.base_fare + (car.fare6 * distance))
            elif distance > common_details.distance_slab6:
                miles_price = (car.base_fare + (car.fare7 * distance));

            if miles_price < car.min_fare:
                miles_price = car.min_fare

            estimatefare = (round(miles_price, 1))
            #adding gratuity
            gratuity = (estimatefare*sitecommondetails.gratuity)/100

            if (sitecommondetails.night_from_time <= datetime.datetime.strptime(ride_time, '%H:%M:%S').time()) or (sitecommondetails.night_to_time >= datetime.datetime.strptime(ride_time, '%H:%M:%S').time()):
                night_charge = sitecommondetails.night_charge
            else:
                night_charge = 0
            total_fare = estimatefare + gratuity + night_charge
            if not result:
                result = {"result" + str(i): (sitecommondetails.company_name, sitecommondetails.website, estimatefare, gratuity, night_charge, sitecommondetails.extra_seat_charge,
                                              sitecommondetails.stopover, sitecommondetails.extra_luggage, car_details.car_name,
                                              car_details.image_path, car_details.pax, car_details.large_luggage, car_details.small_luggage, car_details.car_color, total_fare)};
            else:
                result.update({"result" + str(i): (sitecommondetails.company_name, sitecommondetails.website, estimatefare, gratuity, night_charge, sitecommondetails.extra_seat_charge,
                                              sitecommondetails.stopover, sitecommondetails.extra_luggage, car_details.car_name,
                                                   car_details.image_path, car_details.pax, car_details.large_luggage, car_details.small_luggage, car_details.car_color, total_fare)})

            i += 1

        #return HttpResponse("result: {} ".format(sitecommondetails.booking_active))
        return render(request, "fare.html", {   'pickup': pickup,
                                                 'dropoff': dropoff,
                                                 'ride_time': ride_time,
                                                 'ride_date': ride_date,
                                                 'pax': pax,
                                                 'lugg': lugg,
                                                 'distance': distance,
                                                'range': range(0, 9), 'time': time_sloat,
                                                'result':result,
                                                 })
