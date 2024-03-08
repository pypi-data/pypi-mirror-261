CREATE TABLE `tcs_guide_star_cat` (
  `gscID2` int(11),
  `gsc1ID` varchar(11),
  `hstID` varchar(11),
  `RightAsc` double,
  `Declination` double,
  `PositionEpoch` float,
  `raEpsilon` float,
  `decEpsilon` float,
  `raProperMotion` float,
  `decProperMotion` float,
  `raProperMotionErr` float,
  `decProperMotionErr` float,
  `deltaEpoch` float,
  `FpgMag` float,
  `FpgMagErr` float,
  `FpgMagCode` smallint(6),
  `JpgMag` float,
  `JpgMagErr` float,
  `JpgMagCode` smallint(6),
  `VMag` float,
  `VMagErr` float,
  `VMagCode` smallint(6),
  `NpgMag` float,
  `NpgMagErr` float,
  `NpgMagCode` smallint(6),
  `UMag` float,
  `UMagErr` float,
  `UMagCode` smallint(6),
  `BMag` float,
  `BMagErr` float,
  `BMagCode` smallint(6),
  `RMag` float,
  `RMagErr` float,
  `RMagCode` smallint(6),
  `IMag` float,
  `IMagErr` float,
  `IMagCode` smallint(6),
  `JMag` float,
  `JMagErr` float,
  `JMagCode` smallint(6),
  `HMag` float,
  `HMagErr` float,
  `HMagCode` smallint(6),
  `KMag` float,
  `KMagErr` float,
  `KMagCode` smallint(6),
  `classification` int(11),
  `semiMajorAxis` float,
  `eccentricity` float,
  `positionangle` float,
  `sourceStatus` int(11),
  `variableFlag` int(11),
  `multipleFlag` int(11),
  `htm20ID` bigint(20) unsigned,
  `htm16ID` bigint(20) unsigned,
  `cx` double,
  `cy` double,
  `cz` double,
  KEY `key_hstID` (`hstID`),
  KEY `idx_htm20ID` (`htm20ID`),
  KEY `idx_htm16ID` (`htm16ID`),
  KEY `idx_RightAscDeclination` (`RightAsc`,`Declination`)
) ENGINE=MyISAM;
