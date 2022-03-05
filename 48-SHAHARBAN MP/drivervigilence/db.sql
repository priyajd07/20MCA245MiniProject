/*
SQLyog Community Edition- MySQL GUI v8.03 
MySQL - 5.7.19 : Database - driver_vigilence
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`driver_vigilence` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `driver_vigilence`;

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `driverlogin_id` int(11) DEFAULT NULL,
  `complaint` varchar(50) DEFAULT NULL,
  `replay` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`driverlogin_id`,`complaint`,`replay`,`status`,`date`) values (1,1,'ssf','dsggedg',NULL,'2021-12-03'),(2,2,'gfhgj','pending',NULL,'2020-04-14'),(3,3,'jhjo;kl','dsfwefvsevfdx',NULL,'2019-06-28'),(4,4,'bad service','pending','pending','2021-11-25'),(6,4,'hfc n','pending','pending','2021-11-25');

/*Table structure for table `distraction` */

DROP TABLE IF EXISTS `distraction`;

CREATE TABLE `distraction` (
  `distraction_id` int(11) NOT NULL AUTO_INCREMENT,
  `driverlogin_id` int(11) DEFAULT NULL,
  `placename` varchar(50) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`distraction_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `distraction` */

/*Table structure for table `driver` */

DROP TABLE IF EXISTS `driver`;

CREATE TABLE `driver` (
  `driver_id` int(11) NOT NULL AUTO_INCREMENT,
  `driverlogin_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `house_no` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `contact_no` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`driver_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `driver` */

insert  into `driver`(`driver_id`,`driverlogin_id`,`name`,`house_no`,`place`,`post`,`pin`,`contact_no`,`email`,`photo`) values (1,1,'saa','333','dvv','dfdg',23244,135466,'gfgf@gmail.com',NULL),(2,2,'manu','234','ggg','mjk',787653,1598356,'fdytut@gmail.com',NULL),(3,3,'geetha','565','hgjh','bvj',44478,4654989,'ffjhk@gmail.com',NULL),(4,4,'senthil','h2','p2','karaikkal',655210,9632580741,'noob@gmail.com','/static/driver_image/20211125-100825.jpg'),(5,5,'santhosh','h3','p3','pst',369852,9876453120,'san@gmail.com','/static/driver_image/20211126-101107.jpg');

/*Table structure for table `driver_add_partner` */

DROP TABLE IF EXISTS `driver_add_partner`;

CREATE TABLE `driver_add_partner` (
  `dap_id` int(11) NOT NULL AUTO_INCREMENT,
  `driverlogin_id` int(11) DEFAULT NULL,
  `partnerlogin_id` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`dap_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `driver_add_partner` */

insert  into `driver_add_partner`(`dap_id`,`driverlogin_id`,`partnerlogin_id`,`date`) values (1,5,8,'2021-11-26'),(4,4,8,'2021-11-26');

/*Table structure for table `driver_logs` */

DROP TABLE IF EXISTS `driver_logs`;

CREATE TABLE `driver_logs` (
  `logs_id` int(11) NOT NULL AUTO_INCREMENT,
  `driverlogin_id` int(11) DEFAULT NULL,
  `speed` varchar(50) DEFAULT NULL,
  `angle` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  `latitude` varchar(50) DEFAULT NULL,
  `longitude` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`logs_id`)
) ENGINE=MyISAM AUTO_INCREMENT=247 DEFAULT CHARSET=latin1;

/*Data for the table `driver_logs` */

