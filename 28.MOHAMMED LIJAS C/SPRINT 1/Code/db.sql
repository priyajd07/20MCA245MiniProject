/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - cyberbullying
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`cyberbullying` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `cyberbullying`;

/*Table structure for table `bullying` */

DROP TABLE IF EXISTS `bullying`;

CREATE TABLE `bullying` (
  `l_id` int(11) DEFAULT NULL COMMENT 'contains the login id',
  `bull_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'contains the bullying id',
  `bull_word` varchar(100) DEFAULT NULL COMMENT 'contains the bullying word',
  `date` date DEFAULT NULL COMMENT 'contains the date',
  PRIMARY KEY (`bull_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `bullying` */

insert  into `bullying`(`l_id`,`bull_id`,`bull_word`,`date`) values 
(1,1,'aaaa','2022-01-04');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'contains  chat id',
  `f_id` int(11) DEFAULT NULL COMMENT 'contains from id',
  `t_id` int(11) DEFAULT NULL COMMENT 'contains the to id',
  `msg` text COMMENT 'contains the message',
  `date` date DEFAULT NULL COMMENT 'contains the date',
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

/*Table structure for table `comment` */

DROP TABLE IF EXISTS `comment`;

CREATE TABLE `comment` (
  `c_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'contains the comment id',
  `post_id` int(11) DEFAULT NULL COMMENT 'contains the post id',
  `user_id` int(11) DEFAULT NULL COMMENT 'contains the user id',
  `comment` varchar(100) DEFAULT NULL COMMENT 'contains the comment',
  `date` date DEFAULT NULL COMMENT 'contains the date',
  `status` varchar(100) DEFAULT NULL COMMENT 'contains the status',
  PRIMARY KEY (`c_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `comment` */

/*Table structure for table `good` */

DROP TABLE IF EXISTS `good`;

CREATE TABLE `good` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `word` varchar(500) NOT NULL,
  `date` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `good` */

/*Table structure for table `likke` */

DROP TABLE IF EXISTS `likke`;

CREATE TABLE `likke` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `postid` int(11) DEFAULT NULL,
  `like` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `from_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `likke` */

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `l_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'contains the login id',
  `user_name` varchar(100) DEFAULT NULL COMMENT 'contains the name of users',
  `password` varchar(50) DEFAULT NULL COMMENT 'contains the password',
  `usertype` varchar(50) NOT NULL COMMENT 'contains the usertype',
  PRIMARY KEY (`l_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`l_id`,`user_name`,`password`,`usertype`) values 
(1,'admin','admin','admin');

/*Table structure for table `post` */

DROP TABLE IF EXISTS `post`;

CREATE TABLE `post` (
  `post_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'contains post id',
  `l_id` int(11) DEFAULT NULL COMMENT 'contains login id',
  `post` varchar(100) DEFAULT NULL COMMENT 'contains post',
  `caption` varchar(100) DEFAULT NULL COMMENT 'contains caption',
  `date` date DEFAULT NULL COMMENT 'contains',
  PRIMARY KEY (`post_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `post` */

/*Table structure for table `report` */

DROP TABLE IF EXISTS `report`;

CREATE TABLE `report` (
  `report_id` int(11) NOT NULL AUTO_INCREMENT,
  `l_id` int(11) DEFAULT NULL,
  `post_id` varchar(11) DEFAULT NULL,
  `comment` text,
  `date` date DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`report_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `report` */

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `from_id` int(11) DEFAULT NULL,
  `to_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`request_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `request` */

/*Table structure for table `share` */

DROP TABLE IF EXISTS `share`;

CREATE TABLE `share` (
  `sid` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` int(11) DEFAULT NULL,
  `fromid` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `share` */

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `l_id` int(11) DEFAULT NULL COMMENT 'contains the id of login',
  `user_id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'contains the id of user',
  `f_name` varchar(100) DEFAULT NULL COMMENT 'contains the first name',
  `l_name` varchar(100) DEFAULT NULL COMMENT 'contains the last name',
  `gender` varchar(100) DEFAULT NULL COMMENT 'contains the gender',
  `d_o_b` varchar(100) DEFAULT NULL COMMENT 'contains the date of birth',
  `phone_number` bigint(100) DEFAULT NULL COMMENT 'contains the phone number',
  `photo` varchar(100) DEFAULT NULL COMMENT 'contains photo',
  `bio` varchar(100) DEFAULT NULL COMMENT 'contains the bio',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`l_id`,`user_id`,`f_name`,`l_name`,`gender`,`d_o_b`,`phone_number`,`photo`,`bio`) values 
(2,1,'anu','mol','female','2-3-1999',9987654322,'koala.jpg','ghjktyujk');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
