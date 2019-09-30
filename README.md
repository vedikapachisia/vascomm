# vascomm
dbms project

## prerequisites
1. mysql
1. pip
1. django
1. mysqlclient
1. create a database in mysql named 'django'

## TODO
- [x] List the services offered by our carrier (Shayak, Vedika)
- [x] Design the schemas (Vedika, Shayak)
- [x] Write SQL queries for table creation (Ananya, Shayak)
- [x] Generate random data (Vedika, Shayak)
- [x] Connect it to django (Shayak)
- [ ] Write django models and test (Vedika)
- [ ] Write a simulation (Shayak)
- [ ] Populate the database
- [ ] Simulate the carrier
- [ ] Build the front end
- [ ] Connect the front end

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
