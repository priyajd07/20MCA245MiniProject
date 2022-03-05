/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - road damage
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`road damage` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `road damage`;

/*Table structure for table `alert` */

DROP TABLE IF EXISTS `alert`;

CREATE TABLE `alert` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `imei` varchar(43) DEFAULT NULL,
  `lattitude` varchar(43) DEFAULT NULL,
  `longitude` varchar(43) DEFAULT NULL,
  `image` varchar(43) DEFAULT NULL,
  `result` varchar(34) DEFAULT NULL,
  `datetime` varchar(43) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=153 DEFAULT CHARSET=latin1;

/*Data for the table `alert` */

insert  into `alert`(`id`,`imei`,`lattitude`,`longitude`,`image`,`result`,`datetime`) values 
(1,'2720ecffcba4d58d','11.1409852','75.856845','abc.jpg','cracks','2022-02-01 11:26:56'),
(2,'2720ecffcba4d58d','11.140555','75.8673749','abc.jpg','cracks','2022-02-01 11:42:45'),
(3,'2720ecffcba4d58d','11.140555','75.8673749','abc.jpg','cracks','2022-02-01 11:42:54'),
(4,'2720ecffcba4d58d','11.140555','75.8673749','abc.jpg','cracks','2022-02-01 11:43:04'),
(5,'2720ecffcba4d58d','11.140555','75.8673749','abc.jpg','cracks','2022-02-01 11:43:15'),
(6,'2720ecffcba4d58d','11.140555','75.8673749','abc.jpg','cracks','2022-02-01 11:43:27'),
(7,'2720ecffcba4d58d','11.140555','75.8673749','abc.jpg','cracks','2022-02-01 11:43:39'),
(8,'2720ecffcba4d58d','11.139121','75.8590236','abc.jpg','cracks','2022-02-01 11:43:54'),
(9,'2720ecffcba4d58d','11.1373625','75.8655594','abc.jpg','cracks','2022-02-01 11:44:02'),
(10,'2720ecffcba4d58d','11.140555','75.8673749','abc.jpg','cracks','2022-02-01 11:44:06'),
(11,'2720ecffcba4d58d','11.1342378','75.8579343','abc.jpg','cracks','2022-02-01 11:44:16'),
(12,'2720ecffcba4d58d','11.1342378','75.8579343','abc.jpg','cracks','2022-02-01 11:44:26'),
(13,'2720ecffcba4d58d','11.1342378','75.8579343','abc.jpg','cracks','2022-02-01 11:44:37'),
(14,'2720ecffcba4d58d','11.143505','75.8641071','abc.jpg','cracks','2022-02-01 11:44:50'),
(15,'2720ecffcba4d58d','11.1422789','75.860113','abc.jpg','cracks','2022-02-01 11:45:04'),
(16,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:45:19'),
(17,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:45:34'),
(18,'2720ecffcba4d58d','11.14278779','75.86286368','abc.jpg','cracks','2022-02-01 11:45:50'),
(19,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:46:07'),
(20,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:46:24'),
(21,'2720ecffcba4d58d','11.14280719','75.86261139','abc.jpg','cracks','2022-02-01 11:46:43'),
(22,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:47:04'),
(23,'2720ecffcba4d58d','11.14288907','75.86287248','abc.jpg','cracks','2022-02-01 11:47:24'),
(24,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:47:45'),
(25,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:48:07'),
(26,'2720ecffcba4d58d','11.14286344','75.86279156','abc.jpg','cracks','2022-02-01 11:48:31'),
(27,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:48:59'),
(28,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:49:07'),
(29,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:49:17'),
(30,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:49:27'),
(31,'2720ecffcba4d58d','11.14295336','75.86290568','abc.jpg','cracks','2022-02-01 11:49:39'),
(32,'2720ecffcba4d58d','11.14295336','75.86290568','abc.jpg','cracks','2022-02-01 11:49:51'),
(33,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:50:04'),
(34,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:50:18'),
(35,'2720ecffcba4d58d','11.14292922','75.86289118','abc.jpg','cracks','2022-02-01 11:50:33'),
(36,'2720ecffcba4d58d','11.14292922','75.86289118','abc.jpg','cracks','2022-02-01 11:50:48'),
(37,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:51:05'),
(38,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:51:22'),
(39,'2720ecffcba4d58d','11.14293037','75.86291531','abc.jpg','cracks','2022-02-01 11:51:40'),
(40,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:51:59'),
(41,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:52:18'),
(42,'2720ecffcba4d58d','11.14293862','75.86293235','abc.jpg','cracks','2022-02-01 11:52:38'),
(43,'2720ecffcba4d58d','11.14293862','75.86293235','abc.jpg','cracks','2022-02-01 11:52:59'),
(44,'2720ecffcba4d58d','11.1448855','75.8641071','abc.jpg','cracks','2022-02-01 11:53:22'),
(45,'2720ecffcba4d58d','11.1448855','75.8641071','abc.jpg','cracks','2022-02-01 11:53:45'),
(46,'2720ecffcba4d58d','11.1448855','75.8641071','abc.jpg','cracks','2022-02-01 11:54:09'),
(47,'2720ecffcba4d58d','11.1448855','75.8641071','abc.jpg','cracks','2022-02-01 11:54:34'),
(48,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:55:00'),
(49,'2720ecffcba4d58d','11.14290741','75.86291958','abc.jpg','cracks','2022-02-01 11:55:26'),
(50,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 11:55:56'),
(51,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:56:06'),
(52,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:56:16'),
(53,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:56:27'),
(54,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:56:34'),
(55,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:56:47'),
(56,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:57:02'),
(57,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:57:11'),
(58,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:57:21'),
(59,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:57:32'),
(60,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:57:44'),
(61,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:57:57'),
(62,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:58:06'),
(63,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:58:17'),
(64,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:58:28'),
(65,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:58:40'),
(66,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:58:53'),
(67,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:59:06'),
(68,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:59:21'),
(69,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:59:37'),
(70,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 11:59:54'),
(71,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 12:00:12'),
(72,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 12:00:31'),
(73,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 12:00:51'),
(74,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 12:01:12'),
(75,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 12:01:34'),
(76,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 12:01:57'),
(77,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 12:02:20'),
(78,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 12:02:45'),
(79,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 12:03:12'),
(80,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 12:03:40'),
(81,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 12:04:05'),
(82,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 12:04:19'),
(83,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 12:04:33'),
(84,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 12:04:47'),
(85,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 12:05:01'),
(86,'2720ecffcba4d58d','11.1438484','75.856845','abc.jpg','cracks','2022-02-01 12:05:17'),
(87,'2720ecffcba4d58d','11.1438484','75.856845','abc.jpg','cracks','2022-02-01 12:05:33'),
(88,'2720ecffcba4d58d','11.1448855','75.8641071','abc.jpg','cracks','2022-02-01 12:05:52'),
(89,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 12:06:13'),
(90,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 12:06:36'),
(91,'2720ecffcba4d58d','11.1414864','75.8651963','abc.jpg','cracks','2022-02-01 12:07:10'),
(92,'2720ecffcba4d58d','11.1414864','75.8651963','abc.jpg','cracks','2022-02-01 12:07:22'),
(93,'2720ecffcba4d58d','11.1414864','75.8651963','abc.jpg','cracks','2022-02-01 12:07:34'),
(94,'2720ecffcba4d58d','11.1414864','75.8651963','abc.jpg','cracks','2022-02-01 12:07:45'),
(95,'2720ecffcba4d58d','11.1414864','75.8651963','abc.jpg','cracks','2022-02-01 12:08:00'),
(96,'2720ecffcba4d58d','11.1414864','75.8651963','abc.jpg','cracks','2022-02-01 12:08:13'),
(97,'2720ecffcba4d58d','11.1414864','75.8651963','abc.jpg','cracks','2022-02-01 12:08:27'),
(98,'2720ecffcba4d58d','11.1438484','75.856845','abc.jpg','cracks','2022-02-01 12:08:42'),
(99,'2720ecffcba4d58d','11.1438484','75.856845','abc.jpg','cracks','2022-02-01 12:08:58'),
(100,'2720ecffcba4d58d','11.1438484','75.856845','abc.jpg','cracks','2022-02-01 12:09:16'),
(101,'2720ecffcba4d58d','11.1438484','75.856845','abc.jpg','cracks','2022-02-01 12:09:26'),
(102,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 12:09:37'),
(103,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 12:09:46'),
(104,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 12:09:57'),
(105,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 12:10:12'),
(106,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 12:10:30'),
(107,'2720ecffcba4d58d','11.1448837','75.856845','abc.jpg','cracks','2022-02-01 12:10:48'),
(108,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 12:11:05'),
(109,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 12:11:18'),
(110,'2720ecffcba4d58d','11.1409852','75.8619285','abc.jpg','cracks','2022-02-01 12:11:36'),
(111,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:11:49'),
(112,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:12:04'),
(113,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:12:18'),
(114,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:12:35'),
(115,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:12:52'),
(116,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:13:10'),
(117,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:13:29'),
(118,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:13:49'),
(119,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:14:02'),
(120,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:14:16'),
(121,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:14:31'),
(122,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:14:47'),
(123,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:15:04'),
(124,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:15:22'),
(125,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:15:41'),
(126,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:16:01'),
(127,'2720ecffcba4d58d','11.1432622','75.8590236','abc.jpg','cracks','2022-02-01 12:16:22'),
(128,'2720ecffcba4d58d','11.1432622','75.8590236','abc.jpg','cracks','2022-02-01 12:16:43'),
(129,'2720ecffcba4d58d','11.1432622','75.8590236','abc.jpg','cracks','2022-02-01 12:16:56'),
(130,'2720ecffcba4d58d','11.1409852','75.8619285','abc.jpg','cracks','2022-02-01 12:17:10'),
(131,'2720ecffcba4d58d','11.1409852','75.8619285','abc.jpg','cracks','2022-02-01 12:17:25'),
(132,'2720ecffcba4d58d','11.1409852','75.8619285','abc.jpg','cracks','2022-02-01 12:17:41'),
(133,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:17:58'),
(134,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:18:16'),
(135,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:18:34'),
(136,'2720ecffcba4d58d','11.1429188','75.8662856','abc.jpg','cracks','2022-02-01 12:18:53'),
(137,'2720ecffcba4d58d','11.1422789','75.860113','abc.jpg','cracks','2022-02-01 12:19:15'),
(138,'2720ecffcba4d58d','11.139121','75.8590236','abc.jpg','cracks','2022-02-01 12:19:50'),
(139,'2720ecffcba4d58d','11.1422789','75.860113','abc.jpg','cracks','2022-02-01 12:20:03'),
(140,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 12:20:18'),
(141,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 12:20:34'),
(142,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 12:20:47'),
(143,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 12:21:01'),
(144,'2720ecffcba4d58d','11.1433143','75.860113','abc.jpg','cracks','2022-02-01 12:21:16'),
(145,'2720ecffcba4d58d','11.1448855','75.8641071','abc.jpg','cracks','2022-02-01 12:21:46'),
(146,'2720ecffcba4d58d','11.1448855','75.8641071','abc.jpg','cracks','2022-02-01 12:22:00'),
(147,'2720ecffcba4d58d','11.1448855','75.8641071','abc.jpg','cracks','2022-02-01 12:24:08'),
(148,'2720ecffcba4d58d','11.14307313','75.86298109','abc.jpg','cracks','2022-02-01 12:24:18'),
(149,'2720ecffcba4d58d','11.14307313','75.86298109','abc.jpg','cracks','2022-02-01 12:24:29'),
(150,'2720ecffcba4d58d','11.14307313','75.86298109','abc.jpg','cracks','2022-02-01 12:24:39'),
(151,'2720ecffcba4d58d','11.14307313','75.86298109','abc.jpg','cracks','2022-02-01 12:24:49'),
(152,'2720ecffcba4d58d','11.14307313','75.86298109','abc.jpg','cracks','2022-02-01 12:25:00');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `fid` int(11) NOT NULL AUTO_INCREMENT,
  `user_lid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `feedback` varchar(54) DEFAULT NULL,
  PRIMARY KEY (`fid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`fid`,`user_lid`,`date`,`feedback`) values 
(1,2,'2022-01-29','feedback'),
(2,3,'2022-01-29','vhhh'),
(3,3,'2022-01-29','uuu'),
(4,4,'2022-01-30','jjj');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(54) DEFAULT NULL,
  `password` varchar(54) DEFAULT NULL,
  `usertype` varchar(54) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`usertype`) values 
(1,'admin','admin123','admin'),
(2,'user','user','user'),
(3,'zuu','huu','user'),
(4,'qwerty','qwerty','user');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `nid` int(11) NOT NULL AUTO_INCREMENT,
  `date` date DEFAULT NULL,
  `notification` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`nid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`nid`,`date`,`notification`) values 
(3,'2022-01-05','meeting\r\n');

/*Table structure for table `route` */

DROP TABLE IF EXISTS `route`;

CREATE TABLE `route` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from` varchar(55) DEFAULT NULL,
  `to` varchar(45) DEFAULT NULL,
  `route` varchar(44) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `route` */

insert  into `route`(`id`,`from`,`to`,`route`) values 
(2,'f','t','kk');

/*Table structure for table `track` */

DROP TABLE IF EXISTS `track`;

CREATE TABLE `track` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_lid` int(11) DEFAULT NULL,
  `lattitude` varchar(54) DEFAULT NULL,
  `longitude` varchar(54) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `track` */

insert  into `track`(`id`,`user_lid`,`lattitude`,`longitude`) values 
(1,2,'11.32','75.33');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `uid` int(11) NOT NULL AUTO_INCREMENT,
  `user_lid` int(11) DEFAULT NULL,
  `fname` varchar(55) DEFAULT NULL,
  `lname` varchar(33) DEFAULT NULL,
  `place` varchar(44) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `phone` (`phone`,`email`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`uid`,`user_lid`,`fname`,`lname`,`place`,`phone`,`email`) values 
(1,2,'anu','p','calicut','9922113300','anu@gmail.com'),
(2,3,'hhhhhhhz','zzz','gzz','6958253669','fhh@gmail.com'),
(3,4,'uuu','p','calicut','9625146958','asdkkk@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