insert  into `driver_logs`(`logs_id`,`driverlogin_id`,`speed`,`angle`,`date`,`time`,`latitude`,`longitude`) values (1,4,'','','2021-11-27','10:33:01','11.2589434','75.7839381'),(2,4,'','','2021-11-27','10:33:51','11.2589402','75.7839357'),(3,4,'','','2021-11-27','10:34:42','11.258943','75.7839265'),(4,4,'','','2021-11-27','10:35:32','11.2589407','75.7839315'),(5,4,'','','2021-11-27','10:36:23','11.2589417','75.7839311'),(6,4,'','','2021-11-27','10:37:11','11.2589379','75.7839317'),(7,4,'','','2021-11-27','10:38:02','11.2589408','75.7839343'),(8,4,'','','2021-11-27','10:38:52','11.2589399','75.7839362'),(9,4,'','','2021-11-27','10:39:42','11.2589392','75.7839371'),(10,4,'','','2021-11-27','10:40:32','11.2589418','75.7839346'),(11,4,'','','2021-11-27','10:41:23','11.2589442','75.7839426'),(12,4,'','','2021-11-27','10:42:12','11.2589383','75.7839357'),(13,4,'','','2021-11-27','10:43:02','11.2589447','75.7839254'),(14,4,'0','0.39','2021-11-27','11:02:32','75.7839251','11.2589434'),(15,4,'0','0.10','2021-11-27','11:02:47','75.7839251','11.2589434'),(16,4,'0','0.33','2021-11-27','11:03:03','75.7839294','11.2589458'),(17,4,'0','0.27','2021-11-27','11:03:17','75.7839285','11.2589501'),(18,4,'0','0.10','2021-11-27','11:03:32','75.7839301','11.2589486'),(19,4,'0','0.53','2021-11-27','11:03:47','75.7839301','11.2589486'),(20,4,'0','0.48','2021-11-27','11:04:02','75.7839301','11.2589486'),(21,4,'0','0.45','2021-11-27','11:04:17','75.7839301','11.2589486'),(22,4,'0','-0.20','2021-11-27','11:04:32','75.783936','11.2589447'),(23,4,'0','-0.30','2021-11-27','11:04:47','75.783936','11.2589447'),(24,4,'0','0.09','2021-11-27','11:05:02','75.7839356','11.2589406'),(25,4,'0','0.09','2021-11-27','11:05:17','75.7839309','11.2589444'),(26,4,'0','0.08','2021-11-27','11:05:32','75.7839301','11.2589454'),(27,4,'0','0.09','2021-11-27','11:05:47','75.7839301','11.2589454'),(28,4,'0','0.08','2021-11-27','11:06:02','75.7839344','11.2589425'),(29,4,'0','0.09','2021-11-27','11:06:17','75.7839316','11.2589457'),(30,4,'0','0.08','2021-11-27','11:06:32','75.7839313','11.2589461'),(31,4,'0','0.08','2021-11-27','11:09:02','75.7839313','11.2589461'),(32,4,'0','0.09','2021-11-27','11:11:13','75.7839313','11.2589461'),(33,4,'0','0.08','2021-11-27','11:11:28','75.7839313','11.2589461'),(34,4,'0','0.09','2021-11-27','11:23:38','75.7839313','11.2589461'),(35,4,'0','0.09','2021-11-27','11:26:09','75.7839313','11.2589461'),(36,4,'0','0.09','2021-11-27','11:39:37','75.7839313','11.2589461'),(37,4,'0','0.09','2021-11-27','11:42:02','75.7839313','11.2589461'),(38,4,'0','0.09','2021-11-27','11:42:03','75.7839313','11.2589461'),(39,4,'0','0.09','2021-11-27','11:59:40','75.7839313','11.2589461'),(40,4,'0','0.09','2021-11-27','11:59:41','75.7839313','11.2589461'),(41,4,'0','0.09','2021-11-27','11:59:47','75.7839313','11.2589461'),(42,4,'0','0.09','2021-11-27','12:17:37','75.7839313','11.2589461'),(43,4,'0','0.09','2021-11-27','12:17:37','75.7839313','11.2589461'),(44,4,'0','0.09','2021-11-27','12:22:00','75.7839313','11.2589461'),(45,4,'0','0.16','2021-11-27','12:22:05','75.7839313','11.2589461'),(46,4,'0','-0.18','2021-11-27','12:22:10','75.7839364','11.2589533'),(47,4,'0','-0.98','2021-11-27','12:22:26','75.7839364','11.2589533'),(48,4,'0','-0.19','2021-11-27','12:22:40','75.7839414','11.2589522'),(49,4,'0','-0.19','2021-11-27','12:22:55','75.7839295','11.2589455'),(50,4,'0','-0.20','2021-11-27','12:23:11','75.7839349','11.2589447'),(51,4,'0','-0.19','2021-11-27','12:23:29','75.7839349','11.2589447'),(52,4,'0','-0.44','2021-11-27','12:23:41','75.7839348','11.2589466'),(53,4,'0','-0.93','2021-11-27','12:23:56','75.7839296','11.2589479'),(54,4,'0','-0.97','2021-11-27','12:24:11','75.7839339','11.2589446'),(55,4,'0','-0.33','2021-11-27','12:24:26','75.7839339','11.2589446'),(56,4,'0','-0.08','2021-11-27','12:24:40','75.7839337','11.2589445'),(57,4,'0','-0.28','2021-11-27','12:24:55','75.7839254','11.2589443'),(58,4,'0','-0.28','2021-11-27','12:25:11','75.7839254','11.2589443'),(59,4,'0','-0.28','2021-11-27','12:25:25','75.7839017','11.2589499'),(60,4,'0','-0.25','2021-11-27','12:25:41','75.7839298','11.2589488'),(61,4,'0','-0.28','2021-11-27','12:25:56','75.7839119','11.2589484'),(62,4,'0','-0.30','2021-11-27','12:26:11','75.7839119','11.2589484'),(63,4,'0','-0.30','2021-11-27','12:26:25','75.7839159','11.2589458'),(64,4,'0','-0.30','2021-11-27','12:26:40','75.7839159','11.2589458'),(65,4,'0','-0.28','2021-11-27','12:26:55','75.7839159','11.2589458'),(66,4,'0','-0.29','2021-11-27','12:30:15','75.7839159','11.2589458'),(67,4,'0','-0.29','2021-11-27','12:30:29','75.7839159','11.2589458'),(68,4,'0','-0.29','2021-11-27','12:30:44','75.7839159','11.2589458'),(69,4,'0','-0.29','2021-11-27','12:30:59','75.7839159','11.2589458'),(70,4,'0','-0.29','2021-11-27','12:31:15','75.7839159','11.2589458'),(71,4,'0','-0.29','2021-11-27','12:31:30','75.7839159','11.2589458'),(72,4,'0','-0.29','2021-11-27','12:31:44','75.7839159','11.2589458'),(73,4,'0','-0.29','2021-11-27','12:31:59','75.7839159','11.2589458'),(74,4,'0','-0.29','2021-11-27','12:32:14','75.7839159','11.2589458'),(75,4,'0','-0.29','2021-11-27','12:32:32','75.7839159','11.2589458'),(76,4,'0','-0.29','2021-11-27','12:32:45','75.7839159','11.2589458'),(77,4,'0','0.69','2021-11-27','12:33:00','75.7839003','11.2589458'),(78,4,'0','0.65','2021-11-27','12:33:14','75.7839003','11.2589458'),(79,4,'0','0.65','2021-11-27','12:33:30','75.7839003','11.2589458'),(80,4,'0','0.76','2021-11-27','12:33:45','75.7839003','11.2589458'),(81,4,'0','0.76','2021-11-27','12:34:00','75.7839163','11.2589481'),(82,4,'0','0.76','2021-11-27','12:34:14','75.7839291','11.2589455'),(83,4,'0','0.77','2021-11-27','12:34:29','75.783934','11.2589446'),(84,4,'0','0.76','2021-11-27','12:34:44','75.783934','11.2589446'),(85,4,'0','0.76','2021-11-27','12:34:59','75.7839238','11.2589468'),(86,4,'0','0.04','2021-11-27','12:35:15','75.7839321','11.2589409'),(87,4,'0','0.25','2021-11-27','12:35:29','75.7839333','11.258945'),(88,4,'0','0.26','2021-11-27','12:35:44','75.7839333','11.258945'),(89,4,'0','0.24','2021-11-27','12:35:59','75.7839335','11.2589454'),(90,4,'0','0.24','2021-11-27','12:36:14','75.7839335','11.2589454'),(91,4,'0','0.23','2021-11-27','12:36:29','75.7839335','11.2589454'),(92,4,'0','0.23','2021-11-27','12:36:44','75.7839335','11.2589454'),(93,4,'0','0.23','2021-11-27','12:36:59','75.7839335','11.2589454'),(94,4,'0','0.23','2021-11-27','12:37:15','75.7839335','11.2589454'),(95,4,'0','0.23','2021-11-27','12:37:29','75.7839335','11.2589454'),(96,4,'0','0.23','2021-11-27','12:37:44','75.7839335','11.2589454'),(97,4,'0','0.23','2021-11-27','12:38:00','75.7839335','11.2589454'),(98,4,'0','0.23','2021-11-27','12:38:14','75.7839335','11.2589454'),(99,4,'0','0.23','2021-11-27','12:38:30','75.7839335','11.2589454'),(100,4,'0','0.23','2021-11-27','12:38:45','75.7839335','11.2589454'),(101,4,'0','0.23','2021-11-27','12:39:00','75.7839335','11.2589454'),(102,4,'0','0.23','2021-11-27','12:39:15','75.7839335','11.2589454'),(103,4,'0','0.23','2021-11-27','12:39:30','75.7839335','11.2589454'),(104,4,'0','0.23','2021-11-27','12:39:45','75.7839335','11.2589454'),(105,4,'0','0.23','2021-11-27','12:40:00','75.7839335','11.2589454'),(106,4,'0','0.23','2021-11-27','12:40:15','75.7839335','11.2589454'),(107,4,'0','0.23','2021-11-27','12:40:30','75.7839335','11.2589454'),(108,4,'0','0.23','2021-11-27','12:40:45','75.7839335','11.2589454'),(109,4,'0','0.23','2021-11-27','12:41:00','75.7839335','11.2589454'),(110,4,'0','0.23','2021-11-27','12:41:15','75.7839335','11.2589454'),(111,4,'0','0.23','2021-11-27','12:41:30','75.7839335','11.2589454'),(112,4,'0','0.23','2021-11-27','12:41:45','75.7839335','11.2589454'),(113,4,'0','0.23','2021-11-27','12:42:00','75.7839335','11.2589454'),(114,4,'0','0.23','2021-11-27','12:42:15','75.7839335','11.2589454'),(115,4,'0','0.23','2021-11-27','12:42:30','75.7839335','11.2589454'),(116,4,'0','0.23','2021-11-27','12:42:45','75.7839335','11.2589454'),(117,4,'0','0.23','2021-11-27','12:43:00','75.7839335','11.2589454'),(118,4,'0','0.23','2021-11-27','12:43:15','75.7839335','11.2589454'),(119,4,'0','0.23','2021-11-27','12:43:30','75.7839335','11.2589454'),(120,4,'0','0.23','2021-11-27','12:43:45','75.7839335','11.2589454'),(121,4,'0','0.23','2021-11-27','12:44:00','75.7839335','11.2589454'),(122,4,'0','0.23','2021-11-27','12:44:15','75.7839335','11.2589454'),(123,4,'0','0.23','2021-11-27','12:44:30','75.7839335','11.2589454'),(124,4,'0','0.23','2021-11-27','12:44:45','75.7839335','11.2589454'),(125,4,'0','0.23','2021-11-27','12:45:00','75.7839335','11.2589454'),(126,4,'0','0.23','2021-11-27','12:45:15','75.7839335','11.2589454'),(127,4,'0','0.23','2021-11-27','12:45:30','75.7839335','11.2589454'),(128,4,'0','0.23','2021-11-27','12:45:45','75.7839335','11.2589454'),(129,4,'0','0.23','2021-11-27','12:46:00','75.7839335','11.2589454'),(130,4,'0','0.23','2021-11-27','12:46:15','75.7839335','11.2589454'),(131,4,'0','0.23','2021-11-27','12:46:30','75.7839335','11.2589454'),(132,4,'0','0.23','2021-11-27','12:46:45','75.7839335','11.2589454'),(133,4,'0','0.23','2021-11-27','12:47:00','75.7839335','11.2589454'),(134,4,'0','0.23','2021-11-27','12:47:15','75.7839335','11.2589454'),(135,4,'0','0.23','2021-11-27','12:47:30','75.7839335','11.2589454'),(136,4,'0','0.23','2021-11-27','12:47:45','75.7839335','11.2589454'),(137,4,'0','0.23','2021-11-27','12:48:01','75.7839335','11.2589454'),(138,4,'0','0.23','2021-11-27','12:48:15','75.7839335','11.2589454'),(139,4,'0','0.23','2021-11-27','12:48:31','75.7839335','11.2589454'),(140,4,'0','0.23','2021-11-27','12:48:46','75.7839335','11.2589454'),(141,4,'0','0.23','2021-11-27','12:49:01','75.7839335','11.2589454'),(142,4,'0','0.23','2021-11-27','12:49:16','75.7839335','11.2589454'),(143,4,'0','0.23','2021-11-27','12:49:31','75.7839335','11.2589454'),(144,4,'0','0.23','2021-11-27','12:49:46','75.7839335','11.2589454'),(145,4,'0','0.23','2021-11-27','12:50:01','75.7839335','11.2589454'),(146,4,'0','0.23','2021-11-27','12:50:16','75.7839335','11.2589454'),(147,4,'0','0.23','2021-11-27','12:50:31','75.7839335','11.2589454'),(148,4,'0','0.23','2021-11-27','12:50:46','75.7839335','11.2589454'),(149,4,'0','0.23','2021-11-27','12:51:01','75.7839335','11.2589454'),(150,4,'0','0.23','2021-11-27','12:51:17','75.7839335','11.2589454'),(151,4,'0','0.23','2021-11-27','12:51:31','75.7839335','11.2589454'),(152,4,'0','0.23','2021-11-27','12:51:46','75.7839335','11.2589454'),(153,4,'0','0.23','2021-11-27','12:52:01','75.7839335','11.2589454'),(154,4,'0','0.23','2021-11-27','12:52:16','75.7839335','11.2589454'),(155,4,'0','0.23','2021-11-27','12:52:31','75.7839335','11.2589454'),(156,4,'0','0.23','2021-11-27','12:52:46','75.7839335','11.2589454'),(157,4,'0','0.23','2021-11-27','12:53:02','75.7839335','11.2589454'),(158,4,'0','0.23','2021-11-27','12:53:16','75.7839335','11.2589454'),(159,4,'0','0.23','2021-11-27','12:53:32','75.7839335','11.2589454'),(160,4,'0','0.23','2021-11-27','12:53:47','75.7839335','11.2589454'),(161,4,'0','0.23','2021-11-27','12:54:02','75.7839335','11.2589454'),(162,4,'0','0.23','2021-11-27','12:54:17','75.7839335','11.2589454'),(163,4,'0','0.23','2021-11-27','12:54:32','75.7839335','11.2589454'),(164,4,'0','0.23','2021-11-27','12:54:47','75.7839335','11.2589454'),(165,4,'0','0.23','2021-11-27','12:55:02','75.7839335','11.2589454'),(166,4,'0','0.23','2021-11-27','12:55:17','75.7839335','11.2589454'),(167,4,'0','0.23','2021-11-27','12:55:32','75.7839335','11.2589454'),(168,4,'0','0.23','2021-11-27','12:55:47','75.7839335','11.2589454'),(169,4,'0','0.23','2021-11-27','12:56:02','75.7839335','11.2589454'),(170,4,'0','0.23','2021-11-27','12:56:17','75.7839335','11.2589454'),(171,4,'0','0.23','2021-11-27','12:56:33','75.7839335','11.2589454'),(172,4,'0','0.23','2021-11-27','12:56:47','75.7839335','11.2589454'),(173,4,'0','0.23','2021-11-27','12:57:02','75.7839335','11.2589454'),(174,4,'0','0.23','2021-11-27','12:57:17','75.7839335','11.2589454'),(175,4,'0','0.23','2021-11-27','12:57:32','75.7839335','11.2589454'),(176,4,'0','0.23','2021-11-27','12:57:47','75.7839335','11.2589454'),(177,4,'0','0.23','2021-11-27','12:58:02','75.7839335','11.2589454'),(178,4,'0','0.23','2021-11-27','12:58:17','75.7839335','11.2589454'),(179,4,'0','0.23','2021-11-27','12:58:32','75.7839335','11.2589454'),(180,4,'0','0.23','2021-11-27','12:58:47','75.7839335','11.2589454'),(181,4,'0','0.23','2021-11-27','12:59:02','75.7839335','11.2589454'),(182,4,'0','0.23','2021-11-27','12:59:17','75.7839335','11.2589454'),(183,4,'0','0.23','2021-11-27','12:59:32','75.7839335','11.2589454'),(184,4,'0','0.23','2021-11-27','12:59:47','75.7839335','11.2589454'),(185,4,'0','0.23','2021-11-27','13:00:03','75.7839335','11.2589454'),(186,4,'0','0.23','2021-11-27','13:00:18','75.7839335','11.2589454'),(187,4,'0','0.23','2021-11-27','13:00:33','75.7839335','11.2589454'),(188,4,'0','0.62','2021-11-27','13:00:48','75.7838786','11.2589569'),(189,4,'0','0.66','2021-11-27','14:25:25','75.783931','11.2589453'),(190,4,'0','0.68','2021-11-27','14:25:40','75.7839297','11.2589417'),(191,4,'0','0.09','2021-11-27','14:25:56','75.7839297','11.2589417'),(192,4,'0','0.46','2021-11-27','14:26:10','75.7839423','11.2589561'),(193,4,'0','0.23','2021-11-27','14:26:25','75.7839341','11.2589433'),(194,4,'0','-0.06','2021-11-27','14:26:40','75.7839285','11.2589464'),(195,4,'0','-0.07','2021-11-27','14:26:55','75.7839285','11.2589464'),(196,4,'0','-0.06','2021-11-27','14:27:10','75.7839332','11.2589462'),(197,4,'0','-0.06','2021-11-27','14:27:25','75.7839315','11.2589428'),(198,4,'0','-0.06','2021-11-27','14:27:40','75.7839373','11.2589524'),(199,4,'0','-0.06','2021-11-27','14:27:55','75.7839209','11.2589392'),(200,4,'0','1.04','2021-11-27','14:28:10','75.7839304','11.2589488'),(201,4,'0','0.77','2021-11-27','14:28:26','75.7839304','11.2589488'),(202,4,'0','-0.03','2021-11-27','14:28:40','75.7839327','11.2589438'),(203,4,'0','1.06','2021-11-27','14:28:55','75.7839242','11.2589464'),(204,4,'0','0.71','2021-11-27','14:29:10','75.7839155','11.2589417'),(205,4,'0','0.72','2021-11-27','14:29:25','75.7839155','11.2589417'),(206,4,'0','0.74','2021-11-27','14:29:40','75.7839238','11.2589455'),(207,4,'0','0.35','2021-11-27','14:29:55','75.7839315','11.2589475'),(208,4,'0','0.04','2021-11-27','14:30:10','75.7839261','11.2589471'),(209,4,'0','0.08','2021-11-27','14:30:25','75.7839261','11.2589471'),(210,4,'0','0.09','2021-11-27','14:30:40','75.7839261','11.2589471'),(211,4,'0','0.08','2021-11-27','14:30:55','75.7839261','11.2589471'),(212,4,'0','0.09','2021-11-27','14:31:10','75.7839261','11.2589471'),(213,4,'0','0.09','2021-11-27','14:31:25','75.7839261','11.2589471'),(214,4,'0','0.09','2021-11-27','14:31:41','75.7839261','11.2589471'),(215,4,'0','0.09','2021-11-27','14:31:56','75.7839261','11.2589471'),(216,4,'0','0.09','2021-11-27','14:32:11','75.7839261','11.2589471'),(217,4,'0','0.09','2021-11-27','14:32:26','75.7839261','11.2589471'),(218,4,'0','0.09','2021-11-27','14:32:41','75.7839261','11.2589471'),(219,4,'0','0.09','2021-11-27','14:32:56','75.7839261','11.2589471'),(220,4,'0','0.09','2021-11-27','14:33:11','75.7839261','11.2589471'),(221,4,'0','0.09','2021-11-27','14:33:26','75.7839261','11.2589471'),(222,4,'0','0.09','2021-11-27','14:33:41','75.7839261','11.2589471'),(223,4,'0','0.09','2021-11-27','14:33:56','75.7839261','11.2589471'),(224,4,'0','0.09','2021-11-27','14:34:11','75.7839261','11.2589471'),(225,4,'0','0.09','2021-11-27','14:34:26','75.7839261','11.2589471'),(226,4,'0','0.09','2021-11-27','14:34:41','75.7839261','11.2589471'),(227,4,'0','0.09','2021-11-27','14:34:56','75.7839261','11.2589471'),(228,4,'0','0.09','2021-11-27','14:35:11','75.7839261','11.2589471'),(229,4,'0','0.09','2021-11-27','14:35:26','75.7839261','11.2589471'),(230,4,'0','0.09','2021-11-27','14:35:41','75.7839261','11.2589471'),(231,4,'0','0.09','2021-11-27','14:35:56','75.7839261','11.2589471'),(232,4,'0','0.09','2021-11-27','14:36:11','75.7839261','11.2589471'),(233,4,'0','0.09','2021-11-27','14:36:26','75.7839261','11.2589471'),(234,4,'0','0.09','2021-11-27','14:36:41','75.7839261','11.2589471'),(235,4,'0','0.09','2021-11-27','14:36:56','75.7839261','11.2589471'),(236,4,'0','0.09','2021-11-27','14:37:11','75.7839261','11.2589471'),(237,4,'0','0.09','2021-11-27','14:37:26','75.7839261','11.2589471'),(238,4,'0','0.09','2021-11-27','14:37:41','75.7839261','11.2589471'),(239,4,'0','0.09','2021-11-27','14:37:56','75.7839261','11.2589471'),(240,4,'0','0.09','2021-11-27','14:38:11','75.7839261','11.2589471'),(241,4,'0','0.09','2021-11-27','14:38:26','75.7839261','11.2589471'),(242,4,'0','0.09','2021-11-27','14:38:41','75.7839261','11.2589471'),(243,4,'0','0.09','2021-11-27','14:38:56','75.7839261','11.2589471'),(244,4,'0','0.09','2021-11-27','14:39:11','75.7839261','11.2589471'),(245,4,'0','0.09','2021-11-27','14:39:26','75.7839261','11.2589471'),(246,4,'0','0.09','2021-11-27','14:39:41','75.7839261','11.2589471');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `driverlogin_id` int(11) DEFAULT NULL,
  `feedback` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`driverlogin_id`,`feedback`,`date`) values (1,1,'hfujylskm','2021-03-07'),(2,2,'xdcbchgm','2020-02-12'),(3,3,'cddv','2019-04-22'),(4,4,'lkjhf','2021-11-25');

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `driverlogin_id` int(11) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `latitude` float DEFAULT NULL,
  `longitude` float DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  PRIMARY KEY (`location_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `location` */

insert  into `location`(`location_id`,`driverlogin_id`,`location`,`latitude`,`longitude`,`date`,`time`) values (1,4,'Lakshmi Arcade',75.7839,11.2589,'2021-11-27','14:39:41'),(2,5,NULL,NULL,NULL,'2021-11-26','10:11:07');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `user_type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`user_name`,`password`,`user_type`) values (1,'admin','111','admin'),(2,'user','user','user'),(4,'noob@gmail.com','123','driver'),(5,'san@gmail.com','987654','driver'),(7,'hayato@gmail.com','909090','user'),(8,'chrono@gmail.com','1234','user');

