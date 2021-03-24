/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50729
Source Host           : localhost:3306
Source Database       : cnki

Target Server Type    : MYSQL
Target Server Version : 50729
File Encoding         : 65001

Date: 2021-03-24 11:09:01
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) DEFAULT NULL COMMENT '链接，存储格式为FileName=值1&DbName=值2&DbCode=值3&',
  `title` varchar(255) DEFAULT NULL COMMENT '标题',
  `summary` mediumtext COMMENT '摘要',
  `keyss` mediumtext COMMENT '关键词',
  `funds` mediumtext COMMENT '资助机构',
  `doi` varchar(255) DEFAULT NULL COMMENT 'DOI，指数字对象唯一标识符，是云计算背景下最佳的“大数据”样本存储和应用技术，用于IKE进行协商SA协议统一分配。',
  `album` varchar(255) DEFAULT NULL COMMENT '专辑',
  `special` varchar(255) DEFAULT NULL COMMENT '专题',
  `classNo` varchar(255) DEFAULT NULL COMMENT '分类号',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=310 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of article
-- ----------------------------
INSERT INTO `article` VALUES ('279', 'FileName=XAJD20210319000&DbName=CAPJLAST&DbCode=CAPJ&', '刑事审判人工智能的权力逻辑', '刑事智能办案系统是人工智能技术进入刑事司法场域中的主要表现形式。当前，刑事智能办案系统主要集中在证据审查判断、辅助精准量刑、类案推送和案件偏离预警等领域。随着人工智能技术与刑事司法的深度融合，人的“代具性”原理、自动化偏差认知机制、国家权力的背书与支持、技术外包的研发模式以及系统架构的运行机制等因素推动着智能办案系统从“工具”向“权力”的演化。同时，刑事审判中人工智能技术的权力化可能会引发规训风险、排斥风险与误判风险。为了有效规避刑事审判场域中人工智能技术引发的正当性风险，应当树立权力规制理念，从智能办案系统的适用机制、参与机制以及研发机制三方面进行规制。', '[\"刑事审判\", \"人工智能\", \"技术权力\", \"智能办案\", \"正当程序\", \"司法裁判权\"]', '[\"教育部规划基金项目（19YJA820004）\"]', 'None', '社会科学Ⅰ辑; 信息科技', '诉讼法与司法制度; 自动化技术', 'TP18;D925.2');
INSERT INTO `article` VALUES ('280', 'FileName=YXXB20210319003&DbName=CAPJLAST&DbCode=CAPJ&', '人工智能在基于配体和受体结构的药物筛选中的应用进展', '人工智能技术在药物筛选中的应用日益广泛。本文介绍了人工智能技术的特点，着重从机器学习尤其是深度学习角度，按照基于配体和受体结构两个方面，总结了人工智能技术在药物筛选中的应用和进展，以及如何应用人工智能从这两个方面进行药物设计。本文也讨论了人工智能技术在药物虚拟筛选领域的主要局限性和挑战，对其发展前景作以展望。', '[\"人工智能\", \"虚拟筛选\", \"计算机辅助药物设计\", \"药理学\"]', '[\"国家重大新药创制科技重大专项（2018ZX09711001-012）\", \"中国医学科学院医学与健康科技创新工程（2020-I2M-1-003）\"]', '10.16438/j.0513-4870.2021-0052', '医药卫生科技; 信息科技', '药学; 自动化技术', 'R965.1;TP18');
INSERT INTO `article` VALUES ('281', 'FileName=GRKZ202103019&DbName=CJFDAUTO&DbCode=CJFD&', '智能机器人在新冠肺炎疫情期间的应用探索', '科学日新月异,人工智能、高速网络、精准控制、自动化技术不断发展,智能机器人的应用已日趋成熟,逐步走进生活的各个领域。2019年12月以来,新型冠状病毒肆虐全球,人类抗击疫情,直面病毒的高传染性、感染后较高的致死率,以及社会恐慌等各种挑战。随着科学技术发展和医疗需求的变化,发现智能机器人应用于医疗领域,可以减轻医护人员的工作负担,减少交叉感染的风险;用于科普及防控宣传,可以增加全社会对疾病的认知,减少社会的恐慌。智能机器人与医疗技术的有效结合能达到科学抗疫1加1大于2的效果,具有极大的应用前景,能顺应社会的需求。', '[\"智能机器人\", \"机器人治疗与采样\", \"人工智能\", \"新型冠状病毒\", \"新冠肺炎\", \"COVID-19\"]', '[\"国家自然科学基金资助项目（62041302）\", \"广东省科技厅科技创新战略专项（2020B111126005）\", \"广州市科技创新发展专项资金（2060901）\"]', 'None', '医药卫生科技; 基础科学; 信息科技', '生物学; 生物医学工程; 自动化技术', 'TP242.6;R318');
INSERT INTO `article` VALUES ('282', 'FileName=XDTQ20210319001&DbName=CAPJLAST&DbCode=CAPJ&', '基于人才知识图谱推理的强化学习可解释推荐研究', '[目的] 为解决现有的工作推荐存在难以大规模应用、冷启动、缺乏新颖性和解释性等问题，提出了基于人才知识图谱推理的强化学习可解释推荐方法。[方法] 基于真实的简历数据集构建了人才社会经历知识图谱，依据强化学习的理论在知识图谱上训练一个策略智能体，即将一次推理过程分解为选择方向、选择节点两个子过程，使其能够在知识图谱上寻找潜在的优质推荐目标。[结果] 相比于LR、BPR、JRL-int、JRL-rep及PGPR模型，基于人才知识图谱推理的强化学习可解释推荐模型在工作推荐上的MRR@20（81.7%）、Hit@1（74.8%）、Hit@5（92.2%）以及Hit@10（97.0%）均表现最优。[局限] 实验的数据集规模和任务类型相对有限，可进一步扩充进行模型验证和优化。[结论] 该模型能够有效结合人才历史工作经历、相似人才工作经历进行推荐，结合知识图谱工作岗位的属性关联，在给出推荐结果的同时，提供推理路径，有效应对了冷启动和缺乏新颖性、可解释性问题。', '[\"工作推荐\", \"知识图谱推理\", \"强化学习\", \"可解释推荐\"]', '[\"国家自然科学基金青年项目\"融合知识图谱的用户长尾需求建模研究\"（项目编号:61702564）\", \"广东省软科学面上项目（项目编号:2019A101002020）\", \"国家自然科学基金面上项目\"融合知识图谱和行为经济理论的用户行为建模及推荐研究\"（项目编号:72074231）的研究成果之一\"]', 'None', '电子技术及信息科学', '计算机软件及计算机应用', 'TP391.3');
INSERT INTO `article` VALUES ('283', 'FileName=JSJC20210318004&DbName=CAPJLAST&DbCode=CAPJ&', '利用双向对齐和属性信息的跨语言实体对齐', '实体对齐是在不同的知识图谱中查找引用相同现实身份的实体。目前主流的实体对齐方法是基于图嵌入的方法，但是现在大多数图嵌入的方法并没有使用属性信息，而对齐实体通常都具有相似的属性，使用属性信息可以很好的提高实体对齐的性能。同时由于不同知识图谱之间的知识分布的差异，对齐预测过程中仅仅考虑一个方向不够合理，会导致误导性的对齐结果。针对上述两个问题，这篇文章提出了一种融合属性信息的图卷积神经网络模型，并在对齐预测阶段使用双向对齐机制进行实体对齐。该方法通过一个前馈神经网络编码实体对应的属性信息，与初始的实体嵌入相结合，得到融入属性信息的实体表示，并且在对齐预测时使用双向对齐机制。在三个真实的跨语言数据集上的实验表明，该文方法通过融入更多知识图谱自带的信息能学习到更好的知识图谱表示，实体对齐性能取得了显著的提高。', '[\"实体对齐\", \"知识图谱\", \"属性信息\", \"双向对齐\", \"图卷积神经网络\"]', '[\"国家自然科学基金面上项目（62076045）\", \"辽宁省自然科学基金指导计划（2019-ZD-0569）\"]', '10.19678/j.issn.1000-3428.0060540', '信息科技', '计算机软件及计算机应用', 'TP391.1');
INSERT INTO `article` VALUES ('284', 'FileName=ZGSM202106034&DbName=CJFDAUTO&DbCode=CJFD&', '基于Citespace下关于“投入产出”主题的文献计量分析', '投入产出核算在经济核算中占据着重要位置,一直以来都是学术界讨论和研究的热点内容。以中国期刊全文数据库（CNKI）为数据来源,检索\"投入产出\"关键字文献共计3799篇为研究对象,从文献分布、共现图谱、时间轴视图、突变词轨迹等多视角分析我国现对\"投入产出\"主题研究热点及运用投入产出法进行核算的创新内容。', '[\"投入产出\", \"知识图谱\", \"Citespace\", \"聚类分析\", \"时间轴视图\"]', '', '10.19699/j.cnki.issn2096-0298.2021.06.103', '经济与管理科学; 基础科学; 信息科技', '数学; 图书情报与数字图书馆; 宏观经济管理与可持续发展', 'F224;G353.1');
INSERT INTO `article` VALUES ('285', 'FileName=ZGSM202106057&DbName=CJFDAUTO&DbCode=CJFD&', '基于文献计量学的《中国人力资源开发》信息可视化分析', '为了解国内人力资源管理专业领域的发展趋势和动态,本文选取目前在国内人力资源管理专业唯一的国家级核心期刊——《中国人力资源开发》进行可视化分析。本文依据文献计量学原理,利用VOSviewer知识图谱软件和信息可视化技术,运用发文量、关键词共现、作者共现等方法对1989—2019年在《中国人力资源开发》杂志发表的6868篇文献进行可视化分析,探究我国人力资源管理发展的演进历程,并科学预测未来我国人力资源管理研究趋势和热点问题,为我国人力资源管理理论研究和实践发展提供借鉴。', '[\"文献计量学\", \"人力资源管理\", \"信息\", \"可视化\", \"结论\"]', '', '10.19699/j.cnki.issn2096-0298.2021.06.168', '经济与管理科学; 社会科学Ⅱ辑; 信息科技', '人才学与劳动科学; 图书情报与数字图书馆; 宏观经济管理与可持续发展', 'G353.1;F249.2-55');
INSERT INTO `article` VALUES ('286', 'FileName=SYJJ202106027&DbName=CJFDAUTO&DbCode=CJFD&', '物流园区规划研究进展与热点——基于Citespace的可视化分析', '物流业是我国经济发展中的支柱产业,物流园区的相关研究也是我国物流业研究者广泛关注的热点问题,为了清晰展现物流园区规划的研究脉络和热点分布,本文基于文献统计方法,借助Citespace等可视化工具,挖掘物流园区规划研究现状,对研究特点、主要研究机构、主要发文作者,研究热点以及研究前沿进行归纳和论述,旨在为国内物流园区相关研究工作提供一定参考。研究得出:相关文献数量经过2000-2012年上升期和2013-2019年下降期,目前的研究重点已经从物流园区规划的理论及意义研究,转变到实证分析包括规划模型算法的论证,未来的研究方向应以增加物流园区规划的深度与广度为目标。', '[\"物流园区\", \"园区规划\", \"知识图谱\", \"CiteSpace\", \"文献梳理\"]', '[\"中国物流与采购联合会研究课题“大宗商品交易市场现代物流发展报告”（编号:2018CSLKT001）\"]', 'None', '经济与管理', '宏观经济管理与可持续发展', 'F259.2');
INSERT INTO `article` VALUES ('287', 'FileName=XXWX2021031700R&DbName=CAPJLAST&DbCode=CAPJ&', 'TransPath:一种基于深度迁移强化学习的知识推理方法', '基于深度强化学习（ReinforcementLearning，RL）的知识推理旨在推理缺失事实并补全知识图谱，RL智能体在知识图谱上搜索路径，并基于路径进行事实预测和链接预测。由于具有良好的性能和可解释性，基于深度RL的知识推理方法近几年迅速成为研究热点。然而，对于特定实体来说，动作空间中存在大量的无效动作，RL智能体常常会因选择无效动作而终止游走，所以路径挖掘的成功率很低。为了解决无效动作的问题，本文提出一种基于深度迁移强化学习的知识推理方法——TransPath，在目标任务之外增加了单步游走选择有效动作的源任务。首先在源任务上训练单步游走，帮助RL智能体学会选择有效动作，然后迁移到目标推理任务上进行路径搜索训练，提高路径挖掘的成功率。在数据集FB15K-237和NELL-995上的对比实验结果表明，本文方法不仅大幅提升了路径搜索的成功率，而且在大多数推理任务中性能优于同类方法。', '[\"知识推理\", \"强化学习\", \"迁移学习\", \"深度学习\", \"路径搜索\"]', '[\"云环境下的容灾备份恢复与业务连续性管理关键技术研究与示范应用（SGSHXT00JFJS1900093）资助\"]', 'None', '电子技术及信息科学', '自动化技术', 'TP18');
INSERT INTO `article` VALUES ('288', 'FileName=SZYB20210317000&DbName=CAPJLAST&DbCode=CAPJ&', '基于知识图谱的长江流域内地表蒸散研究进展', '以CNKI和Web of Science数据库为数据源，将长江流域范围内地表蒸散研究与国内外地表蒸散研究利用CiteSpace信息可视化软件进行了计量比较分析。结果表明：1992—2020年，国内外共发表地表蒸散为主题的文章5216篇，其中长江流域范围内179篇，2016年前中英文文章数量皆呈增加趋势；长江流域地表蒸散研究中，南京信息工程大学、河海大学和中国科学院南京地理与湖泊研究所论文数量在研究机构中名列前三，这些研究机构主要依靠所属试验站提供实测蒸散数据和气象数据进行一系列蒸散模拟与验证研究；研究内容以蒸散获取和数值模拟为重点，其次为地表蒸散变化机制与时空演变过程分析，而关于地表蒸散变化的生态环境效应研究相对较少；从高引用趋势可以发现，在地表蒸散估算精度不断提高下，学者们也逐渐关注于蒸散组分的研究；变化机制上，环境因子对长江流域内地表蒸散的影响研究较多，而在土地利用/地表覆被、植被类型等下垫面性质及变化对蒸散的研究还较少；蒸散变化效应分析则主要集中在地表蒸散对水平衡、湿地处理以及作物产量的影响。', '[\"地表蒸散\", \"长江流域\", \"计量分析\", \"Citespace\", \"比较分析\"]', '[\"国家自然科学基金（42061015）\", \"中国科学院青年创新促进会（2018417）\"]', 'None', '理工A(数学物理力学天地生)', '地球物理学', 'P333.1');
INSERT INTO `article` VALUES ('289', 'FileName=SSZK202102017&DbName=CJFDAUTO&DbCode=CJFD&', '村规民约研究热点及未来展望', '借助CiteSpace文献分析软件,对村规民约这一研究主题的发文量、发文作者和发文机构以及关键词进行了分析,通过深入阅读相关文献,发现村规民约的研究热点可归纳为价值功能、现实困境、优化路径三个维度。展望未来,村规民约的研究需吸纳不同学科知识,关注当下社会热点,丰富其研究内容;建设紧密的合作网络,适当借鉴西方理论,提升理论水平;加强政学合作,提高村规民约理论成果的实践应用程度,使村规民约为未来乡村治理发挥其应有价值。', '[\"村规民约\", \"自治\", \"法治\", \"德治\"]', '[\"天津市哲学社会科学规划研究项目“城镇化进程中的村民自治转型研究”（TJZZ15-006）\"]', '10.13573/j.cnki.sjzxyxb.2021.02.016', '教育与社会科学综合; 政治军事与法律', '行政学及国家行政管理; 政党及群众组织', 'D422.6;D638');
INSERT INTO `article` VALUES ('290', 'FileName=DBCH202103003&DbName=CJFDAUTO&DbCode=CJFD&', '基于CiteSpace的国内夜间灯光数据研究知识图谱分析', '借助CiteSpace软件工具梳理国内夜间灯光数据研究进展与热点。研究发现:1)大数据时代的来临助推了夜间灯光数据研究,国内夜间灯光数据研究成果主要集中于地理类、测绘类、经管类三大类期刊,作者间表现出\"大分散、小聚合\"特征,彼此间联系较为分散,国内研究机构间成果差异比较明显; 2) DMSP/OLS是目前夜间灯光数据研究领域中的主流数据源,当前夜间灯光数据主要集中于城市发展、社会经济指标、人口发展、生态环境评估等领域,但研究方法比较单一,尤其是在技术处理上有待加强。NPP/VIIRS数据源对DMSP/OLS数据源有替代与延续的意义,未来应注重学科间的交叉融合,回归于数据技术处理,加强DMSP/OLS与NPP/VIIRS等其余夜间灯光数据源的融合。', '[\"夜间灯光数据\", \"CiteSpace\", \"关键词\", \"共现\", \"图谱\"]', '[\"国家自科基金项目——省际交界区空间结构形成演进与优化整合研究（71703061）资助\"]', 'None', '基础科学; 信息科技', '自然地理学和测绘学; 计算机软件及计算机应用; 图书情报与数字图书馆', 'G353.1;P208');
INSERT INTO `article` VALUES ('291', 'FileName=KJFT202108082&DbName=CJFDAUTO&DbCode=CJFD&', '社会网络分析在教育领域的应用', '目的:了解国内社会网络分析方法在教育领域的应用状况。方法:通过中文献数据的搜集整理,利用Excel统计和UCINET软件工具,从文献和期刊分布、学科和研究方向、研究机构和作者、研究主题和热点问题等方面进行可视化比较分析。结果:以可视化方式呈现了研究文献的年度分布、期刊分布、学科分布等外部特征,及其研究力量、研究主题和研究热点问题的分布状况,并分析了国内应用研究的发展阶段和问题。结论:国内社会网络分析方法在教育领域、研究方向和研究力量都不具有明显的集中性,且分析方法也显得比较单调;研究趋势及方法都值得关注和推广,才能更好地应用社会网络分析方法服务于教育领域。', '[\"社会网络分析\", \"应用状况\", \"可视化\", \"教育\"]', '', '10.19392/j.cnki.1671-7341.202108081', '理工A(数学物理力学天地生); 教育与社会科学综合; 电子技术及信息科学', '教育理论与教育管理; 图书情报与数字图书馆', 'G353.1;G40');
INSERT INTO `article` VALUES ('292', 'FileName=JLGY20210317003&DbName=CAPJLAST&DbCode=CAPJ&', '基于知识图谱嵌入的定义域值域约束补全方法', '定义域值域约束信息是知识图谱的重要组成部分，并在知识图谱嵌入表示和补全中具有重要作用，但它同样面临严重数据缺失问题。本文关注定义域值域约束补全问题，将其转化成链接预测问题并使用基于知识图谱嵌入模型预测缺失数据。针对定义域值域约束补全问题的结构，本文在两种基于翻译的知识图谱嵌入模型TransE和RotatE基础上给出了两种高效的约束补全方法DCaT-T和DCaT-R。特别地，为提升补全方法的预测性能，DCaT-T与DCaT-R方法均采用了两阶段的训练方法。实验结果表明，DCaT-T和DCaT-R优于类型预测方法SDType，DCaT-T方法优于同在TransE基础上实现的嵌入表示模型ConnectE类型预测方法，并且两阶段的训练方法能够进一步提高模型的预测能力。', '[\"人工智能\", \"知识图谱\", \"定义域值域\", \"约束补全\", \"知识图谱嵌入\"]', '[\"国家自然科学基金项目（62076108，61872159，61672261）\"]', '10.13229/j.cnki.jdxbgxb20200755', '电子技术及信息科学', '图书情报与数字图书馆', 'G353.1');
INSERT INTO `article` VALUES ('293', 'FileName=MKZD20210317000&DbName=CAPJLAST&DbCode=CAPJ&', '煤矿装备维护知识图谱构建及应用', '利用大数据管理系统对煤矿装备维护信息进行管理缺乏对煤矿装备维护知识的表示能力，没有形成相对完整的煤矿装备维护知识管理体系，无法实现知识挖掘及知识间关系链接，导致大量具有深度挖掘价值的信息不能得到有效利用。针对上述问题，构建了煤矿装备维护知识图谱。首先通过定义煤矿装备维护的关键概念、关系及属性，进行基于本体的知识建模；然后从结构化、半结构化和非结构化数据源中获取知识，通过命名实体识别、关系抽取及事件抽取完成煤矿装备维护知识抽取；最后利用图数据库Neo4j存储煤矿装备维护知识，形成煤矿装备维护知识图谱。煤矿装备维护知识图谱在智能语义搜索、智能问答及可视化决策支持等方面的应用可提高煤矿装备维护知识管理效率，为煤矿装备智能化动态管理的实现提供有力支持。', '[\"煤矿装备维护\", \"知识图谱\", \"知识建模\", \"知识抽取\", \"知识存储\"]', '[\"国家自然科学基金重点资助项目（51834006）\", \"国家自然科学基金资助项目（51875451）\"]', '10.13272/j.issn.1671-251x.2020090013', '工程科技Ⅰ辑', '矿业工程', 'TD407');
INSERT INTO `article` VALUES ('294', 'FileName=JSJJ20210316009&DbName=CAPJLAST&DbCode=CAPJ&', '基于知识图谱的分布式光伏运维方案匹配方法', '为了提高分布式光伏运维效率，设计了一种利用专业领域知识图谱匹配运维方案的方法。该方法基于运维诉求与分布式光伏运维知识图谱中的信息，匹配准确的运维方案，为运维人员提供方案支持。首先陈述了在单一故障、诉求完整的状况下以知识图谱为媒介匹配运维方案的方法；再基于复合型运维诉求设计了先拆分诉求再分别匹配的流程；然后针对实践中诉求要素缺失的问题，利用知识图谱提供的联想能力，使该方法能够补全诉求并匹配方案。实验对比分析表明，该方法准确度较高，并且在实践中具有理想的可靠性。', '[\"分布式光伏\", \"智能运维\", \"知识图谱\", \"方案匹配\"]', '[\"国家重点研发计划资助项目（2018YFB1500800）\", \"国家电网有限公司科技资助项目（SGTJDK00DYJS2000148）\"]', 'None', '工程科技Ⅱ辑; 信息科技', '电力工业; 计算机软件及计算机应用', 'TM615;TP391.1');
INSERT INTO `article` VALUES ('295', 'FileName=SJKX20210316000&DbName=CAPJLAST&DbCode=CAPJ&', '基于科学知识图谱的针灸专利计量可视化研究', '目的 运用专利计量可视化方法探索针灸技术热点及发展趋势，为针灸技术领域创新研究提供参考，提高针灸技术临床应用，加快针灸技术发展。方法 利用文献计量软件Citespace 5.5.R2对从建库以来至2020年收录在德温特专利数据库（Derwent Innovations Index,DII）的27177篇针灸相关专利文献进行总结、分析，并以可视化图谱的形式展现出针灸专利的申请量、学科分布，专利权人、发明人合作网络，专利技术热点、发展趋势等指标特征。结果 针灸专利申请量呈现逐年上升趋势；学科涉仪器、内科医学、工程学、化学、药物药剂学等方面；中国为发明人和专利权人最多的国家，成都中医药大学、湖南中医药大学、上海中医药大学、河南中医药大学是针灸技术创新的主要创新机构；热点技术领域集中在针灸治疗仪器设备创新、中医经络理论指导下的养生保健设备创新；技术创新的趋势是诊疗一体化、数字化、智能化。结论运用专利计量可视化方法发现目前针灸专利技术发展较快，探测到目前针灸技术领域的热点及趋势，可为针灸技术创新研究提供参考。', '[\"针灸\", \"专利计量\", \"可视化分析\", \"知识图谱\", \"Citespace\"]', '[\"成都中医药大学2019年校级系列金课建设项目（成中医教务[2020]4号）：《中医临床医学数据处理》，负责人：程小恩\", \"成都中医药大学2020年度杏林学者学科人才科研提升计划-青年教师创新专项（成中医科技[2020]2号）：基于DBPNN与GBDT组合模型的2型糖尿病患者证型画像模型构建研究，负责人：程小恩\"]', 'None', '医药卫生; 电子技术及信息科学', '中医学; 图书情报与数字图书馆', 'G353.1;R245');
INSERT INTO `article` VALUES ('296', 'FileName=SDGY20210315001&DbName=CAPJLAST&DbCode=CAPJ&', 'LncRNA与疾病关系的知识图谱构建', '基于LncRNA和疾病关系的分析,对LncRNA和疾病知识概念建模,提出一种有效的LncRNA与疾病关系的知识图谱构建方法。使用Protege构建本体结构,建构概念层,整合结构化与非结构化两种不同来源的数据形成数据层,通过RDF/OWL技术对数据及相应的关系进行描述,采用基于前向推理的产生式规则进行相应的知识推理,通过SPARQL查询语言和可视化技术展示知识查询的推理效果。这一研究将为LncRNA与疾病的关系研究提供进一步的参考阶值,推动该领域的发展。', '[\"LncRNA\", \"知识表示\", \"LncRNA-疾病关联\", \"知识图谱\", \"本体\"]', '[\"国家自然科学基金资助项目（61502243）\", \"浙江省智慧医疗工程技术研究中心资助项目（2016E10011）\", \"中国博士后基金资助项目（2018M632349）\", \"江苏省“六大人才高峰”高层次人才项目（XYDXX-204）\", \"自然资源部城市国土资源监测与仿真重点实验室开放基金资助课题（KF-2019-04-011,KF-2019-04-065）\", \"苏州市姑苏科技创业天使计划项目（CYTS2018233）资助\", \"南京邮电大学引进人才科研启动基金资助（NY217136）\"]', 'None', '基础科学; 医药卫生科技; 信息科技', '生物学; 生物医学工程; 计算机软件及计算机应用', 'R318;TP311.13');
INSERT INTO `article` VALUES ('297', 'FileName=GXBJ20210315006&DbName=CAPJLAST&DbCode=CAPJ&', '基于Citespace的失能老年人照护研究热点及趋势分析', '目的 全面分析近10年我国失能老年人照护的研究现状,以发现我国失能老年人照护的研究热点及发展趋势,为今后研究提供参考。方法 选取中国知网（CNKI）数据库为检索对象,检索发表时间为2010—2020年的有关失能老年人照护领域的文献,统计其发文量。采用Citespace.5.7.R3软件对样本文献作者、研究机构、关键词进行知识图谱的可视化分析。结果 本研究共纳入有效文献数量共531篇。2010—2020年总体发文量呈现逐年上升趋势。2011年发表文献数量最少（6篇）,2019年发表文献数量最多（101篇）。研究机构及作者的聚类知识图谱显示,研究机构和作者主要集中在各大高校及科研院所,整个知识图谱的网络结构较为分散,未形成明显的聚类模块,说明失能老年人照护研究领域中各学者及机构较少进行学术上的交流和合作。在关键词共现知识图谱的基础上提取出排名前10位高频关键词,依次为失能老年人、长期照料、家庭照护者、失能、照护者、社会支持、影响因素、农村失能老年人、农村、需求。从最强突现关键词可知:2013年的最强突现关键词为“照护服务”;2013—2014年的最强突现关键词分别为“家庭照护”和“机构照护”。2014—2015年的最强突现关键词为“对策”和“质性研究”。2018—2020年的最强突现关键词为“老龄化”。从关键词时间线图谱可知,长期照料、照顾者、老年人等聚类领域自2010年起,便有学者开始关注。主要照顾者、质性研究、影响因素分析三大聚类领域在2012年同时受到国内学者的关注。农村失能老年人领域从2018年后逐渐出现聚冷现象。结论 国内学者持续关注的领域是与失能老年人的长期照护及照顾者相关的问题。在失能老年人照顾者方面,学者们重点探寻家庭照顾者在失能老年人照护中承担的责任及照护情况,这说明家庭养老仍是失能老年人长期照护中的首要选择。同时,长期照护、主要照顾者、家庭照顾者和影响因素分析四大聚类领域关键词的密集程度呈现出随时间的增加而变高的现象,表明后期失能老年人的长期照护、照护主体及照护影响因素等研究领域将持续聚热。', '[\"老龄化\", \"失能老年人照护\", \"老年长期照料\", \"养老服务\", \"家庭养老\"]', '[\"国家科技部重点研发项目（2020YFC2006100）\", \"2021年重庆民政政策理论研究专家委托课题（HRZ21C003）\", \"2019年度西南大学人文社科研究重点培育项目（SWU1909036）\"]', 'None', '医药卫生', '临床医学', 'R473');
INSERT INTO `article` VALUES ('298', 'FileName=NYJX20210312003&DbName=CAPJLAST&DbCode=CAPJ&', '基于BERT的水稻表型知识图谱中关系抽取研究', '水稻表型组学通过对生物的遗传信息以及内外各种表型数据进行分析和研究，对水稻的生产以及研究有着重要的指导作用。知识图谱技术通过结构化描述数据中的概念、实体和关系等信息，已经在知识存储、搜索引擎等方面获得了广泛应用。关系抽取任务作为知识图谱中的关键任务和环节，可以抽取文本中的两个实体词之间的联系。针对水稻表型知识图谱中的实体关系抽取问题，本文首先对水稻表型组学数据进行获取、标注和分类，根据植物本体论方法提出了一种对水稻的基因、环境、表型等表型组学实体进行关系分类的方法。随后提取关系数据集中的词向量、位置向量及句子向量，基于BERT实现水稻表型组学关系抽取模型。最后，将BERT模型与卷积神经网络以及分段卷积网络模型进行结果比较，在3种关系抽取模型对比中，BERT获得了更好的表现，精确率达到了95.10%、F1值为95.85%。', '[\"水稻表型\", \"知识图谱\", \"关系抽取\", \"双向转换编码表示\"]', '[\"国家自然科学基金项目（61502236、61806097）\", \"大学生创新创业训练专项计划项目（S20190025）\"]', 'None', '农业; 电子技术及信息科学', '农作物; 计算机软件及计算机应用', 'TP391.1;S511');
INSERT INTO `article` VALUES ('299', 'FileName=XKKJ202103009&DbName=CJFDAUTO&DbCode=CJFD&', '1989—2018年国内作物连作障碍研究现状——基于CNKI的文献计量学分析和科学知识图谱研究', '为介绍国内作物连作障碍的研究进展,基于1989—2018年中国知网数据库（CNKI）中连作障碍相关发文情况,通过文献计量学方法分析文献的年代、期刊、机构、基金、作者、研究对象和主题分布等基础信息,并采用CiteSpace V软件对关键词进行科学知识图谱研究。结果表明,连作障碍文献数量总体上与年度变化呈明显正相关关系;受各类资金资助的文献数为2678篇,占总文献量的42.28%,其中受国家自然科学基金资助的文献发表最多;该研究领域文章的刊载主要涉及农业类杂志,研究机构主要涉及农林类高等院校及科研院所;文献作者毛志泉、许艳丽、韩晓增等在该领域研究成果较多;研究对象主要集中在粮食作物、蔬菜作物、水果（树）、经济作物和药用植物5类;该领域研究热点主要围绕土壤微生物、土壤酶、土传病害、化感自毒作用等方面展开,初步形成了以韩丽梅、许艳丽为中心的研究群体。作物连作障碍研究逐渐受到重视,越来越多学者致力于此方向研究,使该领域科研水平和学术影响力得到了较大提升。但作物连作障碍研究中仍有许多领域具有较大空间,基于土壤微生态环境变化视角,探索连作障碍的防治机制,或许将成为未来研究的主要方向。', '[\"连作障碍\", \"文献计量学\", \"知识图谱\", \"CiteSpace\", \"研究热点\"]', '[\"国家自然科学基金青年项目“营养胁迫下三七根系分泌物化感作用变化及其与连作障碍机理间的关系研究”（81102751）\", \"中央高校基本科研业务费专项资金项目“基于化感作用原理的三七轮作植物筛选及其作用机制研究”（2016-JYB-JSMS-011）\", \"现代农业产业技术体系建设专项“国家中药材产业技术体系”（CARS-21）\"]', 'None', '农业科技; 信息科技', '农艺学; 农作物; 图书情报与数字图书馆', 'G353.1;S344.4');
INSERT INTO `article` VALUES ('300', 'FileName=TSGT20210311009&DbName=CAPJLAST&DbCode=CAPJ&', '信息组织4.0时代智慧化知识组织的知识协同服务', '信息组织4.0时代下的知识组织帮助图书馆实现了知识协同服务，并能从中实现知识的协调共享交互，还能以知识网络合作的服务来发现信息知识资源，从而产生其应用特征。而智慧化知识组织能在专业特色数据库、科研资源情报、元数据智慧化和协同辅助分析组织等服务中实现信息情报资源的共享和知识扩散，并能在知识协同服务管理中实现科研范式。', '[\"信息组织4.0\", \"知识组织\", \"知识协同服务\", \"知识网络合作服务\", \"信息情报\"]', '[\"广东省哲学社会科学“十三五”规划2018年度学科共建项目“基于信息组织4.0的‘云图书馆+’的智慧知识服务”（项目编号：GD18XTS02）\", \"广州市哲学社会科学发展“十三五”规划2019年度共建课题“广州建设粤港澳大湾区教育示范区研究——基于博弈分析的大数据环境对粤港澳大湾区高校图书馆资源协同服务的影响”（项目编号：2019GZGJ115）广州市哲学社会科学发展“十三五”规划2019年度共建课题“高校图书馆微信服务优化研究——基于用户体验的实证”（项目编号：2019GZGJ116）研究成果\"]', 'None', '电子技术及信息科学', '图书情报与数字图书馆', 'G252');
INSERT INTO `article` VALUES ('301', 'FileName=JSJY20210312000&DbName=CAPJLAST&DbCode=CAPJ&', '基于循环神经网络的专利价格自动评估', '专利价格评估是知识产权交易的重要内容，现有方法在进行专利价格评估时没有有效的考虑专利的市场、法律、技术维度对专利价格的影响，而专利的市场因素对专利价格评估起到关键作用。同时，随着人工智能深度学习技术在工程领域的不断成熟，本文提出了基于循环神经网络的专利价格自动评估方法，该方法以市场法为基础，对其他各种因素进行综合考虑，利用门控循环单元（GRU）神经网络的方法实现对专利价格的自动评估。实例测试表明，以专家定性评估结果为基准，本文所提方法的相对准确度值平均为0.85，分别与层次分析法、粗糙集理论方法和逆向传播（BP）神经网络方法相比，所提方法的相对准确度均值分别提升了3.66%、4.94%和2.41%。', '[\"专利价格评估\", \"人工智能\", \"门控循环单元\", \"环神经网络\", \"知识挖掘\"]', '[\"国家重点研发计划（2017YFB1401904）\"]', 'None', '信息科技', '自动化技术', 'TP183');
INSERT INTO `article` VALUES ('302', 'FileName=MKZD20210311000&DbName=CAPJLAST&DbCode=CAPJ&', '智能煤矿技术研究与政策制定现状', '目前针对智能煤矿的研究集中在顶层设计、理论架构、核心技术、管控平台、建设路线、标准制定、评价体系等方面，没有文献针对《关于加快煤矿智能化发展的指导意见》发布前后的技术研究情况进行探讨。智能煤矿具有技术密集型和资金密集型特征，需要由政策引导，形成汇聚政府、学术、产业、金融和用户的合力。以CNKI（中国知网）为工具，挖掘分析了智能煤矿技术研究现状、关注热点和主要研究机构。归纳梳理了国家层面及贵州、山东、山西等主要产煤大省的智能煤矿政策制定现状，各省虽在智能煤矿入手点和实施进度上略有差异，但是均在实施办法和验收定级等方面发布了指导性文件，并在标准制定、创新研发中心设立方面进行了尝试，加速了智能煤矿研究和建设步伐。', '[\"智能煤矿\", \"煤矿智能化\", \"人工智能\", \"顶层设计\", \"标准制定\", \"政策制定\"]', '[\"国家自然科学基金资助项目（51874299，61771474）\", \"山东省重大科技创新工程项目（2019JZZY020505）\", \"中国矿业大学“工业物联网与应急协同”创新团队资助计划（2020ZY002）\"]', '10.13272/j.issn.1671-251x.17708', '工程科技Ⅰ辑; 信息科技', '矿业工程; 自动化技术', 'TD67');
INSERT INTO `article` VALUES ('303', 'FileName=DSJU20210319001&DbName=CAPJLAST&DbCode=CAPJ&', '基于法律裁判文书的法律判决预测研究', '针对智慧司法服务领域中“法律判决预测”任务的实际需求，探讨了“法律判决预测”任务的研究思路与实现路径，介绍了“法律判决预测”的整体框架和具体过程。基于中国法律裁判文书网获取的海量真实案件数据和“中国法研杯”司法人工智能挑战赛的评测数据，整理了实验数据类别，规范了实验数据格式，形成基于裁判文书大数据的法律判决预测数据集。在判决预测模型中，首先使用判决要素抽取方法提取出高质量的判决要素句，然后借鉴法官的判案思路，将整个“法律判决预测”任务转换为法条预测、罪名预测和刑期预测3项子任务，并分别构建了基于判决要素的预测模型。所提的方法在刑法类判决预测数据集上得到了有效验证，开展的研究对新一代智慧司法的应用提供了重要参考。', '[\"法律判决预测\", \"判决要素抽取\", \"法条预测\", \"罪名预测\", \"刑期预测\"]', '[\"国家自然科学基金重点项目（61936012）\", \"国家社会科学基金项目（18BYY074）\", \"山西省自然科学基金项目（201901D111028）\"]', 'None', '社会科学Ⅰ辑', '诉讼法与司法制度; 诉讼法与司法制度', 'D926.2;D925.2');
INSERT INTO `article` VALUES ('304', 'FileName=QBZZ20210310001&DbName=CAPJLAST&DbCode=CAPJ&', '人工智能融入美国情报体系的现状及发展困境分析', '[目的/意义]人工智能是美国情报界正在推动的重要技术之一,无论是学界还是官方都进行了大量的研究和讨论,分析人工智能融入美国情报体系的现状和发展困境,对未来正确运用人工智能、合理有效规避风险有重要的借鉴价值。[方法/过程]从美国情报界运用人工智能的相关报告和研究成果出发,探究人工智能在不同情报手段中的运用现状,并分析其融入情报界所面临的问题和挑战。[结果/结论]美国情报界对人工智能的研究与运用居于世界前列,不能否认人工智能在情报工作中有较好的应用,但也必须重视其带来的一系列伦理和技术问题。', '[\"人工智能\", \"美国情报界\", \"开源情报\", \"地理空间情报\", \"信号情报\", \"伦理困境\"]', '', 'None', '电子技术及信息科学', '自动化技术; 图书情报与数字图书馆', 'G359.7;TP18');
INSERT INTO `article` VALUES ('305', 'FileName=ZYJU202104020&DbName=CJFDAUTO&DbCode=CJFD&', '人工智能背景下中职学校会计人才的培养策略', '近年来,随着信息技术的不断发展,人工智能和大数据已经在社会各界得到了广泛的应用。在会计领域,传统的财务会计正在向管理会计转型,会计从业者受到巨大的影响。文章以中职学校会计专业人才培养现状为着眼点,通过分析中职学校会计人才培养模式存在的问题,提出了以市场需求为导向,设置多元化课程、树立核心素养教育观念、改良教师团队、加强校企合作的改革建议。', '[\"人工智能\", \"中职会计\", \"人才培养\", \"培养策略\"]', '', '10.19552/j.cnki.issn1672-0601.2021.04.019', '教育与社会科学综合; 经济与管理', '职业教育; 会计', 'F230-4;G712');
INSERT INTO `article` VALUES ('306', 'FileName=GJXK202110007&DbName=CJFDAUTO&DbCode=CJFD&', '人工智能类课程改革实践及赋能军事智能发展探索', '针对课程的教学现状,文章围绕人工智能类课程的教学改革与实践展开研究,并对其在军事智能领域的赋能辐射作用和方式进行了探索。在课程的规划设置、教学体系和内容的设计与优化、教学方式的改进、考核方式的创新,以及课程教学向科研学术、技术应用、作战运用的赋能辐射等方面进行了一系列改革实践,提出了措施。', '[\"人工智能\", \"课程改革\", \"军事智能\", \"发展探索\"]', '[\"国家自然科学青年基金“非结构化数据模式分析中的多核融合理论与学习方法研究”（编号：61202332）\", \"陕西省自然科学基金面上项目“数据驱动的高光谱图像像元解混与高精度地物分类”（编号：2020JM-358）陕西省自然科学基金面上项目“视觉认知驱动的SAR图像典型目标非结构化信息表示及识别技术”（编号：2015JM6313）\"]', 'None', '教育与社会科学综合; 电子技术及信息科学', '高等教育; 自动化技术', 'TP18-4;G642');
INSERT INTO `article` VALUES ('307', 'FileName=CGZC202103027&DbName=CJFDAUTO&DbCode=CJFD&', '基于MRI的人工智能在肝纤维化诊断中的应用进展', '肝纤维化是慢性肝病发展为肝硬化及其严重并发症、肝癌的必经途径,肝纤维化的无创性诊断一直是临床研究的热点。随着影像技术及计算机科学的不断发展,影像组学、机器学习等人工智能技术可以高通量提取及学习图像中的特征,更大程度地利用医学影像中人眼无法识别的信息,通过构建模型实现疾病的诊断、预后评估和疗效预测。近年来,人工智能技术的研究逐渐深入,作者就基于MR成像的影像组学和机器学习技术在肝纤维化诊断和分期中的临床应用进展进行综述。', '[\"肝纤维化\", \"磁共振成像\", \"影像组学\", \"机器学习\", \"人工智能\"]', '[\"兰州市城关区科技计划项目（编号：2019SHFZ0037）~~\"]', 'None', '医药卫生', '临床医学; 消化系统疾病', 'R445.2;R575.2');
INSERT INTO `article` VALUES ('308', 'FileName=JXUY202108031&DbName=CJFDAUTO&DbCode=CJFD&', '机器人结合虚拟现实技术对脑卒中偏瘫上肢功能的影响', '目的探讨上肢机器人结合虚拟现实技术对脑卒中偏瘫上肢运动功能和活动能力康复的影响。方法 30例脑卒中偏瘫患者,随机分为试验组（在上肢机器人辅助下进行虚拟游戏训练）15例和对照组（给予常规作业治疗）15例。共治疗2周,每天1次、每次30 min、每周6天。患者在治疗前后均进行Fugl-Meyer量表上肢部分（FMA-UE）评定、上肢功能指数（UEFI）和改良Barthel指数（MBI）评定。结果治疗前,两组患者的FMA-UE、UEFI和MBI比较,差异无统计学意义（P> 0.05）;治疗2周后,两组UEFI及MBI评分均较治疗前明显提高（P <0.05）,试验组FMA-UE评分改善程度显著优于对照组（P <0.05）,两组间UEFI及MBI评分差异无统计学意义（P> 0.05）。试验组FMA-UE评分显著优于治疗前（P <0.05）,对照组FMA-UE评分与治疗前差异无统计学意义（P> 0.05）。结论上肢机器人结合虚拟现实技术训练能有效改善偏瘫上肢运动功能,提高患者对自身上肢功能的满意度,对改善日常生活活动能力也有一定的促进作用。', '[\"机器人\", \"虚拟现实\", \"脑卒中\", \"上肢功能\", \"运动功能\", \"活动能力\"]', '[\"广州医科大学附属第二医院新技术、新业务临床研究与应用基金项目（2017-XJS-E-14）\", \"2018年度广州医科大学大学生实验室开放项目\"]', 'None', '医药卫生科技', '神经病学', 'R743.3');
INSERT INTO `article` VALUES ('309', 'FileName=HXYK202102001&DbName=CJFDAUTO&DbCode=CJFD&', '人工智能推动精准病理诊断的发展', '病理诊断在精准医学中扮演着非常重要的角色,无论是病理医生资源有限的现实,还是不断精细量化的临床诊断需求,都对精准的病理诊断能力提出了更高的挑战。医学界希望人工智能（artificial intelligence, AI）成为从多个方面解决这一难题的得力助手。本文讨论了AI推动精准病理诊断的几个方面:AI辅助病变组织的精准获取、AI辅助组织病理精准诊断、AI辅助组织学分级和定量评分、AI辅助肿瘤生物标记物的精准评估、AI辅助基于HE图像预测分子特征和精准的生物信息解读、AI辅助信息整合实现深层次的精准诊断、AI辅助基于HE图像精准预测患者的生存和预后,为读者展现AI技术为我们迎来的智慧病理的明天。', '[\"人工智能\", \"病理学\", \"精准医学\", \"诊断\"]', '[\"科技部重点研发计划重点专项（No.2017YFC0113908）\", \"四川大学华西医院学科卓越发展1·3·5工程项目（No.ZYGD18012）资助\"]', 'None', '医药卫生科技; 信息科技', '临床医学; 自动化技术', 'TP18;R446.8');

