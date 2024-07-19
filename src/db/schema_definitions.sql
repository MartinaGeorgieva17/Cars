create DATABASE vehiclesdb;
use vehiclesdb;


-- drop TABLE vehicle;

CREATE TABLE vehicle (
    id INT NOT NULL AUTO_INCREMENT,
    model VARCHAR(20) NOT NULL,
    manufacturer VARCHAR(30) NOT NULL,
    `year` INT UNSIGNED NOT NULL,
    color VARCHAR(15) NOT NULL,
    mileage INT UNSIGNED,
    PRIMARY KEY (id)
);


INSERT INTO vehicle ( manufacturer, model,`year`, color, mileage)
VALUES ('BMW', '7', 2020, 'red', 15000);