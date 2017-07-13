class Item:
    def __init__(self,name):
        self.name=name
        self.status='Pending'
    
class Bucket:
    def __init__(self,name):
        self.name=name
        self.items={}

    def get_items(self):
        return self.items

    def add_item(self,item):
        self.items[item.name]=item

class TheUser:    
    def __init__(self,name,username,password):
        self.name=name
        self.username=username
        self.password=password
        self.buckets={}

    def get_buckets(self):
        return self.buckets

    def add_bucket(self,bucket):
        self.buckets[bucket.name]=bucket
    