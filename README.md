# Vascomm
Database Management Systems and Python Project  
created by Ananya R., Shayak Banerjee and Vedika Pachisia

## Abstract
Vascomm is a data monitoring tool for network carriers, that can run on a web browser. It is implemented using Python, Django and MySQL. The monitoring tool is dependent upon a simulation for data. The simulation is written using Python, which simulates calls, messages, mobile data usage in a pseudo random model fitted in a manner that resembles a real network carrier. The data is handled with a Python script, making the process a scalable and highly efficient process. The user base begins at 1,000 users but can be upscaled with only the handling capacity of the server being a limit.  
  
For testing purposes, the user base generation can be done with a python script included in the package, that can generate a unique date of birth and phone number of a user in a pseudo random, near realistic data.

## Prerequisites
1. Python 3.x
1. pip
1. Django
1. MySQL
1. mysqlclient
1. Create a database in mysql named 'django'

## Running the application
1. Open the root folder in the command line and write the command ```python3 djangoproject/manage.py runserver```  
2. Browse to http://127.0.0.1:8000/webapp/
3. After the page opens, paste http://127.0.0.1:8000/webapp/simulate_calls in the browser and go. The values in the webpage will themselves start changing.

### List of services
1. 'INT600' - 
    200 min free talktime, post usage Rs. 5/min  
    1000 free SMS, post usage Rs. 3/SMS  
    12GB free data, post usage Rs. 1/MB  
1. 'DOM339' -  
    Unlimited calls
    1000 free SMS, post usage Rs. 1/SMS  
    30GB free data, post usage Rs. 0.1/MB  
1. 'DOM099' -  
    100 min free talktime, post usage Rs. 0.3/min
    150 free SMS, post usage Rs. 1/SMS  
    10 GB free data, post usage Rs. 0.1/MB  

### Schemas
1. plans  
   1. plan_id  (string, primary key)
   1. free_talktime (number)
   1. free_sms (num)
   1. free_data  (num)
   1. call_rate  (decimal)
   1. sms_rate  (decimal)
   1. data_rate  (decimal)
   1. price  (decimal)
1. user_details 
   1. user_id (int autoincrement)
   1. user_name  (string)
   1. dob  (date)
   1. phone  (num)
   1. plan_id  (string)
1. usage_details  
   1. user_id (number - autoincrement)
   1. call_amount (decimal)
   1. sms_amount (decimal)
   1. data_amount (decimal)
   1. total_amount (decimal)
1. calls_log  
   1. call_id (number, autoincrement)
   1. user_id (number, autoincrement)
   1. call_start (TIME)
   1. call_end (TIME)
1. sms_log 
   1. sms_id  (number, autoincrement)
   1. user_id (number, autoincrement)
   1. message_time (time)
1. data_log 
   1. data_id  (number, autoincrement)
   1. user_id  (number, autoincrement)
   1. usage_time (time)
   1. data_used (decimal)
   
   
   ## TODO
- [x] List the services offered by our carrier (Shayak, Vedika)
- [x] Design the schemas (Vedika, Shayak)
- [x] Write SQL queries for table creation (Ananya, Shayak)
- [x] Generate random data (Vedika, Shayak)
- [x] Connect it to django (Shayak)
- [x] Write django models and test (Vedika)
- [x] Write a simulation (Shayak)
- [x] Populate user_details and plans (Vedika, Shayak)
- [ ] Write the method for populating the dynamic tables
- [x] Simulate the carrier
- [x] Build the front end
- [x] Connect the front end
