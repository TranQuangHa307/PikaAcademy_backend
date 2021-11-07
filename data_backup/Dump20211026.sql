-- MySQL dump 10.13  Distrib 8.0.27, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: edumall
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin_account`
--

DROP TABLE IF EXISTS `admin_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_account` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `user_name` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` longtext CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `role` enum('admin','member') NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `updated_by` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `deleted_flag` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_account`
--

LOCK TABLES `admin_account` WRITE;
/*!40000 ALTER TABLE `admin_account` DISABLE KEYS */;
INSERT INTO `admin_account` VALUES (1,'anhnh','hoanganhkfe99@gmail.com','pbkdf2:sha256:150000$nJoJkV4e$4ba8cea6340a321845b2906ab22fde4442fe56202ad18fe3247181aa37b0683c','admin','2021-08-17 02:25:45','2021-08-17 02:25:45','anhnh','anhnh',NULL);
/*!40000 ALTER TABLE `admin_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int unsigned NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_flag` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_cart_user` (`user_id`),
  CONSTRAINT `fk_cart_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (1,1,'2021-09-29 09:35:04','2021-09-29 09:35:04',NULL);
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart_course`
--

DROP TABLE IF EXISTS `cart_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cart_course` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `cart_id` int unsigned NOT NULL,
  `course_id` int unsigned NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_flag` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_cart_course_cart` (`cart_id`),
  KEY `fk_cart_course_course` (`course_id`),
  CONSTRAINT `fk_cart_course_cart` FOREIGN KEY (`cart_id`) REFERENCES `cart` (`id`),
  CONSTRAINT `fk_cart_course_course` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart_course`
--

LOCK TABLES `cart_course` WRITE;
/*!40000 ALTER TABLE `cart_course` DISABLE KEYS */;
/*!40000 ALTER TABLE `cart_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `category` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `url_image` text,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `updated_by` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `deleted_flag` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Operating Systems','https://www.dropbox.com/s/i9bythpg4ieojs2/1632297294.png?raw=1','2021-09-09 04:15:58','2021-09-22 07:54:56','anhnh','anhnh',NULL),(8,'Programming Language','https://www.dropbox.com/s/by313rubwdhks65/1632297228.png?raw=1','2021-09-18 08:12:19','2021-09-22 07:53:51','anhnh','anhnh',NULL),(9,'sdfdsaf','https://www.dropbox.com/s/gds8635m0fxzie2/1634478452.png?raw=1','2021-10-17 13:47:34','2021-10-17 13:47:46','anhnh','anhnh',_binary '');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chapter`
--

DROP TABLE IF EXISTS `chapter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chapter` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `course_id` int unsigned NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `updated_by` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `deleted_flag` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_chapter_course` (`course_id`),
  CONSTRAINT `fk_chapter_course` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chapter`
--

