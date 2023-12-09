/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.7.40 : Database - tvshow
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`tvshow` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `tvshow`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add category',7,'add_category'),
(26,'Can change category',7,'change_category'),
(27,'Can delete category',7,'delete_category'),
(28,'Can view category',7,'view_category'),
(29,'Can add login',8,'add_login'),
(30,'Can change login',8,'change_login'),
(31,'Can delete login',8,'delete_login'),
(32,'Can view login',8,'view_login'),
(33,'Can add user',9,'add_user'),
(34,'Can change user',9,'change_user'),
(35,'Can delete user',9,'delete_user'),
(36,'Can view user',9,'view_user'),
(37,'Can add tvshow',10,'add_tvshow'),
(38,'Can change tvshow',10,'change_tvshow'),
(39,'Can delete tvshow',10,'delete_tvshow'),
(40,'Can view tvshow',10,'view_tvshow'),
(41,'Can add review',11,'add_review'),
(42,'Can change review',11,'change_review'),
(43,'Can delete review',11,'delete_review'),
(44,'Can view review',11,'view_review'),
(45,'Can add complaint',12,'add_complaint'),
(46,'Can change complaint',12,'change_complaint'),
(47,'Can delete complaint',12,'delete_complaint'),
(48,'Can view complaint',12,'view_complaint');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(2,'auth','permission'),
(3,'auth','group'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(7,'tvshow_app','category'),
(8,'tvshow_app','login'),
(9,'tvshow_app','user'),
(10,'tvshow_app','tvshow'),
(11,'tvshow_app','review'),
(12,'tvshow_app','complaint');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-07-07 11:30:47.218452'),
(2,'auth','0001_initial','2023-07-07 11:30:47.729727'),
(3,'admin','0001_initial','2023-07-07 11:30:47.863799'),
(4,'admin','0002_logentry_remove_auto_add','2023-07-07 11:30:47.875829'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-07-07 11:30:47.885639'),
(6,'contenttypes','0002_remove_content_type_name','2023-07-07 11:30:47.951983'),
(7,'auth','0002_alter_permission_name_max_length','2023-07-07 11:30:47.993977'),
(8,'auth','0003_alter_user_email_max_length','2023-07-07 11:30:48.035394'),
(9,'auth','0004_alter_user_username_opts','2023-07-07 11:30:48.045036'),
(10,'auth','0005_alter_user_last_login_null','2023-07-07 11:30:48.089175'),
(11,'auth','0006_require_contenttypes_0002','2023-07-07 11:30:48.094463'),
(12,'auth','0007_alter_validators_add_error_messages','2023-07-07 11:30:48.112284'),
(13,'auth','0008_alter_user_username_max_length','2023-07-07 11:30:48.160821'),
(14,'auth','0009_alter_user_last_name_max_length','2023-07-07 11:30:48.201824'),
(15,'auth','0010_alter_group_name_max_length','2023-07-07 11:30:48.250339'),
(16,'auth','0011_update_proxy_permissions','2023-07-07 11:30:48.266324'),
(17,'auth','0012_alter_user_first_name_max_length','2023-07-07 11:30:48.306158'),
(18,'sessions','0001_initial','2023-07-07 11:30:48.363908'),
(19,'tvshow_app','0001_initial','2023-07-07 11:30:48.759320'),
(20,'tvshow_app','0002_alter_tvshow_from_time','2023-07-07 11:30:48.793387'),
(21,'tvshow_app','0003_alter_tvshow_description','2023-07-07 11:30:48.831844');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('cxzi4wt754fhzsfvpuy138nptqlsy2w2','e30:1qHk5g:hCLCpuk0udxbOyQUDmXQbQLQtRGqWrhGsh9aQDJ9-1s','2023-07-21 11:57:36.752052');

/*Table structure for table `tvshow_app_category` */

DROP TABLE IF EXISTS `tvshow_app_category`;

CREATE TABLE `tvshow_app_category` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `tvshow_app_category` */

/*Table structure for table `tvshow_app_complaint` */

DROP TABLE IF EXISTS `tvshow_app_complaint`;

CREATE TABLE `tvshow_app_complaint` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `complaint` varchar(500) NOT NULL,
  `status` varchar(100) NOT NULL,
  `reply` varchar(100) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tvshow_app_complaint_USER_id_a3840aaa` (`USER_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `tvshow_app_complaint` */

/*Table structure for table `tvshow_app_login` */

DROP TABLE IF EXISTS `tvshow_app_login`;

CREATE TABLE `tvshow_app_login` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `type` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `tvshow_app_login` */

insert  into `tvshow_app_login`(`id`,`username`,`password`,`type`) values 
(1,'sankardasnasd@gmail.com','61748639','user'),
(2,'admin','admin','admin');

/*Table structure for table `tvshow_app_review` */

DROP TABLE IF EXISTS `tvshow_app_review`;

CREATE TABLE `tvshow_app_review` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `review` varchar(100) NOT NULL,
  `TVSHOW_id` bigint(20) NOT NULL,
  `USER_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tvshow_app_review_TVSHOW_id_2340f5d8` (`TVSHOW_id`),
  KEY `tvshow_app_review_USER_id_20bc1e2c` (`USER_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `tvshow_app_review` */

/*Table structure for table `tvshow_app_tvshow` */

DROP TABLE IF EXISTS `tvshow_app_tvshow`;

CREATE TABLE `tvshow_app_tvshow` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `from_time` varchar(100) NOT NULL,
  `duration` varchar(100) NOT NULL,
  `language` varchar(100) NOT NULL,
  `description` varchar(500) NOT NULL,
  `demo_video` varchar(800) NOT NULL,
  `image` varchar(500) NOT NULL,
  `Date` varchar(100) NOT NULL,
  `channelname` varchar(100) NOT NULL,
  `actors_name` varchar(100) NOT NULL,
  `actress_name` varchar(100) NOT NULL,
  `producer_name` varchar(100) NOT NULL,
  `director_name` varchar(100) NOT NULL,
  `CATEGORY_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tvshow_app_tvshow_CATEGORY_id_fa1595d6` (`CATEGORY_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `tvshow_app_tvshow` */

/*Table structure for table `tvshow_app_user` */

DROP TABLE IF EXISTS `tvshow_app_user`;

CREATE TABLE `tvshow_app_user` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `house_name` varchar(100) NOT NULL,
  `post_name` varchar(100) NOT NULL,
  `landmark` varchar(100) NOT NULL,
  `street_name` varchar(100) NOT NULL,
  `district` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `image` varchar(400) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `LOGIN_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tvshow_app_user_LOGIN_id_6f48b018` (`LOGIN_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `tvshow_app_user` */

insert  into `tvshow_app_user`(`id`,`name`,`house_name`,`post_name`,`landmark`,`street_name`,`district`,`email`,`phone`,`image`,`gender`,`LOGIN_id`) values 
(1,'sankar','hhhhh','679338','kolathur malappuram','ddddddddd','malappuram','sankardasnasd@gmail.com',9961207239,'/media/230707-171108.jpg','male',1);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