/*Table structure for table `message` */

DROP TABLE IF EXISTS `message`;

CREATE TABLE `message` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `message` varchar(200) DEFAULT NULL,
  `driverlogin_id` int(11) DEFAULT NULL,
  `partnerlogin_id` int(11) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `message` */

insert  into `message`(`message_id`,`message`,`driverlogin_id`,`partnerlogin_id`,`type`,`date`) values (5,'hello.. will you be late',4,8,'partner','2021-11-26'),(2,'nthellaaa',4,8,'driver','2021-11-26');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `not_id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(100) DEFAULT NULL,
  `content` varchar(200) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`not_id`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`not_id`,`subject`,`content`,`date`) values (4,'fdgilkh','hjgujlkjhvkjhlkj','2021-11-05'),(6,'cccc','vvb\r\nnnm\r\nnmmm','2021-11-05'),(7,'nbjn','fjklo,km','2021-11-05'),(8,'Avoid phone while driving','For your safety and convenience, dock your phone while in Assistant driving mode.','2021-11-05');

/*Table structure for table `partner` */

DROP TABLE IF EXISTS `partner`;

CREATE TABLE `partner` (
  `partner_id` int(11) NOT NULL AUTO_INCREMENT,
  `partnerlogin_id` int(11) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `house_no` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `contact_no` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `photo` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`partner_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `partner` */

