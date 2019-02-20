/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50724
Source Host           : localhost:3306
Source Database       : bilibili

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2019-02-18 00:05:59
*/

SET FOREIGN_KEY_CHECKS=0;
-- ----------------------------
-- Table structure for `bilibili_video_message`
-- ----------------------------
DROP TABLE IF EXISTS `bilibili_video_message`;
CREATE TABLE `bilibili_video_message` (
  `aid` int(25) NOT NULL,
  `title` varchar(100) DEFAULT NULL,
  `tname` varchar(45) DEFAULT NULL,
  `videos` int(25) DEFAULT NULL,
  `Introduction` varchar(300) DEFAULT NULL,
  `dynamic` varchar(100) DEFAULT NULL,
  `allow_submit` varchar(45) DEFAULT NULL,
  `ctime` varchar(45) DEFAULT NULL,
  `coin` int(30) DEFAULT NULL,
  `danmaku` int(30) DEFAULT NULL,
  `favorite` int(30) DEFAULT NULL,
  `v_like` int(30) DEFAULT NULL,
  `reply` int(30) DEFAULT NULL,
  `share` int(30) DEFAULT NULL,
  `view` int(30) DEFAULT NULL,
  PRIMARY KEY (`aid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of bilibili_video_message
-- ----------------------------
INSERT INTO `bilibili_video_message` VALUES ('43224826', '【偶像大师百万现场MLTD MV】「dear...」(白き鶴の如くSSR) 1080p60 2xFXAA', '手机游戏', '2', '马场阿姨带齐亲朋戚友给你拜年啦!!!  3840x2160 @60FPS  2xMSAA「dear...」(白き鶴の如くSSR)  https://youtu.be/t0SDX_seu48  nico 1080p :  https://www.nicovideo.jp/watch/sm34615305  歌：  馬場このみ(高橋未奈美)     作詞：KOH  作曲：KOH', '#手机游戏##偶像大师##偶像大师百万##MLTD##马场木实##馬場このみ##高橋未奈美#', 'False', '2019-02-11 17:10:26', '118', '0', '100', '108', '56', '56', '1819');
