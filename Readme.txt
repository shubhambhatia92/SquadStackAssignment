I have used request framework to call on pipedrives api as per documentation and used flask framework to
to hande json response coming from webhook url placed in pipedrive

Search by name-
i have used get method to call on the url through request library in python and passed name and term as 
query parameters which are compulsory

search by id-
i have extracted all details of that particular id 
if details are present it means person is present

extract.py
i have attached two webhooks in pipedrive crm one on updation and one on addition of a person
this webhook tranfers the json file which i have routed in my library hypothetically and extracted all the details 
which were required through flask and return a json format.i have also given an example json text to view json file 
coming from pipedrives webhook

Updateperson
simple put request according the pipedrives api 

add note.py
simple post request according to pipedrive api