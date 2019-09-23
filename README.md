# vascomm
dbms project

## TODO
- [x] List the services offered by our carrier
- [x] Design the schemas
- [ ] Connect it to django
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
   1. plan_id  
   1. free_talktime
   1. free_sms
   1. free_data
   1. call_rate
   1. sms_rate
   1. data_rate
   1. price
1. user_details 
   1. user_id
   1. name
   1. dob
   1. phone
   1. plan
1. usage_details  
   1. uid
   1. call_amount
   1. sms_amount
   1. data_amount
   1. total_amount
1. calls_log  
   1. uid
   1. call_start (TIME)
   1. call_end (TIME)
1. sms_log  
   1. uid
   1. message_time
1. data_log  
   1. uid
   1. usage_time
   1. data_used