-- ----------------------------
-- Table structure for article_ex
-- ----------------------------
DROP TABLE IF EXISTS `article_ex`;
CREATE TABLE `article_ex` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) DEFAULT NULL COMMENT '链接',
  `publish_date` varchar(255) DEFAULT NULL COMMENT '发表日期',
  `type` varchar(255) DEFAULT NULL COMMENT '文献类型',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of article_ex
-- ----------------------------
INSERT INTO `article_ex` VALUES ('39', 'FileName=XAJD20210323001&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-23 16:52', '期刊');
INSERT INTO `article_ex` VALUES ('40', 'FileName=XAJD20210319000&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-23 14:23', '期刊');
INSERT INTO `article_ex` VALUES ('41', 'FileName=YXXB20210319003&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-23 10:38', '期刊');
INSERT INTO `article_ex` VALUES ('42', 'FileName=GRKZ202103019&DbName=CJFDAUTO&DbCode=CJFD&', '2021-03-23', '期刊');
INSERT INTO `article_ex` VALUES ('43', 'FileName=SZTQ20210323B021&DbName=CCNDTEMP&DbCode=CCND&', '2021-03-23', '报纸');
INSERT INTO `article_ex` VALUES ('44', 'FileName=XDTQ20210319001&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-23 16:58', '期刊');
INSERT INTO `article_ex` VALUES ('45', 'FileName=JSJC20210318004&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-23 16:15', '期刊');
INSERT INTO `article_ex` VALUES ('46', 'FileName=ZGSM202106034&DbName=CJFDAUTO&DbCode=CJFD&', '2021-03-23', '期刊');
INSERT INTO `article_ex` VALUES ('47', 'FileName=ZGSM202106057&DbName=CJFDAUTO&DbCode=CJFD&', '2021-03-23', '期刊');
INSERT INTO `article_ex` VALUES ('48', 'FileName=SYJJ202106027&DbName=CJFDAUTO&DbCode=CJFD&', '2021-03-22', '期刊');
INSERT INTO `article_ex` VALUES ('49', 'FileName=XXWX2021031700R&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-19 15:00', '期刊');
INSERT INTO `article_ex` VALUES ('50', 'FileName=SZYB20210317000&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-19 14:32', '期刊');
INSERT INTO `article_ex` VALUES ('51', 'FileName=SSZK202102017&DbName=CJFDAUTO&DbCode=CJFD&', '2021-03-19', '期刊');
INSERT INTO `article_ex` VALUES ('52', 'FileName=DBCH202103003&DbName=CJFDAUTO&DbCode=CJFD&', '2021-03-19', '期刊');
INSERT INTO `article_ex` VALUES ('53', 'FileName=KJFT202108082&DbName=CJFDAUTO&DbCode=CJFD&', '2021-03-19', '期刊');
INSERT INTO `article_ex` VALUES ('54', 'FileName=JLGY20210317003&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-18 15:24', '期刊');
INSERT INTO `article_ex` VALUES ('55', 'FileName=MKZD20210317000&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-18 14:40', '期刊');
INSERT INTO `article_ex` VALUES ('56', 'FileName=JSJJ20210316009&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-18 12:00', '期刊');
INSERT INTO `article_ex` VALUES ('57', 'FileName=SJKX20210316000&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-18 10:43', '期刊');
INSERT INTO `article_ex` VALUES ('58', 'FileName=SDGY20210315001&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-18 07:57', '期刊');
INSERT INTO `article_ex` VALUES ('59', 'FileName=GXBJ20210315006&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-16 15:29', '期刊');
INSERT INTO `article_ex` VALUES ('60', 'FileName=NYJX20210312003&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-16 11:32', '期刊');
INSERT INTO `article_ex` VALUES ('61', 'FileName=XKKJ202103009&DbName=CJFDAUTO&DbCode=CJFD&', '2021-03-16', '期刊');
INSERT INTO `article_ex` VALUES ('62', 'FileName=TSGT20210311009&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-15 11:07', '期刊');
INSERT INTO `article_ex` VALUES ('63', 'FileName=XAJD20210323001&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-23 16:52', '期刊');
INSERT INTO `article_ex` VALUES ('64', 'FileName=XAJD20210319000&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-23 14:23', '期刊');
INSERT INTO `article_ex` VALUES ('65', 'FileName=YXXB20210319003&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-23 10:38', '期刊');
INSERT INTO `article_ex` VALUES ('66', 'FileName=GRKZ202103019&DbName=CJFDAUTO&DbCode=CJFD&', '2021-03-23', '期刊');
INSERT INTO `article_ex` VALUES ('67', 'FileName=SZTQ20210323B021&DbName=CCNDTEMP&DbCode=CCND&', '2021-03-23', '报纸');
INSERT INTO `article_ex` VALUES ('68', 'FileName=RMZX202103230052&DbName=CCNDTEMP&DbCode=CCND&', '2021-03-23', '报纸');
INSERT INTO `article_ex` VALUES ('69', 'FileName=RMZX202103230064&DbName=CCNDTEMP&DbCode=CCND&', '2021-03-23', '报纸');
INSERT INTO `article_ex` VALUES ('70', 'FileName=KXSB202103230070&DbName=CCNDTEMP&DbCode=CCND&', '2021-03-23', '报纸');
INSERT INTO `article_ex` VALUES ('71', 'FileName=JSJY20210312000&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-22 11:05', '期刊');
INSERT INTO `article_ex` VALUES ('72', 'FileName=MKZD20210311000&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-22 11:00', '期刊');
INSERT INTO `article_ex` VALUES ('73', 'FileName=DSJU20210319001&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-22 10:18', '期刊');
INSERT INTO `article_ex` VALUES ('74', 'FileName=QBZZ20210310001&DbName=CAPJLAST&DbCode=CAPJ&', '2021-03-22 09:11', '期刊');
INSERT INTO `article_ex` VALUES ('75', 'FileName=ZYJU202104020&DbName=CJFDAUTO&DbCode=CJFD&', '2021-03-22', '期刊');
INSERT INTO `article_ex` VALUES ('76', 'FileName=GJXK202110007&DbName=CJFDAUTO&DbCode=CJFD&', '2021-03-22', '期刊');
INSERT INTO `article_ex` VALUES ('77', 'FileName=CGFB202103220041&DbName=CCNDTEMP&DbCode=CCND&', '2021-03-22', '报纸');
INSERT INTO `article_ex` VALUES ('78', 'FileName=JRSB202103220121&DbName=CCNDTEMP&DbCode=CCND&', '2021-03-22', '报纸');
INSERT INTO `article_ex` VALUES ('79', 'FileName=CGZC202103027&DbName=CJFDAUTO&DbCode=CJFD&', '2021-03-20', '期刊');
INSERT INTO `article_ex` VALUES ('80', 'FileName=JXUY202108031&DbName=CJFDAUTO&DbCode=CJFD&', '2021-03-20', '期刊');
INSERT INTO `article_ex` VALUES ('81', 'FileName=HXYK202102001&DbName=CJFDAUTO&DbCode=CJFD&', '2021-03-20', '期刊');

