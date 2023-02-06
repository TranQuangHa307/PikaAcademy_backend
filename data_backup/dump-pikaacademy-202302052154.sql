-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: pikaacademy
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
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
  `user_name` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `email` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `password` longtext CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `role` enum('admin','member') NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `updated_by` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
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
  `created_by` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `updated_by` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `deleted_flag` bit(1) DEFAULT NULL,
  `interests_id` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_interest` (`interests_id`),
  CONSTRAINT `category_ibfk_1` FOREIGN KEY (`interests_id`) REFERENCES `interests` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (1,'Operating Systems','https://www.dropbox.com/s/i9bythpg4ieojs2/1632297294.png?raw=1','2021-09-09 04:15:58','2021-09-22 07:54:56','anhnh','anhnh',NULL,NULL),(8,'Programming Language','https://www.dropbox.com/s/by313rubwdhks65/1632297228.png?raw=1','2021-09-18 08:12:19','2021-09-22 07:53:51','anhnh','anhnh',NULL,NULL),(9,'sdfdsaf','https://www.dropbox.com/s/gds8635m0fxzie2/1634478452.png?raw=1','2021-10-17 13:47:34','2021-10-17 13:47:46','anhnh','anhnh',_binary '',NULL);
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
  `created_by` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `updated_by` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
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
INSERT INTO `chapter` VALUES (14,'Học Tiếng Anh Theo Chủ Đề - Các Loài Quả (Trái Cây)',14,'2021-10-28 03:24:08','2021-10-28 03:34:00','anhnh','anhnh',NULL),(15,'Học Tiếng Anh Theo Chủ Đề - Các Loài Động Vật',14,'2021-10-28 03:37:08','2021-10-28 03:37:08','anhnh','anhnh',NULL),(16,'Học Tiếng Anh Theo Chủ Đề - Thời Tiết',14,'2021-10-28 03:41:27','2021-10-28 03:42:39','anhnh','anhnh',NULL),(17,'GIỚI THIỆU KHÓA HỌC',15,'2021-10-28 04:05:04','2021-10-28 04:05:04','anhnh','anhnh',NULL),(18,'NỘI DUNG',15,'2021-10-28 04:06:18','2021-10-28 04:06:18','anhnh','anhnh',NULL),(19,'KẾT THÚC KHÓA HỌC',15,'2021-10-28 04:13:19','2021-10-28 04:13:19','anhnh','anhnh',NULL),(20,'GIỚI THIỆU KHÓA HỌC',16,'2021-10-28 07:05:49','2021-10-28 07:05:49','anhnh','anhnh',NULL),(21,'NỘI DUNG',16,'2021-10-28 07:06:26','2021-10-28 07:06:26','anhnh','anhnh',NULL),(22,'KẾT THÚC KHÓA HỌC',16,'2021-10-28 07:11:21','2021-10-28 07:11:21','anhnh','anhnh',NULL),(23,'Bản chất Marketing',17,'2021-10-28 07:35:00','2021-10-28 07:35:46','anhnh','anhnh',NULL),(24,'Phân tích môi trường Marketing',17,'2021-10-28 07:39:25','2021-10-28 07:39:25','anhnh','anhnh',NULL),(25,'Chiến lược xúc tiến hỗn hợp',17,'2021-10-28 07:48:58','2021-10-28 07:48:58','anhnh','anhnh',NULL);
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
  `created_by` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `updated_by` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `deleted_flag` bit(1) DEFAULT NULL,
  `level` enum('beginner','intermediate','advance') NOT NULL DEFAULT 'beginner',
  `rating` int NOT NULL DEFAULT '0',
  `is_active` bit(1) DEFAULT NULL,
  `release` bit(1) DEFAULT NULL,
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
INSERT INTO `course` VALUES (14,'Học Tiếng Anh Theo Chủ Đề','<p>Tự tin sử dụng tiếng Anh theo các chủ đề trong cuộc sống hàng ngày</p>','<p>Khoá học với nội dung cơ bản, ngắn gọn, dễ hiểu, cần thiết</p><ul><li>Học viên thường xuyên được kiểm tra, đánh giá qua các bài kiểm tra trong và sau mỗi bài học</li><li>Luyện các kĩ năng quan trọng trong giao tiếp tiếng anh (nghe, nói, phản xạ, ngữ âm) trong 1 bài học</li><li>Nắm bắt được các từ và các cụm từ thường sử dụng theo các chủ đề</li><li>Tự tin, thoải mái trò chuyện và chia sẻ cảm xúc với bạn bè, đồng nghiệp, đối tác...</li></ul><p>Lộ trình học tập:</p><p>21 bài học về từ vựng và cấu trúc câu xoay quanh chủ đề At the cinema</p>','https://www.dropbox.com/s/9g4qwjtpnaupron/1635391069.jfif?raw=1','https://www.dropbox.com/s/ud7wyxkfimehkrp/1635391074.mp4?raw=1','<ul><li>Chi phí rẻ, tiết kiệm thời gian</li><li>Học mọi lúc mọi nơi</li><li>Các tình huống cụ thể được minh họa sinh động qua video học liệu full HD</li><li>Tự tin, thoải mái trò chuyện và chia sẻ cảm xúc với bạn bè, đồng nghiệp, đối tác...</li><li>Chủ động thời gian và không gian</li><li>Khoá học với 100% giảng viên người bản ngữ, đến từ Topica Native</li></ul>',0,0,0,43,1,2,'2021-10-28 03:18:02','2021-10-28 03:33:38','anhnh','anhnh',NULL,'beginner',0,NULL,NULL),(15,'Lập trình PHP cơ bản','<p>Khoá học cung cấp cho học viên đầy đủ các kỹ năng lập trình PHP căn bản thông qua các ví dụ để học viên có thể thực hành theo và ứng dụng vào thực tế.</p>','<p>Khoá học cung cấp cho học viên đầy đủ các kỹ năng lập trình PHP căn bản thông qua các ví dụ để học viên có thể thực hành theo và ứng dụng vào thực tế. Điểm khác biệt của khóa học là nội dung đầy đủ, thực hành chi tiết, cung cấp đủ thời lượng để bạn có thể hiểu được bản chất của việc lập trình PHP cơ bản.</p><p>Lộ trình học tập:</p><p>Khóa học cơ bản gồm 2 phần:&nbsp;</p><p>+ Phần một là lý thuyết cơ bản về ngôn ngữ PHP&nbsp;</p><p>+ Phần hai là học thực hành để hiểu bản chất, ứng dụng thực tế</p>','https://www.dropbox.com/s/r6dwge20zrlhqev/1635393790.jfif?raw=1','https://www.dropbox.com/s/e5nvxy6eu1ilgoi/1635393793.webm?raw=1','<ul><li>Khoá học sẽ giúp học viên: Có kiến thức cơ bản về ngôn ngữ lập trình PHP.</li><li>Có khả năng giải quyết những bài toán căn bản.</li></ul>',0,1,0,39,8,3,'2021-10-28 04:03:17','2021-10-28 08:57:16','anhnh','anhnh',NULL,'beginner',0,NULL,NULL),(16,'JAVA CORE - Lập trình hướng đối tượng từ Zero','<p>JAVA là ngôn ngữ lập trình rất phổ biến nhất hiện nay, học JAVA CORE bạn sẽ có rất nhiều hướng đi, từ lập trình Mobile app, Java web, Desktop App, Game,... và tất cả đều sử dụng nền tảng của JAVA CORE.</p>','<p>JAVA là ngôn ngữ lập trình rất phổ biến nhất hiện nay, học JAVA CORE bạn sẽ có rất nhiều hướng đi, từ lập trình Mobile app, Java web, Desktop App, Game,... và tất cả đều sử dụng nền tảng của JAVA CORE.</p><p>Kết thúc khóa học bạn sẽ :</p><p>1. Nắm được các khái niệm lập trình Java cơ bản.</p><p>2. Nắm được các kiến thức về lập trình hướng đối tượng Java (OOP).</p><p>3. Từ kiến thức cơ bản JAVA core bạn có thể tự học các ngôn ngữ lập trình hướng đối tượng khác như C++/C#,Python,...</p>','https://www.dropbox.com/s/ixvvhmht2rf5ewa/1635395918.jfif?raw=1','https://www.dropbox.com/s/8603enpr8wp63uf/1635395921.mp4?raw=1','<ul><li>1. Nắm được kiến thức java cơ bản cũng như kiến thức về lập trình hướng đối tượng.</li><li>2. Có thể viết được các chương trình java cơ bản như các ứng dụng Console App, Desktop App.</li><li>3. Làm nền tảng để học tiếp các khóa học nâng cao về java (Java advance, Java web, Android...).</li><li>4. Có thể xin làm java fresher hoặc thực tập tại các công ty phần mềm.</li></ul>',0,0,0,39,8,3,'2021-10-28 04:38:45','2021-10-28 04:38:45','anhnh','anhnh',NULL,'intermediate',0,NULL,NULL),(17,'Marketing cho người bắt đầu','<p>Nếu bạn là một chủ doanh nghiệp, quán ăn, cửa hiệu, bán hàng online..., dù bạn làm gì thì cũng phải bán hàng, và tìm kiếm khách hàng để gia tăng lợi nhuận!</p><p>Vậy làm thế nào để tìm khách và và xây dựng thương hiệu trên Internet?</p><p>Bạn có thể thấy người khác quảng cáo, SEO website... nhưng đó là phương pháp rất cũ, cạnh tranh cao, tốn kém chi phí, hiệu quả đi xuống theo thời gian, phức tạp nếu bạn không am hiểu về nó và có thể mất rất nhiều tiền!</p><p>Vậy bây giờ bạn phải làm gì để phát triển được trên Internet để tìm khách hàng!</p><p>Video Marketing có thể giúp bạn, tự động, hiệu quả và ngày càng phát triển, cạnh tranh cực thấp, chi phí gần như = 0</p>','<p>Nếu bạn là một chủ doanh nghiệp, quán ăn, cửa hiệu, bán hàng online..., dù bạn làm gì thì cũng phải bán hàng, và tìm kiếm khách hàng để gia tăng lợi nhuận!</p><p>Vậy làm thế nào để tìm khách và và xây dựng thương hiệu trên Internet?</p><p>Bạn có thể thấy người khác quảng cáo, SEO website... nhưng đó là phương pháp rất cũ, cạnh tranh cao, tốn kém chi phí, hiệu quả đi xuống theo thời gian, phức tạp nếu bạn không am hiểu về nó và có thể mất rất nhiều tiền!</p><p>Vậy bây giờ bạn phải làm gì để phát triển được trên Internet để tìm khách hàng!</p><p>Video Marketing có thể giúp bạn, tự động, hiệu quả và ngày càng phát triển, cạnh tranh cực thấp, chi phí gần như = 0</p><p>Vậy làm thế nào để áp dụng video marketing cho việc kinh doanh của bạn!</p><p>Bước 1: Xác định chủ đề và ý tưởng,</p><p>Bước 2: Quay video,</p><p>Bước 3: Chỉnh sữa video,</p><p>Bước 4: Tải lên mạng và tối ưu</p><p>Nếu bạn không rành công nghệ, muốn tiết kiệm thời gian và tiền bạc thì hãy tham khảo khóa học để làm chủ được VIDEO MARKETING</p>','https://www.dropbox.com/s/cu6cbvgr8d5nfrs/1635406479.jfif?raw=1','https://www.dropbox.com/s/gku6x4notjs5sw5/1635406482.mp4?raw=1','<ul><li>Sau khi học xong bạn sẽ:</li><li>Tạo cho mình hàng trăm video giá trị cho khách hàng</li><li>Bạn sẽ không bao giờ sợ quay video thêm một lần nào nữa</li><li>Bạn sẽ sáng tạo ra những ý tưởng quay video</li><li>Bạn sẽ nắm vững kỹ năng body language trong video</li><li>Bạn sẽ sở hữu kỷ năng thuyết trình chuyên nghiệp</li></ul>',0,0,0,40,1,5,'2021-10-28 07:34:47','2021-10-28 07:34:47','anhnh','anhnh',NULL,'advance',0,NULL,NULL);
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
  `created_by` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `updated_by` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
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
-- Table structure for table `notification`
--

DROP TABLE IF EXISTS `notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notification` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `content` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  `action_id` int unsigned DEFAULT NULL,
  `user_id` int unsigned NOT NULL,
  `role` enum('admin','teacher','user') DEFAULT NULL,
  `type` int unsigned DEFAULT NULL,
  `is_seen` bit(1) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `updated_by` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `deleted_flag` bit(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notification`
