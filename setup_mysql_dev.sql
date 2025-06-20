#thr econnection
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
USE hbnb_dev_db;
GRANT ALL PRIVILEDGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
USE performance_schema;
GRANT SELECT ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEDGES;
SET FOREIGN_KEY_CHECKS=1;
