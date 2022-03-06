/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.5.20-log : Database - career_tech
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`career_tech` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `career_tech`;

/*Table structure for table `apply` */

DROP TABLE IF EXISTS `apply`;

CREATE TABLE `apply` (
  `apply_id` int(11) NOT NULL AUTO_INCREMENT,
  `candidate_id` int(11) NOT NULL,
  `job_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY (`apply_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `apply` */

insert  into `apply`(`apply_id`,`candidate_id`,`job_id`,`date`,`status`) values 
(1,35,6,'2022-01-31','pending'),
(2,36,6,'2022-01-31','pending'),
(3,36,7,'2022-01-31','pending'),
(4,35,7,'2022-01-31','pending'),
(5,36,8,'2022-01-31','pending'),
(6,38,6,'2022-01-31','pending');

/*Table structure for table `candidate` */

DROP TABLE IF EXISTS `candidate`;

CREATE TABLE `candidate` (
  `candidate_id` int(11) NOT NULL AUTO_INCREMENT,
  `candidate_name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `contact_01` bigint(20) NOT NULL,
  `conatct_02` bigint(20) NOT NULL,
  `login_id` int(20) DEFAULT NULL,
  PRIMARY KEY (`candidate_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `candidate` */

insert  into `candidate`(`candidate_id`,`candidate_name`,`email`,`contact_01`,`conatct_02`,`login_id`) values 
(2,'Anusree','anu@gmail.com',9736428647,8625186257,22),
(3,'AparnaKodiyatt','aparnakodiyatt@gmail.com',9876543210,9876543210,27),
(6,'Anjana','anjana@gmail.com',9876543210,9123456780,31),
(7,'Mubi','mubi@gmail.com',9876543321,9235678905,32),
(8,'Aparna','kodiyatt@gmail.com',9876543210,9876543210,29),
(9,'Hari','havwas42hari@gmail.com ',9876543210,9876543210,35),
(10,'Rahul','rahul@gmail.com',9876543210,9876512300,36),
(11,'naveen','naveen@gmail.com',9877568645,768636756,38);

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL,
  `candidate_id` int(11) NOT NULL,
  `company_id` int(11) DEFAULT NULL,
  `question` varchar(100) NOT NULL,
  `answer` varchar(100) NOT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

/*Table structure for table `company_details` */

DROP TABLE IF EXISTS `company_details`;

CREATE TABLE `company_details` (
  `company_id` int(11) NOT NULL AUTO_INCREMENT,
  `company_name` varchar(50) NOT NULL,
  `place` varchar(30) NOT NULL,
  `post` varchar(20) NOT NULL,
  `pin` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `contact_no` bigint(20) NOT NULL,
  `about` varchar(200) NOT NULL,
  `established_date` date NOT NULL,
  `login_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

/*Data for the table `company_details` */

insert  into `company_details`(`company_id`,`company_name`,`place`,`post`,`pin`,`email`,`contact_no`,`about`,`established_date`,`login_id`) values 
(24,'adasf','safsaf','afasdf',0,'',0,'','0000-00-00',25),
(25,'riss','mavoor road','vadakara',678456,'riss@gmail.com',9867564534,'ddddd','1996-01-06',37);

/*Table structure for table `company_question` */

DROP TABLE IF EXISTS `company_question`;

CREATE TABLE `company_question` (
  `qid` int(11) NOT NULL AUTO_INCREMENT,
  `post_id` int(11) DEFAULT NULL,
  `question` varchar(200) DEFAULT NULL,
  `option1` varchar(50) DEFAULT NULL,
  `option2` varchar(50) DEFAULT NULL,
  `option3` varchar(50) DEFAULT NULL,
  `option4` varchar(50) DEFAULT NULL,
  `correct_answer` varchar(50) DEFAULT NULL,
  `company_loginid` int(11) DEFAULT NULL,
  KEY `qid` (`qid`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `company_question` */

insert  into `company_question`(`qid`,`post_id`,`question`,`option1`,`option2`,`option3`,`option4`,`correct_answer`,`company_loginid`) values 
(2,2,'qw','sa','zx','vc','mm','sa',3),
(3,4,'who developed python','Billgates','challsbabage','george','samual','Billgates',21),
(4,6,'The index numbers of five commodities are 121, 123','123.8','124.2','124.6','125.2','124.6',25),
(5,6,'Number of wheels in a car','1','2','3','4','4',25),
(6,10,'Founder of C?','Dennis Rechie','Thomas ','Edson','Mubashira','Dennis Rechie',33),
(7,10,'1+2','1','3','4','2','3',33);

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `candidate_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `complaint` varchar(500) NOT NULL,
  `reply` varchar(500) NOT NULL,
  PRIMARY KEY (`complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaint_id`,`candidate_id`,`date`,`complaint`,`reply`) values 
(1,1,'2021-04-02','sfdgeryrtut','pending'),
(2,29,'2021-05-20','hii all','pending'),
(3,31,'2021-05-20','Exam not working properly ','pending'),
(4,35,'2021-05-20','hii','pending'),
(5,22,'2021-12-13','kooi','pending');

/*Table structure for table `education_qualification` */

DROP TABLE IF EXISTS `education_qualification`;

CREATE TABLE `education_qualification` (
  `education_id` int(11) NOT NULL AUTO_INCREMENT,
  `candidate_id` int(11) NOT NULL,
  `education` varchar(50) NOT NULL,
  `institution_board` varchar(100) NOT NULL,
  `year_of_pass` year(4) NOT NULL,
  `university_no` varchar(20) NOT NULL,
  `percentage_mark` varchar(50) NOT NULL,
  PRIMARY KEY (`education_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `education_qualification` */

insert  into `education_qualification`(`education_id`,`candidate_id`,`education`,`institution_board`,`year_of_pass`,`university_no`,`percentage_mark`) values 
(4,22,'B-Tech','SIMAT',2021,'SPT17CS008','95'),
(5,31,'B-Tech, M-Tech','SIMAT',2021,'SPT17CS007','95'),
(6,35,'B-Tech, M-Tech','SIMAT',2021,'SPT17CS013','97'),
(7,36,'B-Tech','Simat',2021,'rahul2233','95'),
(8,38,'btech','awh',2018,'pwanscs376','90');

/*Table structure for table `exam_shedule` */

DROP TABLE IF EXISTS `exam_shedule`;

CREATE TABLE `exam_shedule` (
  `eid` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `time` varchar(50) DEFAULT NULL,
  `candiid` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`eid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `exam_shedule` */

insert  into `exam_shedule`(`eid`,`date`,`time`,`candiid`,`password`) values 
(1,'2021-06-22','08:10','35','hari@1');

/*Table structure for table `feedbacks` */

DROP TABLE IF EXISTS `feedbacks`;

CREATE TABLE `feedbacks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `feedback` varchar(600) DEFAULT NULL,
  `date` varchar(90) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `feedbacks` */

insert  into `feedbacks`(`id`,`uid`,`feedback`,`date`) values 
(1,22,'good','22-01-2021'),
(2,35,'hai','2022-01-31');

/*Table structure for table `job_post` */

DROP TABLE IF EXISTS `job_post`;

CREATE TABLE `job_post` (
  `job_id` int(11) NOT NULL AUTO_INCREMENT,
  `job_name` varchar(50) NOT NULL,
  `company_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `skills_required` varchar(200) NOT NULL,
  `description` varchar(500) NOT NULL,
  `qualification` varchar(100) DEFAULT NULL,
  `experience` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`job_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `job_post` */

insert  into `job_post`(`job_id`,`job_name`,`company_id`,`date`,`skills_required`,`description`,`qualification`,`experience`) values 
(6,'Associate Engg. Trainee',25,'2021-05-18','Python','You will identify business opportunities','BTech, Mtech','2 years'),
(7,'Business Consultant',25,'2021-05-18','English, Tally','You will be responsible for a group of project managers, their teams and the deliverables for your set of accounts.','B.Com, MBA','1 year'),
(8,'Manager',26,'2021-05-20','Python, Java, C','TCS manager','B-Tech, M-tech','1 year'),
(9,'Software Engg.',30,'2021-05-20','C, C++,Java,Python','Best one for software development','B-Tech','6 months'),
(10,'Assistant Professor',33,'2021-05-20','Python, Java, C, C++','Striving for excellence in generation and dissemination of knowledge.','B-Tech, M-Tech','2 years'),
(11,'HOD CSE',33,'2021-05-21','Programming Languages','Recruitment for the Professor CSE Dept.','B-Tech, M-Tech, PHD in CS','2 years as lecture'),
(12,'Manager',34,'2021-05-22','Python, Java, C, C++','Manager Post','B-Tech, M-tech','1 year'),
(13,'hr',25,'2021-10-20','kkm','kkm','765765','2yr'),
(14,'hr',25,'2021-10-21','kkm','kkm','123456','2yr');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `user_type` varchar(50) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`user_name`,`password`,`user_type`) values 
(1,'admin','admin','admin'),
(22,'anjana','anjana@123','user'),
(25,'Infosis','infosis123','company'),
(26,'TCS','tcs123','company'),
(29,'Aparna','aparna123','user'),
(30,'HP','hp123','company'),
(32,'mubi','muni123','user'),
(33,'SIMAT','simat123','company'),
(34,'IBM','ibm123','company'),
(35,'hari','hari123','user'),
(36,'rahul','rahul123','user'),
(37,'riss','riss','company'),
(38,'naveen','naveen','user');

/*Table structure for table `notification_table` */

DROP TABLE IF EXISTS `notification_table`;

CREATE TABLE `notification_table` (
  `notification_no` int(11) NOT NULL AUTO_INCREMENT,
  `company_id` int(11) NOT NULL,
  `message` varchar(200) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`notification_no`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `notification_table` */

insert  into `notification_table`(`notification_no`,`company_id`,`message`,`date`) values 
(1,25,'You have selected in our team','2021-05-18'),
(2,25,'Add new post to recruit students','2021-05-18'),
(3,30,'Hiii','2021-05-20'),
(4,33,'Hello SIMAT. You have successfully registered in our team!','2021-05-21'),
(5,34,'you are registered','2021-05-22');

/*Table structure for table `opeclose` */

DROP TABLE IF EXISTS `opeclose`;

CREATE TABLE `opeclose` (
  `id` int(11) NOT NULL,
  `opedate` varchar(43) DEFAULT NULL,
  `closedate` varchar(43) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `opeclose` */

insert  into `opeclose`(`id`,`opedate`,`closedate`) values 
(1,'2021-10-20','2021-10-30'),
(14,'2021-10-21','2021-10-06'),
(15,'2022-01-10','2022-01-25');

/*Table structure for table `qualification_details` */

DROP TABLE IF EXISTS `qualification_details`;

CREATE TABLE `qualification_details` (
  `qid` int(11) NOT NULL AUTO_INCREMENT,
  `candidate_id` int(11) DEFAULT NULL,
  `skills` varchar(50) DEFAULT NULL,
  `experience` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`qid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `qualification_details` */

insert  into `qualification_details`(`qid`,`candidate_id`,`skills`,`experience`) values 
(1,29,'Python','1 year'),
(2,31,'C, C++','6 months '),
(3,35,'Python, Java, C','1 year'),
(4,36,'Python, Java, C, C++','2 years');

/*Table structure for table `questions_and_answers` */

DROP TABLE IF EXISTS `questions_and_answers`;

CREATE TABLE `questions_and_answers` (
  `qstn_no` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(500) NOT NULL,
  `option1` varchar(100) NOT NULL,
  `option2` varchar(100) NOT NULL,
  `option3` varchar(100) NOT NULL,
  `option4` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  `correct_answer` varchar(500) NOT NULL,
  `login_id` int(11) NOT NULL,
  `comid` int(11) DEFAULT NULL,
  `postid` int(11) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`qstn_no`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

/*Data for the table `questions_and_answers` */

insert  into `questions_and_answers`(`qstn_no`,`question`,`option1`,`option2`,`option3`,`option4`,`type`,`correct_answer`,`login_id`,`comid`,`postid`,`status`) values 
(12,'What is the fourth proportional of 0.006, 1.2 & 6/25? ','36','48','3.6','4.8','Aptitude','48',1,25,6,'accepted'),
(17,'I have a vivid imagination','I agree','I strongly agree','I disagree','I strongly disagree','Personality','I agree',1,33,8,'accepted'),
(19,' limitation of selective breeding studies is that they cannot',' tell us anything about the role of genes','be used to study human beings','provide information relevant to the nature/nurture debate','tell us anything about the role of the environment','Personality',' be used to study human beings',33,34,8,'accepted'),
(20,'Which neo-Freudian challenged his ideas about penis envy?','Adler','Fromm',' Jung','Horney','Personality','Horney',33,33,8,'accepted'),
(24,'(112 x 54) = ?','67000','70000','76500','77200','Aptitude','70000',33,33,8,'accepted'),
(27,'1397 x 1397 = ?','1951609','1981709','18362619','2031719','Aptitude','1951609',33,33,8,'accepted');

/*Table structure for table `recommendation` */

DROP TABLE IF EXISTS `recommendation`;

CREATE TABLE `recommendation` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `job_id` int(11) NOT NULL,
  `candidate_id` int(11) NOT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `recommendation` */

/*Table structure for table `result` */

DROP TABLE IF EXISTS `result`;

CREATE TABLE `result` (
  `result_id` int(11) NOT NULL AUTO_INCREMENT,
  `candidate_id` int(11) NOT NULL,
  `com_id` int(11) NOT NULL,
  `post_id` varchar(100) NOT NULL,
  `marks` float NOT NULL,
  `totalqstn` int(11) DEFAULT NULL,
  PRIMARY KEY (`result_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `result` */

insert  into `result`(`result_id`,`candidate_id`,`com_id`,`post_id`,`marks`,`totalqstn`) values 
(1,35,33,'10',2,2),
(2,36,33,'10',1,5),
(3,35,33,'10',3,4),
(4,36,33,'10',4,5);

/*Table structure for table `resume` */

DROP TABLE IF EXISTS `resume`;

CREATE TABLE `resume` (
  `resume_no` int(11) NOT NULL AUTO_INCREMENT,
  `photo` varchar(100) NOT NULL,
  `dob` date NOT NULL,
  `objective` varchar(200) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `house` varchar(100) NOT NULL,
  `place` varchar(50) NOT NULL,
  `post` varchar(50) NOT NULL,
  `pin` bigint(11) NOT NULL,
  `father` varchar(50) NOT NULL,
  `mother` varchar(50) NOT NULL,
  `guardian` varchar(50) NOT NULL,
  `relation_to_guardian` varchar(20) NOT NULL,
  `canid` int(11) DEFAULT NULL,
  PRIMARY KEY (`resume_no`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `resume` */

insert  into `resume`(`resume_no`,`photo`,`dob`,`objective`,`gender`,`house`,`place`,`post`,`pin`,`father`,`mother`,`guardian`,`relation_to_guardian`,`canid`) values 
(1,'images_6.jpeg','0000-00-00','cg','Female','vbj','jgf','aijg',658457,'vcf','lkah','tgdj','vh',22),
(2,'images_6.jpeg','1970-01-01','HAri','Male','KKK','PPP','PO',679576,'SSSS','SSS','FFF','FFF',35);

/*Table structure for table `shortlist` */

DROP TABLE IF EXISTS `shortlist`;

CREATE TABLE `shortlist` (
  `serial_no` int(11) NOT NULL AUTO_INCREMENT,
  `candidate_id` int(11) NOT NULL,
  `rank` int(11) NOT NULL,
  PRIMARY KEY (`serial_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `shortlist` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
