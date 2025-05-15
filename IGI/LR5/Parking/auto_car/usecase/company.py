from auto_car.repository import company as company_db

def get_info():
    return company_db.get_company_info()

def get_free_parking_places():
    return company_db.get_free_parking_places()

def get_cars(id):
    return company_db.get_cars(id)

def park_car(p_id, c_id):
    return company_db.park_car(p_id, c_id)

def unpark_car(c_id):
    return company_db.unpark_car(c_id)