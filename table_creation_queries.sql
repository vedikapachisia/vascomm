CREATE TABLE plans(
	plan_id VARCHAR(6) PRIMARY KEY, 
	free_talktime INT,
    free_sms INT,
    free_data INT,
    call_rate INT,
    sms_rate DECIMAL,
    data_rate DECIMAL,
    price DECIMAL
    );
CREATE TABLE user_details(
    user_id INT AUTO_INCREMENT,
    user_name VARCHAR(45),
    dob DATE,
    phone INT,
    plan_id VARCHAR(45)
    );
CREATE TABLE usage_details(
    user_id INT AUTO_INCREMENT,
    call_amount DECIMAL,
    sms_amount DECIMAL,
    data_amount DECIMAL,
    total_amount DECIMAL
    );
CREATE TABLE calls_log(
    call_id INT AUTO_INCREMENT,
    user_id INT AUTO_INCREMENT,
    call_start TIME,
    call_end TIME
    );
CREATE TABLE sms_log(
    sms_id INT AUTO_INCREMENT,
    user_id INT AUTO_INCREMENT, 
    message_time TIME
    );
CREATE TABLE data_log(
    data_id INT AUTO_INCREMENT,
    user_id INT AUTO_INCREMENT,
    usage_time TIME,
    data_used DECIMAL
    );
    
    
    
    
    
    