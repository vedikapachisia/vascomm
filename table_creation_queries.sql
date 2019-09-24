CREATE TABLE plans(
	plan_id VARCHAR(6) PRIMARY KEY, 
	free_talktime INT NOT NULL,
    free_sms INT NOT NULL,
    free_data INT NOT NULL,
    call_rate INT NOT NULL,
    sms_rate DECIMAL NOT NULL,
    data_rate DECIMAL NOT NULL,
    price DECIMAL NOT NULL
);

/* Contents of plans table*/
INSERT INTO plans VALUES
('INT600', 200, 1000, 12, 5, 3, 1),
('DOM339', 0, 1000, 30, 0, 1, 0.1),
('DOM099', 100, 150, 10, 0.3, 1, 0.1);

CREATE TABLE user_details(
    user_id INT AUTO_INCREMENT NOT NULL,
    user_name VARCHAR(45) NOT NULL,
    dob DATE NOT NULL,
    phone INT NOT NULL,
    plan_id VARCHAR(45) NOT NULL
);

CREATE TABLE usage_details(
    user_id INT AUTO_INCREMENT NOT NULL,
    call_amount DECIMAL NOT NULL,
    sms_amount DECIMAL NOT NULL,
    data_amount DECIMAL NOT NULL,
    total_amount DECIMAL NOT NULL
);

CREATE TABLE calls_log(
    call_id INT AUTO_INCREMENT NOT NULL,
    user_id INT AUTO_INCREMENT NOT NULL,
    call_start TIME NOT NULL,
    call_end TIME NOT NULL
);

CREATE TABLE sms_log(
    sms_id INT AUTO_INCREMENT NOT NULL,
    user_id INT AUTO_INCREMENT NOT NULL, 
    message_time TIME NOT NULL
);

CREATE TABLE data_log(
    data_id INT AUTO_INCREMENT NOT NULL,
    user_id INT AUTO_INCREMENT NOT NULL,
    usage_time TIME NOT NULL,
    data_used DECIMAL NOT NULL
);
    