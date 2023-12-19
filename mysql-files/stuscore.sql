
#创建名为stuCourse的数据库。
create database stucourse;
use  stucourse;

 
create table student
(
   sid char(10) not null primary key,
   sname char(8) not null,
   sex char(2) null,
   age int null,
   dept varchar(20) null
);

insert into student values
('1001', '宋江',      '男',  '25',  '计算机系'),
('3002', '张明',     '男',  '23',  '生物系' ),
('1003', '李小鹏',   '男',  '26',  '计算机系' ),
('1004', '郑冬',     '女',  '25',  '计算机系' ),
('4005', '李小红',   '女',  '27',  '工商管理' ),
('5006', '赵紫月',   '女',  '24',  '外语系'); 



create table teacher
(
  tid char(10) not null primary key,
  tname char(8) not null,
  title varchar(20) ,
  salary float,
  dept varchar(20),
  cid char(10)
);

insert into teacher values
('3102',  '李明',       '初级',   '2500',   '计算机系',    'C1'),
('3108',  '黄小明',     '初级',   '4000',   '生物系',      'C3' ),
('4105',  '张小红',     '中级',   '3500',   '工商管理',    'C2'),
('5102',  '宋力月',     '高级',   '3500',   '物理系',      'C4' ),
('3106',  '赵明阳',     '初级',   '1500',   '地理系',      'C2'),
('7108',  '张丽',       '高级',   '3500',   '生物系',      'C3' ),
('9103',  '王彬',       '高级',   '3500',   '计算机系',    'C1'),
('7101',  '王力号',     '初级',   '1800',   '生物系',      'C1' ); 


create table courseinfo
(
   cid char(10) primary key not null,
   cname varchar(20), 
   cbook char(10),
   ctest datetime, 
   dept varchar(10)
);



insert into courseinfo values
('C1',   '计算机基础',     'b1231',    '2009-4-6',    '计算机系'),
('C2',   '工商管理基础',   'b1232',    '2009-7-16',   '工商管理'),
('C3',   '生物科学',       'b1233',    '2010-3-6',    '生物系'),
('C4',   '大学物理',       'b1234',    '2009-4-26',   '物理系' ),
('C5',   '数据库原理',     'b1235',    '2010-2-6',    '计算机系');  



create table bookinfo  
(
    bid char(10) primary key,
    bname varchar(30),
    bpublish  varchar(30),
    bprice double(5,2),
    quantity int
);

insert into bookinfo values
('b1231',    'Image Processing',           '人民出版社',   '34.56',  8 ),
('b1232',    'Signal Processing',          '清华出版社',   '51.75',  10),
('b1233',    'Digital Signal Processing',  '邮电出版社',   '48.5',   11 ),
('b1234',    'The Logic Circuit',          '北大出版社',   '49.2',   40),
('b1235',    'SQL Techniques',             '邮电出版社',   '65.4',   20 ); 



create table scourse
(
   sid char(10) not null ,
   score int  null,
   cid char(5)  null,
   tid char(10)
);

insert into scourse values
('1001',  87,   'C1',   '3102'),
('1001',  77,   'C2',   '4105' ),
('1001',  63,   'C3',   '3108' ),
('1001',  56,   'C4',   '3108'),
('3002',  78,   'C3',   '3108'),
('3002',  78,   'C4',   '5102' ),
('1003',  89,   'C1',   '9103'),
('1004',  56,   'C2',   '3106'),
('4005',  87,   'C4',   '5102' ),
('5006',  null, 'C1',   '7101');