from django.db import models
import supabase as supabase
def create_supabase_folder(unique_id):
    url = 'https://zwxpudmuwltonzohjbse.supabase.co'
    key= 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp3eHB1ZG11d2x0b256b2hqYnNlIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQwOTE1NjMsImV4cCI6MjAwOTY2NzU2M30.Gk7IHFmxLj6cnr_3g1o8dv0HvodDihm2oCNG-Ica3Mw'
    clients = supabase.Client(url, key)
    vid_res = clients.storage.from_('sihbucketbackend').upload(f'{unique_id}/Videos/supabasetry.txt', file='DataMan\supabasetry.txt')
    docs_res = clients.storage.from_('sihbucketbackend').upload(f'{unique_id}/Documents/supabasetry.txt', file='DataMan\supabasetry.txt')

def retrieve_supabase_folder(UniqueID):
    url = 'https://zwxpudmuwltonzohjbse.supabase.co'
    key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp3eHB1ZG11d2x0b256b2hqYnNlIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQwOTE1NjMsImV4cCI6MjAwOTY2NzU2M30.Gk7IHFmxLj6cnr_3g1o8dv0HvodDihm2oCNG-Ica3Mw'
    clients = supabase.Client(url, key)

    bucket_name= "sihbucketbackend"
    path=f"{UniqueID}/Videos"

    data = clients.storage.from_(bucket_name).list(path=path)
    print(data,'ama')

# Create your models here.
class mainUserCentral(models.Model):
    name=models.CharField(max_length=30, null=False, blank=False)
    age=models.IntegerField(null=False, blank=False)
    gender=models.CharField(null=False, blank=False)
    email=models.EmailField(null=False, blank=False)
    phone=models.CharField(max_length=20 ,null=False, blank=False)
    address= models.CharField(max_length=50, null=False, blank=False)
    bucket_url=models.URLField(null=True, blank=False)
    password=models.CharField(max_length=25, null=True, blank=False)
    UniqueID=models.CharField(null=True, blank=True, default='')
    
    """def save(self, *args, **kwargs):
        if not self.pk:
            self.UniqueID = None
        super().save(*args, **kwargs)
        if self.id and self.UniqueID is None:
            self.UniqueID = f'{"SIH1016FS"}{str(self.id).zfill(3)}'
            create_supabase_folder(str(self.UniqueID))
            super().save(*args, **kwargs)"""

