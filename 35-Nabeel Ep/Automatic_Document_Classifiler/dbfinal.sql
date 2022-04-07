/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - automatic_document_classifier
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`automatic_document_classifier` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `automatic_document_classifier`;

/*Table structure for table `dataset` */

DROP TABLE IF EXISTS `dataset`;

CREATE TABLE `dataset` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `words_type` varchar(30) DEFAULT NULL,
  `keyword` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `dataset` */

insert  into `dataset`(`id`,`words_type`,`keyword`) values 
(1,'Tech','camera'),
(2,'Tech','phone'),
(3,'Tech','mobile where the data attributes to be classified\r\n are text-type. In this way, it is proposed to use the association for computing machinery taxonomy to obtain\r\n the similarity between documents, where each document consists of a set of keywords. According to the\r\n results obtained, the algorithm is competitive, which indicates that the proposal of a knowledge-based genetic\r\n algorithm is a viable approach to solve the classification problem.'),
(4,'Tech','analysts '),
(5,'entertainment','dubbed'),
(6,'entertainment','top stars'),
(7,'entertainment','box office'),
(8,'entertainment','film industry'),
(9,'business','bank loses'),
(10,'business','customer'),
(11,'business','employees'),
(12,'aaaa','cccc'),
(13,'documents','genetic'),
(14,'texts ','genetic \r\nalgorithm'),
(15,'text-type','genetic');

/*Table structure for table `document` */

DROP TABLE IF EXISTS `document`;

CREATE TABLE `document` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `file` varchar(100) DEFAULT NULL,
  `user_id` varchar(100) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  `hash` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `document` */

insert  into `document`(`id`,`file`,`user_id`,`type`,`hash`) values 
(1,'210930-103026210930-101019210922-124913.txt','1','business','0a198c8a538ccbf40ea83562dc4a3872cde80ae3'),
(2,'220203-163831210922-124252.txt','1','business','7242cb1a3b2cc212b2988c2f161042d0229a538b');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(100) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `type` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values 
(1,'aaa@gmail.com','111','User'),
(2,'admin','admin','Admin');

/*Table structure for table `messages` */

DROP TABLE IF EXISTS `messages`;

CREATE TABLE `messages` (
  `m_id` int(100) NOT NULL AUTO_INCREMENT,
  `user_id` int(100) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`m_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `messages` */

insert  into `messages`(`m_id`,`user_id`,`message`,`reply`,`status`) values 
(1,1,'vcgc','Not Replied','pending'),
(2,1,'bbb','Not Replied','pending'),
(3,1,'ooo','Not Replied','pending');

/*Table structure for table `user_details` */

DROP TABLE IF EXISTS `user_details`;

CREATE TABLE `user_details` (
  `id` int(100) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `district` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`,`phone`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `user_details` */

insert  into `user_details`(`id`,`name`,`gender`,`address`,`district`,`email`,`phone`,`status`) values 
(1,'aswin','MALE','aaaa','KASARGOD','aaa@gmail.com','9988776688','pending');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
