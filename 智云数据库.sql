-- --------------------------------------------------------
-- 主机:                          
-- 服务器版本:                        8.0.33 - MySQL Community Server - GPL
-- 服务器操作系统:                      Linux
-- HeidiSQL 版本:                  12.5.0.6677
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- 导出 wlw 的数据库结构
CREATE DATABASE IF NOT EXISTS `wlw` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `wlw`;

-- 导出  表 wlw.itme 结构
CREATE TABLE IF NOT EXISTS `itme` (
  `id` int NOT NULL,
  `clientid` char(6) NOT NULL,
  `topic` text NOT NULL,
  `ip` text NOT NULL,
  `name` char(11) NOT NULL DEFAULT '新设备',
  PRIMARY KEY (`id`),
  UNIQUE KEY `clientid` (`clientid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 正在导出表  wlw.itme 的数据：~21 rows (大约)
INSERT INTO `itme` (`id`, `clientid`, `topic`, `ip`, `name`) VALUES
	(1119, '虎', '㎡r', 'null', '的'),
	(1254, '㎜说此', '我', 'null', '、加办'),
	(1557, '1', '、r', 'null', '叫'),
	(1735, '‘㎡', '凯', 'null', '㎡'),
	(1811, '罗', '有一个吧', 'null', '给个红包吧'),
	(2145, '咖', '䄻', 'null', '睡'),
	(2245, 'zjsj', 'xgzhhz', 'null', 'shsjsk'),
	(2465, '.VI', '`叭', 'null', '、㎜'),
	(2672, '1884', '疏散', 'null', '这是谁家'),
	(4356, '0Ⅷ', '〈嘹', 'null', 'cplm'),
	(6550, 'zz', 'zz', 'null', '电脑'),
	(6584, '耀', '〈㎎一ucTr', 'null', '㎡yu'),
	(6766, 'tan', '矿', 'null', '..CQm'),
	(7119, 'car', '燃', 'null', '吡'),
	(7535, 'qqqaaa', 'ddx', 'null', 'aaa'),
	(8327, '江西信息应用', 'aads', 'null', '世界经济家'),
	(9333, '、an', '嗯', 'null', 'cmccw'),
	(9477, 'nm', 'nua', 'null', 'mcm'),
	(9530, '郗', '饥', 'null', '断'),
	(9561, '泓。↗匕↙', 'aiur', 'null', '谈'),
	(9955, '啊啊啊', '滚滚滚', 'null', '好尴尬');

-- 导出  表 wlw.view 结构
CREATE TABLE IF NOT EXISTS `view` (
  `view` text NOT NULL,
  `gn` text NOT NULL,
  `viewid` int NOT NULL,
  `id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `clientid` (`viewid`),
  CONSTRAINT `view_ibfk_1` FOREIGN KEY (`viewid`) REFERENCES `itme` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- 正在导出表  wlw.view 的数据：~57 rows (大约)
INSERT INTO `view` (`view`, `gn`, `viewid`, `id`) VALUES
	('Button', 'ss', 6550, 1072),
	('Button', 'ss', 6550, 1388),
	('Button', 'ss', 1557, 2419),
	('Button', 'ss', 1557, 2429),
	('Button', 'ss', 6550, 2575),
	('Button', 'ss', 6766, 2588),
	('Button', 'ss', 1557, 2640),
	('Button', 'ss', 6550, 2675),
	('Button', 'ss', 9955, 2697),
	('Button', 'ss', 1557, 2744),
	('Button', 'ss', 9955, 2747),
	('Button', 'ss', 1735, 3055),
	('Button', 'ss', 1735, 3193),
	('Button', 'ss', 9477, 3469),
	('Button', 'ss', 1557, 3582),
	('Button', 'ss', 1735, 3679),
	('Button', 'ss', 7535, 3948),
	('Button', 'ss', 9955, 4092),
	('Button', 'ss', 9477, 4093),
	('Button', 'ss', 1557, 4254),
	('Button', 'ss', 1557, 4351),
	('Button', 'ss', 1735, 4523),
	('Button', 'ss', 6766, 4585),
	('Button', 'ss', 1557, 5000),
	('Button', 'ss', 1557, 5262),
	('Button', 'ss', 9955, 5502),
	('Button', 'ss', 1557, 5780),
	('Button', 'ss', 1557, 5873),
	('Button', 'ss', 1557, 5949),
	('Button', 'ss', 1557, 6070),
	('Button', 'ss', 6550, 6162),
	('Button', 'ss', 1557, 6240),
	('Button', 'ss', 6550, 6420),
	('Button', 'ss', 1557, 6716),
	('Button', 'ss', 1735, 6806),
	('Button', 'ss', 9477, 7023),
	('Button', 'ss', 9955, 7117),
	('Button', 'ss', 1557, 7239),
	('Button', 'ss', 1557, 7611),
	('Button', 'ss', 1557, 7741),
	('Button', 'ss', 9955, 7868),
	('Button', 'ss', 1557, 8059),
	('Button', 'ss', 1735, 8123),
	('Button', 'ss', 6550, 8161),
	('Button', 'ss', 1735, 8213),
	('Button', 'ss', 1735, 8260),
	('Button', 'ss', 1735, 8299),
	('Button', 'ss', 1557, 8327),
	('Button', 'ss', 1557, 8465),
	('Button', 'ss', 9955, 8575),
	('Button', 'ss', 6550, 8966),
	('Button', 'ss', 1557, 9029),
	('Button', 'ss', 1557, 9237),
	('Button', 'ss', 6550, 9375),
	('Button', 'ss', 1557, 9418),
	('Button', 'ss', 1557, 9909),
	('Button', 'ss', 1557, 9928);

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
