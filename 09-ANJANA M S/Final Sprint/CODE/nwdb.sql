/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - project
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`project` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `project`;

/*Table structure for table `answer` */

DROP TABLE IF EXISTS `answer`;

CREATE TABLE `answer` (
  `ans_id` int(10) NOT NULL AUTO_INCREMENT,
  `student_id` int(10) DEFAULT NULL,
  `exam_id` int(10) DEFAULT NULL,
  `ans_paper` text,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  PRIMARY KEY (`ans_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `answer` */

insert  into `answer`(`ans_id`,`student_id`,`exam_id`,`ans_paper`,`date`,`time`) values 
(1,6,3,'storage_6666-3331_DCIM_Camera_20170423_172907.jpg','2022-02-08','21:57:42'),
(2,6,2,'storage_emulated_0_Download_teacher-education-school-classroom-computer-icons-teacher.jpg','2022-02-09','02:33:24');

/*Table structure for table `course_table` */

DROP TABLE IF EXISTS `course_table`;

CREATE TABLE `course_table` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `course` varchar(20) DEFAULT NULL,
  `description` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `course_table` */

insert  into `course_table`(`id`,`course`,`description`) values 
(1,'BCA','Bachelor of Computer Application'),
(2,'BSC CS','Computer Science'),
(3,'B.Com CA','Computer Application'),
(4,'BA English','English Language');

/*Table structure for table `exam` */

DROP TABLE IF EXISTS `exam`;

CREATE TABLE `exam` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sid` int(11) DEFAULT NULL,
  `date` varchar(20) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  `q_paper` varchar(100) DEFAULT NULL,
  `duration` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `exam` */

insert  into `exam`(`id`,`sid`,`date`,`time`,`q_paper`,`duration`) values 
(2,1,'2022-02-10','01:05','key.png','1');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(20) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'rahul123','123rahul','staff'),
(3,'arjun123','123arjun','staff'),
(4,'beena123','123beena','staff'),
(5,'sachin123','123sachin','staff'),
(6,'a','a','student'),
(7,'priya','1234','student');

/*Table structure for table `pics` */

DROP TABLE IF EXISTS `pics`;

CREATE TABLE `pics` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stud_id` int(11) DEFAULT NULL,
  `pic` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `pics` */

insert  into `pics`(`id`,`stud_id`,`pic`) values 
(1,6,'aa.jpg'),
(2,7,'user.jpg');

/*Table structure for table `student_table` */

DROP TABLE IF EXISTS `student_table`;

CREATE TABLE `student_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `first_name` varchar(20) DEFAULT NULL,
  `middle_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(20) DEFAULT NULL,
  `dob` varchar(20) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `course` int(11) DEFAULT NULL,
  `place` varchar(20) DEFAULT NULL,
  `post` varchar(20) DEFAULT NULL,
  `pin` bigint(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(30) DEFAULT NULL,
  `date_of_admision` varchar(30) DEFAULT NULL,
  `semester` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`,`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `student_table` */

insert  into `student_table`(`id`,`login_id`,`first_name`,`middle_name`,`last_name`,`dob`,`gender`,`course`,`place`,`post`,`pin`,`phone`,`email`,`date_of_admision`,`semester`) values 
(1,6,'Mhd','shahil','KP','2001-02-01','male',1,'kottakkal','kottakkal',786959,7886959584,'shahil@gmail.com','2020-08-11','1'),
(2,7,'priya','s','nair','1995-12-25','female',2,'calicut','calicut',890989,9090897878,'priyasnair@gmail.com','2021-02-02','1');

/*Table structure for table `study_material` */

DROP TABLE IF EXISTS `study_material`;

CREATE TABLE `study_material` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sub_id` int(30) DEFAULT NULL,
  `material` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `study_material` */

insert  into `study_material`(`id`,`sub_id`,`material`) values 
(1,1,'Blackboard_Teachers_Day_Poster'),
(2,2,'CF_M4_S3_MASC.pdf');

/*Table structure for table `subject_table` */

DROP TABLE IF EXISTS `subject_table`;

CREATE TABLE `subject_table` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `course_id` int(5) NOT NULL,
  `semester` varchar(15) NOT NULL,
  `subject` varchar(20) NOT NULL,
  `description` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

/*Data for the table `subject_table` */

insert  into `subject_table`(`id`,`course_id`,`semester`,`subject`,`description`) values 
(1,1,'1','Descrete Maths','1st Semester BCA subject'),
(2,1,'1','HTML','BCA subject'),
(3,1,'2','Financial Management','BCA subject'),
(4,1,'2','Operation Research','2nd sem subject'),
(5,2,'3','Python Programming','Cs'),
(6,2,'4','Computer Graphics','cG'),
(7,3,'5','Statistics','bcom'),
(8,3,'2','finance','bcom'),
(9,4,'2','zeitgiest','english'),
(10,1,'4','journalism','english');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