LOCK TABLES `chapter` WRITE;
/*!40000 ALTER TABLE `chapter` DISABLE KEYS */;
/*!40000 ALTER TABLE `chapter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `description` text NOT NULL,
  `about` text NOT NULL,
  `url_image` text NOT NULL,
  `url_intro_video` text NOT NULL,
  `result` text NOT NULL,
  `views` int NOT NULL DEFAULT '0',
  `likes` int NOT NULL DEFAULT '0',
  `purchases` int NOT NULL DEFAULT '0',
  `interests_id` int unsigned NOT NULL,
  `category_id` int unsigned NOT NULL,
  `teacher_id` int unsigned NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `updated_by` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `deleted_flag` bit(1) DEFAULT NULL,
  `level` enum('beginner','intermediate','advance') NOT NULL DEFAULT 'beginner',
  `rating` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `fk_course_interests` (`interests_id`),
  KEY `fk_course_category` (`category_id`),
  KEY `fk_course_teacher` (`teacher_id`),
  CONSTRAINT `fk_course_category` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`),
  CONSTRAINT `fk_course_interests` FOREIGN KEY (`interests_id`) REFERENCES `interests` (`id`),
  CONSTRAINT `fk_course_teacher` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `discount_promotion`
--

DROP TABLE IF EXISTS `discount_promotion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `discount_promotion` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `course_id` int unsigned NOT NULL,
  `discount` int DEFAULT NULL,
  `begin_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `end_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `is_active` bit(1) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_flag` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_discount_promotion_course` (`course_id`),
  CONSTRAINT `fk_discount_promotion_course` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discount_promotion`
--

LOCK TABLES `discount_promotion` WRITE;
/*!40000 ALTER TABLE `discount_promotion` DISABLE KEYS */;
/*!40000 ALTER TABLE `discount_promotion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `interests`
--

DROP TABLE IF EXISTS `interests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `interests` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `description` text NOT NULL,
  `url_image` text,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `updated_by` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `deleted_flag` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interests`
--

LOCK TABLES `interests` WRITE;
/*!40000 ALTER TABLE `interests` DISABLE KEYS */;
INSERT INTO `interests` VALUES (39,'Technology','Increase tech skills with our teachers','https://www.dropbox.com/s/6mpzm9hmom3azyw/1632295070.png?raw=1','2021-09-18 08:10:05','2021-09-22 07:17:54','anhnh','anhnh',NULL),(40,'Business','Be an entrepreneur or learn about business','https://www.dropbox.com/s/7b409e02krgzt1r/1632294998.png?raw=1','2021-09-22 07:16:41','2021-09-22 07:16:41','anhnh','anhnh',NULL),(41,'Creative','Unleash your creativity with our programs','https://www.dropbox.com/s/5is648jptthxnbv/1632295044.png?raw=1','2021-09-22 07:17:27','2021-09-22 07:17:27','anhnh','anhnh',NULL),(42,'Self-growth','Improve yourself and be a better person','https://www.dropbox.com/s/inmfgzlrj0wamw1/1632295129.png?raw=1','2021-09-22 07:18:52','2021-09-22 07:18:52','anhnh','anhnh',NULL),(43,'Language','Master your language skill. Find your English online courses for','https://www.dropbox.com/s/ootgpiuc909k48s/1632295202.png?raw=1','2021-09-22 07:20:05','2021-09-22 07:20:05','anhnh','anhnh',NULL),(44,'ahihi','ahuhudsf',NULL,'2021-10-17 13:47:11','2021-10-17 13:47:21','anhnh','anhnh',_binary '');
/*!40000 ALTER TABLE `interests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `interests_category`
--

DROP TABLE IF EXISTS `interests_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `interests_category` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `interests_id` int unsigned NOT NULL,
  `category_id` int unsigned NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_flag` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_interests` (`interests_id`),
  KEY `fk_category` (`category_id`),
  CONSTRAINT `fk_category` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`),
  CONSTRAINT `fk_interests` FOREIGN KEY (`interests_id`) REFERENCES `interests` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `interests_category`
--

LOCK TABLES `interests_category` WRITE;
/*!40000 ALTER TABLE `interests_category` DISABLE KEYS */;
INSERT INTO `interests_category` VALUES (10,39,1,'2021-09-22 07:55:42','2021-09-22 07:55:42',NULL),(11,39,8,'2021-09-22 07:55:42','2021-09-22 07:55:42',NULL);
/*!40000 ALTER TABLE `interests_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `price`
--

DROP TABLE IF EXISTS `price`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `price` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `course_id` int unsigned NOT NULL,
  `price` decimal(10,0) NOT NULL,
  `is_active` bit(1) DEFAULT b'1',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_flag` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_price_course` (`course_id`),
  CONSTRAINT `fk_price_course` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `price`
--

LOCK TABLES `price` WRITE;
/*!40000 ALTER TABLE `price` DISABLE KEYS */;
/*!40000 ALTER TABLE `price` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `session`
--

DROP TABLE IF EXISTS `session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `session` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` text NOT NULL,
  `url_video` text NOT NULL,
  `time` int DEFAULT '0',
  `chapter_id` int unsigned NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `updated_by` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `deleted_flag` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_session_chapter` (`chapter_id`),
  CONSTRAINT `fk_session_chapter` FOREIGN KEY (`chapter_id`) REFERENCES `chapter` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session`
--

LOCK TABLES `session` WRITE;
/*!40000 ALTER TABLE `session` DISABLE KEYS */;
/*!40000 ALTER TABLE `session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teacher`
--

DROP TABLE IF EXISTS `teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teacher` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `full_name` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `date_of_birth` datetime DEFAULT NULL,
  `gender` enum('not_specific','male','female') NOT NULL DEFAULT 'not_specific',
  `phone_number` varchar(11) DEFAULT NULL,
  `about` text NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_flag` bit(1) DEFAULT NULL,
  `url_avatar` text NOT NULL,
  `email` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (1,'string','2021-09-21 00:00:00','not_specific','string','string','2021-09-21 09:48:17','2021-09-21 09:49:13',_binary '','string','string'),(2,'Topica Native','2021-09-21 00:00:00','male','012345678','<p>Topica Native là đơn vị cung cấp chương trình tiếng Anh giao tiếp với hơn 1,600 giảng viên Âu - Úc - Mỹ, được phát triển tại 3 quốc gia Đông Nam Á. Các khóa học trực tiếp và trực tuyến theo nhóm nhỏ của Topica Native kéo dài từ 8h-24h cho phép bạn học tiếng Anh ở mọi lúc, mọi nơi, mọi thiết bị. Website: https://topicanative.edu.vn/</p>','2021-09-21 09:56:18','2021-09-21 16:22:31',NULL,'https://www.dropbox.com/s/qstp5tfis1j9lln/1632241246.jpg?raw=1','test1@gmail.com'),(3,'Lưu Trường Hải Lân','2021-09-21 00:00:00','not_specific',NULL,'<p>Quản lý đào tạo tại ZendVN</p><p>Vị trí đã từng đảm nhiệm: Developer, Teamleader, Project manager, Training manager</p><p>Công việc hiện nay: Training manager &amp; Project manager tại ZendVN</p><p>Xây dựng kênh học lập trình miễn phí với hơn 5 triệu lượt xem trên Youtube</p><p>Các khóa học trực tuyến đã xây dựng: NodeJS, Laravel, Angular, ReactJS, Lập trình PHP, Zend Framework 2.x, jQuery Master, Bootstrap, HTML, CSS, Javascript, Python, ...</p>','2021-09-21 16:03:01','2021-09-21 16:03:01',NULL,'https://www.dropbox.com/s/5kfgnu8bp88y38x/1632240178.png?raw=1','test@gmail.com'),(4,'1','2021-09-21 00:00:00','not_specific','0384930792','<p>1</p>','2021-09-21 16:30:05','2021-09-21 16:31:37',_binary '','https://www.dropbox.com/s/amqj70675vmhx7t/1632241801.png?raw=1','hoanganhnguyenkfe99@mail.com'),(5,'Nguyễn Thành Long','1989-09-20 00:00:00','male','012369852','<p><i>Giảng viên Nguyễn Thành Long là người đã có hơn 10 năm kinh nghiệm quản lý, phân tích, lên kế hoạch &amp; triển khai nhiều chiến dịch, dự án về Digital tại các công ty tên tuổi như Admicro, Cốc Cốc, FPT, Anphabe...Bên cạnh đó, ông còn được đánh giá cao trong lĩnh vực giảng dạy và là diễn giả nổi tiếng chuyên về chủ đề Digital Marketing</i></p>','2021-10-25 16:45:09','2021-10-25 16:45:09',NULL,'https://www.dropbox.com/s/j3o8u4g03isqvtd/1635180306.jpg?raw=1','longnt@gmail.com');
/*!40000 ALTER TABLE `teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction`
--

DROP TABLE IF EXISTS `transaction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `code` varchar(36) DEFAULT (uuid()),
  `user_id` int unsigned NOT NULL,
  `first_name` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `phone_number` varchar(11) DEFAULT NULL,
  `voucher_id` int unsigned DEFAULT NULL,
  `discount` int DEFAULT '0',
  `total` decimal(10,0) NOT NULL,
  `payment_mode` enum('bank','paypal') NOT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` enum('initial','canceled','pending','success') DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_flag` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_transaction_user` (`user_id`),
  CONSTRAINT `fk_transaction_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
/*!40000 ALTER TABLE `transaction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaction_course`
--

DROP TABLE IF EXISTS `transaction_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaction_course` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `transaction_id` int unsigned NOT NULL,
  `course_id` int unsigned NOT NULL,
  `price_id` int unsigned NOT NULL,
  `original_price` decimal(10,0) NOT NULL,
  `discount_promotion_id` int unsigned DEFAULT NULL,
  `discount` int DEFAULT '0',
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_flag` bit(1) DEFAULT NULL,
  `course_name` text NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_transaction_course_transaction` (`transaction_id`),
  KEY `fk_transaction_course_course` (`course_id`),
  KEY `fk_transaction_course_price` (`price_id`),
  KEY `fk_transaction_course_discount_promotion` (`discount_promotion_id`),
  CONSTRAINT `fk_transaction_course_course` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`),
  CONSTRAINT `fk_transaction_course_discount_promotion` FOREIGN KEY (`discount_promotion_id`) REFERENCES `discount_promotion` (`id`),
  CONSTRAINT `fk_transaction_course_price` FOREIGN KEY (`price_id`) REFERENCES `price` (`id`),
  CONSTRAINT `fk_transaction_course_transaction` FOREIGN KEY (`transaction_id`) REFERENCES `transaction` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction_course`
--

LOCK TABLES `transaction_course` WRITE;
/*!40000 ALTER TABLE `transaction_course` DISABLE KEYS */;
/*!40000 ALTER TABLE `transaction_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `first_name` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `last_name` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `email` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `url_avatar` text NOT NULL,
  `date_of_birth` datetime DEFAULT NULL,
  `gender` enum('not_specific','male','female') NOT NULL DEFAULT 'not_specific',
  `phone_number` varchar(11) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_flag` bit(1) DEFAULT NULL,
  `hash_pwd` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Hoang Anh','Nguyen','anhnh@hybrid-technologies.vn','https://www.dropbox.com/s/w314azqx6byctwg/1633349305.png?raw=1','1999-04-01 00:00:00','male','0963058211','2021-09-25 07:34:32','2021-10-04 12:12:59',NULL,'pbkdf2:sha256:150000$nJoJkV4e$4ba8cea6340a321845b2906ab22fde4442fe56202ad18fe3247181aa37b0683c');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_like_course`
--

DROP TABLE IF EXISTS `user_like_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_like_course` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int unsigned NOT NULL,
  `course_id` int unsigned NOT NULL,
  `time` datetime DEFAULT CURRENT_TIMESTAMP,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_flag` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_user_like_course_course` (`course_id`),
  KEY `fk_user_like_course_user` (`user_id`),
  CONSTRAINT `fk_user_like_course_course` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`),
  CONSTRAINT `fk_user_like_course_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_like_course`
--

LOCK TABLES `user_like_course` WRITE;
/*!40000 ALTER TABLE `user_like_course` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_like_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_purchase_course`
--

DROP TABLE IF EXISTS `user_purchase_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_purchase_course` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int unsigned NOT NULL,
  `course_id` int unsigned NOT NULL,
  `transaction_id` int unsigned NOT NULL,
  `time` datetime DEFAULT CURRENT_TIMESTAMP,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_flag` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_user_purchase_course_user` (`user_id`),
  KEY `fk_user_purchase_course_course` (`course_id`),
  KEY `fk_user_purchase_course_transaction` (`transaction_id`),
  CONSTRAINT `fk_user_purchase_course_course` FOREIGN KEY (`course_id`) REFERENCES `course` (`id`),
  CONSTRAINT `fk_user_purchase_course_transaction` FOREIGN KEY (`transaction_id`) REFERENCES `transaction` (`id`),
  CONSTRAINT `fk_user_purchase_course_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_purchase_course`
--

LOCK TABLES `user_purchase_course` WRITE;
/*!40000 ALTER TABLE `user_purchase_course` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_purchase_course` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-10-26  0:07:42
