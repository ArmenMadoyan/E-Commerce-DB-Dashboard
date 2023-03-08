CREATE DATABASE  IF NOT EXISTS `coolina`;
USE `coolina`;

-- SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS; 
-- SET FOREIGN_KEY_CHECKS=0;

DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer` (
    `email` VARCHAR(50) NOT NULL,
    `full_name` VARCHAR(50) NOT NULL,
    `location` VARCHAR(50),
    PRIMARY KEY (`email`)
)  ENGINE=INNODB DEFAULT CHARSET=LATIN1;


DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders` (
    `order_id` VARCHAR(11) NOT NULL,
    `created_at` TIMESTAMP NOT NULL,
    `financial_status` VARCHAR(50) NOT NULL,
    `paid_at` TIMESTAMP NOT NULL,
    `fulfillment_status` VARCHAR(50) NOT NULL,
    `fulfilled_at` TIMESTAMP,
    `accepts_marketing` VARCHAR(10),
    `currency` VARCHAR(10) NOT NULL,
    `subtotal` VARCHAR(10) NOT NULL,
    `shipping` VARCHAR(10) NOT NULL,
    `taxes` VARCHAR(10) NOT NULL,
    `total` VARCHAR(10) NOT NULL,
    `discount_code` VARCHAR(50),
    `discount_amount` VARCHAR(50),
    `shipping_method` VARCHAR(50),
    `billing_name` VARCHAR(50),
    `billing_address1` VARCHAR(50),
    `billing_address2` VARCHAR(50),
    `billing_city` VARCHAR(20),
    `billing_zip` VARCHAR(20),
    `billing_province` VARCHAR(50),
    `billing_country` VARCHAR(20),
    `billing_phone` VARCHAR(50),
    `shipping_name` VARCHAR(50),
    `shipping_address1` VARCHAR(50),
    `shipping_address2` VARCHAR(50),
    `shipping_city` VARCHAR(20),
    `shipping_zip` VARCHAR(20),
    `shipping_province` VARCHAR(50),
    `shipping_country` VARCHAR(20),
    `shipping_phone` VARCHAR(50),
    `notes` VARCHAR(300),
    `payment_method` VARCHAR(50),
    `email` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`order_id`),
    FOREIGN KEY (`email`)
        REFERENCES `customer` (`email`)
)  ENGINE=INNODB DEFAULT CHARSET=LATIN1;



DROP TABLE IF EXISTS `abandoned_order`;
CREATE TABLE `abandoned_order` (
    `abandoned_order_id` VARCHAR(20) NOT NULL,
    `created_at` TIMESTAMP NOT NULL,
    `accepts_marketing` VARCHAR(10),
    `currency` VARCHAR(10) NOT NULL,
    `subtotal` VARCHAR(10) NOT NULL,
    `shipping` VARCHAR(10) NOT NULL,
    `taxes` VARCHAR(10) NOT NULL,
    `total` VARCHAR(10) NOT NULL,
    `discount_code` VARCHAR(50),
    `discount_amount` VARCHAR(10),
    `shipping_method` VARCHAR(100),
    `billing_name` VARCHAR(50),
    `billing_address1` VARCHAR(50),
    `billing_address2` VARCHAR(50),
    `billing_city` VARCHAR(20),
    `billing_zip` VARCHAR(20),
    `billing_province` VARCHAR(50),
    `billing_country` VARCHAR(20),
    `billing_phone` VARCHAR(50),
    `shipping_name` VARCHAR(50),
    `shipping_address1` VARCHAR(50),
    `shipping_address2` VARCHAR(50),
    `shipping_city` VARCHAR(20),
    `shipping_zip` VARCHAR(20),
    `shipping_province` VARCHAR(50),
    `shipping_country` VARCHAR(20),
    `shipping_phone` VARCHAR(50),
    `notes` VARCHAR(300),
    `email` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`abandoned_order_id`),
    FOREIGN KEY (`email`)
        REFERENCES `customer` (`email`)
)  ENGINE=INNODB DEFAULT CHARSET=LATIN1;

DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
    `product_sku` VARCHAR(50) NOT NULL,
    `product_name` VARCHAR(100),
    `product_price` VARCHAR(50),
    `product_compare_at_price` VARCHAR(10),
    `product_requires_shipping` VARCHAR(100),
    `product_taxable` VARCHAR(10),
    PRIMARY KEY (`product_sku`)
)  ENGINE=INNODB DEFAULT CHARSET=LATIN1;



DROP TABLE IF EXISTS `order_item`;
CREATE TABLE `order_item` (
    `order_id` VARCHAR(20) NOT NULL,
    `product_sku` VARCHAR(50) NOT NULL,
    `quantity` VARCHAR(5),
    `product_fulfillment` VARCHAR(20),
    FOREIGN KEY (`order_id`)
        REFERENCES `orders` (`order_id`),
    FOREIGN KEY (`product_sku`)
        REFERENCES `product` (`product_sku`),
    PRIMARY KEY (`order_id` , `product_sku`)    
)  ENGINE=INNODB DEFAULT CHARSET=LATIN1;


DROP TABLE IF EXISTS `abandoned_order_item`;
CREATE TABLE `abandoned_order_item` (
    `abandoned_order_id` VARCHAR(20) NOT NULL,
    `product_sku` VARCHAR(50) NOT NULL,
    `quantity` VARCHAR(5),
    `product_fulfillment` VARCHAR(20),
    PRIMARY KEY (`abandoned_order_id` , `product_sku`),
    FOREIGN KEY (`abandoned_order_id`)
        REFERENCES `abandoned_order` (`abandoned_order_id`),
    FOREIGN KEY (`product_sku`)
        REFERENCES `product` (`product_sku`)
)  ENGINE=INNODB DEFAULT CHARSET=LATIN1;

-- SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;