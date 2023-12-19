/*
 Navicat Premium Data Transfer

 Source Server         : root
 Source Server Type    : MySQL
 Source Server Version : 80021
 Source Host           : localhost:3306
 Source Schema         : model

 Target Server Type    : MySQL
 Target Server Version : 80021
 File Encoding         : 65001

 Date: 19/12/2023 16:03:48
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Function structure for rand_rand
-- ----------------------------
DROP FUNCTION IF EXISTS `rand_rand`;
delimiter ;;
CREATE FUNCTION `rand_rand`(i int)
 RETURNS varchar(9999) CHARSET utf8mb4
begin
declare a int default 0;
declare b varchar(9999) default "";

e:while a < i do

set a = a + 1;
select concat(b,truncate(rand() * 10,0)) into b;

if a = 1 and b = '0' then
set a = 0;
set b = "";
iterate e;
end if;

end while;

return b; 
end
;;
delimiter ;

-- ----------------------------
-- Function structure for rand_randa
-- ----------------------------
DROP FUNCTION IF EXISTS `rand_randa`;
delimiter ;;
CREATE FUNCTION `rand_randa`(i int, u int)
 RETURNS varchar(999) CHARSET utf8mb4
begin
declare a varchar(999) default "";
select truncate((rand() * (u-i)) + i,0) into a;
return a;
end
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
