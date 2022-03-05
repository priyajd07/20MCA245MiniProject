/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.6.12-log : Database - transportation
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`transportation` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `transportation`;

/*Table structure for table `advertisement` */

DROP TABLE IF EXISTS `advertisement`;

CREATE TABLE `advertisement` (
  `advertisementid` int(11) NOT NULL AUTO_INCREMENT,
  `photo` varchar(500) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`advertisementid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `advertisement` */

insert  into `advertisement`(`advertisementid`,`photo`,`date`,`latitude`,`longitude`) values (5,'/static/advertisement/Dori-Red-Georgette-Printed-Saree_0c0076f71bcd535ca0816765235e79f5_images_360_480_mini.jpg','2022-01-08','25','35'),(8,'/static/advertisement/kitty_2-wallpaper-1920x1080.jpg','2022-01-31','11.67','35'),(9,'/static/advertisement/cute_white_cat-wallpaper-1920x1080.jpg','2022-02-01','11.25903903','75.78386225');

/*Table structure for table `bus` */

DROP TABLE IF EXISTS `bus`;

CREATE TABLE `bus` (
  `busid` int(11) NOT NULL AUTO_INCREMENT,
  `busname` varchar(70) DEFAULT NULL,
  `regno` varchar(50) DEFAULT NULL,
  `color` varchar(70) DEFAULT NULL,
  `model` varchar(70) DEFAULT NULL,
  `photo` varchar(500) DEFAULT NULL,
  `routeid` int(11) DEFAULT NULL,
  PRIMARY KEY (`busid`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;

/*Data for the table `bus` */

insert  into `bus`(`busid`,`busname`,`regno`,`color`,`model`,`photo`,`routeid`) values (28,'Delax','KL4876','Blue','Minibus','/static/bus/Mulakkal.jpg',5),(29,'Amnu','KL4876','blue','hg','/static/bus/Mulakkal.jpg',5);

/*Table structure for table `bus_locations` */

DROP TABLE IF EXISTS `bus_locations`;

CREATE TABLE `bus_locations` (
  `locid` int(11) NOT NULL AUTO_INCREMENT,
  `busid` int(11) DEFAULT NULL,
  `latitude` varchar(20) DEFAULT NULL,
  `longitude` varchar(20) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `Date` date DEFAULT NULL,
  `Time` varchar(200) DEFAULT NULL,
  `stopid` int(11) DEFAULT NULL,
  PRIMARY KEY (`locid`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=latin1;

/*Data for the table `bus_locations` */

insert  into `bus_locations`(`locid`,`busid`,`latitude`,`longitude`,`place`,`Date`,`Time`,`stopid`) values (1,29,'11.602','75.1211','kakkur','2022-02-19','11',1),(2,29,'11.602','75.1211','chelannur','2022-02-19','12',2),(3,29,'11.602','75.1211','kumaraswami','2022-02-19','13',3),(4,29,'11.602','75.1211','kakkodi','2022-02-19','14',4),(5,29,'11.602','75.1211','kakkur','2022-02-20','11',1),(6,29,'11.602','75.1211','chelannur','2022-02-20','12',2),(7,29,'11.602','75.1211','kumaraswami','2022-02-20','13',3),(8,29,'11.6565','75.6686','kakkodi ','2022-02-20','14',4),(9,29,'11.602','75.1211','kakkur','2022-02-21','11',1),(10,29,'11.602','75.1211','chelannur','2022-02-21','12',2),(11,29,'11.602','75.1211','kumaraswami','2022-02-21','13',3),(12,29,'11.6511','75.6612','kakkodi ','2022-02-21','14',4),(13,29,'11.602','75.1211','kakkur','2022-02-22','11',1),(14,29,'11.602','75.1211','chelannur','2022-02-22','12',2),(15,29,'11.602','75.1211','kumaraswami','2022-02-22','13',3),(16,29,'11.6565','75.6686','kakkodi ','2022-02-22','14',4),(17,29,'11.6565','75.6686','kakkur','2022-02-23','11',1),(18,29,'11.6565','75.6686','chelannur','2022-02-23','12',2),(19,29,'11.6565','75.6686','kumaraswami','2022-02-23','13',3),(30,28,'67687676','7687676','hjhj','2022-03-01','03:00',NULL),(31,28,'67687676','7687676','hjhj','2022-03-01','03:00',NULL),(32,28,'67687676','7687676','hjhj','2022-03-01','03:00',NULL),(33,28,'h76876','7687676','jhjg','2022-03-10','02:10',NULL),(34,28,'h76876','7687676','jhjg','2022-03-10','02:10',NULL),(35,28,'h76876','7687676','jhjg','2022-03-10','02:10',NULL),(36,28,'h76876','7687676','jhjg','2022-03-10','02:10',NULL),(37,28,'h76876','7687676','jhjg','2022-03-10','02:10',NULL),(38,28,'h76876','7687676','jhjg','2022-03-10','02:10',NULL),(39,28,'h76876','7687676','jhjg','2022-03-10','130',NULL);

/*Table structure for table `emergency` */

DROP TABLE IF EXISTS `emergency`;

CREATE TABLE `emergency` (
  `emergency_id` int(11) NOT NULL AUTO_INCREMENT,
  `message` varchar(100) DEFAULT NULL,
  `date` varchar(40) DEFAULT NULL,
  `time` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`emergency_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `emergency` */

insert  into `emergency`(`emergency_id`,`message`,`date`,`time`) values (2,'Be alert','2022-01-28','11:30:06');

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `location id` int(11) NOT NULL AUTO_INCREMENT,
  `latitude` varchar(70) DEFAULT NULL,
  `longitude` varchar(70) DEFAULT NULL,
  `busid` int(11) DEFAULT NULL,
  `status` varchar(70) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  PRIMARY KEY (`location id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `location` */

insert  into `location`(`location id`,`latitude`,`longitude`,`busid`,`status`,`date`,`time`) values (1,'79.6','45.8',4,'fghv','0000-00-00','01:30:00'),(2,'36.7','80',18,'hnbm','0000-00-00','04:25:00'),(3,'100','100',19,'jjnm',NULL,NULL),(4,'11.4357996','75.8263402',2,'user','2022-02-19','22:19:55');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(70) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values (1,'admin@gmail.com','admin','admin'),(2,'u','u','user'),(4,'thasreefa777@gmail.com','8606588653','user');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notid` int(11) NOT NULL AUTO_INCREMENT,
  `notification` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`notid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notid`,`notification`,`date`) values (1,'you are arrived at Thrissu',NULL),(3,'Reached shoranur',NULL),(6,'hiiiiiiiiiiiiiiiiiiiiii','2022-01-28');

/*Table structure for table `route` */

DROP TABLE IF EXISTS `route`;

CREATE TABLE `route` (
  `routeid` int(11) NOT NULL AUTO_INCREMENT,
  `routename` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`routeid`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `route` */

insert  into `route`(`routeid`,`routename`) values (5,'Kozhikkod'),(7,'Thrissur'),(9,'Malappuram'),(10,'Kuttippuram'),(11,'Kuttippuram'),(12,'Pattambi'),(13,'Valanchery'),(14,'Koppam');

/*Table structure for table `stop` */

DROP TABLE IF EXISTS `stop`;

CREATE TABLE `stop` (
  `stopid` int(11) NOT NULL AUTO_INCREMENT,
  `routeid` int(11) DEFAULT NULL,
  `stopname` varchar(70) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`stopid`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `stop` */

insert  into `stop`(`stopid`,`routeid`,`stopname`,`latitude`,`longitude`,`place`) values (1,5,'kakkur','11.6012','75.1211','kakkur'),(2,5,'chelannur','11.6511','75.6612','chelannur'),(3,5,'kumaraswami','11.6535','75.6634','kumaraswami'),(4,5,'kakkodi','11.6565','75.6686','kakkodi');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `user id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(70) DEFAULT NULL,
  `photo` varchar(500) DEFAULT NULL,
  `place` varchar(70) DEFAULT NULL,
  `post` varchar(70) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `district` varchar(70) DEFAULT NULL,
  `email` varchar(80) DEFAULT NULL,
  `contact` bigint(20) DEFAULT NULL,
  `lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`user id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`user id`,`name`,`photo`,`place`,`post`,`pin`,`district`,`email`,`contact`,`lid`) values (1,'Thasreefa P M','/static/userpics/2022_02_19_12_11_22.099499.jpg','Cheruthuruthi','Cheruthuruthi',679531,'Thrissur','thasreefa777@gmail.com',8606588653,3);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
