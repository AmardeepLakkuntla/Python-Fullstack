docters = [
    {
        'id':1,
        'name':'shiva',
        'contact':8184941910,
        'available_date':'2025-11-10',
        'available_time':'10:00 AM to 01:00 PM'
        
    },
    {
        'id':2,
        'name':'arun',
        'contact':8790063545,
        'available_date':'2025-11-10',
        'available_time':'01:00 PM to 05:00 PM'
        
    }
]

def add_docter(id,name,contact,available_date,available_time):
    docters.append(
        {
        'id':id,
        'name':name,
        'contact':contact,
        'available_date':available_date,
        'available_time':available_time
        
    }
        
    )
    
def update_docter(docter_id,available_date,available_time):
    for docter in docters:
        if docter['id'] == docter_id:
            docter[available_date] == available_date
            docter[available_time] == available_time
            print('docter updated suucessfully')
            return
        print('product not found')
        
    
def delete_docter(docter_id):
    for docter in docters:
        if docter['id']==docter_id:
            docters.remove(docter)
            print('docter removed sucessfully')
        return
    print('doctor not found')
            
            
    
def get_doctors():
    return docters

