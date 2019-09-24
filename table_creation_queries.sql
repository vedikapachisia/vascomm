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
('INT600', 200, 1000, 12, 5, 3, 1, 600),
('DOM339', 0, 1000, 30, 0, 1, 0.1, 339),
('DOM099', 100, 150, 10, 0.3, 1, 0.1, 99);

CREATE TABLE user_details(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(45) NOT NULL,
    dob DATE NOT NULL,
    phone VARCHAR(10) NOT NULL,
    /*size of plan_id will be equal to plans.plan_id*/
    plan_id VARCHAR(6) NOT NULL,
    FOREIGN KEY (plan_id) REFERENCES plans(plan_id)
);

CREATE TABLE usage_details(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    call_amount DECIMAL NOT NULL,
    sms_amount DECIMAL NOT NULL,
    data_amount DECIMAL NOT NULL,
    total_amount DECIMAL NOT NULL
);

CREATE TABLE calls_log(
    call_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    call_start TIME NOT NULL,
    call_end TIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user_details(user_id)
);

CREATE TABLE sms_log(
    sms_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL, 
    message_time TIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user_details(user_id)
);

CREATE TABLE data_log(
    data_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    usage_time TIME NOT NULL,
    data_used DECIMAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user_details(user_id)
);
    