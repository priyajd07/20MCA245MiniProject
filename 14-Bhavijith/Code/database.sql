/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - crimescene_recomendation
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE crimescene_recomendation` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `crimescene_recomendation`;

/*Table structure for table `case` */

DROP TABLE IF EXISTS `case`;

CREATE TABLE `case` (
  `caseid` int(11) NOT NULL AUTO_INCREMENT,
  `policeid` int(11) DEFAULT NULL,
  `case` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `criminal` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`caseid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `case` */

insert  into `case`(`caseid`,`policeid`,`case`,`date`,`place`,`type`,`description`,`criminal`) values 
(1,1,'murder','2022-01-03','clt','aaa','aaaaaaaaaaa','ttttt');

/*Table structure for table `crime_report` */

DROP TABLE IF EXISTS `crime_report`;

CREATE TABLE `crime_report` (
  `reportid` int(11) NOT NULL AUTO_INCREMENT,
  `caseid` int(11) DEFAULT NULL,
  `report` varchar(60) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `evidence` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`reportid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `crime_report` */

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'qqq','qqq','vo'),
(3,'qwerty','1234','vo'),
(4,'qwerty','123','vo'),
(5,'qwerty','123','vo');

/*Table structure for table `police` */

DROP TABLE IF EXISTS `police`;

CREATE TABLE `police` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `age` bigint(20) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `police` */

insert  into `police`(`pid`,`lid`,`fname`,`lname`,`age`,`gender`,`place`,`post`,`pin`,`phone`,`email`) values 
(4,5,'haz','v',20,'female','clt','clt',678543,'4565666','aaa@gmail.com');

/*Table structure for table `work_assign` */

DROP TABLE IF EXISTS `work_assign`;

CREATE TABLE `work_assign` (
  `assignid` int(11) NOT NULL AUTO_INCREMENT,
  `policeid` int(11) DEFAULT NULL,
  `work` varchar(80) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`assignid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `work_assign` */

/*Table structure for table `work_report` */

DROP TABLE IF EXISTS `work_report`;

CREATE TABLE `work_report` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `workid` int(11) DEFAULT NULL,
  `report` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `work_report` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
