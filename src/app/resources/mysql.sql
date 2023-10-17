-- 데이터베이스 및 테이블 생성

create database buzz;

CREATE TABLE buzz.ad_campaigns(
id INT(10) NOT NULL PRIMARY KEY,
name VARCHAR(20),
image_url VARCHAR(100),
landing_url VARCHAR(100),
weight INT(10),
target_country CHAR(2),
target_gender CHAR(1),
reward INT(10),
regidate TIMESTAMP 	DEFAULT CURRENT_TIMESTAMP
) CHARSET=utf8;

CREATE TABLE buzz.ad_users(
id INT(10) NOT NULL PRIMARY KEY,
name VARCHAR(20),
current_reward INT(10),
regidate TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) CHARSET=utf8;

CREATE TABLE buzz.user_reward_history(
id INT(10) NOT NULL,
vector CHAR(1),
amount INT(10),
regidate TIMESTAMP 	DEFAULT CURRENT_TIMESTAMP
) CHARSET=utf8;

-- 샘플데이터 넣기

1) buzz.ad_campaigns 에 대한 데이터는 제작한 "http://localhost:8080/importDB" API를 통해 INSERT합니다.

2) 기타 임의이 데이터는 SQL로 입력
INSERT INTO buzz.ad_users (
                id,
                name,
                current_reward
                
            ) VALUES (
                11329,
                "SIHO KIM",
                0
            );

