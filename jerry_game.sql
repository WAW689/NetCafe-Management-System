-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: jerry_game
-- ------------------------------------------------------
-- Server version	9.6.0

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
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '26e40073-1967-11f1-830f-107c616f71c3:1-254';

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `admin_id` int NOT NULL AUTO_INCREMENT,
  `login_name` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `real_name` varchar(50) DEFAULT NULL,
  `role` varchar(20) DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'admin','123456','系统管理员','管理员',1);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `computer`
--

DROP TABLE IF EXISTS `computer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `computer` (
  `comp_id` int NOT NULL AUTO_INCREMENT,
  `area` varchar(50) DEFAULT NULL,
  `seat_no` int DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `hourly_rate` decimal(10,2) DEFAULT NULL,
  `spec` text,
  PRIMARY KEY (`comp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `computer`
--

LOCK TABLES `computer` WRITE;
/*!40000 ALTER TABLE `computer` DISABLE KEYS */;
INSERT INTO `computer` VALUES (1,'A区',1,'空闲',5.00,'i5+16G'),(2,'A区',2,'空闲',5.00,'i5+16G'),(3,'B区',1,'使用中',8.00,'i7+32G'),(5,'A区',3,'空闲',5.00,'i5+16G');
/*!40000 ALTER TABLE `computer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `internet_record`
--

DROP TABLE IF EXISTS `internet_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `internet_record` (
  `record_id` int NOT NULL AUTO_INCREMENT,
  `member_id` int DEFAULT NULL,
  `comp_id` int DEFAULT NULL,
  `admin_id` int DEFAULT NULL,
  `start_time` datetime DEFAULT NULL,
  `amount_due` decimal(10,2) DEFAULT NULL,
  `amount_paid` decimal(10,2) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  PRIMARY KEY (`record_id`),
  KEY `member_id` (`member_id`),
  KEY `comp_id` (`comp_id`),
  KEY `admin_id` (`admin_id`),
  CONSTRAINT `internet_record_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`member_id`),
  CONSTRAINT `internet_record_ibfk_2` FOREIGN KEY (`comp_id`) REFERENCES `computer` (`comp_id`),
  CONSTRAINT `internet_record_ibfk_3` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `internet_record`
--

LOCK TABLES `internet_record` WRITE;
/*!40000 ALTER TABLE `internet_record` DISABLE KEYS */;
INSERT INTO `internet_record` VALUES (1,1,1,1,'2026-06-02 18:11:49',5.00,5.00,'已完成','2026-06-02 18:14:00'),(2,2,3,1,'2026-06-02 23:44:52',8.00,8.00,'已完成','2026-06-02 23:46:01'),(3,2,3,1,'2026-06-04 21:46:33',NULL,NULL,'上机中',NULL),(4,1,1,1,'2026-06-04 22:10:31',5.00,5.00,'已完成','2026-06-04 22:11:36'),(5,2,1,1,'2026-06-08 22:49:00',5.00,5.00,'已完成','2026-06-08 22:49:26'),(6,2,1,1,'2026-06-08 22:55:30',5.00,5.00,'已完成','2026-06-08 22:55:56'),(7,1,1,1,'2026-06-08 23:03:15',5.00,5.00,'已完成','2026-06-08 23:03:34');
/*!40000 ALTER TABLE `internet_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `member`
--

DROP TABLE IF EXISTS `member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `member` (
  `member_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `gender` char(1) DEFAULT NULL,
  `id_card` char(18) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `balance` decimal(10,2) DEFAULT NULL,
  `level` varchar(20) DEFAULT NULL,
  `register_date` date DEFAULT NULL,
  `status` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `member`
--

LOCK TABLES `member` WRITE;
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` VALUES (1,'张三','M',NULL,'17894851515',95.00,'普通会员','2026-06-02',1),(2,'武建宁','F',NULL,'1888888888',1460.00,'普通会员','2026-06-02',1),(3,'李晨','F',NULL,'18809338868',888.00,'普通会员','2026-06-02',1),(4,'杜昕洋','F',NULL,'18809338848',1288.00,'普通会员','2026-06-02',1);
/*!40000 ALTER TABLE `member` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_detail`
--

DROP TABLE IF EXISTS `order_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order_detail` (
  `detail_id` int NOT NULL AUTO_INCREMENT,
  `order_id` int DEFAULT NULL,
  `product_id` int DEFAULT NULL,
  `quantity` int DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`detail_id`),
  KEY `order_id` (`order_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `order_detail_ibfk_1` FOREIGN KEY (`order_id`) REFERENCES `sales_order` (`order_id`),
  CONSTRAINT `order_detail_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_detail`
--

LOCK TABLES `order_detail` WRITE;
/*!40000 ALTER TABLE `order_detail` DISABLE KEYS */;
INSERT INTO `order_detail` VALUES (1,1,1,2,16.00),(2,2,2,5,30.00),(3,3,4,18,144.00),(4,4,4,20,160.00),(5,5,5,20,1360.00),(6,6,4,3,24.00);
/*!40000 ALTER TABLE `order_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `product_id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(50) DEFAULT NULL,
  `price` decimal(10,2) DEFAULT NULL,
  `stock` int DEFAULT NULL,
  `unit` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'红牛',8.00,98,'罐'),(2,'泡面',6.00,45,'桶'),(3,'矿泉水',3.00,80,'瓶'),(4,'奶茶',8.00,9,'杯'),(5,'很久以前羊肉串',68.00,0,'串');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales_order`
--

DROP TABLE IF EXISTS `sales_order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales_order` (
  `order_id` int NOT NULL AUTO_INCREMENT,
  `member_id` int DEFAULT NULL,
  `admin_id` int DEFAULT NULL,
  `sale_time` datetime DEFAULT NULL,
  `total_amount` decimal(10,2) DEFAULT NULL,
  `pay_method` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `member_id` (`member_id`),
  KEY `admin_id` (`admin_id`),
  CONSTRAINT `sales_order_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`member_id`),
  CONSTRAINT `sales_order_ibfk_2` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales_order`
--

LOCK TABLES `sales_order` WRITE;
/*!40000 ALTER TABLE `sales_order` DISABLE KEYS */;
INSERT INTO `sales_order` VALUES (1,1,1,'2026-06-02 18:33:35',16.00,'现金'),(2,2,1,'2026-06-02 23:47:54',30.00,'现金'),(3,2,1,'2026-06-03 08:49:55',144.00,'现金'),(4,2,1,'2026-06-08 22:51:11',160.00,'现金'),(5,2,1,'2026-06-08 22:56:53',1360.00,'现金'),(6,2,1,'2026-06-08 23:04:55',24.00,'现金');
/*!40000 ALTER TABLE `sales_order` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `topup_record`
--

DROP TABLE IF EXISTS `topup_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `topup_record` (
  `topup_id` int NOT NULL AUTO_INCREMENT,
  `member_id` int DEFAULT NULL,
  `admin_id` int DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `bonus` decimal(10,2) DEFAULT NULL,
  `topup_time` datetime DEFAULT NULL,
  PRIMARY KEY (`topup_id`),
  KEY `member_id` (`member_id`),
  KEY `admin_id` (`admin_id`),
  CONSTRAINT `topup_record_ibfk_1` FOREIGN KEY (`member_id`) REFERENCES `member` (`member_id`),
  CONSTRAINT `topup_record_ibfk_2` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`admin_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `topup_record`
--

LOCK TABLES `topup_record` WRITE;
/*!40000 ALTER TABLE `topup_record` DISABLE KEYS */;
INSERT INTO `topup_record` VALUES (1,2,1,888.00,0.00,'2026-06-02 23:35:59'),(2,3,1,888.00,0.00,'2026-06-02 23:42:50'),(3,4,1,1288.00,0.00,'2026-06-03 08:48:24'),(4,2,1,455.00,0.00,'2026-06-04 21:46:14'),(5,2,1,15.00,0.00,'2026-06-04 22:10:04'),(6,2,1,20.00,0.00,'2026-06-08 22:48:16'),(7,2,1,100.00,0.00,'2026-06-08 22:55:05'),(8,1,1,10.00,0.00,'2026-06-08 23:02:53');
/*!40000 ALTER TABLE `topup_record` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-06-10 20:16:57
