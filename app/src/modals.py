class Item:
    def __init__(self,name):
        self.name=name
        self.status='Pending'

    def set_status(self,status):
        if status=='Pending' or status=='Done':
            self.status=status
            return True
        else:
            return 'Invalid status'


    def get_status(self):
        return self.status

    def set_name(self,name):
        if name is None:
            return 'Name cannot be None'
        elif name=='':
            return 'Name cannot be empty'
        else:
            self.name=name
            return True

    def get_name(self):
        return self.name

class Bucket:
    def __init__(self,name):
        self.name=name
        self.items={}

    def get_items(self):
        return self.items

    def add_item(self,item):
        if item is None:
            return 'Input cannot be None'
        elif not isinstance(item,Item):
            return 'Input should be of type Item'
        else:
            self.items[item.name]=item
            return True

class TheUser:    
    def __init__(self,name,username,password):
        self.name=name
        self.username=username
        self.password=password
        self.buckets={}

    def get_buckets(self):
        return self.buckets

    def add_bucket(self,bucket):
        if bucket is None:
            return 'Input cannot be None'
        elif not isinstance(bucket,Bucket):
            return 'Input must be of type Bucket'
        else:
            self.buckets[bucket.name]=bucket
            return True
    