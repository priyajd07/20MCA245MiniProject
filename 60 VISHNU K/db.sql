/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.27 : Database - bone_deformity
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bone_deformity` /*!40100 DEFAULT CHARACTER SET latin1 */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `bone_deformity`;

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `id` int NOT NULL AUTO_INCREMENT,
  `lid` int DEFAULT NULL,
  `feedback` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`id`,`lid`,`feedback`,`date`) values 
(1,2,'good','2025-12-22'),
(2,4,'good\r\n','2022-01-30'),
(3,5,'jlll','2022-01-31');

/*Table structure for table `image` */

DROP TABLE IF EXISTS `image`;

CREATE TABLE `image` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userid` int DEFAULT NULL,
  `image` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `image` */

insert  into `image`(`id`,`userid`,`image`,`date`) values 
(1,4,'09.jpg','2022-02-01'),
(2,4,'04.jpg','2022-02-01'),
(3,5,'03.png','2022-02-01'),
(4,5,'H48.jpg','2022-02-01'),
(5,4,'09.jpg','2022-02-01'),
(6,4,'F2.JPG','2022-02-01'),
(7,4,'F2.JPG','2022-02-01');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'user','user','user'),
(4,'sanju','123','user'),
(5,'ann','annA12345','user');

/*Table structure for table `prediction_result` */

DROP TABLE IF EXISTS `prediction_result`;

CREATE TABLE `prediction_result` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userid` int DEFAULT NULL,
  `image` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  `prediction` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `prediction_result` */

insert  into `prediction_result`(`id`,`userid`,`image`,`date`,`prediction`) values 
(1,4,1,'2022-02-01','20220201_123127.jpg'),
(2,4,2,'2022-02-01','20220201_123211.jpg'),
(3,5,3,'2022-02-01','20220201_124029.jpg'),
(4,5,4,'2022-02-01','20220201_124054.jpg'),
(5,4,5,'2022-02-01','20220201_124242.jpg'),
(6,4,5,'2022-02-01','20220201_124243.jpg'),
(7,4,6,'2022-02-01','20220201_125830.jpg'),
(8,4,7,'2022-02-01','20220201_125915.jpg');

/*Table structure for table `user_registration` */

DROP TABLE IF EXISTS `user_registration`;

CREATE TABLE `user_registration` (
  `id` int NOT NULL AUTO_INCREMENT,
  `lid` int DEFAULT NULL,
  `firstname` varchar(200) DEFAULT NULL,
  `lastname` varchar(200) DEFAULT NULL,
  `gender` varchar(200) DEFAULT NULL,
  `place` varchar(200) DEFAULT NULL,
  `post` varchar(200) DEFAULT NULL,
  `pin` int DEFAULT NULL,
  `phone` bigint DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `user_registration` */

insert  into `user_registration`(`id`,`lid`,`firstname`,`lastname`,`gender`,`place`,`post`,`pin`,`phone`) values 
(1,2,'amal','dev','male','kanure','kokkallure',674536,3344556677),
(2,4,'sanju','p','Male','clt','clt',673456,9876543210),
(3,5,'ada','sdf','Male','dff','ddg',656745,8956789056);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
