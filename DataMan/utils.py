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

#The utility function to upload a video to supabase bucket
def upload_video_to_bucket(dest, video_file):
    url = 'https://zwxpudmuwltonzohjbse.supabase.co'
    key= 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp3eHB1ZG11d2x0b256b2hqYnNlIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQwOTE1NjMsImV4cCI6MjAwOTY2NzU2M30.Gk7IHFmxLj6cnr_3g1o8dv0HvodDihm2oCNG-Ica3Mw'
    clients = supabase.Client(url, key)
    response=clients.storage.from_('sihbucketbackend').upload(dest, file=video_file)
    return response
#The utility function to list all videos for a user.
def list_user_videos_bucket(UniqueID):
    url = 'https://zwxpudmuwltonzohjbse.supabase.co'
    key= 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp3eHB1ZG11d2x0b256b2hqYnNlIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQwOTE1NjMsImV4cCI6MjAwOTY2NzU2M30.Gk7IHFmxLj6cnr_3g1o8dv0HvodDihm2oCNG-Ica3Mw'
    clients = supabase.Client(url, key)
    resp = clients.storage.from_('sihbucketbackend').list(path=f'{UniqueID}/Videos')
    return resp
#The utility function to get a file public url for a video file
def get_video_url_from_supabase(UniqueID, file_name):
    url = 'https://zwxpudmuwltonzohjbse.supabase.co'
    key= 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp3eHB1ZG11d2x0b256b2hqYnNlIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQwOTE1NjMsImV4cCI6MjAwOTY2NzU2M30.Gk7IHFmxLj6cnr_3g1o8dv0HvodDihm2oCNG-Ica3Mw'
    clients = supabase.Client(url, key)
    resp=clients.storage.from_('sihbucketbackend').get_public_url(f'{UniqueID}/Videos/{file_name}')
    return resp 

#The utility to upload document 
def upload_document_to_bucket(dest, document_file):
    url = 'https://zwxpudmuwltonzohjbse.supabase.co'
    key= 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp3eHB1ZG11d2x0b256b2hqYnNlIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQwOTE1NjMsImV4cCI6MjAwOTY2NzU2M30.Gk7IHFmxLj6cnr_3g1o8dv0HvodDihm2oCNG-Ica3Mw'
    clients = supabase.Client(url, key)
    response=clients.storage.from_('sihbucketbackend').upload(dest, file=document_file)
    return response
#The utility function to list all documents for a user.
def list_user_documents_bucket(UniqueID):
    url = 'https://zwxpudmuwltonzohjbse.supabase.co'
    key= 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp3eHB1ZG11d2x0b256b2hqYnNlIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQwOTE1NjMsImV4cCI6MjAwOTY2NzU2M30.Gk7IHFmxLj6cnr_3g1o8dv0HvodDihm2oCNG-Ica3Mw'
    clients = supabase.Client(url, key)
    resp = clients.storage.from_('sihbucketbackend').list(path=f'{UniqueID}/Documents')
    return resp
#The utility function to get a file public url for a video file
def get_document_url_from_supabase(UniqueID, file_name):
    url = 'https://zwxpudmuwltonzohjbse.supabase.co'
    key= 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inp3eHB1ZG11d2x0b256b2hqYnNlIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQwOTE1NjMsImV4cCI6MjAwOTY2NzU2M30.Gk7IHFmxLj6cnr_3g1o8dv0HvodDihm2oCNG-Ica3Mw'
    clients = supabase.Client(url, key)
    resp=clients.storage.from_('sihbucketbackend').get_public_url(f'{UniqueID}/Documents/{file_name}')
    return resp 