-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 04, 2022 at 05:30 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.4.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `turf`
--

-- --------------------------------------------------------

--
-- Table structure for table `aid_information`
--

CREATE TABLE `aid_information` (
  `id` int(11) NOT NULL,
  `m_id` int(11) NOT NULL,
  `medicine_name` varchar(50) NOT NULL,
  `details` varchar(100) NOT NULL,
  `purpose` varchar(100) NOT NULL,
  `mode of usage` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `aid_information`
--

INSERT INTO `aid_information` (`id`, `m_id`, `medicine_name`, `details`, `purpose`, `mode of usage`) VALUES
(1, 0, 'actine d metz', 'using for maint', 'head ache', 'xx'),
(2, 0, 'derrr', 'using for maintxsf', 'rrr', 'uuuu'),
(3, 0, 'actine d metz', 'using for maint', 'head ache', 'xx'),
(4, 0, 'actine d metz', 'using for maint', 'head ache', 'xx');

-- --------------------------------------------------------

--
-- Table structure for table `aid_team`
--

CREATE TABLE `aid_team` (
  `a_id` int(11) NOT NULL,
  `m_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `turf location` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `gender` varchar(11) NOT NULL,
  `district` varchar(30) NOT NULL,
  `dob` varchar(15) NOT NULL,
  `qualification` varchar(100) NOT NULL,
  `department` varchar(100) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(100) NOT NULL,
  `repeatpassword` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `aid_team`
--

INSERT INTO `aid_team` (`a_id`, `m_id`, `name`, `turf location`, `address`, `phone`, `gender`, `district`, `dob`, `qualification`, `department`, `email`, `password`, `repeatpassword`) VALUES
(10, 0, 'aswin', 'kannur', 'Azhiyour', '956854522', 'Male', 'Kozhikode', '2021-07-20', 'asd', 'ssss', 'aid', 'aid', 'aid'),
(11, 0, 'Shijin P', 'azhioor', 'presanna nivas \r\nnear ghss azhiyoor', '7736592025', 'Male', 'Thiruvananthapuram', '1997-11-03', 'MCA', 'COMPUTER SCIENCE', 'shijin270@gmail.com', 'shijin123', 'shijin123'),
(14, 0, 'reehan', 'Caliut', 'asd dds gses s', '956854522', 'Male', 'Kozhikode', '2021-09-04', 'MCA', 'COMPUTER SCIENCE', 'neeraj.ar', 'asd', 'asd'),
(15, 0, 'alan', 'amal', 'UHUdascass', '7736592025', 'Male', 'Wayanad', '2021-08-07', 'MCA', 'COMPUTER SCIENCE', 'alan@gmai', 'aaa', 'aaa'),
(16, 8, 'soorya', 'Caliut', 'Azhiyour', '7736592025', 'Female', 'Thiruvananthapuram', '2021-08-26', 'asd', 'hyuj', 'soorya', 'aaa', 'aaa'),
(18, 7, 'afnan', 'Cochin', 'eertHOUSE\r\nCHAKKAD ', '956854522', 'Male', 'Wayanad', '2021-08-13', 'asd', 'COMPUTER SCIENCE', 'afnany', 'qqq', 'qqw'),
(19, 7, 'Shijin P', 'Trivandrum', 'Azhiyour', '7736539898', 'Male', 'Kollam', '2021-08-19', 'asd', 'aaa', 'azaar@gmail.com', 'a', 'as'),
(20, 7, 'Shijixaan P', 'Mlappuram', 'Azhiyour', '7736592025', 'Male', 'Alappuzha', '2021-09-03', 'MCA', 'hyuj', 'rizwan@gmail.com', 'qqqq', 'qqqq');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `booking`
--

CREATE TABLE `booking` (
  `b_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `m_id` int(11) NOT NULL,
  `t_id` varchar(11) NOT NULL,
  `turflocation` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(50) NOT NULL,
  `status` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `booking`
--

INSERT INTO `booking` (`b_id`, `u_id`, `m_id`, `t_id`, `turflocation`, `name`, `phone`, `email`, `date`, `time`, `status`) VALUES
(5, 18, 7, '3', 'kalloor', 'nihal', '98986521', 'wt@gmail.com', '2021-08-09', '13:24:00', 'approved'),
(6, 2, 7, '3', 'kalloor', 'nihal', '98986521', 'wt@gmail.com', '2021-08-09', '13:24:00', 'approved'),
(7, 8, 1, '4', 'asst', 'anin', '2147483647', 'shiji@gmail.com', '2021-12-12', '11:20:11', 'pending'),
(8, 13, 12, '9', 'Sparta Arena', 'gm', '1234568901', 'g', '2021-09-22', '17 : 20', 'pending'),
(9, 13, 16, '13', 'kakkanad', 'gm', '1234568901', 'g', '2021-09-22', '6:0', 'approved'),
(10, 1, 20, '1', 'calicut', 'thejhsw', '1223244', 'dafdfsdfs', '2022-01-15', '2022-01-15 11:37:10.279447', 'pending'),
(11, 1, 14, '16', 'Mahe', 'thejhsw', '1223244', 'dafdfsdfs', '2022-01-15', '2022-01-15 11:38:25.852015', 'approved with #1000'),
(12, 1, 13, '10', 'vadakara', 'thejhsw', '1223244', 'dafdfsdfs', '2022-01-15', '2022-01-15 11:39:35.565077', 'pending'),
(13, 1, 20, '1', 'calicut', 'thejhsw', '1223244', 'dafdfsdfs', '2022-01-15', '11:51:21', 'pending'),
(14, 1, 20, '1', 'calicut', 'thejhsw', '1223244', 'dafdfsdfs', '2022-01-15', '11:56:25', 'pending'),
(15, 1, 30, '22', 'calicut', 'thejhsw', '1223244', 'dafdfsdfs', '2022-01-15', '12:09:55', 'approved with #2000'),
(16, 1, 30, '22', 'calicut', 'thejhsw', '1223244', 'dafdfsdfs', '2022-01-19', '16:43', 'approved with #1000'),
(17, 14, 30, '22', 'calicut', 'suhail', '1231231234', 'fasna@gamil.com', '2022-01-16', '14:02', 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `complaint`
--

CREATE TABLE `complaint` (
  `c_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `phone` int(15) NOT NULL,
  `email` varchar(30) NOT NULL,
  `address` varchar(100) NOT NULL,
  `complaint` varchar(120) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `complaint`
--

INSERT INTO `complaint` (`c_id`, `u_id`, `name`, `phone`, `email`, `address`, `complaint`, `date`, `reply`) VALUES
(1, 0, 'Turf 2', 23461284, 'sk@gmail.com', 'asfsfsc', '', '2021-07-14', 'granted\r\n'),
(2, 0, 'nivedh', 23461284, 'sk@gmail.com', 'sdfgn', 'aasdfghjk', '2021-07-08', 'yes'),
(5, 0, 'nihal', 98986521, 'ss', 'sSWDADA', 'Asss', '2021-07-07', ''),
(6, 44, 'aneesh', 80000000, 'nulll', 'an niavs', 'turf problem', '2021-07-22', 'lll'),
(7, 55, 'nihal', 78999999, 'wt@gmail.com', 'dfghjkl;\'', 'hgutyt', '2021-07-16', 'pending'),
(8, 1, 'jhon', 778965955, 'jhon@gmail.com', 'kr villa calicut', 'dfgtdt', '2021-09-03', 'pending'),
(9, 1, 'jhon', 778965955, 'jhon@gmail.com', 'kr villa calicut', 'dfgtdt', '2021-09-03', 'pending'),
(10, 1, 'jhon', 778965955, 'jhon@gmail.com', 'kr villa calicut', 'hqqqqqqqq', '2021-09-06', 'pending'),
(11, 1, 'jhon', 778965955, 'jhon@gmail.com', 'kr villa calicut', 'fffff', '2021-09-06', 'pending'),
(12, 1, 'thejhsw', 1223244, 'dafdfsdfs', 'sdddafdf', 'Testing', '2021-09-06', 'pending'),
(13, 13, 'gm', 1234568901, 'g', 'wAYANAD', 'teting', '2021-09-12', 'pending'),
(14, 1, 'thejhsw', 1223244, 'dafdfsdfs', 'sdddafdf', 'hbj', '2022-01-17', 'pending'),
(15, 1, 'thejhsw', 1223244, 'dafdfsdfs', 'sdddafdf', 'hbj', '2022-01-17', 'pending'),
(16, 1, 'thejhsw', 1223244, 'dafdfsdfs', 'sdddafdf', 'hbj', '2022-01-17', 'pending'),
(17, 1, 'thejhsw', 1223244, 'dafdfsdfs', 'sdddafdf', 'nbhjb ', '2022-01-17', 'hgjk');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-07-29 05:27:39.872044'),
(2, 'auth', '0001_initial', '2021-07-29 05:27:50.657138'),
(3, 'admin', '0001_initial', '2021-07-29 05:27:52.885865'),
(4, 'admin', '0002_logentry_remove_auto_add', '2021-07-29 05:27:52.986134'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2021-07-29 05:27:53.228777'),
(6, 'contenttypes', '0002_remove_content_type_name', '2021-07-29 05:27:54.392890'),
(7, 'auth', '0002_alter_permission_name_max_length', '2021-07-29 05:27:55.488274'),
(8, 'auth', '0003_alter_user_email_max_length', '2021-07-29 05:27:55.674696'),
(9, 'auth', '0004_alter_user_username_opts', '2021-07-29 05:27:55.718811'),
(10, 'auth', '0005_alter_user_last_login_null', '2021-07-29 05:27:56.362108'),
(11, 'auth', '0006_require_contenttypes_0002', '2021-07-29 05:27:56.414702'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2021-07-29 05:27:56.506948'),
(13, 'auth', '0008_alter_user_username_max_length', '2021-07-29 05:27:56.764309'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2021-07-29 05:27:57.127744'),
(15, 'auth', '0010_alter_group_name_max_length', '2021-07-29 05:27:57.371339'),
(16, 'auth', '0011_update_proxy_permissions', '2021-07-29 05:27:57.490656'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2021-07-29 05:27:57.603996'),
(18, 'sessions', '0001_initial', '2021-07-29 05:27:58.511874');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0jyy5anpi9sta7b55pdyvs73dlzmyuba', 'ZTM4NDA0NDY0MjEzMDM0N2U0NTJhNzAyNTA2Yzc4MzY1NmQ5ZTI0Yzp7InVpZCI6MH0=', '2022-01-27 11:01:45.076331'),
('1k4tzkcrgoeiv1cf5e4v0l9s0fybji7n', 'eyJ1aWQiOjB9:1mLiEe:wTxWRQHLZ_O8Z8Gc3CCERMkkfBr6zpHgkwTl5Z6578Y', '2021-09-16 08:38:12.073679'),
('28m3rknewue56rpsz2hbgsltvtcrm3g4', 'eyJ1aWQiOjE2fQ:1mPKtj:Fmpc2gUNjiWn-rxqjIe-b0VzGscPVvt1JgPVNubsX6o', '2021-09-26 08:31:35.107474'),
('bzpj2iapvfhu94ev26sidtng8358y1gs', 'NWNmNjdiNjk5NTliZWFhMDRlNDI1N2ZiMzA1NWQyNWNmMGY2NDM4NDp7InVpZCI6MTN9', '2022-02-02 04:39:15.465154'),
('eaipsatgbhptnkrr8hw4ugka1ab431yb', 'NzNlYzg4YWE0NGMyNzdhNjA5MTU4ZTQyMWI1ZTBiZGRhMjhmNGUwZTp7InVpZCI6N30=', '2022-02-16 08:39:34.934580'),
('l3wnoeqct6h139rgafmy2ilwgbcsqz6s', 'eyJ1aWQiOjd9:1mLLFG:BuJTprR6Un_B3IiHbgtzEOeq1OWlPiYd4Qt5jkZkvsg', '2021-09-15 08:05:18.966557'),
('qfm6yww55wuyy752cwf2c10zwcxc8hlj', 'eyJ1aWQiOjd9:1mEOd6:wvFnnkxoCv6Y5mlNz8ma9nE-x8s2n8APYM5q0S4Dwjc', '2021-08-27 04:17:12.397183'),
('skke0sfcabcnuoblti8ey79yzj4pk9wd', 'eyJ1aWQiOjE2fQ:1mPKuF:nlSbbkFH1kd4TNj0BTcJu7fxA9yGZvYnbD-F0XqFgiI', '2021-09-26 08:32:07.289502'),
('vxzf9vyvd9uw3tqle5b5kbswuzdxp8cl', 'eyJ1aWQiOjE2fQ:1mPKiT:Jt2eYui9FWkCcCK8HXBLx-9719-i10VYUNIEJ3jOOl0', '2021-09-26 08:19:57.529966'),
('ym7tuwemq1bmy8ay430r9pf4zmibav89', 'NjJhOThlZjMwZmQ0NDVkMzllZGJlMGUyYjdjN2FjZjgxZDNkODMyNTp7InVpZCI6MX0=', '2022-02-14 11:13:53.732278');

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `f_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `feedback` varchar(150) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `feedback`
--

INSERT INTO `feedback` (`f_id`, `u_id`, `feedback`, `date`, `reply`) VALUES
(1, 0, 'haiiiiiiiiiiiii', '2021-07-14', 'okkkkkkkk'),
(2, 2, 'hey', '2021-07-13', 'pending'),
(3, 2, 'adsasd', '2021-02-02', 'hyess'),
(4, 2, 'adsasd', '2021-02-02', 'yes'),
(5, 2, 'adsasd', '2021-02-02', 'pending'),
(6, 2, 'hey', '2021-07-13', 'pending'),
(7, 1, 'Godd', '2021-09-02', 'pending'),
(8, 1, 'Good', '2021-09-02', 'pending'),
(9, 1, 'Good', '2021-09-02', 'pending'),
(10, 1, 'bdf', '2021-09-03', 'pending'),
(11, 1, 'gfng', '2021-09-06', 'pending'),
(12, 1, 'gfng', '2021-09-06', 'pending'),
(13, 1, 'fffffffffffffff', '2021-09-06', 'pending'),
(14, 13, 'Good', '2021-09-12', 'pending'),
(15, 0, 'bvfvg', '2022-01-13', 'pending'),
(16, 0, ' agvg', '2022-01-13', 'pending'),
(17, 0, 'csdc', '2022-01-13', 'pending'),
(18, 0, 'mnnjkm', '2022-01-13', 'n ');

-- --------------------------------------------------------

--
-- Table structure for table `health_record`
--

CREATE TABLE `health_record` (
  `id` int(11) NOT NULL,
  `a_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `gender` varchar(15) NOT NULL,
  `email` varchar(30) NOT NULL,
  `age` int(11) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `address` varchar(100) NOT NULL,
  `height` int(11) NOT NULL,
  `heart rate` int(11) NOT NULL,
  `cholestrol` int(11) NOT NULL,
  `weight` varchar(25) NOT NULL,
  `blood pressure` int(11) NOT NULL,
  `oxygen level` int(11) NOT NULL,
  `blood group` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `health_record`
--

INSERT INTO `health_record` (`id`, `a_id`, `u_id`, `name`, `gender`, `email`, `age`, `phone`, `address`, `height`, `heart rate`, `cholestrol`, `weight`, `blood pressure`, `oxygen level`, `blood group`) VALUES
(2, 0, 0, 'Shijin P', 'none', 'shijin270@gmail.com', 23, '9846298535', 'Azhiyour', 180, 96, 150, '75', 78, 96, 'B+'),
(3, 0, 0, 'Shijin P', 'Male', 'shijin270@gmail.com', 23, '9846298535', 'Azhiyour', 180, 96, 150, '74', 78, 96, 'B+'),
(4, 10, 1, 'ARUN', 'Male', 'arun@gmai.com', 23, '956854522', 'presanna nivas azhiyoor', 180, 85, 120, '75', 55, 99, 'AB-');

-- --------------------------------------------------------

--
-- Table structure for table `help`
--

CREATE TABLE `help` (
  `id` int(11) NOT NULL,
  `a_id` int(11) NOT NULL,
  `m_id` int(11) NOT NULL,
  `turf location` varchar(20) NOT NULL,
  `time` varchar(15) NOT NULL,
  `date` varchar(15) NOT NULL,
  `help notification` varchar(100) NOT NULL,
  `reply` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `help`
--

INSERT INTO `help` (`id`, `a_id`, `m_id`, `turf location`, `time`, `date`, `help notification`, `reply`) VALUES
(1, 0, 0, 'kannur', '11:30:30', '2021-02-02', 'hai\r\n', 'read'),
(2, 0, 0, 'azhiyoor', '0', '0', 'there is an emergency please healp', ''),
(3, 0, 0, 'kannur', '0', '0', 'fgdfhhhhhhhhhhhhh', 'read'),
(4, 0, 0, 'xxx', '0', '0', 'axsaces', ''),
(5, 0, 7, 'calicut', '2021-08-04', '2021-08-04 11:2', 'haiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii', ''),
(6, 0, 7, 'calicut', '11:32:50.044696', '2021-08-04 11:3', 'shdghabjf', ''),
(7, 0, 7, 'calicut', '11:34:46.338341', '2021-08-04', 'fwwfda', ''),
(8, 0, 10, 'amal', '11:47:47.723403', '2021-08-04', 'zzzzz', ''),
(9, 0, 7, 'Cochin', '11:54:34.729774', '2021-08-09', 'gefsfe', '');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `l_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `type` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`l_id`, `u_id`, `username`, `password`, `type`) VALUES
(1, 0, 'abcd@gmail.com', '1234', 'manager'),
(2, 0, 'admin', 'admin', 'admin'),
(3, 7, 'manager', 'manager', 'manager'),
(4, 10, 'aid', 'aid', 'aidteam'),
(5, 11, 'shijin270@gmail.com', 'shijin123', 'aidteam'),
(6, 12, 'aparna@gmail.com`', 'aparna', 'aidteam'),
(7, 8, 'shaa', 'shaa', 'manager'),
(8, 13, 'as', 'as', 'aidteam'),
(9, 9, 'Anil@gmail.com', 'anil', 'manager'),
(10, 10, 'aid', 'aid', 'manager'),
(11, 13, 'anu', 'anu', 'manager'),
(12, 14, 'neeraj', 'asd', 'aidteam'),
(13, 15, 'alan@gmai', 'aaa', 'aidteam'),
(14, 16, 'soorya', 'aaa', 'aidteam'),
(15, 14, 'sinan@gmail.com', 'ase', 'manager'),
(16, 17, 'ram', '123', 'aidteam'),
(17, 18, 'afnan', 'qqq', 'aidteam'),
(18, 16, 'a@gmail.com', 'aaa', 'manager'),
(19, 17, 'a@gmail.com', 'aaa', 'manager'),
(20, 18, 'sss@gmail.com', 'aaa', 'manager'),
(21, 19, 'appu@gmail.com', '123', 'manager'),
(22, 19, 'azaar@gmail.com', 'a', 'user'),
(23, 20, 'rizwan@gmail.com', 'qqqq', 'aidteam'),
(24, 1, 'u', 'u', 'user'),
(25, 2, 'james@123', 'afsghe', 'user'),
(26, 10, 'asd ', 'asd', 'user'),
(27, 11, 'user', 'pass', 'user'),
(28, 12, 'qwe', 'qwe', 'user'),
(29, 13, 'g', 'g', 'user'),
(30, 25, 'vb@gmail.com', '12', 'manager'),
(31, 26, 'dtc@fhg', '12', 'manager'),
(32, 27, 'dtc@fhg', '12', 'manager'),
(35, 30, 'jishad@gmail.com', '12', 'manager'),
(36, 14, 'fasna@gamil.com', '12', 'user');

-- --------------------------------------------------------

--
-- Table structure for table `manager_registration`
--

CREATE TABLE `manager_registration` (
  `m_id` int(11) NOT NULL,
  `t_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `address` varchar(100) NOT NULL,
  `turf location` varchar(30) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `district` varchar(30) NOT NULL,
  `gender` varchar(11) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  `password` varchar(30) NOT NULL,
  `repeatpassword` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `manager_registration`
--

INSERT INTO `manager_registration` (`m_id`, `t_id`, `name`, `address`, `turf location`, `phone`, `district`, `gender`, `dob`, `email`, `password`, `repeatpassword`) VALUES
(13, 10, 'anoop', 'presanna nivas azhiyoor', 'vadakara', '8485558632', 'Malappuram', 'Male', '2021-08-03', 'anu', 'anu', 'anh'),
(14, 16, 'Sinan jdf', 'sk house', 'Mahe', '7763584523', 'Kannur', 'Male', '2021-08-12', 'sinan@gmail.com', 'ase', 'ase'),
(16, 13, 'aaa', 'ccaca', 'kakkanad', '7736592025', 'Wayanad', 'Male', '2021-08-05', 'a@gmail.com', 'aaa', 'ssss'),
(19, 12, 'Shijin P', 'Azhiyour', 'Kozhikode', '3636595656', 'Eranakulam ', 'Male', '2021-08-03', 'appu@gmail.com', '123', '123'),
(20, 1, 'asd', 'adsfv', 'calicut', '1231231232', 'Kozhikode', 'Male', '2000-01-13', 'ac@gmail.com', '123', '123'),
(23, 20, 'asd', 'calicut', 'calicut', '1231232123', 'Kozhikode', 'Male', '2022-01-13', 'saa@gmail.com', '1234', '1234'),
(30, 22, 'jishad', 'xcbfvxhf', 'calicut', '1231231234', 'Kozhikode', 'Male', '2022-01-14', 'jishad@gmail.com', '12', '12');

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `id` int(11) NOT NULL,
  `b_id` int(11) NOT NULL,
  `u_id` int(11) NOT NULL,
  `m_id` varchar(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `phone` int(15) NOT NULL,
  `email` varchar(20) NOT NULL,
  `amount` varchar(30) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`id`, `b_id`, `u_id`, `m_id`, `name`, `phone`, `email`, `amount`, `date`) VALUES
(1, 0, 0, '0', 'aswin', 23461284, 'sk@gmail.com', '2500', '2021-07-14'),
(2, 0, 0, '0', 'aswin', 23461284, 'sk@gmail.com', '2500', '2021-07-14'),
(3, 1, 2, '4', 'shaa', 778546935, 'shijin@gmail.com', '2500', '2021-09-02'),
(4, 9, 13, '16', 'gm', 1234568901, 'g', '900', '2021-09-12'),
(5, 9, 13, '16', 'gm', 1234568901, 'g', '900', '2021-09-12');

-- --------------------------------------------------------

--
-- Table structure for table `time_slot`
--

CREATE TABLE `time_slot` (
  `ts_id` int(11) NOT NULL,
  `t_id` int(11) NOT NULL,
  `m_id` int(11) NOT NULL,
  `turf location` varchar(30) NOT NULL,
  `date` date NOT NULL,
  `district` varchar(30) NOT NULL,
  `place` varchar(30) NOT NULL,
  `time` varchar(15) NOT NULL,
  `fees` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `time_slot`
--

INSERT INTO `time_slot` (`ts_id`, `t_id`, `m_id`, `turf location`, `date`, `district`, `place`, `time`, `fees`) VALUES
(1, 0, 0, 'Turf 2', '2021-07-16', 'Calicut', 'Nadakkav', '02:22', '202'),
(2, 0, 0, 'amal', '2021-07-09', 'ggggg', 'g', '15:56', '202'),
(3, 0, 0, 'asas', '2021-08-13', 'kannur', 'kannur', '02:00', '202'),
(4, 13, 7, 'Mlappuram', '2021-08-15', 'kannur', 'Nadakkav', '11:58', '200'),
(5, 13, 7, 'Kozhikode', '2021-07-31', 'Idukki', 'nadakkavv', '12:06', '825'),
(6, 13, 7, 'kakkanad', '2021-08-07', 'Eranakulam ', 'nadakkavv', '00:24', '825'),
(7, 10, 7, 'kochi', '2022-01-14', 'Kozhikode', 'calicut', '15:30', '1000'),
(8, 10, 7, 'kochi', '2022-01-14', 'Kottayam ', 'calicut', '18:28', '1000'),
(9, 11, 7, 'Mlappuram', '2022-01-14', 'Kottayam ', 'atholi', '14:54', '2500');

-- --------------------------------------------------------

--
-- Table structure for table `turf_location`
--

CREATE TABLE `turf_location` (
  `l_id` int(11) NOT NULL,
  `l_name` varchar(30) NOT NULL,
  `turf_name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `turf_location`
--

INSERT INTO `turf_location` (`l_id`, `l_name`, `turf_name`) VALUES
(1, 'calicut', 'dof'),
(10, 'kochi', 'Parkway'),
(11, 'Mlappuram', 'MTM Sports'),
(12, 'Kozhikode', 'Lake Zone'),
(13, 'kakkanad', 'Sporthood'),
(15, 'Cochin', 'Cochin sport Arena'),
(16, 'Mahe', 'Global turf'),
(18, 'Trivandrum', 'Sparta Arena'),
(19, 'calicut', 'arena'),
(20, 'calicut', 'soocer'),
(21, 'calicut', 'cx'),
(22, 'calicut', 'riversoccer');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `u_id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `place` varchar(30) NOT NULL,
  `address` varchar(50) NOT NULL,
  `email` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`u_id`, `name`, `phone`, `place`, `address`, `email`) VALUES
(1, 'thejhsw', '1223244', 'ddsffsfsf', 'sdddafdf', 'dafdfsdfs'),
(2, 'james', '7736592025', 'azhiyoor', 'dar qul villa mahe', 'james@123'),
(10, 'alan', '778956255', 'mahe', 'also villa', 'asd '),
(11, 'anwar', '9956481126', 'malappuram', 'milan house vadakara', 'user'),
(12, 'anu', '6669852236', 'ssss', 'sdfgtre', 'qwe'),
(13, 'gm', '1234568901', 'tHARIODE', 'wAYANAD', 'g'),
(14, 'suhail', '1231231234', 'koyilandi', 'calicut', 'fasna@gamil.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `aid_information`
--
ALTER TABLE `aid_information`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `aid_team`
--
ALTER TABLE `aid_team`
  ADD PRIMARY KEY (`a_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `booking`
--
ALTER TABLE `booking`
  ADD PRIMARY KEY (`b_id`);

--
-- Indexes for table `complaint`
--
ALTER TABLE `complaint`
  ADD PRIMARY KEY (`c_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`f_id`);

--
-- Indexes for table `health_record`
--
ALTER TABLE `health_record`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `help`
--
ALTER TABLE `help`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`l_id`);

--
-- Indexes for table `manager_registration`
--
ALTER TABLE `manager_registration`
  ADD PRIMARY KEY (`m_id`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `time_slot`
--
ALTER TABLE `time_slot`
  ADD PRIMARY KEY (`ts_id`);

--
-- Indexes for table `turf_location`
--
ALTER TABLE `turf_location`
  ADD PRIMARY KEY (`l_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`u_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `aid_information`
--
ALTER TABLE `aid_information`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `aid_team`
--
ALTER TABLE `aid_team`
  MODIFY `a_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `booking`
--
ALTER TABLE `booking`
  MODIFY `b_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `complaint`
--
ALTER TABLE `complaint`
  MODIFY `c_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `f_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `login`
--
ALTER TABLE `login`
  MODIFY `l_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `manager_registration`
--
ALTER TABLE `manager_registration`
  MODIFY `m_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `time_slot`
--
ALTER TABLE `time_slot`
  MODIFY `ts_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `turf_location`
--
ALTER TABLE `turf_location`
  MODIFY `l_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `u_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
