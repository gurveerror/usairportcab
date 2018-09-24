from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class Site(models.Model):
    logo = models.ImageField(upload_to='static/images/', blank=True)
    companyname = models.CharField(max_length=200, db_index=True)
    address = models.CharField(max_length=500)
    telno = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    website = models.CharField(max_length=200)


    class Meta:
        ordering = ('companyname',)

    def __str__(self):
         return self.companyname

class Car(models.Model):
    car_name = models.CharField(max_length=500, db_index=True)
    car_color = models.CharField(max_length=200)
    car_feature = models.TextField(blank=True)
    status = models.DecimalField(max_digits=9, decimal_places=2)
    small_luggage = models.DecimalField(max_digits=9, decimal_places=2)
    large_luggage = models.DecimalField(max_digits=9, decimal_places=2)
    pax = models.DecimalField(max_digits=9, decimal_places=2)
    image_path = models.ImageField(upload_to="static/images/cars/", blank=True)

    class Meta:
        ordering = ('car_name',)


    def __str__(self):
        return self.car_name



class Sites_common_detail(models.Model):
    logo = models.ImageField(upload_to='static/images/', blank=True)
    company_name = models.CharField(max_length=200, db_index=True)
    address = models.CharField(max_length=500)
    phone_no = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    website = models.CharField(max_length=200)

    list_of_holidays = models.TextField(blank=True)
    holiday_surcharge = models.DecimalField(max_digits=9, decimal_places=2)
    gratuity = models.DecimalField(max_digits=9, decimal_places=2)
    night_charge = models.DecimalField(max_digits=9, decimal_places=2)
    night_from_time = models.TimeField(max_length=100)
    night_to_time = models.TimeField(max_length=100)
    extra_seat_charge = models.DecimalField(max_digits=9, decimal_places=2)
    stopover = models.DecimalField(max_digits=9, decimal_places=2)
    extra_luggage = models.DecimalField(max_digits=9, decimal_places=2)
    booking_active = models.DecimalField(max_digits=9, decimal_places=2)
    update_data = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('company_name',)

    def __str__(self):
        return self.company_name

class Common_detail(models.Model):
    distance_slab1 = models.DecimalField(max_digits=9, decimal_places=2)
    distance_slab2 = models.DecimalField(max_digits=9, decimal_places=2)
    distance_slab3 = models.DecimalField(max_digits=9, decimal_places=2)
    distance_slab4 = models.DecimalField(max_digits=9, decimal_places=2)
    distance_slab5 = models.DecimalField(max_digits=9, decimal_places=2)
    distance_slab6 = models.DecimalField(max_digits=9, decimal_places=2)
    update_data = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('update_data',)

    #def __str__(self):
         #return self.update_data


class Car_fare(models.Model):
    car_name = models.ForeignKey(Car, related_name = 'car_fare')
    base_fare = models.DecimalField(max_digits=10, decimal_places=2)
    min_fare = models.DecimalField(max_digits=10, decimal_places=2)
    fare1 = models.DecimalField(max_digits=10, decimal_places=2)
    fare2 = models.DecimalField(max_digits=10, decimal_places=2)
    fare3 = models.DecimalField(max_digits=10, decimal_places=2)
    fare4 = models.DecimalField(max_digits=10, decimal_places=2)
    fare5 = models.DecimalField(max_digits=10, decimal_places=2)
    fare6 = models.DecimalField(max_digits=10, decimal_places=2)
    fare7 = models.DecimalField(max_digits=10, decimal_places=2)
    site_name = models.ForeignKey(Sites_common_detail, related_name = 'company')

    class Meta:
        ordering = ('site_name',)


    #def __str__(self):
        #return self.carname
    def get_absolute_url(self):
        return reverse('user:editfare',
                       args=[self.id])

    def get_delete_url(self):
        return reverse('user:deletecarfare',
                       args=[self.id])





