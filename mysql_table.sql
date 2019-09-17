SET NAMES utf8;
SET time_zone = '+00:00';

DROP DATABASE IF EXISTS `management_db`;
CREATE DATABASE `management_db` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `management_db`;

DROP TABLE IF EXISTS `APP_RCPT_M`; 
CREATE TABLE `APP_RCPT_M` (
  `APPLICATIONVERSION` varchar(30) NOT NULL,
  `EMAIL_LIST` varchar(1000) NOT NULL,
  KEY `APPLICATIONVERSION` (`APPLICATIONVERSION`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `BATCH_LIST`;
CREATE TABLE `BATCH_LIST` (
  `APPLICATIONVERSION` varchar(30) NOT NULL,
  `EMAIL_LIST` varchar(1000) NOT NULL,
  KEY `APPLICATIONVERSION` (`APPLICATIONVERSION`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `ISSUE`;
CREATE TABLE `ISSUE` (
  `APPLICATIONVERSION` varchar(30) NOT NULL,
  `TOTAL_ISSUE` int(7) NOT NULL,
  `NEW_ISSUE` int(7) NOT NULL,
  PRIMARY KEY (`APPLICATIONVERSION`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `U_MASTER`;
CREATE TABLE `U_MASTER` (
  `DOMAIN` varchar(2) NOT NULL,
  `EMP_CODE` varchar(5) NOT NULL,
  `EMP_NM` varchar(30) NOT NULL,
  `DEPT_CD` varchar(5) NOT NULL,
  `DEPT_NM` varchar(30) NOT NULL,
  `EMAIL` varchar(50) DEFAULT NULL,
  `MOBILE` varchar(13) DEFAULT NULL,
  `EMP_GUBUN` varchar(10) NOT NULL,
  `LAST_WORK_YMD` date DEFAULT NULL,
  `STATUS_NM` varchar(10) NOT NULL,
  `LEADER_SABUN` varchar(5) DEFAULT NULL,
  `LEADER_NAME` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`EMP_CODE`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `ISSUE_LIST`;
CREATE TABLE `ISSUE_LIST` (
  `IID` varchar(32) NOT NULL PRIMARY KEY,
  `ISSUE_NAME` varchar(100) NOT NULL,
  `CRITICALITY` varchar(30) NOT NULL,
  `PATH` varchar(1000) NOT NULL,
  `FILENAME` varchar(256) NOT NULL,
  `LINE` int(7) NOT NULL,
  `SOURCE` varchar(256) DEFAULT NULL,
  `SOURCE_LINE` int(7) DEFAULT NULL,
  `APPLICATIONVERSION` varchar(30) DEFAULT NULL,
  `COMMENT` varchar(1000) DEFAULT NULL, 
    KEY `IID` (`IID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

USE `management_db`;

DROP TABLE IF EXISTS `APP_RCPT_M`;
CREATE TABLE `APP_RCPT_M` (
  `APPLICATIONVERSION` varchar(30) NOT NULL,
  `EMAIL_LIST` varchar(1000) NOT NULL,
  `JIRA_NO` varchar(30),
  `ASSIGNER` varchar(30),
  KEY `APPLICATIONVERSION` (`APPLICATIONVERSION`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `APP_RCPT_M` (`APPLICATIONVERSION`, `EMAIL_LIST`,`JIRA_NO`,`ASSIGNER`) VALUES
('wms',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('세일즈원방송',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('MC회원',	'park.jh@gsshop.com, jsunsam@it.gsshop.com','',''),
('안드로이드APP',	'park.jh@gsshop.com, jsunsam@it.gsshop.com','',''),
('MC보험몰',	'park.jh@gsshop.com, jsunsam@it.gsshop.com','',''),
('컴퍼니사이트',	'park.jh@gsshop.com, jsunsam@it.gsshop.com','',''),
('위드넷',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('데이터홈쇼핑',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('MC단품',	'park.jh@gsshop.com, jsunsam@it.gsshop.com','',''),
('MC주문',	'park.jh@gsshop.com, jsunsam@it.gsshop.com','',''),
('세일즈원방송실시간',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('MC공통',	'park.jh@gsshop.com, jsunsam@it.gsshop.com','',''),
('MC매장',	'park.jh@gsshop.com, jsunsam@it.gsshop.com','',''),
('상품정보방-서버',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('EC분석',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('모바일세일즈원-클라이언트',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('상품정보방-클라이언트',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('모바일세일즈원-서버',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('annapurna',	'park.jh@gsshop.com, soonkee@gsshop.com','',''),
('smart4c',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('BI포털',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('통합보험',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('EC어드민',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('manaslu',	'park.jh@gsshop.com, soonkee@gsshop.com','',''),
('Azalea',	'park.jh@gsshop.com, kang.tw@gsshop.com','',''),
('PC공통',	'park.jh@gsshop.com, jsunsam@it.gsshop.com','',''),
('Begonia',	'park.jh@gsshop.com, kang.tw@gsshop.com','',''),
('Crocus',	'park.jh@gsshop.com, kang.tw@gsshop.com','',''),
('구ecb2bAPI',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('전자전표',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('btob',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('MC구조개선',	'park.jh@gsshop.com, jsunsam@it.gsshop.com','',''),
('menu-mon',	'park.jh@gsshop.com, kk.lim@gsshop.com','',''),
('data-provider',	'park.jh@gsshop.com, kk.lim@gsshop.com','',''),
('csp-core',	'park.jh@gsshop.com, kk.lim@gsshop.com','',''),
('신ecb2bAPI',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('노스페이스',	'park.jh@gsshop.com','',''),
('NIKE-CTM',	'park.jh@gsshop.com','',''),
('smart4c-batch',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','',''),
('trendmon',	'park.jh@gsshop.com, kk.lim@gsshop.com','',''),
('cg-mon',	'park.jh@gsshop.com, kk.lim@gsshop.com','',''),
('csp-export',	'park.jh@gsshop.com, kk.lim@gsshop.com','',''),
('법틀',	'park.jh@gsshop.com, you.wd@gsshop.com','',''),
('인사',	'park.jh@gsshop.com, kpk418@it.gsshop.com, phs0926@it.gsshop.com','','')
ON DUPLICATE KEY UPDATE `APPLICATIONVERSION` = VALUES(`APPLICATIONVERSION`), `EMAIL_LIST` = VALUES(`EMAIL_LIST`);