insert  into `partner`(`partner_id`,`partnerlogin_id`,`name`,`house_no`,`place`,`post`,`pin`,`contact_no`,`email`,`photo`) values (2,8,'akhil','veemas','irattapilakkool','pallur',670672,963085,'chrono@gmail.com','/static/user_image/20211126-130221.jpg');

/*Table structure for table `speed_settings` */

DROP TABLE IF EXISTS `speed_settings`;

CREATE TABLE `speed_settings` (
  `speed_id` int(11) NOT NULL AUTO_INCREMENT,
  `driver_lid` int(11) DEFAULT NULL,
  `speed` varchar(50) DEFAULT NULL,
  `mode` varchar(50) DEFAULT NULL,
  `brightness` varchar(50) DEFAULT NULL,
  `touch` varchar(50) DEFAULT NULL,
  `callblock` varchar(50) DEFAULT NULL,
  `auto_msg` varchar(50) DEFAULT NULL,
  `msg_type` varchar(50) DEFAULT NULL,
  `message` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`speed_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `speed_settings` */

insert  into `speed_settings`(`speed_id`,`driver_lid`,`speed`,`mode`,`brightness`,`touch`,`callblock`,`auto_msg`,`msg_type`,`message`) values (1,4,'0-40','silent','50','no','yes','yes',NULL,'asdfgh');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
