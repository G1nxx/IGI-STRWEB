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

def get_last_news():
    return company_db.get_last_news()

def get_reviews():
    return company_db.get_reviews()

def create_review(data):
    return company_db.create_review(data)

def get_contacts():
    return company_db.get_contacts()

def get_promocodes():
    return company_db.get_promocodes()

def get_glossaries():
    return company_db.get_glossaries()

def get_vacancies():
    return company_db.get_vacancies()

def get_year_history():
    return company_db.get_year_history()

def get_services():
    return company_db.get_services()

def get_partners():
    return company_db.get_partners()

def add_to_cart(u_id, id):
    return company_db.add_to_cart(u_id, id)

def get_cart(u_id):
    return company_db.get_cart(u_id)

def update_order(id, val):
    company_db.update_order(id, val)

def delete_order(id):
    company_db.delete_order(id)

def bye_cart(u_id):
    company_db.bye_cart(u_id)