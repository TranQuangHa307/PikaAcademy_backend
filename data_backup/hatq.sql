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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (1,1,'2021-09-29 09:35:04','2021-09-29 09:35:04',NULL),(2,7,'2021-10-27 17:18:06','2021-10-27 17:18:06',NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chapter`
--

LOCK TABLES `chapter` WRITE;
/*!40000 ALTER TABLE `chapter` DISABLE KEYS */;
INSERT INTO `chapter` VALUES (14,'Há»�c Tiáº¿ng Anh Theo Chá»§ Ä�á»� - CÃ¡c LoÃ i Quáº£ (TrÃ¡i CÃ¢y)',14,'2021-10-28 03:24:08','2021-10-28 03:34:00','anhnh','anhnh',NULL),(15,'Há»�c Tiáº¿ng Anh Theo Chá»§ Ä�á»� - CÃ¡c LoÃ i Ä�á»™ng Váº­t',14,'2021-10-28 03:37:08','2021-10-28 03:37:08','anhnh','anhnh',NULL),(16,'Há»�c Tiáº¿ng Anh Theo Chá»§ Ä�á»� - Thá»�i Tiáº¿t',14,'2021-10-28 03:41:27','2021-10-28 03:42:39','anhnh','anhnh',NULL),(17,'GIá»šI THIá»†U KHÃ“A Há»ŒC',15,'2021-10-28 04:05:04','2021-10-28 04:05:04','anhnh','anhnh',NULL),(18,'Ná»˜I DUNG',15,'2021-10-28 04:06:18','2021-10-28 04:06:18','anhnh','anhnh',NULL),(19,'Káº¾T THÃšC KHÃ“A Há»ŒC',15,'2021-10-28 04:13:19','2021-10-28 04:13:19','anhnh','anhnh',NULL),(20,'GIá»šI THIá»†U KHÃ“A Há»ŒC',16,'2021-10-28 07:05:49','2021-10-28 07:05:49','anhnh','anhnh',NULL),(21,'Ná»˜I DUNG',16,'2021-10-28 07:06:26','2021-10-28 07:06:26','anhnh','anhnh',NULL),(22,'Káº¾T THÃšC KHÃ“A Há»ŒC',16,'2021-10-28 07:11:21','2021-10-28 07:11:21','anhnh','anhnh',NULL),(23,'Báº£n cháº¥t Marketing',17,'2021-10-28 07:35:00','2021-10-28 07:35:46','anhnh','anhnh',NULL),(24,'PhÃ¢n tÃ­ch mÃ´i trÆ°á»�ng Marketing',17,'2021-10-28 07:39:25','2021-10-28 07:39:25','anhnh','anhnh',NULL),(25,'Chiáº¿n lÆ°á»£c xÃºc tiáº¿n há»—n há»£p',17,'2021-10-28 07:48:58','2021-10-28 07:48:58','anhnh','anhnh',NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (14,'Há»�c Tiáº¿ng Anh Theo Chá»§ Ä�á»�','<p>Tá»± tin sá»­ dá»¥ng tiáº¿ng Anh theo cÃ¡c chá»§ Ä‘á»� trong cuá»™c sá»‘ng hÃ ng ngÃ y</p>','<p>KhoÃ¡ há»�c vá»›i ná»™i dung cÆ¡ báº£n, ngáº¯n gá»�n, dá»… hiá»ƒu, cáº§n thiáº¿t</p><ul><li>Há»�c viÃªn thÆ°á»�ng xuyÃªn Ä‘Æ°á»£c kiá»ƒm tra, Ä‘Ã¡nh giÃ¡ qua cÃ¡c bÃ i kiá»ƒm tra trong vÃ  sau má»—i bÃ i há»�c</li><li>Luyá»‡n cÃ¡c kÄ© nÄƒng quan trá»�ng trong giao tiáº¿p tiáº¿ng anh (nghe, nÃ³i, pháº£n xáº¡, ngá»¯ Ã¢m) trong 1 bÃ i há»�c</li><li>Náº¯m báº¯t Ä‘Æ°á»£c cÃ¡c tá»« vÃ  cÃ¡c cá»¥m tá»« thÆ°á»�ng sá»­ dá»¥ng theo cÃ¡c chá»§ Ä‘á»�</li><li>Tá»± tin, thoáº£i mÃ¡i trÃ² chuyá»‡n vÃ  chia sáº» cáº£m xÃºc vá»›i báº¡n bÃ¨, Ä‘á»“ng nghiá»‡p, Ä‘á»‘i tÃ¡c...</li></ul><p>Lá»™ trÃ¬nh há»�c táº­p:</p><p>21 bÃ i há»�c vá»� tá»« vá»±ng vÃ  cáº¥u trÃºc cÃ¢u xoay quanh chá»§ Ä‘á»� At the cinema</p>','https://www.dropbox.com/s/9g4qwjtpnaupron/1635391069.jfif?raw=1','https://www.dropbox.com/s/ud7wyxkfimehkrp/1635391074.mp4?raw=1','<ul><li>Chi phÃ­ ráº», tiáº¿t kiá»‡m thá»�i gian</li><li>Há»�c má»�i lÃºc má»�i nÆ¡i</li><li>CÃ¡c tÃ¬nh huá»‘ng cá»¥ thá»ƒ Ä‘Æ°á»£c minh há»�a sinh Ä‘á»™ng qua video há»�c liá»‡u full HD</li><li>Tá»± tin, thoáº£i mÃ¡i trÃ² chuyá»‡n vÃ  chia sáº» cáº£m xÃºc vá»›i báº¡n bÃ¨, Ä‘á»“ng nghiá»‡p, Ä‘á»‘i tÃ¡c...</li><li>Chá»§ Ä‘á»™ng thá»�i gian vÃ  khÃ´ng gian</li><li>KhoÃ¡ há»�c vá»›i 100% giáº£ng viÃªn ngÆ°á»�i báº£n ngá»¯, Ä‘áº¿n tá»« Topica Native</li></ul>',0,0,0,43,1,2,'2021-10-28 03:18:02','2021-10-28 03:33:38','anhnh','anhnh',NULL,'beginner',0),(15,'Láº­p trÃ¬nh PHP cÆ¡ báº£n','<p>KhoÃ¡ há»�c cung cáº¥p cho há»�c viÃªn Ä‘áº§y Ä‘á»§ cÃ¡c ká»¹ nÄƒng láº­p trÃ¬nh PHP cÄƒn báº£n thÃ´ng qua cÃ¡c vÃ­ dá»¥ Ä‘á»ƒ há»�c viÃªn cÃ³ thá»ƒ thá»±c hÃ nh theo vÃ  á»©ng dá»¥ng vÃ o thá»±c táº¿.</p>','<p>KhoÃ¡ há»�c cung cáº¥p cho há»�c viÃªn Ä‘áº§y Ä‘á»§ cÃ¡c ká»¹ nÄƒng láº­p trÃ¬nh PHP cÄƒn báº£n thÃ´ng qua cÃ¡c vÃ­ dá»¥ Ä‘á»ƒ há»�c viÃªn cÃ³ thá»ƒ thá»±c hÃ nh theo vÃ  á»©ng dá»¥ng vÃ o thá»±c táº¿. Ä�iá»ƒm khÃ¡c biá»‡t cá»§a khÃ³a há»�c lÃ  ná»™i dung Ä‘áº§y Ä‘á»§, thá»±c hÃ nh chi tiáº¿t, cung cáº¥p Ä‘á»§ thá»�i lÆ°á»£ng Ä‘á»ƒ báº¡n cÃ³ thá»ƒ hiá»ƒu Ä‘Æ°á»£c báº£n cháº¥t cá»§a viá»‡c láº­p trÃ¬nh PHP cÆ¡ báº£n.</p><p>Lá»™ trÃ¬nh há»�c táº­p:</p><p>KhÃ³a há»�c cÆ¡ báº£n gá»“m 2 pháº§n:&nbsp;</p><p>+ Pháº§n má»™t lÃ  lÃ½ thuyáº¿t cÆ¡ báº£n vá»� ngÃ´n ngá»¯ PHP&nbsp;</p><p>+ Pháº§n hai lÃ  há»�c thá»±c hÃ nh Ä‘á»ƒ hiá»ƒu báº£n cháº¥t, á»©ng dá»¥ng thá»±c táº¿</p>','https://www.dropbox.com/s/r6dwge20zrlhqev/1635393790.jfif?raw=1','https://www.dropbox.com/s/e5nvxy6eu1ilgoi/1635393793.webm?raw=1','<ul><li>KhoÃ¡ há»�c sáº½ giÃºp há»�c viÃªn: CÃ³ kiáº¿n thá»©c cÆ¡ báº£n vá»� ngÃ´n ngá»¯ láº­p trÃ¬nh PHP.</li><li>CÃ³ kháº£ nÄƒng giáº£i quyáº¿t nhá»¯ng bÃ i toÃ¡n cÄƒn báº£n.</li></ul>',0,1,0,39,8,3,'2021-10-28 04:03:17','2021-10-28 08:57:16','anhnh','anhnh',NULL,'beginner',0),(16,'JAVA CORE - Láº­p trÃ¬nh hÆ°á»›ng Ä‘á»‘i tÆ°á»£ng tá»« Zero','<p>JAVA lÃ  ngÃ´n ngá»¯ láº­p trÃ¬nh ráº¥t phá»• biáº¿n nháº¥t hiá»‡n nay, há»�c JAVA CORE báº¡n sáº½ cÃ³ ráº¥t nhiá»�u hÆ°á»›ng Ä‘i, tá»« láº­p trÃ¬nh Mobile app, Java web, Desktop App, Game,... vÃ  táº¥t cáº£ Ä‘á»�u sá»­ dá»¥ng ná»�n táº£ng cá»§a JAVA CORE.</p>','<p>JAVA lÃ  ngÃ´n ngá»¯ láº­p trÃ¬nh ráº¥t phá»• biáº¿n nháº¥t hiá»‡n nay, há»�c JAVA CORE báº¡n sáº½ cÃ³ ráº¥t nhiá»�u hÆ°á»›ng Ä‘i, tá»« láº­p trÃ¬nh Mobile app, Java web, Desktop App, Game,... vÃ  táº¥t cáº£ Ä‘á»�u sá»­ dá»¥ng ná»�n táº£ng cá»§a JAVA CORE.</p><p>Káº¿t thÃºc khÃ³a há»�c báº¡n sáº½ :</p><p>1. Náº¯m Ä‘Æ°á»£c cÃ¡c khÃ¡i niá»‡m láº­p trÃ¬nh Java cÆ¡ báº£n.</p><p>2. Náº¯m Ä‘Æ°á»£c cÃ¡c kiáº¿n thá»©c vá»� láº­p trÃ¬nh hÆ°á»›ng Ä‘á»‘i tÆ°á»£ng Java (OOP).</p><p>3. Tá»« kiáº¿n thá»©c cÆ¡ báº£n JAVA core báº¡n cÃ³ thá»ƒ tá»± há»�c cÃ¡c ngÃ´n ngá»¯ láº­p trÃ¬nh hÆ°á»›ng Ä‘á»‘i tÆ°á»£ng khÃ¡c nhÆ° C++/C#,Python,...</p>','https://www.dropbox.com/s/ixvvhmht2rf5ewa/1635395918.jfif?raw=1','https://www.dropbox.com/s/8603enpr8wp63uf/1635395921.mp4?raw=1','<ul><li>1. Náº¯m Ä‘Æ°á»£c kiáº¿n thá»©c java cÆ¡ báº£n cÅ©ng nhÆ° kiáº¿n thá»©c vá»� láº­p trÃ¬nh hÆ°á»›ng Ä‘á»‘i tÆ°á»£ng.</li><li>2. CÃ³ thá»ƒ viáº¿t Ä‘Æ°á»£c cÃ¡c chÆ°Æ¡ng trÃ¬nh java cÆ¡ báº£n nhÆ° cÃ¡c á»©ng dá»¥ng Console App, Desktop App.</li><li>3. LÃ m ná»�n táº£ng Ä‘á»ƒ há»�c tiáº¿p cÃ¡c khÃ³a há»�c nÃ¢ng cao vá»� java (Java advance, Java web, Android...).</li><li>4. CÃ³ thá»ƒ xin lÃ m java fresher hoáº·c thá»±c táº­p táº¡i cÃ¡c cÃ´ng ty pháº§n má»�m.</li></ul>',0,0,0,39,8,3,'2021-10-28 04:38:45','2021-10-28 04:38:45','anhnh','anhnh',NULL,'intermediate',0),(17,'Marketing cho ngÆ°á»�i báº¯t Ä‘áº§u','<p>Náº¿u báº¡n lÃ  má»™t chá»§ doanh nghiá»‡p, quÃ¡n Äƒn, cá»­a hiá»‡u, bÃ¡n hÃ ng online..., dÃ¹ báº¡n lÃ m gÃ¬ thÃ¬ cÅ©ng pháº£i bÃ¡n hÃ ng, vÃ  tÃ¬m kiáº¿m khÃ¡ch hÃ ng Ä‘á»ƒ gia tÄƒng lá»£i nhuáº­n!</p><p>Váº­y lÃ m tháº¿ nÃ o Ä‘á»ƒ tÃ¬m khÃ¡ch vÃ  vÃ  xÃ¢y dá»±ng thÆ°Æ¡ng hiá»‡u trÃªn Internet?</p><p>Báº¡n cÃ³ thá»ƒ tháº¥y ngÆ°á»�i khÃ¡c quáº£ng cÃ¡o, SEO website... nhÆ°ng Ä‘Ã³ lÃ  phÆ°Æ¡ng phÃ¡p ráº¥t cÅ©, cáº¡nh tranh cao, tá»‘n kÃ©m chi phÃ­, hiá»‡u quáº£ Ä‘i xuá»‘ng theo thá»�i gian, phá»©c táº¡p náº¿u báº¡n khÃ´ng am hiá»ƒu vá»� nÃ³ vÃ  cÃ³ thá»ƒ máº¥t ráº¥t nhiá»�u tiá»�n!</p><p>Váº­y bÃ¢y giá»� báº¡n pháº£i lÃ m gÃ¬ Ä‘á»ƒ phÃ¡t triá»ƒn Ä‘Æ°á»£c trÃªn Internet Ä‘á»ƒ tÃ¬m khÃ¡ch hÃ ng!</p><p>Video Marketing cÃ³ thá»ƒ giÃºp báº¡n, tá»± Ä‘á»™ng, hiá»‡u quáº£ vÃ  ngÃ y cÃ ng phÃ¡t triá»ƒn, cáº¡nh tranh cá»±c tháº¥p, chi phÃ­ gáº§n nhÆ° = 0</p>','<p>Náº¿u báº¡n lÃ  má»™t chá»§ doanh nghiá»‡p, quÃ¡n Äƒn, cá»­a hiá»‡u, bÃ¡n hÃ ng online..., dÃ¹ báº¡n lÃ m gÃ¬ thÃ¬ cÅ©ng pháº£i bÃ¡n hÃ ng, vÃ  tÃ¬m kiáº¿m khÃ¡ch hÃ ng Ä‘á»ƒ gia tÄƒng lá»£i nhuáº­n!</p><p>Váº­y lÃ m tháº¿ nÃ o Ä‘á»ƒ tÃ¬m khÃ¡ch vÃ  vÃ  xÃ¢y dá»±ng thÆ°Æ¡ng hiá»‡u trÃªn Internet?</p><p>Báº¡n cÃ³ thá»ƒ tháº¥y ngÆ°á»�i khÃ¡c quáº£ng cÃ¡o, SEO website... nhÆ°ng Ä‘Ã³ lÃ  phÆ°Æ¡ng phÃ¡p ráº¥t cÅ©, cáº¡nh tranh cao, tá»‘n kÃ©m chi phÃ­, hiá»‡u quáº£ Ä‘i xuá»‘ng theo thá»�i gian, phá»©c táº¡p náº¿u báº¡n khÃ´ng am hiá»ƒu vá»� nÃ³ vÃ  cÃ³ thá»ƒ máº¥t ráº¥t nhiá»�u tiá»�n!</p><p>Váº­y bÃ¢y giá»� báº¡n pháº£i lÃ m gÃ¬ Ä‘á»ƒ phÃ¡t triá»ƒn Ä‘Æ°á»£c trÃªn Internet Ä‘á»ƒ tÃ¬m khÃ¡ch hÃ ng!</p><p>Video Marketing cÃ³ thá»ƒ giÃºp báº¡n, tá»± Ä‘á»™ng, hiá»‡u quáº£ vÃ  ngÃ y cÃ ng phÃ¡t triá»ƒn, cáº¡nh tranh cá»±c tháº¥p, chi phÃ­ gáº§n nhÆ° = 0</p><p>Váº­y lÃ m tháº¿ nÃ o Ä‘á»ƒ Ã¡p dá»¥ng video marketing cho viá»‡c kinh doanh cá»§a báº¡n!</p><p>BÆ°á»›c 1: XÃ¡c Ä‘á»‹nh chá»§ Ä‘á»� vÃ  Ã½ tÆ°á»Ÿng,</p><p>BÆ°á»›c 2: Quay video,</p><p>BÆ°á»›c 3: Chá»‰nh sá»¯a video,</p><p>BÆ°á»›c 4: Táº£i lÃªn máº¡ng vÃ  tá»‘i Æ°u</p><p>Náº¿u báº¡n khÃ´ng rÃ nh cÃ´ng nghá»‡, muá»‘n tiáº¿t kiá»‡m thá»�i gian vÃ  tiá»�n báº¡c thÃ¬ hÃ£y tham kháº£o khÃ³a há»�c Ä‘á»ƒ lÃ m chá»§ Ä‘Æ°á»£c VIDEO MARKETING</p>','https://www.dropbox.com/s/cu6cbvgr8d5nfrs/1635406479.jfif?raw=1','https://www.dropbox.com/s/gku6x4notjs5sw5/1635406482.mp4?raw=1','<ul><li>Sau khi há»�c xong báº¡n sáº½:</li><li>Táº¡o cho mÃ¬nh hÃ ng trÄƒm video giÃ¡ trá»‹ cho khÃ¡ch hÃ ng</li><li>Báº¡n sáº½ khÃ´ng bao giá»� sá»£ quay video thÃªm má»™t láº§n nÃ o ná»¯a</li><li>Báº¡n sáº½ sÃ¡ng táº¡o ra nhá»¯ng Ã½ tÆ°á»Ÿng quay video</li><li>Báº¡n sáº½ náº¯m vá»¯ng ká»¹ nÄƒng body language trong video</li><li>Báº¡n sáº½ sá»Ÿ há»¯u ká»· nÄƒng thuyáº¿t trÃ¬nh chuyÃªn nghiá»‡p</li></ul>',0,0,0,40,1,5,'2021-10-28 07:34:47','2021-10-28 07:34:47','anhnh','anhnh',NULL,'advance',0);
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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `discount_promotion`
--

LOCK TABLES `discount_promotion` WRITE;
/*!40000 ALTER TABLE `discount_promotion` DISABLE KEYS */;
INSERT INTO `discount_promotion` VALUES (7,16,20,'2021-10-28 09:00:00','2022-01-01 19:00:00',_binary '\0','2021-10-28 04:38:46','2021-10-28 05:16:13',NULL),(8,16,20,'2021-10-28 07:00:00','2022-01-31 22:00:00',_binary '\0','2021-10-28 05:16:13','2021-10-28 05:19:11',NULL),(9,16,20,'2021-10-28 06:00:00','2022-02-01 09:00:00',_binary '\0','2021-10-28 05:19:12','2021-10-28 05:24:00',NULL),(10,16,20,'2021-10-28 16:00:00','2022-02-03 05:00:00',_binary '\0','2021-10-28 05:24:00','2021-10-28 05:32:24',NULL),(11,16,20,'2021-10-27 23:00:00','2022-02-03 10:00:00',_binary '\0','2021-10-28 05:32:25','2021-10-28 06:01:42',NULL),(12,16,20,'2021-10-28 02:00:00','2021-11-01 10:00:00',_binary '','2021-10-28 06:03:01','2021-10-28 06:03:01',NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `price`
--

LOCK TABLES `price` WRITE;
/*!40000 ALTER TABLE `price` DISABLE KEYS */;
INSERT INTO `price` VALUES (17,14,700000,_binary '','2021-10-28 03:18:03','2021-10-28 03:18:03',NULL),(18,15,0,_binary '','2021-10-28 04:03:17','2021-10-28 04:03:17',NULL),(19,16,900000,_binary '','2021-10-28 04:38:46','2021-10-28 04:38:46',NULL),(20,17,500000,_binary '','2021-10-28 07:34:48','2021-10-28 07:34:48',NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `session`
--

LOCK TABLES `session` WRITE;
/*!40000 ALTER TABLE `session` DISABLE KEYS */;
INSERT INTO `session` VALUES (13,'CÃ¡c LoÃ i Quáº£ (TrÃ¡i CÃ¢y)','https://www.dropbox.com/s/si1f7aj9fct50e1/1635392084.mp4?raw=1',428,14,'2021-10-28 03:26:25','2021-10-28 03:34:49','anhnh','anhnh',NULL),(14,'Há»�c Tiáº¿ng Anh Theo Chá»§ Ä�á»� - CÃ¡c LoÃ i Ä�á»™ng Váº­t - Pháº§n 1','https://www.dropbox.com/s/b7pygizhkv3x3ij/1635392245.webm?raw=1',301,15,'2021-10-28 03:37:33','2021-10-28 03:37:33','anhnh','anhnh',NULL),(15,'Há»�c Tiáº¿ng Anh Theo Chá»§ Ä�á»� - CÃ¡c LoÃ i Ä�á»™ng Váº­t - Pháº§n 2','https://www.dropbox.com/s/nwl9iuji8ebxlz7/1635392371.webm?raw=1',173,15,'2021-10-28 03:39:36','2021-10-28 03:39:36','anhnh','anhnh',NULL),(16,'Há»�c Tiáº¿ng Anh Theo Chá»§ Ä�á»� - CÃ¡c LoÃ i Ä�á»™ng Váº­t - Pháº§n 3','https://www.dropbox.com/s/ukk328299n0c3hv/1635392457.webm?raw=1',190,15,'2021-10-28 03:41:02','2021-10-28 03:41:02','anhnh','anhnh',NULL),(17,'Há»�c Tiáº¿ng Anh Theo Chá»§ Ä�á»� - Thá»�i Tiáº¿t - Pháº§n 1','https://www.dropbox.com/s/y66tvqlgsbp7n42/1635392586.webm?raw=1',182,16,'2021-10-28 03:43:10','2021-10-28 03:43:10','anhnh','anhnh',NULL),(18,'Há»�c Tiáº¿ng Anh Theo Chá»§ Ä�á»� - Thá»�i Tiáº¿t - Pháº§n 2','https://www.dropbox.com/s/b3e2696wb4tpw3o/1635392616.webm?raw=1',174,16,'2021-10-28 03:43:43','2021-10-28 03:43:43','anhnh','anhnh',NULL),(19,'CÃ i Ä‘áº·t PHP trÃªn Window','https://www.dropbox.com/s/luud57n0o9xlrm0/1635393940.webm?raw=1',339,17,'2021-10-28 04:05:45','2021-10-28 04:05:45','anhnh','anhnh',NULL),(20,'Syntax trong PHP','https://www.dropbox.com/s/f2zge780lm5klru/1635393999.webm?raw=1',474,18,'2021-10-28 04:06:43','2021-10-28 04:06:43','anhnh','anhnh',NULL),(21,'Biáº¿n trong PHP','https://www.dropbox.com/s/h67iivdgzavqrfe/1635394055.webm?raw=1',553,18,'2021-10-28 04:07:42','2021-10-28 04:07:42','anhnh','anhnh',NULL),(22,'ToÃ¡n tá»­ trong PHP','https://www.dropbox.com/s/q6sfnbw9ky8gi2o/1635394105.webm?raw=1',227,18,'2021-10-28 04:08:30','2021-10-28 04:08:30','anhnh','anhnh',NULL),(23,'Chuá»—i trong PHP','https://www.dropbox.com/s/jxyno7e2ryn2qsu/1635394152.webm?raw=1',158,18,'2021-10-28 04:09:16','2021-10-28 04:09:16','anhnh','anhnh',NULL),(24,'Máº£ng trong PHP','https://www.dropbox.com/s/29wh730w0vlr2io/1635394232.webm?raw=1',597,18,'2021-10-28 04:10:36','2021-10-28 04:10:36','anhnh','anhnh',NULL),(25,'CÃ¢u Ä‘iá»�u kiá»‡n trong PHP IF Else','https://www.dropbox.com/s/u1tcpryd54wgkfi/1635394266.webm?raw=1',265,18,'2021-10-28 04:11:11','2021-10-28 04:11:11','anhnh','anhnh',NULL),(26,'HÃ m trong PHP','https://www.dropbox.com/s/90o5hk9scgoauu7/1635394318.webm?raw=1',639,18,'2021-10-28 04:12:03','2021-10-28 04:12:03','anhnh','anhnh',NULL),(27,'VÃ²ng láº·p trong PHP','https://www.dropbox.com/s/fe7vanczutvljwc/1635394354.webm?raw=1',390,18,'2021-10-28 04:12:40','2021-10-28 04:12:40','anhnh','anhnh',NULL),(28,'Tá»•ng káº¿t','https://www.dropbox.com/s/my34xw005w5kumu/1635394506.webm?raw=1',462,19,'2021-10-28 04:15:12','2021-10-28 04:15:12','anhnh','anhnh',NULL),(29,'Pháº§n má»�m há»�c Java','https://www.dropbox.com/s/pp43ykic7qjgofz/1635404773.mp4?raw=1',524,20,'2021-10-28 07:06:18','2021-10-28 07:06:18','anhnh','anhnh',NULL),(30,'ChÆ°Æ¡ng trÃ¬nh Java Ä‘áº§u tiÃªn','https://www.dropbox.com/s/tvfdoxqotzxzfyb/1635404808.mp4?raw=1',369,21,'2021-10-28 07:06:52','2021-10-28 07:06:52','anhnh','anhnh',NULL),(31,'BiÃªn dá»‹ch táº­p tin java','https://www.dropbox.com/s/1ypht7h7x8rdkoy/1635404847.mp4?raw=1',489,21,'2021-10-28 07:07:32','2021-10-28 07:07:32','anhnh','anhnh',NULL),(32,'Biáº¿n trong Java','https://www.dropbox.com/s/kxfeuoqv6fgmokf/1635404927.mp4?raw=1',148,21,'2021-10-28 07:08:51','2021-10-28 07:08:51','anhnh','anhnh',NULL),(33,'TÃ¬m hiá»ƒu Package','https://www.dropbox.com/s/3odw0h63ygnafa1/1635404979.mp4?raw=1',303,21,'2021-10-28 07:09:44','2021-10-28 07:09:44','anhnh','anhnh',NULL),(34,'Khai bÃ¡o biáº¿n trong Java 01','https://www.dropbox.com/s/nqwkez6i1w4qgad/1635405009.mp4?raw=1',474,21,'2021-10-28 07:10:14','2021-10-28 07:10:14','anhnh','anhnh',NULL),(35,'Khai bÃ¡o biáº¿n trong Java 02','https://www.dropbox.com/s/zv9y0graog9pih6/1635405048.mp4?raw=1',486,21,'2021-10-28 07:10:54','2021-10-28 07:10:54','anhnh','anhnh',NULL),(36,'Xem ThÃªm Videos vá»� Láº­p trÃ¬nh Java cÆ¡ báº£n','https://www.dropbox.com/s/5err8jhzj128cqh/1635405093.webm?raw=1',54,22,'2021-10-28 07:11:37','2021-10-28 07:11:37','anhnh','anhnh',NULL),(37,'Báº£n cháº¥t Marketing','https://www.dropbox.com/s/9xyvrtxmvx4wgl5/1635406583.mp4?raw=1',568,23,'2021-10-28 07:36:30','2021-10-28 07:38:39','anhnh','anhnh',NULL),(38,'PhÃ¢n tÃ­ch mÃ´i trÆ°á»�ng Marketing (Pháº§n 1)','https://www.dropbox.com/s/n00yihs7pbv1sd0/1635406813.mp4?raw=1',592,24,'2021-10-28 07:40:23','2021-10-28 07:40:23','anhnh','anhnh',NULL),(39,'PhÃ¢n tÃ­ch mÃ´i trÆ°á»�ng Marketing (Pháº§n 2)','https://www.dropbox.com/s/gneaekjri87fhoc/1635407142.mp4?raw=1',438,24,'2021-10-28 07:45:50','2021-10-28 07:45:50','anhnh','anhnh',NULL),(40,'Chiáº¿n lÆ°á»£c xÃºc tiáº¿n há»—n há»£p (Pháº§n 1)','https://www.dropbox.com/s/qk2rmf2ww6lhf9z/1635407353.mp4?raw=1',586,25,'2021-10-28 07:49:18','2021-10-28 07:50:16','anhnh','anhnh',NULL),(41,'Chiáº¿n lÆ°á»£c xÃºc tiáº¿n há»—n há»£p (Pháº§n 2)','https://www.dropbox.com/s/l7j6acq1os7wf0h/1635407385.mp4?raw=1',597,25,'2021-10-28 07:50:06','2021-10-28 07:50:06','anhnh','anhnh',NULL);
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
INSERT INTO `teacher` VALUES (1,'string','2021-09-21 00:00:00','not_specific','string','string','2021-09-21 09:48:17','2021-09-21 09:49:13',_binary '','string','string'),(2,'Topica Native','1975-03-05 00:00:00','male','012345678','<p>Topica Native lÃ  Ä‘Æ¡n vá»‹ cung cáº¥p chÆ°Æ¡ng trÃ¬nh tiáº¿ng Anh giao tiáº¿p vá»›i hÆ¡n 1,600 giáº£ng viÃªn Ã‚u - Ãšc - Má»¹, Ä‘Æ°á»£c phÃ¡t triá»ƒn táº¡i 3 quá»‘c gia Ä�Ã´ng Nam Ã�. CÃ¡c khÃ³a há»�c trá»±c tiáº¿p vÃ  trá»±c tuyáº¿n theo nhÃ³m nhá»� cá»§a Topica Native kÃ©o dÃ i tá»« 8h-24h cho phÃ©p báº¡n há»�c tiáº¿ng Anh á»Ÿ má»�i lÃºc, má»�i nÆ¡i, má»�i thiáº¿t bá»‹. Website: https://topicanative.edu.vn/</p>','2021-09-21 09:56:18','2021-10-28 03:51:26',NULL,'https://www.dropbox.com/s/vg8f7h4grg3t76c/1635393084.png?raw=1','test1@gmail.com'),(3,'LÆ°u TrÆ°á»�ng Háº£i LÃ¢n','1975-03-05 00:00:00','not_specific','0123456789','<p>Quáº£n lÃ½ Ä‘Ã o táº¡o táº¡i ZendVN</p><p>Vá»‹ trÃ­ Ä‘Ã£ tá»«ng Ä‘áº£m nhiá»‡m: Developer, Teamleader, Project manager, Training manager</p><p>CÃ´ng viá»‡c hiá»‡n nay: Training manager &amp; Project manager táº¡i ZendVN</p><p>XÃ¢y dá»±ng kÃªnh há»�c láº­p trÃ¬nh miá»…n phÃ­ vá»›i hÆ¡n 5 triá»‡u lÆ°á»£t xem trÃªn Youtube</p><p>CÃ¡c khÃ³a há»�c trá»±c tuyáº¿n Ä‘Ã£ xÃ¢y dá»±ng: NodeJS, Laravel, Angular, ReactJS, Láº­p trÃ¬nh PHP, Zend Framework 2.x, jQuery Master, Bootstrap, HTML, CSS, Javascript, Python, ...</p>','2021-09-21 16:03:01','2021-10-28 03:51:07',NULL,'https://www.dropbox.com/s/shsjhc70jpq7ww2/1635393065.jpg?raw=1','test@gmail.com'),(4,'1','2021-09-21 00:00:00','not_specific','0384930792','<p>1</p>','2021-09-21 16:30:05','2021-09-21 16:31:37',_binary '','https://www.dropbox.com/s/amqj70675vmhx7t/1632241801.png?raw=1','hoanganhnguyenkfe99@mail.com'),(5,'Nguyá»…n ThÃ nh Long','1971-12-22 00:00:00','male','012369852','<p><i>Giáº£ng viÃªn Nguyá»…n ThÃ nh Long lÃ  ngÆ°á»�i Ä‘Ã£ cÃ³ hÆ¡n 10 nÄƒm kinh nghiá»‡m quáº£n lÃ½, phÃ¢n tÃ­ch, lÃªn káº¿ hoáº¡ch &amp; triá»ƒn khai nhiá»�u chiáº¿n dá»‹ch, dá»± Ã¡n vá»� Digital táº¡i cÃ¡c cÃ´ng ty tÃªn tuá»•i nhÆ° Admicro, Cá»‘c Cá»‘c, FPT, Anphabe...BÃªn cáº¡nh Ä‘Ã³, Ã´ng cÃ²n Ä‘Æ°á»£c Ä‘Ã¡nh giÃ¡ cao trong lÄ©nh vá»±c giáº£ng dáº¡y vÃ  lÃ  diá»…n giáº£ ná»•i tiáº¿ng chuyÃªn vá»� chá»§ Ä‘á»� Digital Marketing</i></p>','2021-10-25 16:45:09','2021-10-28 03:50:28',NULL,'https://www.dropbox.com/s/2zo7jyqf60scwwv/1635393026.jpg?raw=1','longnt@gmail.com');
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
  `payment_mode` enum('bank','paypal') DEFAULT NULL,
  `time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` enum('initial','canceled','pending','success') DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_flag` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_transaction_user` (`user_id`),
  CONSTRAINT `fk_transaction_user` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction`
--

LOCK TABLES `transaction` WRITE;
/*!40000 ALTER TABLE `transaction` DISABLE KEYS */;
INSERT INTO `transaction` VALUES (19,'54a82980-37ce-11ec-ac3c-0242ac130003',7,'Nguyen','Hoang Anh','hoanganhkfe99@gmail.com','0963058211',NULL,0,0,NULL,'2021-10-28 09:06:26','success','2021-10-28 09:06:26','2021-10-28 09:06:26',NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaction_course`
--

LOCK TABLES `transaction_course` WRITE;
/*!40000 ALTER TABLE `transaction_course` DISABLE KEYS */;
INSERT INTO `transaction_course` VALUES (28,19,15,18,0,NULL,0,'2021-10-28 09:06:26','2021-10-28 09:06:26',NULL,'Láº­p trÃ¬nh PHP cÆ¡ báº£n');
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Hoang Anh','Nguyen','anhnh@hybrid-technologies.vn','https://www.dropbox.com/s/tc4098l368iud8c/1635393399.jpg?raw=1','1970-04-18 00:00:00','male','0963058211','2021-09-25 07:34:32','2021-10-28 03:56:41',NULL,'pbkdf2:sha256:150000$nJoJkV4e$4ba8cea6340a321845b2906ab22fde4442fe56202ad18fe3247181aa37b0683c'),(7,'Nguyen','Hoang Anh','hoanganhkfe99@gmail.com','https://www.dropbox.com/s/ljftdc3rnkrp90c/1635393435.jpg?raw=1','1975-03-06 00:00:00','male','0963058211','2021-10-27 17:18:06','2021-10-28 03:57:18',NULL,'pbkdf2:sha256:150000$rpULkpOq$11ff79342932d3f07306b4342890e28c8bada5bb24b401624c1c00d222ac384e');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_like_course`
--

LOCK TABLES `user_like_course` WRITE;
/*!40000 ALTER TABLE `user_like_course` DISABLE KEYS */;
INSERT INTO `user_like_course` VALUES (3,7,15,'2021-10-28 08:57:15','2021-10-28 08:57:15','2021-10-28 08:57:15',NULL);
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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_purchase_course`
--

LOCK TABLES `user_purchase_course` WRITE;
/*!40000 ALTER TABLE `user_purchase_course` DISABLE KEYS */;
INSERT INTO `user_purchase_course` VALUES (19,7,15,19,'2021-10-28 09:06:26','2021-10-28 09:06:26','2021-10-28 09:06:26',NULL);
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

-- Dump completed on 2021-10-29  0:06:58