-- ----------------------------
-- Table structure for author
-- ----------------------------
DROP TABLE IF EXISTS `author`;
CREATE TABLE `author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) DEFAULT NULL COMMENT '链接，格式：dbcode=值1&sfield=au&skey=值2&code=值3',
  `name` varchar(255) DEFAULT NULL COMMENT '姓名',
  `major` varchar(255) DEFAULT NULL COMMENT '专业',
  `sum_publish` varchar(255) DEFAULT NULL COMMENT '总发布量',
  `sum_download` varchar(255) DEFAULT NULL COMMENT '总下载量',
  `fields` varchar(255) DEFAULT NULL COMMENT '专注领域',
  `has_teacher` int(11) DEFAULT '0' COMMENT '是否有导师，0无1有',
  `has_student` int(11) DEFAULT '0' COMMENT '是否有学生，0无1有',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of author
-- ----------------------------

-- ----------------------------
-- Table structure for re_article_author
-- ----------------------------
DROP TABLE IF EXISTS `re_article_author`;
CREATE TABLE `re_article_author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url_article` varchar(255) DEFAULT NULL COMMENT '文章链接',
  `url_author` varchar(255) DEFAULT NULL COMMENT '作者链接',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=331 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of re_article_author
-- ----------------------------
INSERT INTO `re_article_author` VALUES ('220', 'FileName=XAJD20210319000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%8d%ab%e6%99%a8%e6%9b%99&code=47959806');
INSERT INTO `re_article_author` VALUES ('221', 'FileName=YXXB20210319003&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%88%98%e6%b6%a6%e5%93%b2&code=48796971');
INSERT INTO `re_article_author` VALUES ('222', 'FileName=YXXB20210319003&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%ae%8b%e4%bf%8a%e7%a7%91&code=25161339');
INSERT INTO `re_article_author` VALUES ('223', 'FileName=YXXB20210319003&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%88%98%e8%89%be%e6%9e%97&code=22814902');
INSERT INTO `re_article_author` VALUES ('224', 'FileName=YXXB20210319003&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%9d%9c%e5%86%a0%e5%8d%8e&code=21768183');
INSERT INTO `re_article_author` VALUES ('225', 'FileName=GRKZ202103019&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e6%9d%8e%e5%b0%91%e5%bc%ba&code=35223260');
INSERT INTO `re_article_author` VALUES ('226', 'FileName=GRKZ202103019&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e5%88%98%e6%b5%a9&code=28592716');
INSERT INTO `re_article_author` VALUES ('227', 'FileName=GRKZ202103019&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e9%83%ad%e6%96%87%e4%ba%ae&code=35219867');
INSERT INTO `re_article_author` VALUES ('228', 'FileName=GRKZ202103019&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e5%91%a8%e5%9c%86%e5%9c%86&code=29320962');
INSERT INTO `re_article_author` VALUES ('229', 'FileName=GRKZ202103019&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e6%9d%8e%e6%97%b6%e6%82%a6&code=35219869');
INSERT INTO `re_article_author` VALUES ('230', 'FileName=XDTQ20210319001&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e9%98%ae%e5%b0%8f%e8%8a%b8&code=48798538');
INSERT INTO `re_article_author` VALUES ('231', 'FileName=XDTQ20210319001&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%bb%96%e5%81%a5%e6%96%8c&code=48798540');
INSERT INTO `re_article_author` VALUES ('232', 'FileName=XDTQ20210319001&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%9d%8e%e7%a5%a5&code=28728513');
INSERT INTO `re_article_author` VALUES ('233', 'FileName=XDTQ20210319001&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%9d%a8%e9%98%b3&code=28741000');
INSERT INTO `re_article_author` VALUES ('234', 'FileName=XDTQ20210319001&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%9d%8e%e5%b2%b1%e5%b3%b0&code=43573473');
INSERT INTO `re_article_author` VALUES ('235', 'FileName=JSJC20210318004&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e8%bd%a6%e8%b6%85&code=32097134');
INSERT INTO `re_article_author` VALUES ('236', 'FileName=JSJC20210318004&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%88%98%e8%bf%aa&code=48794378');
INSERT INTO `re_article_author` VALUES ('237', 'FileName=ZGSM202106034&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e8%b5%b5%e7%94%9c&code=48814953');
INSERT INTO `re_article_author` VALUES ('238', 'FileName=ZGSM202106057&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e8%a3%b4%e6%95%8f&code=42026247');
INSERT INTO `re_article_author` VALUES ('239', 'FileName=SYJJ202106027&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e5%a7%9c%e6%97%ad&code=23551102');
INSERT INTO `re_article_author` VALUES ('240', 'FileName=SYJJ202106027&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e5%ad%9f%e7%b9%81%e5%ae%87&code=43035126');
INSERT INTO `re_article_author` VALUES ('241', 'FileName=XXWX2021031700R&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%b4%94%e5%91%98%e5%ae%81&code=43931005');
INSERT INTO `re_article_author` VALUES ('242', 'FileName=XXWX2021031700R&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%9d%8e%e9%9d%99&code=08725881');
INSERT INTO `re_article_author` VALUES ('243', 'FileName=XXWX2021031700R&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e9%99%88%e7%90%b0&code=30497703');
INSERT INTO `re_article_author` VALUES ('244', 'FileName=XXWX2021031700R&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e9%99%86%e6%ad%a3%e5%98%89&code=32474615');
INSERT INTO `re_article_author` VALUES ('245', 'FileName=SZYB20210317000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%ad%a3%e6%b0%b8%e6%9c%88&code=44514363');
INSERT INTO `re_article_author` VALUES ('246', 'FileName=SZYB20210317000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e9%99%88%e5%90%89%e9%be%99&code=33244603');
INSERT INTO `re_article_author` VALUES ('247', 'FileName=SZYB20210317000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%94%90%e9%9d%92%e9%9d%92&code=48763969');
INSERT INTO `re_article_author` VALUES ('248', 'FileName=SZYB20210317000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%90%b4%e8%83%9c%e5%86%9b&code=33234781');
INSERT INTO `re_article_author` VALUES ('249', 'FileName=SZYB20210317000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%99%8f%e9%bb%8e%e6%98%8e&code=21118445');
INSERT INTO `re_article_author` VALUES ('250', 'FileName=SSZK202102017&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e8%b5%b5%e9%93%b6%e7%ba%a2&code=22418064');
INSERT INTO `re_article_author` VALUES ('251', 'FileName=SSZK202102017&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e9%97%ab%e8%90%8d&code=48435357');
INSERT INTO `re_article_author` VALUES ('252', 'FileName=DBCH202103003&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e6%9b%be%e5%86%b0&code=35340566');
INSERT INTO `re_article_author` VALUES ('253', 'FileName=KJFT202108082&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e5%ae%8b%e4%bd%b3%e7%9b%8a&code=48764963');
INSERT INTO `re_article_author` VALUES ('254', 'FileName=JLGY20210317003&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e9%9b%b7%e6%99%af%e4%bd%a9&code=30844284');
INSERT INTO `re_article_author` VALUES ('255', 'FileName=JLGY20210317003&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%ac%a7%e9%98%b3%e4%b8%b9%e5%bd%a4&code=07669226');
INSERT INTO `re_article_author` VALUES ('256', 'FileName=JLGY20210317003&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%bc%a0%e7%ab%8b%e6%98%8e&code=17514809');
INSERT INTO `re_article_author` VALUES ('257', 'FileName=MKZD20210317000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%9b%b9%e7%8e%b0%e5%88%9a&code=09096271');
INSERT INTO `re_article_author` VALUES ('258', 'FileName=MKZD20210317000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%bc%a0%e6%a2%a6%e5%9b%ad&code=35786779');
INSERT INTO `re_article_author` VALUES ('259', 'FileName=MKZD20210317000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e9%9b%b7%e5%8d%93&code=44898352');
INSERT INTO `re_article_author` VALUES ('260', 'FileName=MKZD20210317000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%ae%b5%e6%ac%a3%e5%ae%87&code=48756474');
INSERT INTO `re_article_author` VALUES ('261', 'FileName=MKZD20210317000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e9%99%88%e7%91%9e%e6%98%8a&code=48756475');
INSERT INTO `re_article_author` VALUES ('262', 'FileName=JSJJ20210316009&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%ac%a7%e4%b8%80%e9%b8%a3&code=47084332');
INSERT INTO `re_article_author` VALUES ('263', 'FileName=JSJJ20210316009&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e8%8b%8f%e9%9b%8d%e8%b4%ba&code=47084333');
INSERT INTO `re_article_author` VALUES ('264', 'FileName=JSJJ20210316009&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e9%9d%b3%e5%81%a5&code=31346095');
INSERT INTO `re_article_author` VALUES ('265', 'FileName=JSJJ20210316009&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%80%aa%e7%8e%ae%e6%99%a8&code=36379329');
INSERT INTO `re_article_author` VALUES ('266', 'FileName=JSJJ20210316009&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e9%99%b6%e9%a3%9e&code=23979587');
INSERT INTO `re_article_author` VALUES ('267', 'FileName=SJKX20210316000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e7%8e%8b%e7%a6%8f%e6%b0%91&code=37533394');
INSERT INTO `re_article_author` VALUES ('268', 'FileName=SJKX20210316000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e8%83%a1%e8%bf%9c%e6%a8%9f&code=41154483');
INSERT INTO `re_article_author` VALUES ('269', 'FileName=SJKX20210316000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e9%93%b6%e5%ad%90%e6%b6%b5&code=40303444');
INSERT INTO `re_article_author` VALUES ('270', 'FileName=SJKX20210316000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e9%83%ad%e9%9b%a8%e6%80%a1&code=44259090');
INSERT INTO `re_article_author` VALUES ('271', 'FileName=SJKX20210316000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%9d%8e%e6%99%ba%e5%a8%81&code=43579378');
INSERT INTO `re_article_author` VALUES ('272', 'FileName=SDGY20210315001&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e9%be%9a%e4%b9%90%e5%90%9b&code=34511875');
INSERT INTO `re_article_author` VALUES ('273', 'FileName=SDGY20210315001&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%9d%a8%e7%92%90&code=36280603');
INSERT INTO `re_article_author` VALUES ('274', 'FileName=SDGY20210315001&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e9%ab%98%e5%bf%97%e5%ae%8f&code=33191483');
INSERT INTO `re_article_author` VALUES ('275', 'FileName=SDGY20210315001&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%9d%8e%e5%8d%8e%e5%ba%b7&code=30773842');
INSERT INTO `re_article_author` VALUES ('276', 'FileName=GXBJ20210315006&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%90%b4%e5%ae%97%e8%be%89&code=10731270');
INSERT INTO `re_article_author` VALUES ('277', 'FileName=GXBJ20210315006&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e8%8b%9f%e7%bf%a0%e8%90%8d&code=48737086');
INSERT INTO `re_article_author` VALUES ('278', 'FileName=GXBJ20210315006&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%9d%8e%e5%ae%b6%e8%81%98&code=43605104');
INSERT INTO `re_article_author` VALUES ('279', 'FileName=GXBJ20210315006&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%88%b4%e4%b8%bd&code=35406149');
INSERT INTO `re_article_author` VALUES ('280', 'FileName=NYJX20210312003&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e8%a2%81%e5%9f%b9%e6%a3%ae&code=31833256');
INSERT INTO `re_article_author` VALUES ('281', 'FileName=NYJX20210312003&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%9d%8e%e6%b6%a6%e9%9a%86&code=42636124');
INSERT INTO `re_article_author` VALUES ('282', 'FileName=NYJX20210312003&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e7%8e%8b%e7%bf%80&code=28755111');
INSERT INTO `re_article_author` VALUES ('283', 'FileName=NYJX20210312003&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%be%90%e7%84%95%e8%89%af&code=14241691');
INSERT INTO `re_article_author` VALUES ('284', 'FileName=XKKJ202103009&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e5%a4%8f%e6%a2%85%e6%a2%85&code=41142997');
INSERT INTO `re_article_author` VALUES ('285', 'FileName=XKKJ202103009&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e9%92%9f%e5%ae%9b%e5%87%8c&code=37906843');
INSERT INTO `re_article_author` VALUES ('286', 'FileName=XKKJ202103009&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e6%ac%a7%e9%98%b3%e9%87%8c%e5%b1%b1&code=43180906');
INSERT INTO `re_article_author` VALUES ('287', 'FileName=XKKJ202103009&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e5%ad%99%e5%bf%97%e8%93%89&code=06436433');
INSERT INTO `re_article_author` VALUES ('288', 'FileName=XKKJ202103009&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e5%bc%a0%e5%ad%90%e9%be%99&code=17441430');
INSERT INTO `re_article_author` VALUES ('289', 'FileName=TSGT20210311009&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%9e%97%e6%99%93%e6%ac%a3&code=33806502');
INSERT INTO `re_article_author` VALUES ('290', 'FileName=XAJD20210319000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%8d%ab%e6%99%a8%e6%9b%99&code=47959806');
INSERT INTO `re_article_author` VALUES ('291', 'FileName=YXXB20210319003&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%88%98%e6%b6%a6%e5%93%b2&code=48796971');
INSERT INTO `re_article_author` VALUES ('292', 'FileName=YXXB20210319003&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%ae%8b%e4%bf%8a%e7%a7%91&code=25161339');
INSERT INTO `re_article_author` VALUES ('293', 'FileName=YXXB20210319003&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%88%98%e8%89%be%e6%9e%97&code=22814902');
INSERT INTO `re_article_author` VALUES ('294', 'FileName=YXXB20210319003&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%9d%9c%e5%86%a0%e5%8d%8e&code=21768183');
INSERT INTO `re_article_author` VALUES ('295', 'FileName=GRKZ202103019&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e6%9d%8e%e5%b0%91%e5%bc%ba&code=35223260');
INSERT INTO `re_article_author` VALUES ('296', 'FileName=GRKZ202103019&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e5%88%98%e6%b5%a9&code=28592716');
INSERT INTO `re_article_author` VALUES ('297', 'FileName=GRKZ202103019&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e9%83%ad%e6%96%87%e4%ba%ae&code=35219867');
INSERT INTO `re_article_author` VALUES ('298', 'FileName=GRKZ202103019&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e5%91%a8%e5%9c%86%e5%9c%86&code=29320962');
INSERT INTO `re_article_author` VALUES ('299', 'FileName=GRKZ202103019&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e6%9d%8e%e6%97%b6%e6%82%a6&code=35219869');
INSERT INTO `re_article_author` VALUES ('300', 'FileName=JSJY20210312000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%88%98%e5%ad%90%e8%be%b0&code=32199509');
INSERT INTO `re_article_author` VALUES ('301', 'FileName=JSJY20210312000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%9d%8e%e5%b0%8f%e5%a8%9f&code=28319591');
INSERT INTO `re_article_author` VALUES ('302', 'FileName=JSJY20210312000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e9%9f%a6%e4%bc%9f&code=36764411');
INSERT INTO `re_article_author` VALUES ('303', 'FileName=MKZD20210311000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e8%83%a1%e9%9d%92%e6%9d%be&code=09654578');
INSERT INTO `re_article_author` VALUES ('304', 'FileName=MKZD20210311000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e9%92%b1%e5%bb%ba%e7%94%9f&code=09655759');
INSERT INTO `re_article_author` VALUES ('305', 'FileName=MKZD20210311000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%9d%8e%e4%b8%96%e9%93%b6&code=09654937');
INSERT INTO `re_article_author` VALUES ('306', 'FileName=MKZD20210311000&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%ad%99%e5%bd%a6%e6%99%af&code=09656397');
INSERT INTO `re_article_author` VALUES ('307', 'FileName=DSJU20210319001&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e5%bc%a0%e8%99%8e&code=08403299');
INSERT INTO `re_article_author` VALUES ('308', 'FileName=DSJU20210319001&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%bd%98%e9%82%a6%e6%b3%bd&code=48773676');
INSERT INTO `re_article_author` VALUES ('309', 'FileName=DSJU20210319001&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e8%b0%ad%e7%ba%a2%e5%8f%b6&code=08402552');
INSERT INTO `re_article_author` VALUES ('310', 'FileName=DSJU20210319001&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e6%9d%8e%e8%8c%b9&code=08453268');
INSERT INTO `re_article_author` VALUES ('311', 'FileName=QBZZ20210310001&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e8%b0%a2%e7%90%aa%e5%bd%ac&code=46059265');
INSERT INTO `re_article_author` VALUES ('312', 'FileName=QBZZ20210310001&DbName=CAPJLAST&DbCode=CAPJ&', 'dbcode=CAPJ&sfield=au&skey=%e7%9f%b3%e5%ae%87&code=48703447');
INSERT INTO `re_article_author` VALUES ('313', 'FileName=ZYJU202104020&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e5%af%87%e7%ab%8b%e7%be%8e&code=48719101');
INSERT INTO `re_article_author` VALUES ('314', 'FileName=ZYJU202104020&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e4%be%af%e6%87%bf&code=48766699');
INSERT INTO `re_article_author` VALUES ('315', 'FileName=GJXK202110007&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e6%b1%aa%e6%b4%aa%e6%a1%a5&code=35556429');
INSERT INTO `re_article_author` VALUES ('316', 'FileName=GJXK202110007&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e8%94%a1%e8%89%b3%e5%ae%81&code=48767442');
INSERT INTO `re_article_author` VALUES ('317', 'FileName=GJXK202110007&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e4%bc%8d%e6%98%8e&code=36145256');
INSERT INTO `re_article_author` VALUES ('318', 'FileName=GJXK202110007&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e4%bb%98%e5%85%89%e8%bf%9c&code=35497819');
INSERT INTO `re_article_author` VALUES ('319', 'FileName=GJXK202110007&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e9%ad%8f%e6%8c%af%e5%8d%8e&code=36065976');
INSERT INTO `re_article_author` VALUES ('320', 'FileName=CGZC202103027&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e6%a8%8a%e5%87%a4%e4%bb%99&code=45437932');
INSERT INTO `re_article_author` VALUES ('321', 'FileName=CGZC202103027&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e5%a7%9c%e8%89%b3%e4%b8%bd&code=30941260');
INSERT INTO `re_article_author` VALUES ('322', 'FileName=CGZC202103027&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e7%8e%8b%e4%bf%8a&code=45437933');
INSERT INTO `re_article_author` VALUES ('323', 'FileName=CGZC202103027&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e9%bb%84%e6%96%87%e9%9d%99&code=45437931');
INSERT INTO `re_article_author` VALUES ('324', 'FileName=CGZC202103027&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e5%bc%a0%e9%b9%8f%e9%a3%9e&code=45437934');
INSERT INTO `re_article_author` VALUES ('325', 'FileName=JXUY202108031&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e9%99%88%e6%98%8e%e8%93%89&code=48794369');
INSERT INTO `re_article_author` VALUES ('326', 'FileName=JXUY202108031&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e5%ba%9e%e5%86%ac%e8%8c%b9&code=48794370');
INSERT INTO `re_article_author` VALUES ('327', 'FileName=JXUY202108031&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e6%a2%81%e7%87%95%e5%a9%b7&code=48794371');
INSERT INTO `re_article_author` VALUES ('328', 'FileName=JXUY202108031&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e6%9b%be%e7%91%9e%e6%b6%93&code=48794372');
INSERT INTO `re_article_author` VALUES ('329', 'FileName=JXUY202108031&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e5%a7%9c%e8%8d%a3%e8%8d%a3&code=35224999');
INSERT INTO `re_article_author` VALUES ('330', 'FileName=HXYK202102001&DbName=CJFDAUTO&DbCode=CJFD&', 'dbcode=CJFD&sfield=au&skey=%e6%ad%a5%e5%ae%8f&code=15436278');

-- ----------------------------
-- Table structure for re_article_source
-- ----------------------------
DROP TABLE IF EXISTS `re_article_source`;
CREATE TABLE `re_article_source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url_article` varchar(255) DEFAULT NULL COMMENT '文章链接',
  `url_source` varchar(255) DEFAULT NULL COMMENT '来源链接',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=102 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of re_article_source
-- ----------------------------
INSERT INTO `re_article_source` VALUES ('64', 'FileName=XDTQ20210319001&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=XDTQ');
INSERT INTO `re_article_source` VALUES ('65', 'FileName=JSJC20210318004&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=JSJC');
INSERT INTO `re_article_source` VALUES ('66', 'FileName=ZGSM202106034&DbName=CJFDAUTO&DbCode=CJFD&', 'DBCode=CJFD&BaseID=ZGSM');
INSERT INTO `re_article_source` VALUES ('67', 'FileName=ZGSM202106057&DbName=CJFDAUTO&DbCode=CJFD&', 'DBCode=CJFD&BaseID=ZGSM');
INSERT INTO `re_article_source` VALUES ('68', 'FileName=SYJJ202106027&DbName=CJFDAUTO&DbCode=CJFD&', 'DBCode=CJFD&BaseID=SYJJ');
INSERT INTO `re_article_source` VALUES ('69', 'FileName=XXWX2021031700R&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=XXWX');
INSERT INTO `re_article_source` VALUES ('70', 'FileName=SZYB20210317000&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=SZYB');
INSERT INTO `re_article_source` VALUES ('71', 'FileName=SSZK202102017&DbName=CJFDAUTO&DbCode=CJFD&', 'DBCode=CJFD&BaseID=SSZK');
INSERT INTO `re_article_source` VALUES ('72', 'FileName=DBCH202103003&DbName=CJFDAUTO&DbCode=CJFD&', 'DBCode=CJFD&BaseID=DBCH');
INSERT INTO `re_article_source` VALUES ('73', 'FileName=KJFT202108082&DbName=CJFDAUTO&DbCode=CJFD&', 'DBCode=CJFD&BaseID=KJFT');
INSERT INTO `re_article_source` VALUES ('74', 'FileName=JLGY20210317003&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=JLGY');
INSERT INTO `re_article_source` VALUES ('75', 'FileName=MKZD20210317000&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=MKZD');
INSERT INTO `re_article_source` VALUES ('76', 'FileName=JSJJ20210316009&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=JSJJ');
INSERT INTO `re_article_source` VALUES ('77', 'FileName=SJKX20210316000&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=SJKX');
INSERT INTO `re_article_source` VALUES ('78', 'FileName=SDGY20210315001&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=SDGY');
INSERT INTO `re_article_source` VALUES ('79', 'FileName=GXBJ20210315006&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=GXBJ');
INSERT INTO `re_article_source` VALUES ('80', 'FileName=NYJX20210312003&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=NYJX');
INSERT INTO `re_article_source` VALUES ('81', 'FileName=XKKJ202103009&DbName=CJFDAUTO&DbCode=CJFD&', 'DBCode=CJFD&BaseID=XKKJ');
INSERT INTO `re_article_source` VALUES ('82', 'FileName=TSGT20210311009&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=TSGT');
INSERT INTO `re_article_source` VALUES ('83', 'FileName=XAJD20210323001&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=XAJD');
INSERT INTO `re_article_source` VALUES ('84', 'FileName=XAJD20210319000&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=XAJD');
INSERT INTO `re_article_source` VALUES ('85', 'FileName=YXXB20210319003&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=YXXB');
INSERT INTO `re_article_source` VALUES ('86', 'FileName=GRKZ202103019&DbName=CJFDAUTO&DbCode=CJFD&', 'DBCode=CJFD&BaseID=GRKZ');
INSERT INTO `re_article_source` VALUES ('87', 'FileName=SZTQ20210323B021&DbName=CCNDTEMP&DbCode=CCND&', 'DBCode=CCND&BaseID=SZTQ');
INSERT INTO `re_article_source` VALUES ('88', 'FileName=RMZX202103230052&DbName=CCNDTEMP&DbCode=CCND&', 'DBCode=CCND&BaseID=RMZX');
INSERT INTO `re_article_source` VALUES ('89', 'FileName=RMZX202103230064&DbName=CCNDTEMP&DbCode=CCND&', 'DBCode=CCND&BaseID=RMZX');
INSERT INTO `re_article_source` VALUES ('90', 'FileName=KXSB202103230070&DbName=CCNDTEMP&DbCode=CCND&', 'DBCode=CCND&BaseID=KXSB');
INSERT INTO `re_article_source` VALUES ('91', 'FileName=JSJY20210312000&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=JSJY');
INSERT INTO `re_article_source` VALUES ('92', 'FileName=MKZD20210311000&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=MKZD');
INSERT INTO `re_article_source` VALUES ('93', 'FileName=DSJU20210319001&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=DSJU');
INSERT INTO `re_article_source` VALUES ('94', 'FileName=QBZZ20210310001&DbName=CAPJLAST&DbCode=CAPJ&', 'DBCode=CAPJ&BaseID=QBZZ');
INSERT INTO `re_article_source` VALUES ('95', 'FileName=ZYJU202104020&DbName=CJFDAUTO&DbCode=CJFD&', 'DBCode=CJFD&BaseID=ZYJU');
INSERT INTO `re_article_source` VALUES ('96', 'FileName=GJXK202110007&DbName=CJFDAUTO&DbCode=CJFD&', 'DBCode=CJFD&BaseID=GJXK');
INSERT INTO `re_article_source` VALUES ('97', 'FileName=CGFB202103220041&DbName=CCNDTEMP&DbCode=CCND&', 'DBCode=CCND&BaseID=CGFB');
INSERT INTO `re_article_source` VALUES ('98', 'FileName=JRSB202103220121&DbName=CCNDTEMP&DbCode=CCND&', 'DBCode=CCND&BaseID=JRSB');
INSERT INTO `re_article_source` VALUES ('99', 'FileName=CGZC202103027&DbName=CJFDAUTO&DbCode=CJFD&', 'DBCode=CJFD&BaseID=CGZC');
INSERT INTO `re_article_source` VALUES ('100', 'FileName=JXUY202108031&DbName=CJFDAUTO&DbCode=CJFD&', 'DBCode=CJFD&BaseID=JXUY');
INSERT INTO `re_article_source` VALUES ('101', 'FileName=HXYK202102001&DbName=CJFDAUTO&DbCode=CJFD&', 'DBCode=CJFD&BaseID=HXYK');

-- ----------------------------
-- Table structure for re_author_school
-- ----------------------------
DROP TABLE IF EXISTS `re_author_school`;
CREATE TABLE `re_author_school` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url_author` varchar(255) DEFAULT NULL COMMENT '作者链接',
  `url_school` varchar(255) DEFAULT NULL COMMENT '学校链接',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of re_author_school
