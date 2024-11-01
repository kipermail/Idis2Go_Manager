class User:
    def __init__(self, first_name='', last_name='', 
                 email='', password='', language='EN', 
                 role='', distributor='', customer='',
                 email_verified=False, is_active=False, is_doctor=False):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.language = language
        self.role = role
        self.distributor = distributor
        self.customer = customer
        self.email_verified = email_verified
        self.is_active = is_active
        self.is_doctor = is_doctor
