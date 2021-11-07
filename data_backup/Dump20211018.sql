-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
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
INSERT INTO `cart_course` VALUES (1,1,7,'2021-09-29 09:36:12','2021-09-30 14:40:00',_binary ''),(2,1,6,'2021-09-29 09:36:40','2021-09-29 09:37:00',_binary ''),(3,1,4,'2021-09-30 09:36:46','2021-09-30 14:39:48',_binary ''),(4,1,6,'2021-09-30 14:12:37','2021-09-30 14:39:52',_binary ''),(5,1,4,'2021-09-30 16:34:36','2021-10-04 03:24:51',_binary ''),(6,1,1,'2021-09-30 16:43:45','2021-10-04 03:24:51',_binary ''),(7,1,7,'2021-10-04 03:40:21','2021-10-04 03:41:07',_binary ''),(8,1,4,'2021-10-04 03:40:40','2021-10-04 03:41:07',_binary ''),(9,1,6,'2021-10-07 14:54:50','2021-10-07 15:38:34',_binary ''),(10,1,1,'2021-10-07 15:38:45','2021-10-07 15:46:08',_binary ''),(11,1,4,'2021-10-07 15:52:00','2021-10-07 15:52:51',_binary ''),(12,1,7,'2021-10-07 15:52:07','2021-10-07 15:52:51',_binary ''),(13,1,4,'2021-10-11 15:42:50','2021-10-11 15:55:44',_binary ''),(14,1,7,'2021-10-11 15:57:31','2021-10-11 15:59:16',_binary ''),(15,1,7,'2021-10-11 16:03:00','2021-10-11 16:03:08',_binary ''),(16,1,4,'2021-10-11 16:05:35','2021-10-11 16:06:00',_binary ''),(17,1,7,'2021-10-11 16:06:20','2021-10-11 16:06:49',_binary ''),(18,1,4,'2021-10-13 07:35:49','2021-10-13 07:36:16',_binary ''),(19,1,6,'2021-10-13 07:35:59','2021-10-13 07:36:16',_binary ''),(20,1,7,'2021-10-14 02:19:03','2021-10-14 02:19:12',_binary '');
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
INSERT INTO `chapter` VALUES (1,'Giới Thiệu Khóa Học',3,'2021-09-14 09:45:43','2021-09-15 08:22:55','anhnh','anhnh',NULL),(2,'Nội Dung Khóa Học',3,'2021-09-15 07:01:31','2021-09-15 08:24:54','anhnh','anhnh',NULL),(3,'Kết Thúc Khóa Học',3,'2021-09-15 08:09:44','2021-09-15 08:25:24','anhnh','anhnh',NULL),(4,'Giới Thiệu Khóa Học',3,'2021-09-15 08:15:21','2021-09-15 08:31:50','anhnh','anhnh',_binary ''),(5,'Hello NodeJS',3,'2021-09-16 09:10:59','2021-09-16 09:26:20','anhnh','anhnh',_binary ''),(6,'Kết Thúc Khóa Học',3,'2021-09-16 09:22:02','2021-09-16 09:26:16','anhnh','anhnh',_binary ''),(7,'1',3,'2021-09-16 09:27:07','2021-09-16 09:27:10','anhnh','anhnh',_binary ''),(8,'Yêu lại ngữ pháp từ đầu',7,'2021-09-20 08:20:51','2021-09-20 08:20:51','anhnh','anhnh',NULL),(9,'ahihi123',3,'2021-10-16 14:57:45','2021-10-17 11:27:27','anhnh','anhnh',_binary ''),(10,'ahuhu',3,'2021-10-17 11:01:44','2021-10-17 11:52:34','anhnh','anhnh',_binary ''),(11,'sdfsdaf123',3,'2021-10-17 11:46:58','2021-10-17 11:47:03','anhnh','anhnh',NULL),(12,'ahihi',13,'2021-10-17 12:51:59','2021-10-17 12:51:59','anhnh','anhnh',NULL),(13,'sdfdsaf',13,'2021-10-17 13:17:29','2021-10-17 13:17:29','anhnh','anhnh',NULL);
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
INSERT INTO `course` VALUES (1,'Hướng dẫn lập trình java cơ bản','Giới thiệu về Các cấu trúc trong lập trình Java như cấu trúc điều kiện, lặp, chuỗi.','Có thể lập trình cơ bản về Java\n\nLộ trình học tập:\n\nCác bài học giúp học viên có thể lập trình JAVA một cách dễ dàng.','https://www.dropbox.com/s/1r9fzjndrcc25to/1632128558.jpg?raw=1','https://www.dropbox.com/s/389kwpwftn1cixm/1632128564.mp4?raw=1','Có thể lập trình cơ bản về Java.',0,0,0,39,8,3,'2021-09-11 14:26:28','2021-09-27 15:35:47','string','string',NULL,'beginner',0),(3,'Lập trình NodeJs cơ bản','Khoá học cung cấp cho học viên các kiến thức cơ bản về lập trình NodeJs, cách cài đặt và áp dụng NodeJS trong việc xây dựng các project chúng ta thường gặp trong thực tế.','Khoá học cung cấp cho học viên các kiến thức cơ bản về lập trình NodeJs, cách cài đặt và áp dụng NodeJS trong việc xây dựng các project chúng ta thường gặp trong thực tế.\n\nLộ trình học tập:\n\n22 bài học chia làm 3 chương gúp học viên nắm chắc được kiến thức về lập trình Nodejs.','https://www.dropbox.com/s/kyw6lakli0lj9f2/1632128404.jpg?raw=1','https://www.dropbox.com/s/9engog9atookoff/1632128412.mp4?raw=1','Có kiến thức cơ bản về ngôn ngữ lập trình Nodejs.\nBiết cách cài đặt, khởi tạo NodeJs cho ứng dụng.\nBổ trợ các kỹ năng nghe, nói, đọc, viết.',0,1,0,39,8,2,'2021-09-13 16:09:05','2021-09-27 15:45:37','anhnh','anhnh',NULL,'beginner',0),(4,'Thành thạo Web Automation Test với Selenium VÀ NodeJS','Khóa học Thành thạo Web Automation Test với Selenium và Nodejs được thiết kế bài bản, chắt lọc đồng thời vẫn đảm bảo độ chi tiết, tính ứng dụng cao. Từ đó, giúp học viên dễ dàng tiếp thu, thực hành kiến thức mới một cách nhanh chóng và hiệu quả nhất. Khóa học bao gồm 7 phần với 66 bài giảng, trong thời lượng 7h49p đem đến cho người học những nội dung sau:\n\n- Kiến thức từ cơ bản đến nâng cao cho Web Automation\n- Cách dùng ngôn ngữ JavaScript và thực thi với NodeJS\n- Cách dùng các client API để tương tác với các Web Element trong Automation\n- Kiến thức về tổ chức Page Object, Test verification, Test Script khoa học','Khóa học Thành thạo Web Automation Test với Selenium và Nodejs được thiết kế bài bản, chắt lọc đồng thời vẫn đảm bảo độ chi tiết, tính ứng dụng cao. Từ đó, giúp học viên dễ dàng tiếp thu, thực hành kiến thức mới một cách nhanh chóng và hiệu quả nhất. Khóa học bao gồm 7 phần với 66 bài giảng, trong thời lượng 7h49p đem đến cho người học những nội dung sau:\n\n- Kiến thức từ cơ bản đến nâng cao cho Web Automation\n- Cách dùng ngôn ngữ JavaScript và thực thi với NodeJS\n- Cách dùng các client API để tương tác với các Web Element trong Automation\n- Kiến thức về tổ chức Page Object, Test verification, Test Script khoa học','https://www.dropbox.com/s/zvi3ig6xrqpz2fy/1632128283.jfif?raw=1','https://www.dropbox.com/s/a4nro6cuhbdazyh/1632128286.mp4?raw=1','Biết cách triển khai dự án Automation trên Web và tích lũy kiến thức nền tảng cho Automation trên Mobile\nNâng cao khả năng thiết kế Test Framework trong thực tế\nĐược tương tác với giảng viên để giải đáp thắc mắc trong quá trình học tập\nNhận được tài liệu bám sát với giáo trình, hỗ trợ cho việc học và thực hành.\n',0,2,3,39,8,3,'2021-09-18 11:43:28','2021-10-13 07:36:36','anhnh','anhnh',NULL,'beginner',0),(5,'Lập trình PHP Level 1','Khóa học sẽ cung cấp cho các bạn kiến thức căn bản về lập trình PHP một cách đầy đủ và có hệ thống, đảm bảo những ai vừa mới bắt đầu cũng có thể nắm bắt được nền tảng cốt lõi để phát triển kỹ năng lập trình của mình ở cấp cao hơn.','Khóa học sẽ cung cấp cho các bạn kiến thức căn bản về lập trình PHP một cách đầy đủ và có hệ thống, đảm bảo những ai vừa mới bắt đầu cũng có thể nắm bắt được nền tảng cốt lõi để phát triển kỹ năng lập trình của mình ở cấp cao hơn.','https://www.dropbox.com/s/8r0gn25eaaq4vzw/1632128188.jfif?raw=1','https://www.dropbox.com/s/u80u2fni0c2qiex/1632128191.mp4?raw=1','Nắm vững kiến thức căn bản về lập trình PHP một cách đầy đủ và có hệ thống.\nĐảm bảo những ai vừa mới bắt đầu cũng có thể nắm bắt được nền tảng cốt lõi.\nPhát triển kỹ năng lập trình của mình ở cấp cao hơn.',0,1,0,39,8,2,'2021-09-18 11:53:15','2021-09-30 07:59:29','anhnh','anhnh',NULL,'beginner',0),(6,'Lập trình game 2D bằng Unity (2020)','Qua khóa học này bạn sẽ có được kiến thức nền tảng để tự mình phát triển 2D game bằng Unity. Bạn sẽ nhận được sự hướng dẫn giải đáp chi tiết về môi trường làm việc trong Unity, hệ thống API, các công cụ, các điều quan trọng, cần biết và cần chú ý khi phát triển game bằng Unity. Bạn sẽ học được cách thiết kể, tổ chức hệ thống linh hoạt có khả năng tái sử dụng cao. Khóa học này sẽ áp dụng một số công nghệ mới của Unity 2019. Sau khóa học này bạn sẽ có đủ kiến thức và tự tin để tự làm một game 2D theo ý thích. Khóa học này KHÔNG bao gồm các chủ đề: - Lập trình Editor, Plugin - Lập trình server, game online - ECS, DOTs','Qua khóa học này bạn sẽ có được kiến thức nền tảng để tự mình phát triển 2D game bằng Unity. Bạn sẽ nhận được sự hướng dẫn giải đáp chi tiết về môi trường làm việc trong Unity, hệ thống API, các công cụ, các điều quan trọng, cần biết và cần chú ý khi phát triển game bằng Unity. Bạn sẽ học được cách thiết kể, tổ chức hệ thống linh hoạt có khả năng tái sử dụng cao. Khóa học này sẽ áp dụng một số công nghệ mới của Unity 2019. Sau khóa học này bạn sẽ có đủ kiến thức và tự tin để tự làm một game 2D theo ý thích. Khóa học này KHÔNG bao gồm các chủ đề: - Lập trình Editor, Plugin - Lập trình server, game online - ECS, DOTs','https://www.dropbox.com/s/prw38l7o08lqfv8/1632128157.jfif?raw=1','https://www.dropbox.com/s/b67g8u8lueicdt9/1632128160.mp4?raw=1','Bạn sẽ nhận được sự hướng dẫn từ giảng viên với nhiều năm kinh nghiệm trong lĩnh vực phát triển game bằng Unity.\nCó được kiến thức nền tảng để phát triển game 2D bằng Unity.\nNắm được cách tổ chức, thiết kế hệ thống linh hoạt dễ tái sử dụng.\nĐược học và sử dụng các công nghệ mới của Unity 2019 giúp tăng tốc phát triển game\nKết thúc khóa học này bạn sẽ có đầy đủ kiến thức và tự tin để tự làm hoàn chỉnh một game 2D theo ý thích',0,1,1,39,8,3,'2021-09-18 12:34:06','2021-10-13 07:36:36','anhnh','anhnh',NULL,'beginner',0),(7,'Hướng dẫn cài đặt Eclipse','Hướng dẫn cách cài đặt và cấu hình, cách sử dụng cơ bản Eclipse','Eclipse là một môi trường phát triển tích hợp dùng cho lập trình máy tính, nó chứa một không gian làm việc cơ sở và một hệ thống plugin để mở rộng và tùy chỉnh môi trường. Đây là 1 nền tảng hữu ích cho người dùng trong việc viết phần mềm. Khóa học này sẽ giúp bạn tìm hiểu về cách cài đặt và cấu hình, cách sử dụng cơ bản Eclipse.\n\nLộ trình học tập:\n\n5 bài học hướng dẫn chi tiết về cách tải Eclipse','https://www.dropbox.com/s/5oj3i2e4vcwlfao/1632128075.jfif?raw=1','https://www.dropbox.com/s/eycuzstp27mu3be/1632128080.mp4?raw=1','Biết cách cài đặt, sử dụng cơ bản các tính năng của Eclipse',0,2,4,39,8,2,'2021-09-18 12:36:55','2021-10-14 02:44:25','anhnh','anhnh',NULL,'beginner',0),(9,'fsadfds','<p>dsfad</p>','<p>dsfdsfa</p>','https://www.dropbox.com/s/qqixq7repf00h1z/1634370582.png?raw=1','https://www.dropbox.com/s/63079trqasihlbx/1634370586.mp4?raw=1','<p>dsfadf</p>',0,0,0,40,1,2,'2021-10-16 07:49:53','2021-10-17 13:48:39','anhnh','anhnh',_binary '','intermediate',0),(10,'dsfdsf','<p>dsfdsf</p>','<p>sdfdsf</p>','https://www.dropbox.com/s/zmqwhhdt1hzp7ke/1634372004.png?raw=1','https://www.dropbox.com/s/ewxykr5uokauk9x/1634372008.mp4?raw=1','<p>dfadsfd</p>',0,0,0,41,1,2,'2021-10-16 08:13:48','2021-10-17 13:48:45','anhnh','anhnh',_binary '','beginner',0),(11,'dffdsafsd','<p>dsfsdaf</p>','<p>dsfdsaf</p>','https://www.dropbox.com/s/p3knhckp9clw39f/1634372364.png?raw=1','https://www.dropbox.com/s/g9685v7d04x7krx/1634372367.mp4?raw=1','<p>dsfdsf</p>',0,0,0,40,1,2,'2021-10-16 08:19:49','2021-10-17 13:48:36','anhnh','anhnh',_binary '','intermediate',0),(12,'dsfdsaf','<p>dsfdsaf</p>','<p>dsfadsf</p>','https://www.dropbox.com/s/pqg4y8hhs9qhejt/1634372482.png?raw=1','https://www.dropbox.com/s/0z1dbx55aa2p9v6/1634372484.mp4?raw=1','<p>dsfdsf</p>',0,0,0,40,1,2,'2021-10-16 08:21:38','2021-10-17 13:48:34','anhnh','anhnh',_binary '','intermediate',0),(13,'dsfdsaf','<p>dsfdsf</p>','<p>dsfdsf</p>','https://www.dropbox.com/s/tjvmn3bluvn84e5/1634373244.png?raw=1','https://www.dropbox.com/s/7pd8p2kroidj8n0/1634373248.mp4?raw=1','<p>dsfdsf</p>',0,0,0,40,1,2,'2021-10-16 08:34:45','2021-10-17 13:48:31','anhnh','anhnh',_binary '','intermediate',0);
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
INSERT INTO `discount_promotion` VALUES (1,7,10,'2021-09-28 07:08:11','2021-11-01 07:08:11',_binary '','2021-09-28 07:12:54','2021-10-04 03:35:37',NULL),(2,13,2,'2021-10-16 06:00:00','2021-10-16 06:00:00',_binary '','2021-10-16 08:34:46','2021-10-16 08:34:46',NULL),(3,13,5,'2021-10-16 00:00:00','2021-10-16 00:00:00',_binary '','2021-10-16 10:52:16','2021-10-16 10:52:16',NULL),(4,13,5,'2021-10-16 00:00:00','2021-11-30 00:00:00',_binary '\0','2021-10-16 10:56:32','2021-10-16 10:58:15',NULL),(5,13,5,'2021-10-16 00:00:00','2021-11-16 00:00:00',_binary '\0','2021-10-16 10:58:15','2021-10-16 12:47:47',NULL),(6,13,12,'2021-10-16 00:00:00','2021-11-30 00:00:00',_binary '','2021-10-16 12:48:46','2021-10-16 12:48:46',NULL);
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
INSERT INTO `price` VALUES (1,7,500000,_binary '','2021-09-28 07:08:11','2021-09-28 07:08:11',NULL),(2,6,300000,_binary '','2021-09-28 07:08:11','2021-09-28 07:08:11',NULL),(3,5,0,_binary '','2021-09-28 07:08:11','2021-09-28 07:08:11',NULL),(4,4,1000000,_binary '','2021-09-28 07:08:11','2021-09-28 07:08:11',NULL),(5,3,0,_binary '','2021-09-28 07:08:11','2021-09-28 07:08:11',NULL),(6,1,700000,_binary '','2021-09-28 07:08:11','2021-09-28 07:08:11',NULL),(7,9,0,_binary '','2021-10-16 07:49:54','2021-10-16 07:49:54',NULL),(8,10,800000,_binary '','2021-10-16 08:13:49','2021-10-16 08:13:49',NULL),(9,11,1000000,_binary '','2021-10-16 08:19:49','2021-10-16 08:19:49',NULL),(10,12,500000,_binary '','2021-10-16 08:21:39','2021-10-16 08:21:39',NULL),(11,13,800000,_binary '\0','2021-10-16 08:34:46','2021-10-16 10:45:05',NULL),(12,13,10,_binary '\0','2021-10-16 10:45:05','2021-10-16 10:46:31',NULL),(13,13,0,_binary '\0','2021-10-16 10:46:31','2021-10-16 10:52:16',NULL),(14,13,1000000,_binary '\0','2021-10-16 10:52:16','2021-10-16 12:47:47',NULL),(15,13,0,_binary '\0','2021-10-16 12:47:47','2021-10-16 12:48:23',NULL),(16,13,800000,_binary '','2021-10-16 12:48:24','2021-10-16 12:48:24',NULL);
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
INSERT INTO `session` VALUES (1,'test','string',0,6,'2021-09-15 09:20:43','2021-09-16 09:23:54','string','string',_binary ''),(2,'Giới thiệu khóa học lập trình NodeJS Level 1','https://www.youtube.com/embed/wlflGIcdwnE',0,1,'2021-09-15 09:26:50','2021-09-15 09:26:50','anhnh','anhnh',NULL),(3,'Install NodeJS','https://www.youtube.com/embed/CB6WU5hzp0s',0,2,'2021-09-15 09:28:32','2021-09-16 10:39:38','anhnh','anhnh',_binary ''),(4,'Visual Studio Code','https://www.youtube.com/embed/mWdMyr_ATOA',0,2,'2021-09-15 09:29:31','2021-09-16 09:39:22','anhnh','anhnh',_binary ''),(5,'Hello NodeJS','https://www.dropbox.com/s/kdamo8nq7k5095o/1632128598.mp4?raw=1',550,2,'2021-09-16 09:12:16','2021-09-20 09:03:58','anhnh','anhnh',NULL),(6,'Template 01','https://www.dropbox.com/s/4qxh3q5oc4mazfh/1632128667.mp4?raw=1',138,3,'2021-09-16 09:26:50','2021-09-20 09:04:47','anhnh','anhnh',NULL),(7,'12345','https://www.dropbox.com/s/uulc7h9dgyc3dei/1631788808.mp4?raw=1',0,2,'2021-09-16 10:40:14','2021-09-16 10:41:22','anhnh','anhnh',_binary ''),(8,'Yêu lại ngữ pháp từ đầu','https://www.dropbox.com/s/n32rx09z4srctkx/1632128650.mp4?raw=1',19,2,'2021-09-20 08:22:09','2021-09-20 09:04:15','anhnh','anhnh',NULL),(9,'Giới Thiệu Khóa Học','https://www.dropbox.com/s/ns3sdx0xwecuyzh/1632128705.mp4?raw=1',35,3,'2021-09-20 08:25:16','2021-09-20 09:05:13','anhnh','anhnh',NULL),(10,'ahihi123','https://www.dropbox.com/s/nb8vwlr7rb4gwd0/1634476524.mp4?raw=1',35,12,'2021-10-17 13:09:09','2021-10-17 13:15:29','anhnh','anhnh',NULL),(11,'dsfdsf','https://www.dropbox.com/s/j7vqo9xvhijiq8m/1634476663.mp4?raw=1',19,13,'2021-10-17 13:17:52','2021-10-17 13:22:57','anhnh','anhnh',_binary ''),(12,'dsfdsafd','https://www.dropbox.com/s/rbri5zsqlnq80s9/1634476687.mp4?raw=1',50,13,'2021-10-17 13:18:14','2021-10-17 13:18:14','anhnh','anhnh',NULL);
/*!40000 ALTER TABLE `session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `table`
--

DROP TABLE IF EXISTS `table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `table` (
  `uuid` varchar(36) NOT NULL DEFAULT (uuid()),
  `col1` varchar(30) NOT NULL,
  PRIMARY KEY (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `table`
--

LOCK TABLES `table` WRITE;
/*!40000 ALTER TABLE `table` DISABLE KEYS */;
/*!40000 ALTER TABLE `table` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teacher`
--

LOCK TABLES `teacher` WRITE;
/*!40000 ALTER TABLE `teacher` DISABLE KEYS */;
INSERT INTO `teacher` VALUES (1,'string','2021-09-21 00:00:00','not_specific','string','string','2021-09-21 09:48:17','2021-09-21 09:49:13',_binary '','string','string'),(2,'Topica Native','2021-09-21 00:00:00','male','012345678','<p>Topica Native là đơn vị cung cấp chương trình tiếng Anh giao tiếp với hơn 1,600 giảng viên Âu - Úc - Mỹ, được phát triển tại 3 quốc gia Đông Nam Á. Các khóa học trực tiếp và trực tuyến theo nhóm nhỏ của Topica Native kéo dài từ 8h-24h cho phép bạn học tiếng Anh ở mọi lúc, mọi nơi, mọi thiết bị. Website: https://topicanative.edu.vn/</p>','2021-09-21 09:56:18','2021-09-21 16:22:31',NULL,'https://www.dropbox.com/s/qstp5tfis1j9lln/1632241246.jpg?raw=1','test1@gmail.com'),(3,'Lưu Trường Hải Lân','2021-09-21 00:00:00','not_specific',NULL,'<p>Quản lý đào tạo tại ZendVN</p><p>Vị trí đã từng đảm nhiệm: Developer, Teamleader, Project manager, Training manager</p><p>Công việc hiện nay: Training manager &amp; Project manager tại ZendVN</p><p>Xây dựng kênh học lập trình miễn phí với hơn 5 triệu lượt xem trên Youtube</p><p>Các khóa học trực tuyến đã xây dựng: NodeJS, Laravel, Angular, ReactJS, Lập trình PHP, Zend Framework 2.x, jQuery Master, Bootstrap, HTML, CSS, Javascript, Python, ...</p>','2021-09-21 16:03:01','2021-09-21 16:03:01',NULL,'https://www.dropbox.com/s/5kfgnu8bp88y38x/1632240178.png?raw=1','test@gmail.com'),(4,'1','2021-09-21 00:00:00','not_specific','0384930792','<p>1</p>','2021-09-21 16:30:05','2021-09-21 16:31:37',_binary '','https://www.dropbox.com/s/amqj70675vmhx7t/1632241801.png?raw=1','hoanganhnguyenkfe99@mail.com');
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
INSERT INTO `transaction` VALUES (16,'39658049-2bf8-11ec-a531-0242ac120003',1,'Hoang Anh','Nguyen','anhnh@hybrid-technologies.vn','0963058211',NULL,0,1298000,'bank','2021-10-13 07:36:05','success','2021-10-13 07:36:05','2021-10-13 07:36:35',NULL),(17,'1cae9b90-2c95-11ec-abdd-0242ac120003',1,'Hoang Anh','Nguyen','anhnh@hybrid-technologies.vn','0963058211',NULL,0,449000,'bank','2021-10-14 02:19:08','success','2021-10-14 02:19:08','2021-10-14 02:44:25',NULL);
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
INSERT INTO `transaction_course` VALUES (24,16,4,4,1000000,NULL,0,'2021-10-13 07:36:05','2021-10-13 07:36:05',NULL,'Thành thạo Web Automation Test với Selenium VÀ NodeJS'),(25,16,6,2,300000,NULL,0,'2021-10-13 07:36:05','2021-10-13 07:36:05',NULL,'Lập trình game 2D bằng Unity (2020)'),(26,17,7,1,500000,1,10,'2021-10-14 02:19:08','2021-10-14 02:19:08',NULL,'Hướng dẫn cài đặt Eclipse');
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
INSERT INTO `user_like_course` VALUES (1,1,4,'2021-10-04 08:33:05','2021-10-04 08:33:05','2021-10-04 08:33:05',NULL),(2,1,7,'2021-10-04 08:33:06','2021-10-04 08:33:06','2021-10-04 08:33:06',NULL);
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
INSERT INTO `user_purchase_course` VALUES (15,1,4,16,'2021-10-13 07:36:35','2021-10-13 07:36:35','2021-10-13 07:36:35',NULL),(16,1,6,16,'2021-10-13 07:36:35','2021-10-13 07:36:35','2021-10-13 07:36:35',NULL),(17,1,7,17,'2021-10-14 02:44:25','2021-10-14 02:44:25','2021-10-14 02:44:25',NULL);
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

-- Dump completed on 2021-10-18 22:29:33