-- ----------------------------

-- ----------------------------
-- Table structure for re_teacher_student
-- ----------------------------
DROP TABLE IF EXISTS `re_teacher_student`;
CREATE TABLE `re_teacher_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url_teacher` varchar(255) DEFAULT NULL COMMENT '老师链接',
  `url_student` varchar(255) DEFAULT NULL COMMENT '学生链接',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of re_teacher_student
-- ----------------------------

-- ----------------------------
-- Table structure for school
-- ----------------------------
DROP TABLE IF EXISTS `school`;
CREATE TABLE `school` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) DEFAULT NULL COMMENT '链接',
  `name` varchar(255) DEFAULT NULL COMMENT '名称',
  `name_used` varchar(255) DEFAULT NULL COMMENT '曾用名',
  `region` varchar(255) DEFAULT NULL COMMENT '地域',
  `official_website` varchar(255) DEFAULT NULL COMMENT '官网',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of school
-- ----------------------------

-- ----------------------------
-- Table structure for source_journal
-- ----------------------------
DROP TABLE IF EXISTS `source_journal`;
CREATE TABLE `source_journal` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) DEFAULT NULL COMMENT '链接',
  `name` varchar(255) DEFAULT NULL COMMENT '名称',
  `name_en` varchar(255) DEFAULT NULL COMMENT '英文名称',
  `journals` varchar(255) DEFAULT NULL COMMENT '收录机构',
  `basic_info` varchar(255) DEFAULT NULL COMMENT '基本信息',
  `album` varchar(255) DEFAULT NULL COMMENT '专辑',
  `special` varchar(255) DEFAULT NULL COMMENT '专题',
  `count_publish` varchar(255) DEFAULT NULL COMMENT '出版文献量',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of source_journal
-- ----------------------------

-- ----------------------------
-- Table structure for source_school
-- ----------------------------
DROP TABLE IF EXISTS `source_school`;
CREATE TABLE `source_school` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(255) DEFAULT NULL COMMENT '链接',
  `name` varchar(255) DEFAULT NULL COMMENT '名称',
  `name_used` varchar(255) DEFAULT NULL COMMENT '曾用名',
  `region` varchar(255) DEFAULT NULL COMMENT '地域',
  `count_articles` varchar(255) DEFAULT NULL COMMENT '文献篇数',
  `count_refer` varchar(255) DEFAULT NULL COMMENT '总被引次数',
  `count_downloads` varchar(255) DEFAULT NULL COMMENT '总下载次数',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of source_school
-- ----------------------------
