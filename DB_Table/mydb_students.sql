-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	5.7.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `sex` varchar(11) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `major` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2016102541 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (2016102501,'张文远','男','1994-01-01','计算机技术'),(2016102502,'张杰','男','1994-02-02','软件工程'),(2016102503,'周婕纶','女','1995-03-04','计算机技术'),(2016102504,'周婕纶','女','1995-03-04','计算机技术'),(2016102505,'张杰','男','1994-02-02','软件工程'),(2016102506,'张杰','男','1994-02-02','软件工程'),(2016102507,'张杰','男','1994-02-02','软件工程'),(2016102508,'张杰','男','1994-02-02','软件工程'),(2016102509,'张杰','男','1994-02-02','软件工程'),(2016102510,'张杰','男','1994-02-02','软件工程'),(2016102511,'张杰','男','1994-02-02','软件工程'),(2016102512,'张杰','男','1994-02-02','软件工程'),(2016102513,'张杰','男','1994-02-02','软件工程'),(2016102514,'张杰','男','1994-02-02','软件工程'),(2016102515,'张杰','男','1994-02-02','软件工程'),(2016102516,'张杰','男','1994-02-02','软件工程'),(2016102517,'张杰','男','1994-02-02','软件工程'),(2016102518,'张杰','男','1994-02-02','软件工程'),(2016102519,'张杰','男','1994-02-02','软件工程'),(2016102520,'张杰','男','1994-02-02','软件工程'),(2016102521,'张杰','男','1994-02-02','软件工程'),(2016102522,'张杰','男','1994-02-02','软件工程'),(2016102523,'张杰','男','1994-02-02','软件工程'),(2016102524,'张杰','男','1994-02-02','软件工程'),(2016102525,'张杰','男','1994-02-02','软件工程'),(2016102526,'张杰','男','1994-02-02','软件工程'),(2016102527,'张杰','男','1994-02-02','软件工程'),(2016102528,'张杰','男','1994-02-02','软件工程'),(2016102529,'张杰','男','1994-02-02','软件工程'),(2016102530,'张杰','男','1994-02-02','软件工程'),(2016102531,'张杰','男','1994-02-02','软件工程'),(2016102532,'张杰','男','1994-02-02','软件工程'),(2016102533,'张杰','男','1994-02-02','软件工程'),(2016102534,'张杰','男','1994-02-02','软件工程'),(2016102535,'张杰','男','1994-02-02','软件工程'),(2016102536,'张杰','男','1994-02-02','软件工程'),(2016102537,'张杰','男','1994-02-02','软件工程'),(2016102538,'谢娜','女','1994-06-06','计算机技术'),(2016102539,'神乐','女','1995-11-03','计算机技术'),(2016102540,'神乐','女','1995-11-03','计算机技术');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-06-07 17:30:21
