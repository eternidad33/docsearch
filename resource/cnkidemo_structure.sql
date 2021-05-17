/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50729
Source Host           : localhost:3306
Source Database       : cnkidemo

Target Server Type    : MYSQL
Target Server Version : 50729
File Encoding         : 65001

Date: 2021-05-17 10:18:13
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `url` varchar(255) NOT NULL COMMENT '链接，主键',
  `title` varchar(255) NOT NULL COMMENT '标题',
  `summary` mediumtext COMMENT '摘要',
  `keywords` varchar(255) DEFAULT NULL COMMENT '关键词',
  `date` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT '发表日期',
  `status` int(1) unsigned zerofill DEFAULT '0' COMMENT '0代表未导入neo4j，1代表已导入，其他表类似',
  PRIMARY KEY (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='文章';

-- ----------------------------
-- Table structure for author
-- ----------------------------
DROP TABLE IF EXISTS `author`;
CREATE TABLE `author` (
  `url` varchar(255) NOT NULL COMMENT '链接，主键',
  `name` varchar(255) NOT NULL COMMENT '姓名',
  `major` varchar(255) DEFAULT NULL COMMENT '专业',
  `sum_publish` int(11) DEFAULT NULL COMMENT '总发布量',
  `sum_download` int(11) DEFAULT NULL COMMENT '总下载量',
  `status` int(1) unsigned zerofill DEFAULT '0',
  PRIMARY KEY (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='作者';

-- ----------------------------
-- Table structure for organization
-- ----------------------------
DROP TABLE IF EXISTS `organization`;
CREATE TABLE `organization` (
  `url` varchar(255) NOT NULL COMMENT '链接，主键',
  `name` varchar(255) NOT NULL COMMENT '名称',
  `used_name` varchar(255) DEFAULT NULL COMMENT '曾用名',
  `region` varchar(255) DEFAULT NULL COMMENT '区域',
  `website` varchar(255) DEFAULT NULL COMMENT '官网',
  `status` int(1) unsigned zerofill DEFAULT '0',
  PRIMARY KEY (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='组织';

-- ----------------------------
-- Table structure for re_article_author
-- ----------------------------
DROP TABLE IF EXISTS `re_article_author`;
CREATE TABLE `re_article_author` (
  `url_article` varchar(255) NOT NULL,
  `url_author` varchar(255) NOT NULL,
  `status` int(1) unsigned zerofill DEFAULT '0',
  PRIMARY KEY (`url_article`,`url_author`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='文献-作者';

-- ----------------------------
-- Table structure for re_article_source
-- ----------------------------
DROP TABLE IF EXISTS `re_article_source`;
CREATE TABLE `re_article_source` (
  `url_article` varchar(255) NOT NULL,
  `url_source` varchar(255) NOT NULL,
  `status` int(1) unsigned zerofill DEFAULT '0',
  PRIMARY KEY (`url_article`,`url_source`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='文献-来源';

-- ----------------------------
-- Table structure for re_author_organization
-- ----------------------------
DROP TABLE IF EXISTS `re_author_organization`;
CREATE TABLE `re_author_organization` (
  `url_author` varchar(255) NOT NULL COMMENT '一个作者只有一个组织，主键',
  `url_organization` varchar(255) DEFAULT NULL COMMENT '机构链接',
  `status` int(1) unsigned zerofill DEFAULT '0',
  PRIMARY KEY (`url_author`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='作者-组织';

-- ----------------------------
-- Table structure for re_teacher_student
-- ----------------------------
DROP TABLE IF EXISTS `re_teacher_student`;
CREATE TABLE `re_teacher_student` (
  `url_teacher` varchar(255) NOT NULL,
  `url_student` varchar(255) NOT NULL,
  `status` int(1) unsigned zerofill DEFAULT '0',
  PRIMARY KEY (`url_teacher`,`url_student`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='老师-学生';

-- ----------------------------
-- Table structure for source
-- ----------------------------
DROP TABLE IF EXISTS `source`;
CREATE TABLE `source` (
  `url` varchar(255) NOT NULL COMMENT '链接，主键',
  `name` varchar(255) DEFAULT NULL COMMENT '名称',
  `basic_info` varchar(255) DEFAULT NULL COMMENT '基本信息',
  `publish_info` varchar(255) DEFAULT NULL COMMENT '出版信息',
  `evaluation` mediumtext COMMENT '评价信息',
  `status` int(1) unsigned zerofill DEFAULT '0',
  PRIMARY KEY (`url`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='来源';
