from django.db import models

# Create your models here.
class Bidders(models.Model):
    bidder_fname = models.CharField(max_length=100)
    bidder_lname = models.CharField(max_length=100)
    bidder_add = models.TextField()
    bidder_email = models.EmailField()
    bidder_date_joined = models.DateField()
    bidder_phone = models.CharField(max_length=50)
    bidder_credit_details = models.TextField

    def __str__(self):
        return u'%s %s'%(self.bidder_fname,self.bidder_lname)

class Auction_Items(models.Model):
    auction_item_desc = models.TextField()
    auction_start_date = models.DateField()
    auction_actual_close_date = models.DateTimeField()
    auctions_planned_close_date = models.DateTimeField()
    auction_item_actual_selling_price = models.IntegerField()
    auction_item_reserve_price = models.IntegerField()
    auction_item_payment_amount = models.IntegerField()
    auction_item_payment_date = models.DateTimeField()
    auction_item_successful_bidder = models.ForeignKey(Bidders)
    auction_item_comments = models.TextField()

    def __str__(self):
        return self.auction_item_desc

class Bids(models.Model):
    bid_low_price = models.IntegerField()
    bid_preferred_price = models.IntegerField()
    bid_high_price = models.IntegerField()
    bid_comments = models.TextField()

    def __str__(self):
        return self.bid_preferred_price

class Auction_Item_Categories(models.Model):
    item_category_descr = models.TextField()

    def __str__(self):
        return self.item_category_descr

class Shipment(models.Model):
    shipment_planned_date = models.DateTimeField()
    shipment_actual_date = models.DateTimeField()
    shippent_cost = models.IntegerField()
    shipment_comments = models.CharField(max_length=200)
    shipment_id = models.ForeignKey(Auction_Items)

    def __str__(self):
        return self.shipment_actual_date

# class Sellers(models.Model):
#     author_id = models.ForeignKey(Auction_Items)
#     author_first_name = models.CharField(max_lenght = 50)
#     author_last_name  = models.CharField(max_length=50)
#