--

LOCK TABLES `notification` WRITE;
/*!40000 ALTER TABLE `notification` DISABLE KEYS */;
/*!40000 ALTER TABLE `notification` ENABLE KEYS */;
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
  `created_by` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `updated_by` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
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
INSERT INTO `session` VALUES (13,'Các Loài Quả (Trái Cây)','https://www.dropbox.com/s/si1f7aj9fct50e1/1635392084.mp4?raw=1',428,14,'2021-10-28 03:26:25','2021-10-28 03:34:49','anhnh','anhnh',NULL),(14,'Học Tiếng Anh Theo Chủ Đề - Các Loài Động Vật - Phần 1','https://www.dropbox.com/s/b7pygizhkv3x3ij/1635392245.webm?raw=1',301,15,'2021-10-28 03:37:33','2021-10-28 03:37:33','anhnh','anhnh',NULL),(15,'Học Tiếng Anh Theo Chủ Đề - Các Loài Động Vật - Phần 2','https://www.dropbox.com/s/nwl9iuji8ebxlz7/1635392371.webm?raw=1',173,15,'2021-10-28 03:39:36','2021-10-28 03:39:36','anhnh','anhnh',NULL),(16,'Học Tiếng Anh Theo Chủ Đề - Các Loài Động Vật - Phần 3','https://www.dropbox.com/s/ukk328299n0c3hv/1635392457.webm?raw=1',190,15,'2021-10-28 03:41:02','2021-10-28 03:41:02','anhnh','anhnh',NULL),(17,'Học Tiếng Anh Theo Chủ Đề - Thời Tiết - Phần 1','https://www.dropbox.com/s/y66tvqlgsbp7n42/1635392586.webm?raw=1',182,16,'2021-10-28 03:43:10','2021-10-28 03:43:10','anhnh','anhnh',NULL),(18,'Học Tiếng Anh Theo Chủ Đề - Thời Tiết - Phần 2','https://www.dropbox.com/s/b3e2696wb4tpw3o/1635392616.webm?raw=1',174,16,'2021-10-28 03:43:43','2021-10-28 03:43:43','anhnh','anhnh',NULL),(19,'Cài đặt PHP trên Window','https://www.dropbox.com/s/luud57n0o9xlrm0/1635393940.webm?raw=1',339,17,'2021-10-28 04:05:45','2021-10-28 04:05:45','anhnh','anhnh',NULL),(20,'Syntax trong PHP','https://www.dropbox.com/s/f2zge780lm5klru/1635393999.webm?raw=1',474,18,'2021-10-28 04:06:43','2021-10-28 04:06:43','anhnh','anhnh',NULL),(21,'Biến trong PHP','https://www.dropbox.com/s/h67iivdgzavqrfe/1635394055.webm?raw=1',553,18,'2021-10-28 04:07:42','2021-10-28 04:07:42','anhnh','anhnh',NULL),(22,'Toán tử trong PHP','https://www.dropbox.com/s/q6sfnbw9ky8gi2o/1635394105.webm?raw=1',227,18,'2021-10-28 04:08:30','2021-10-28 04:08:30','anhnh','anhnh',NULL),(23,'Chuỗi trong PHP','https://www.dropbox.com/s/jxyno7e2ryn2qsu/1635394152.webm?raw=1',158,18,'2021-10-28 04:09:16','2021-10-28 04:09:16','anhnh','anhnh',NULL),(24,'Mảng trong PHP','https://www.dropbox.com/s/29wh730w0vlr2io/1635394232.webm?raw=1',597,18,'2021-10-28 04:10:36','2021-10-28 04:10:36','anhnh','anhnh',NULL),(25,'Câu điều kiện trong PHP IF Else','https://www.dropbox.com/s/u1tcpryd54wgkfi/1635394266.webm?raw=1',265,18,'2021-10-28 04:11:11','2021-10-28 04:11:11','anhnh','anhnh',NULL),(26,'Hàm trong PHP','https://www.dropbox.com/s/90o5hk9scgoauu7/1635394318.webm?raw=1',639,18,'2021-10-28 04:12:03','2021-10-28 04:12:03','anhnh','anhnh',NULL),(27,'Vòng lặp trong PHP','https://www.dropbox.com/s/fe7vanczutvljwc/1635394354.webm?raw=1',390,18,'2021-10-28 04:12:40','2021-10-28 04:12:40','anhnh','anhnh',NULL),(28,'Tổng kết','https://www.dropbox.com/s/my34xw005w5kumu/1635394506.webm?raw=1',462,19,'2021-10-28 04:15:12','2021-10-28 04:15:12','anhnh','anhnh',NULL),(29,'Phần mềm học Java','https://www.dropbox.com/s/pp43ykic7qjgofz/1635404773.mp4?raw=1',524,20,'2021-10-28 07:06:18','2021-10-28 07:06:18','anhnh','anhnh',NULL),(30,'Chương trình Java đầu tiên','https://www.dropbox.com/s/tvfdoxqotzxzfyb/1635404808.mp4?raw=1',369,21,'2021-10-28 07:06:52','2021-10-28 07:06:52','anhnh','anhnh',NULL),(31,'Biên dịch tập tin java','https://www.dropbox.com/s/1ypht7h7x8rdkoy/1635404847.mp4?raw=1',489,21,'2021-10-28 07:07:32','2021-10-28 07:07:32','anhnh','anhnh',NULL),(32,'Biến trong Java','https://www.dropbox.com/s/kxfeuoqv6fgmokf/1635404927.mp4?raw=1',148,21,'2021-10-28 07:08:51','2021-10-28 07:08:51','anhnh','anhnh',NULL),(33,'Tìm hiểu Package','https://www.dropbox.com/s/3odw0h63ygnafa1/1635404979.mp4?raw=1',303,21,'2021-10-28 07:09:44','2021-10-28 07:09:44','anhnh','anhnh',NULL),(34,'Khai báo biến trong Java 01','https://www.dropbox.com/s/nqwkez6i1w4qgad/1635405009.mp4?raw=1',474,21,'2021-10-28 07:10:14','2021-10-28 07:10:14','anhnh','anhnh',NULL),(35,'Khai báo biến trong Java 02','https://www.dropbox.com/s/zv9y0graog9pih6/1635405048.mp4?raw=1',486,21,'2021-10-28 07:10:54','2021-10-28 07:10:54','anhnh','anhnh',NULL),(36,'Xem Thêm Videos về Lập trình Java cơ bản','https://www.dropbox.com/s/5err8jhzj128cqh/1635405093.webm?raw=1',54,22,'2021-10-28 07:11:37','2021-10-28 07:11:37','anhnh','anhnh',NULL),(37,'Bản chất Marketing','https://www.dropbox.com/s/9xyvrtxmvx4wgl5/1635406583.mp4?raw=1',568,23,'2021-10-28 07:36:30','2021-10-28 07:38:39','anhnh','anhnh',NULL),(38,'Phân tích môi trường Marketing (Phần 1)','https://www.dropbox.com/s/n00yihs7pbv1sd0/1635406813.mp4?raw=1',592,24,'2021-10-28 07:40:23','2021-10-28 07:40:23','anhnh','anhnh',NULL),(39,'Phân tích môi trường Marketing (Phần 2)','https://www.dropbox.com/s/gneaekjri87fhoc/1635407142.mp4?raw=1',438,24,'2021-10-28 07:45:50','2021-10-28 07:45:50','anhnh','anhnh',NULL),(40,'Chiến lược xúc tiến hỗn hợp (Phần 1)','https://www.dropbox.com/s/qk2rmf2ww6lhf9z/1635407353.mp4?raw=1',586,25,'2021-10-28 07:49:18','2021-10-28 07:50:16','anhnh','anhnh',NULL),(41,'Chiến lược xúc tiến hỗn hợp (Phần 2)','https://www.dropbox.com/s/l7j6acq1os7wf0h/1635407385.mp4?raw=1',597,25,'2021-10-28 07:50:06','2021-10-28 07:50:06','anhnh','anhnh',NULL);
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
  `full_name` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `date_of_birth` datetime DEFAULT NULL,
  `gender` enum('not_specific','male','female') NOT NULL DEFAULT 'not_specific',
  `phone_number` varchar(11) DEFAULT NULL,
  `about` text NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_flag` bit(1) DEFAULT NULL,
  `url_avatar` text NOT NULL,
  `email` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `is_active` bit(1) DEFAULT NULL,
  `followed` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (1,'string','2021-09-21 00:00:00','not_specific','string','string','2021-09-21 09:48:17','2021-09-21 09:49:13',_binary '','string','string',NULL,NULL),(2,'Topica Native','1975-03-05 00:00:00','male','012345678','<p>Topica Native là đơn vị cung cấp chương trình tiếng Anh giao tiếp với hơn 1,600 giảng viên Âu - Úc - Mỹ, được phát triển tại 3 quốc gia Đông Nam Á. Các khóa học trực tiếp và trực tuyến theo nhóm nhỏ của Topica Native kéo dài từ 8h-24h cho phép bạn học tiếng Anh ở mọi lúc, mọi nơi, mọi thiết bị. Website: https://topicanative.edu.vn/</p>','2021-09-21 09:56:18','2021-10-28 03:51:26',NULL,'https://www.dropbox.com/s/vg8f7h4grg3t76c/1635393084.png?raw=1','test1@gmail.com',NULL,NULL),(3,'Lưu Trường Hải Lân','1975-03-05 00:00:00','not_specific','0123456789','<p>Quản lý đào tạo tại ZendVN</p><p>Vị trí đã từng đảm nhiệm: Developer, Teamleader, Project manager, Training manager</p><p>Công việc hiện nay: Training manager &amp; Project manager tại ZendVN</p><p>Xây dựng kênh học lập trình miễn phí với hơn 5 triệu lượt xem trên Youtube</p><p>Các khóa học trực tuyến đã xây dựng: NodeJS, Laravel, Angular, ReactJS, Lập trình PHP, Zend Framework 2.x, jQuery Master, Bootstrap, HTML, CSS, Javascript, Python, ...</p>','2021-09-21 16:03:01','2021-10-28 03:51:07',NULL,'https://www.dropbox.com/s/shsjhc70jpq7ww2/1635393065.jpg?raw=1','test@gmail.com',NULL,NULL),(4,'1','2021-09-21 00:00:00','not_specific','0384930792','<p>1</p>','2021-09-21 16:30:05','2021-09-21 16:31:37',_binary '','https://www.dropbox.com/s/amqj70675vmhx7t/1632241801.png?raw=1','hoanganhnguyenkfe99@mail.com',NULL,NULL),(5,'Nguyễn Thành Long','1971-12-22 00:00:00','male','012369852','<p><i>Giảng viên Nguyễn Thành Long là người đã có hơn 10 năm kinh nghiệm quản lý, phân tích, lên kế hoạch &amp; triển khai nhiều chiến dịch, dự án về Digital tại các công ty tên tuổi như Admicro, Cốc Cốc, FPT, Anphabe...Bên cạnh đó, ông còn được đánh giá cao trong lĩnh vực giảng dạy và là diễn giả nổi tiếng chuyên về chủ đề Digital Marketing</i></p>','2021-10-25 16:45:09','2021-10-28 03:50:28',NULL,'https://www.dropbox.com/s/2zo7jyqf60scwwv/1635393026.jpg?raw=1','longnt@gmail.com',NULL,NULL);
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
  `first_name` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `last_name` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `email` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
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
INSERT INTO `transaction_course` VALUES (28,19,15,18,0,NULL,0,'2021-10-28 09:06:26','2021-10-28 09:06:26',NULL,'Lập trình PHP cơ bản');
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
  `first_name` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `last_name` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `email` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `url_avatar` text NOT NULL,
  `date_of_birth` datetime DEFAULT NULL,
  `gender` enum('not_specific','male','female') NOT NULL DEFAULT 'not_specific',
  `phone_number` varchar(11) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `deleted_flag` bit(1) DEFAULT NULL,
  `hash_pwd` varchar(256) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Hoang Anh','Nguyen','anhnh@hybrid-technologies.vn','https://www.dropbox.com/s/tc4098l368iud8c/1635393399.jpg?raw=1','1970-04-18 00:00:00','male','0963058211','2021-09-25 07:34:32','2021-10-28 03:56:41',NULL,'pbkdf2:sha256:150000$nJoJkV4e$4ba8cea6340a321845b2906ab22fde4442fe56202ad18fe3247181aa37b0683c'),(7,'Nguyen','Hoang Anh','hoanganhkfe99@gmail.com','https://www.dropbox.com/s/ljftdc3rnkrp90c/1635393435.jpg?raw=1','1975-03-06 00:00:00','male','0963058211','2021-10-27 17:18:06','2021-10-28 03:57:18',NULL,'pbkdf2:sha256:150000$rpULkpOq$11ff79342932d3f07306b4342890e28c8bada5bb24b401624c1c00d222ac384e'),(8,'ha','tq','hatq@gmail.com','string','2023-02-05 00:00:00','male','string','2023-02-05 18:45:42','2023-02-05 18:45:42',NULL,'pbkdf2:sha256:150000$wGWjaejK$f2bb8a7ce57572d3981196d0ab9e476851acc963eb4a24bddfb0bfdb704a27dd');
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

--
-- Dumping routines for database 'pikaacademy'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-05 21:54:11
