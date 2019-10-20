-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: 192.168.1.10    Database: java_test
-- ------------------------------------------------------
-- Server version	8.0.3-rc-log

use stromverbrauch;

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
-- Table structure for table `log`
--

DROP TABLE IF EXISTS `log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `log` (
  `t` datetime DEFAULT NULL,
  `comment` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log`
--

LOCK TABLES `log` WRITE;
/*!40000 ALTER TABLE `log` DISABLE KEYS */;
INSERT INTO `log` VALUES ('2015-04-24 12:01:38',' NEW.id 2 newid 5 oldid 4 checkvbr -900'),('2015-04-24 12:03:24',' NEW.id 2 newid 5 oldid 4 checkvbr -800'),('2015-04-24 12:09:11',' NEW.id 2 chid 2 b4chid 1 checkvbr 1600'),('2015-04-24 12:09:49',' NEW.id 3 chid 3 b4chid 2 checkvbr 400'),('2015-04-24 12:10:02',' NEW.id 4 chid 4 b4chid 3 checkvbr 500'),('2015-04-24 12:21:34',NULL),('2015-04-24 12:21:43',' NEW.id 2 chid 2 b4chid 1 checkvbr 246.71'),('2015-04-24 12:21:43',' NEW.id 3 chid 3 b4chid 2 checkvbr 266.46'),('2015-04-24 12:21:43',' NEW.id 4 chid 4 b4chid 3 checkvbr 238.32'),('2015-04-24 12:22:37',NULL),('2015-04-24 12:22:37',' NEW.id 2 chid 2 b4chid 1 checkvbr 246.71'),('2015-04-24 12:22:37',' NEW.id 3 chid 3 b4chid 2 checkvbr 266.46'),('2015-04-24 12:22:37',' NEW.id 4 chid 4 b4chid 3 checkvbr 238.32'),('2015-04-24 12:26:06',NULL),('2015-04-24 12:26:06',' NEW.id 2 chid 2 b4chid 1 checkvbr 1944.44'),('2015-04-24 12:26:06',' NEW.id 3 chid 3 b4chid 2 checkvbr 2166.18'),('2015-04-24 12:26:07',' NEW.id 4 chid 4 b4chid 3 checkvbr 2266.46');
/*!40000 ALTER TABLE `log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stromsonst`
--

DROP TABLE IF EXISTS `stromsonst`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stromsonst` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datum` date NOT NULL,
  `zaehlerstand` float NOT NULL,
  `verbrauch` float DEFAULT '0',
  `preis` float(4,4) NOT NULL,
  `kosten` float DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=56 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stromsonst`
--

LOCK TABLES `stromsonst` WRITE;
/*!40000 ALTER TABLE `stromsonst` DISABLE KEYS */;
INSERT INTO `stromsonst` VALUES (1,'2015-01-01',1448.42,0,0.2576,0),(2,'2015-02-01',1695.13,246.71,0.2576,63.5525),(3,'2015-03-01',1961.59,266.46,0.2576,68.6401),(4,'2015-04-01',2199.91,238.32,0.2576,61.3912),(5,'2015-05-01',2485.63,285.72,0.2576,73.6015),(7,'2015-06-01',2685.89,200.26,0.2576,51.587),(8,'2015-07-01',2908.92,223.03,0.2576,57.4525),(9,'2015-08-01',3097.16,188.24,0.2576,48.4906),(10,'2015-09-01',3353.97,256.81,0.2576,66.1543),(11,'2015-10-01',3648.21,294.24,0.2576,75.7962),(12,'2015-11-01',3995.01,346.8,0.2576,89.3357),(13,'2015-12-01',4320.08,325.07,0.2576,83.7381),(14,'2016-01-01',4679.02,358.94,0.2576,92.4629),(16,'2016-02-01',5041.63,362.61,0.2576,93.4083),(18,'2016-03-01',5359.63,318,0.2607,82.9026),(19,'2016-04-01',5731.47,371.84,0.2607,96.9388),(20,'2016-05-01',6052.48,321.01,0.2607,83.6872),(21,'2016-06-01',6364.64,312.16,0.2607,81.3801),(22,'2016-07-01',6633.86,269.22,0.2207,59.4168),(23,'2016-08-01',6927.25,293.39,0.2207,64.7512),(24,'2016-09-01',7136.32,209.07,0.2207,46.1417),(25,'2016-10-01',7414.94,278.62,0.2207,61.4915),(26,'2016-11-01',7748.1,333.16,0.2207,73.5284),(27,'2016-12-01',8103.06,354.96,0.2207,78.3397),(28,'2017-01-01',8489.99,386.93,0.2207,85.3955),(29,'2017-02-01',8857.39,367.399,0.2207,81.0851),(30,'2017-03-01',9175.42,318.03,0.2207,70.1893),(31,'2017-04-01',9514.86,339.44,0.2207,74.9145),(32,'2017-05-01',9835.64,320.779,0.2207,70.796),(33,'2017-05-31',10117.4,281.721,0.2207,62.1758),(34,'2017-07-01',10393.3,275.93,0.2463,67.9615),(35,'2017-08-08',10680.4,287.14,0.2463,70.7225),(36,'2017-09-01',10922.6,242.13,0.2463,59.6366),(37,'2017-10-01',11227.6,305.08,0.2463,75.1412),(38,'2017-11-01',11551.5,323.86,0.2463,79.7668),(39,'2017-12-01',11911.8,360.35,0.2463,88.7541),(40,'2018-01-01',12336.7,424.931,0.2463,104.66),(41,'2018-02-01',12731.8,395.02,0.2463,97.2933),(42,'2018-03-01',13058.8,327.08,0.2463,80.5598),(43,'2018-04-01',13404.3,345.45,0.2463,85.0844),(44,'2018-05-01',13638.1,233.83,0.2463,57.5923),(45,'2018-06-01',13952,313.899,0.2463,77.3134),(46,'2018-07-01',14225.9,273.841,0.2463,67.447),(47,'2018-08-01',14472.1,246.279,0.2463,60.6586),(48,'2018-09-01',14755.8,283.681,0.2463,69.8705),(49,'2018-10-01',15065.4,309.62,0.2463,76.2594),(50,'2018-11-01',15407.1,341.64,0.2463,84.1458),(51,'2018-12-01',15778.3,371.18,0.2463,91.4216),(52,'2019-01-01',16183.7,405.4,0.2463,99.8501),(53,'2019-02-01',16582.4,398.789,0.2463,98.2217),(54,'2019-03-01',16929.1,346.66,0.2463,85.3824),(55,'2019-04-01',17274.7,345.561,0.2463,85.1116);
/*!40000 ALTER TABLE `stromsonst` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`python_user`@`%`*/ /*!50003 TRIGGER `calcStrINS` BEFORE INSERT ON `stromsonst` FOR EACH ROW BEGIN
    DECLARE lastrow, secondlastrow, secondlastid INT(11) DEFAULT 0;
    DECLARE secondlastzst, checkvbr FLOAT DEFAULT 0;
    SET lastrow = (select count(*) from stromsonst);
    SET secondlastrow = lastrow - 1;
    SET secondlastid = (SELECT id FROM stromsonst LIMIT secondlastrow,1);
    SET secondlastzst = (SELECT zaehlerstand FROM stromsonst WHERE id=secondlastid);
    SET checkvbr = (NEW.zaehlerstand - secondlastzst);
    IF (checkvbr > 0) THEN
      SET NEW.verbrauch=checkvbr;
    ELSE
      SET NEW.verbrauch = 0;
    END IF;
    SET NEW.kosten=NEW.verbrauch*NEW.preis;
  END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `waermepumpe`
--

DROP TABLE IF EXISTS `waermepumpe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `waermepumpe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datum` date NOT NULL,
  `zaehlerstand` float NOT NULL,
  `verbrauch` float DEFAULT '0',
  `preis` float(4,4) NOT NULL,
  `kosten` float DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `waermepumpe`
--

LOCK TABLES `waermepumpe` WRITE;
/*!40000 ALTER TABLE `waermepumpe` DISABLE KEYS */;
INSERT INTO `waermepumpe` VALUES (1,'2015-01-01',2995.42,0,0.1872,0),(2,'2015-02-01',3392.86,397.44,0.1872,74.4008),(3,'2015-03-01',3861.31,468.45,0.1872,87.6938),(4,'2015-04-01',4228.05,366.74,0.1872,68.6537),(5,'2015-05-01',4454.82,226.77,0.1872,42.4513),(6,'2015-06-01',4547.57,92.75,0.1872,17.3628),(7,'2015-07-01',4633.15,85.5801,0.1872,16.0206),(8,'2015-08-01',4692.64,59.4902,0.1872,11.1366),(9,'2015-09-01',4766.11,73.4697,0.1872,13.7535),(10,'2015-10-01',4866.95,100.84,0.1872,18.8773),(11,'2015-11-01',5079.06,212.11,0.1872,39.707),(12,'2015-12-01',5350.29,271.23,0.1872,50.7743),(13,'2016-01-01',5664.02,313.73,0.1872,58.7303),(14,'2016-02-01',6150.3,486.28,0.1872,91.0316),(15,'2016-03-01',6585.24,434.94,0.1903,82.7692),(16,'2016-04-01',6961.4,376.16,0.1903,71.5832),(17,'2016-05-01',7197.97,236.57,0.1903,45.0193),(18,'2016-06-01',7317.47,119.5,0.1903,22.7409),(19,'2016-07-01',7402.64,85.1699,0.1903,16.2078),(20,'2016-08-01',7492.49,89.8501,0.1903,17.0985),(21,'2016-09-01',7558.12,65.6299,0.1903,12.4894),(22,'2016-10-01',7638.58,80.46,0.1903,15.3115),(23,'2016-11-01',7890.4,251.82,0.1903,47.9213),(24,'2016-12-01',8290.88,400.48,0.1903,76.2113),(25,'2017-01-01',8775.17,484.29,0.1903,92.1604),(26,'2017-02-01',9422.65,647.48,0.1903,123.216),(27,'2017-03-01',9778.71,356.06,0.1903,67.7581),(28,'2017-04-01',10076.4,297.65,0.1903,56.6429),(29,'2017-05-01',10327.3,250.949,0.1903,47.7556),(30,'2017-05-31',10436.8,109.511,0.1903,20.8399),(31,'2017-07-01',10508.3,71.4395,0.1903,13.5949),(32,'2017-08-08',10581.6,73.3301,0.1903,13.9547),(33,'2017-09-01',10643.1,61.5303,0.1903,11.7092),(34,'2017-10-01',10738,94.9102,0.1903,18.0614),(35,'2017-11-01',10865.5,127.46,0.1903,24.2556),(36,'2017-12-01',11155.2,289.75,0.1903,55.1394),(37,'2018-01-01',11572.6,417.43,0.1903,79.4369),(38,'2018-02-01',11971.2,398.54,0.1903,75.8422),(39,'2018-03-01',12522.1,550.92,0.1903,104.84),(40,'2018-04-01',12882.9,360.78,0.1903,68.6565),(41,'2018-05-01',12963.9,81.0498,0.1903,15.4238),(42,'2018-06-01',13049.5,85.5605,0.1903,16.2822),(43,'2018-07-01',13117.8,68.29,0.1903,12.9956),(44,'2018-08-01',13171.5,53.6699,0.1903,10.2134),(45,'2018-09-01',13225.7,54.29,0.1903,10.3314),(46,'2018-10-01',13318.1,92.3994,0.1903,17.5836),(47,'2018-11-01',13475.1,157,0.1903,29.8771),(48,'2018-12-01',13790.9,315.721,0.1903,60.0816),(49,'2019-01-01',14175.7,384.88,0.1903,73.2426),(50,'2019-02-01',14692.3,516.609,0.1903,98.3108),(51,'2019-03-01',15034.9,342.551,0.1903,65.1874),(52,'2019-04-01',15309.8,274.859,0.1903,52.3057);
/*!40000 ALTER TABLE `waermepumpe` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`python_user`@`%`*/ /*!50003 TRIGGER `calcWPINS` BEFORE INSERT ON `waermepumpe` FOR EACH ROW BEGIN
    DECLARE lastrow, secondlastrow, secondlastid INT(11) DEFAULT 0;
    DECLARE secondlastzst, checkvbr FLOAT DEFAULT 0;
    SET lastrow = (select count(*) from waermepumpe);
    SET secondlastrow = lastrow - 1;
    SET secondlastid = (SELECT id FROM waermepumpe LIMIT secondlastrow,1);
    SET secondlastzst = (SELECT zaehlerstand FROM waermepumpe WHERE id=secondlastid);
    SET checkvbr = (NEW.zaehlerstand - secondlastzst);
    IF (checkvbr > 0) THEN
      SET NEW.verbrauch=checkvbr;
    ELSE
      SET NEW.verbrauch = 0;
    END IF;
    SET NEW.kosten=NEW.verbrauch*NEW.preis;
  END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `wasser`
--

DROP TABLE IF EXISTS `wasser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wasser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `datum` date NOT NULL,
  `zaehlerstand` float NOT NULL,
  `verbrauch` float DEFAULT '0',
  `preis` float NOT NULL,
  `kosten` float DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wasser`
--

LOCK TABLES `wasser` WRITE;
/*!40000 ALTER TABLE `wasser` DISABLE KEYS */;
INSERT INTO `wasser` VALUES (1,'2015-01-01',55,10,1.8032,18.032),(2,'2015-02-01',65,10,1.8032,18.032),(3,'2015-03-01',75,10,1.8032,18.032),(10,'2015-04-01',85,10,1.8032,18.032),(11,'2015-05-01',95,10,1.8032,18.032),(12,'2015-06-01',105,10,1.8032,18.032),(16,'2015-07-01',115,10,1.8032,18.032),(17,'2015-08-01',122,7,1.8032,12.6224),(18,'2015-09-01',134,12,1.8032,21.6384),(19,'2015-10-01',145,11,1.8032,19.8352),(20,'2015-11-01',156,11,1.8032,19.8352),(21,'2015-12-01',167,11,1.8032,19.8352),(22,'2016-01-01',179,12,1.8032,21.6384),(24,'2016-02-01',191,12,1.8032,21.6384),(25,'2016-03-01',202,11,1.8032,19.8352),(26,'2016-04-01',214,12,1.8032,21.6384),(27,'2016-05-01',227,13,1.8032,23.4416),(28,'2016-06-01',240,13,1.8032,23.4416),(29,'2016-07-01',252,12,1.8032,21.6384),(30,'2016-08-01',264,12,1.8032,21.6384),(31,'2016-09-01',274,10,1.8032,18.032),(32,'2016-10-01',285,11,1.8032,19.8352),(33,'2016-11-01',298,13,1.8032,23.4416),(34,'2016-12-01',310,12,1.8032,21.6384),(35,'2017-01-01',322,12,1.8032,21.6384),(36,'2017-02-01',334,12,1.8032,21.6384),(37,'2017-03-01',346,12,1.8032,21.6384),(38,'2017-04-01',358,12,1.8032,21.6384),(39,'2017-05-01',370,12,1.8032,21.6384),(40,'2017-05-31',383,13,1.8032,23.4416),(41,'2017-07-01',395,12,1.8032,21.6384),(42,'2017-08-08',405,10,1.8032,18.032),(43,'2017-09-01',415,10,1.8032,18.032),(44,'2017-10-01',426,11,1.8032,19.8352),(45,'2017-11-01',439,13,1.8032,23.4416),(46,'2017-12-01',450,11,1.8032,19.8352),(47,'2018-01-01',463,13,1.8032,23.4416),(48,'2018-02-01',476,13,1.8032,23.4416),(49,'2018-03-01',487,11,1.8032,19.8352),(50,'2018-04-01',497,10,1.8032,18.032),(51,'2018-05-01',507,10,1.8032,18.032),(52,'2018-06-01',521,14,1.8032,25.2448),(53,'2018-07-01',533,12,1.8032,21.6384),(54,'2018-08-01',541,8,1.8032,14.4256),(55,'2018-09-01',554,13,1.8032,23.4416),(56,'2018-10-01',567,13,1.8032,23.4416),(57,'2018-11-01',579,12,1.8032,21.6384),(58,'2018-12-01',591,12,1.8032,21.6384),(59,'2019-01-01',603,12,1.8032,21.6384),(60,'2019-02-01',616,13,1.8032,23.4416),(61,'2019-03-01',628,12,1.8032,21.6384),(62,'2019-04-01',640,12,1.8032,21.6384);
/*!40000 ALTER TABLE `wasser` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8 */ ;
/*!50003 SET character_set_results = utf8 */ ;
/*!50003 SET collation_connection  = utf8_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`python_user`@`%`*/ /*!50003 TRIGGER `calcWasserINS` BEFORE INSERT ON `wasser` FOR EACH ROW BEGIN
    DECLARE lastrow, secondlastrow, secondlastid INT(11) DEFAULT 0;
    DECLARE secondlastzst, checkvbr FLOAT DEFAULT 0;
    SET lastrow = (select count(*) from wasser);
    SET secondlastrow = lastrow - 1;
    SET secondlastid = (SELECT id FROM wasser LIMIT secondlastrow,1);
    SET secondlastzst = (SELECT zaehlerstand FROM wasser WHERE id=secondlastid);
    SET checkvbr = (NEW.zaehlerstand - secondlastzst);
    IF (checkvbr > 0) THEN
      SET NEW.verbrauch=checkvbr;
    ELSE
      SET NEW.verbrauch = 0;
    END IF;
    SET NEW.kosten=NEW.verbrauch*NEW.preis;
  END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-10-20 20:57:53
