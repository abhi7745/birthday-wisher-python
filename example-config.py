from datetime import datetime

curr_datetime = datetime.now()
curr_year = str(curr_datetime.date().year)

SENDER_EMAIL = 'xyz@gmail.com'
PASSWORD = 'xyz'


RECEIVER_EMAIL_DICT = {
            'user1': ['raju@gmail.com', curr_year+'-02-10', 'Raju'], 
            'user2': ['robert@gmail.com', curr_year+'-04-30', 'Robert'],
            'user3': ['kiran@gmail.com', curr_year+'-10-12', 'Kiran'],
            'user4': ['joby@gmail.com', curr_year+'-11-08', 'Joby']
        }