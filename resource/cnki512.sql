/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50729
Source Host           : localhost:3306
Source Database       : cnki

Target Server Type    : MYSQL
Target Server Version : 50729
File Encoding         : 65001

Date: 2021-05-13 11:18:50
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL COMMENT '链接',
  `title` varchar(255) NOT NULL COMMENT '标题',
  `summary` varchar(255) DEFAULT NULL COMMENT '摘要',
  `keywords` varchar(255) DEFAULT NULL,
  `date` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '发表日期',
  `status` int(1) unsigned zerofill DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for author
-- ----------------------------
DROP TABLE IF EXISTS `author`;
CREATE TABLE `author` (
  `id` int(11) NOT NULL,
  `url` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `major` varchar(255) DEFAULT NULL,
  `sum_publish` int(11) DEFAULT NULL,
  `sum_download` int(11) DEFAULT NULL,
  `status` int(1) unsigned zerofill DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for organization
-- ----------------------------
DROP TABLE IF EXISTS `organization`;
CREATE TABLE `organization` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `used_name` varchar(255) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  `status` int(1) unsigned zerofill DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for re_article_author
-- ----------------------------
DROP TABLE IF EXISTS `re_article_author`;
CREATE TABLE `re_article_author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url_article` varchar(255) DEFAULT NULL,
  `url_author` varchar(255) DEFAULT NULL,
  `status` int(1) unsigned zerofill DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=591 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for re_article_source
-- ----------------------------
DROP TABLE IF EXISTS `re_article_source`;
CREATE TABLE `re_article_source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url_article` varchar(255) DEFAULT NULL,
  `url_source` varchar(255) DEFAULT NULL,
  `status` int(1) unsigned zerofill DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=111 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for re_author_organization
-- ----------------------------
DROP TABLE IF EXISTS `re_author_organization`;
CREATE TABLE `re_author_organization` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url_zuthor` varchar(255) DEFAULT NULL,
  `url_organization` varchar(255) DEFAULT NULL,
  `status` int(1) unsigned zerofill DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for re_teacher_student
-- ----------------------------
DROP TABLE IF EXISTS `re_teacher_student`;
CREATE TABLE `re_teacher_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url_teacher` varchar(255) DEFAULT NULL,
  `url_student` varchar(255) DEFAULT NULL,
  `status` int(1) unsigned zerofill DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for source
-- ----------------------------
DROP TABLE IF EXISTS `source`;
CREATE TABLE `source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `basic_info` varchar(255) DEFAULT NULL,
  `publish_info` varchar(255) DEFAULT NULL,
  `evaluation` varchar(255) DEFAULT NULL,
  `status` int(1) unsigned zerofill DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
