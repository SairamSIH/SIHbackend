import supabase as supabase
def create_supabase_folder(unique_id):
    url = 'https://zwxpudmuwltonzohjbse.supabase.co'
    key= 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp3eHB1ZG11d2x0b256b2hqYnNlIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQwOTE1NjMsImV4cCI6MjAwOTY2NzU2M30.Gk7IHFmxLj6cnr_3g1o8dv0HvodDihm2oCNG-Ica3Mw'
    clients = supabase.Client(url, key)
    try:
        with open("supabasetry.txt","x") as d:
            pass 
    except:
        pass
    vid_res = clients.storage.from_('sihbucketbackend').upload(f'{unique_id}/Videos/supabasetry.txt', file='supabasetry.txt')
    docs_res = clients.storage.from_('sihbucketbackend').upload(f'{unique_id}/Documents/supabasetry.txt', file='supabasetry.txt')