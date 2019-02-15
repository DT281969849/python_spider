/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50724
Source Host           : localhost:3306
Source Database       : bilibili

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2019-02-15 14:39:42
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `bilibili_user`
-- ----------------------------
DROP TABLE IF EXISTS `bilibili_user`;
CREATE TABLE `bilibili_user` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `mid` int(20) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `sex` varchar(45) DEFAULT NULL,
  `rank` varchar(45) DEFAULT NULL,
  `level` varchar(45) DEFAULT NULL,
  `fan_badge` varchar(45) DEFAULT NULL,
  `jointime` varchar(45) DEFAULT NULL,
  `moral` varchar(20) DEFAULT NULL,
  `sign` varchar(300) DEFAULT NULL,
  `face` varchar(200) DEFAULT NULL,
  `vip_status` varchar(45) DEFAULT NULL,
  `vip_type` varchar(45) DEFAULT NULL,
  `coins` int(20) DEFAULT NULL,
  `silence` int(20) DEFAULT NULL,
  `theme` varchar(45) DEFAULT NULL,
  `following` int(20) DEFAULT NULL,
  `black` int(20) DEFAULT NULL,
  `follower` int(20) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of bilibili_user
-- ----------------------------
