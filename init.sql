CREATE DATABASE reddit;
CREATE USER 'redditor'@'localhost' IDENTIFIED BY 'qweasd';
USE reddit;
GRANT ALL ON reddit.* TO 'redditor'@'localhost';
GRANT RELOAD ON *.* TO 'redditor'@'localhost';
quit;

