drop database if exists bookshop;


create database bookshop;



use bookshop;

create table category
(
   caid  char(2) not null primary key,
   caname  varchar(20),
   cadeleted bit
);

 INSERT INTO category(caid ,caname,cadeleted) VALUES
('01','自然科学',0),
('02','医学卫生',0),
('03','旅游地理',0),
('04','青春文学',1),
('05','软件开发',0),
('06','人工智能',0),
('07','计算机理论',0),
('08','电子电工电信',0),
('09','临床医学',0),
('10','工业技术',0);


create table customers
(
  cid  char(6) not null primary key,
  ctruename  varchar(50),
  cpassword varchar(50),
  csex  char(2),
  caddress  varchar(50),
  cmobile  varchar(11),
  cemail  varchar(50),
  cregisterdate  datetime
);



insert into customers(cid,ctruename,cpassword,csex,caddress,cmobile,cemail,cregisterdate)values
('c0001','刘小和','123456','男','广东广州市','13512612846','liuxh@163.com','2009/8/6' ),
( 'c0002','张嘉靖','123456','男','广东广州市','13544345647','zhangjj002@163.com','2010/9/4'),
( 'c0003','罗红红','123456','女','广东珠海市','13556786472','','2008/11/24' ),
('c0004','李浩华','123456','女','广东珠海市','13634215643','lihaohua@163.com','2008/11/24'),
( 'c0005','吴美霞','123456','女','湖南长沙市','13643256756','wumeixia@163.com','2010/10/22'),
( 'c0006','陈毅名','123456','男','江西南昌市','13978657860','chenym@163.com','2010/12/21' ),
('c0007','黄小波','123456','男','湖北武汉市','13845637569','huangxb@163.com','2011/1/22'),
('c0008','张丰盛','123456','男','广西桂林市','13644556789','zhangfs@163.com','2009/7/25'),
( 'c0009','许志敏','123456','女','广东珠海市','13966885897','xzhiming@163.com','2011/1/6' ),
( 'c0010','王天成','123456','男','广东佛山市','13643256789','wangtc@163.com','2007/7/24' );

create table goods
(
  gid  char(6)  not null primary key,
  gname  varchar(50),
  gtypeid  char(2)  references catogory(caid),
  gwriter  varchar(50),
  gpublisher  varchar(50),
  gISBN  varchar(50),
  gprice  double,
  gnumber  int
);
 


		
insert into goods( gid,gname ,gtypeid, gwriter,gpublisher,gISBN,gprice ,gnumber)values
( '010001','高分子物理','01','何曼君','复旦大学出版社','9787309054145','35','200'),
(  '020001','现代遗传学','02','赵寿元','高等教育出版社','9787040239737','36','100'),
( '030001','野外求生宝典','03','梶原玲','南海出版社','9787544240345','28','150' ),
(  '030002','欧洲日记','03','张明','湖南教育出版社','9787224240341','60','200' ),
(  '030003','西藏行','03','毛毛','湖南教育出版社','9787224240342','50','100' ),
( '040001','游园惊梦','04','夏达明','湖南少儿出版社','9787535838823','24','250' ),
(  '050001','软件工程导论','05','张海藩','清华大学出版社','9787302164745','35','300'),
( '050002','软件架构设计','05','张海藩','清华大学出版社','9787302164748','40','200' ),
( '050003','走进软件世界','05','刘一明','科学出版社','9787030189609','30','100' ),
( '060001','自动控制原理','06','胡寿松','科学出版社','9787030189654','52','150'),
( '070001','算法导论','07','科曼','机械工业出版社','9787111187712','85','250' );

create table comment
(
  cmid  char(6) not null primary key,
  cmcommenderid  char(6) references customers(cid),
  cmbookid char(6)   references goods(gid),
  cmtitle varchar(200),
  cmcontent text,
  cmdate  datetime
);
   
insert into comment(cmid ,cmcommenderid,cmbookid,cmtitle ,cmcontent,cmdate  )values
( '0001','c0001','010001','书很不错','我很喜欢这本书 ',' 2011/6/10'),
( '0002','c0002','010001','书应该是正版的','书写得不错，里面的插图也很详细','2011/6/10'),
(  '0003','c0003','030001','强烈推荐','强烈推荐大家看这本书，值得一看','2011/6/15' ),
( '0004','c0007','040001','书里内容很详细！！','内容详细，适合初学者','2011/8/29' ),
( '0005','c0004','060001','书写得一般','里面内容写得一般。','2011/8/28' );

-- mysql –u root –p --execute="SELECT * FROM comment;" bookshop>D:\bak_comment.txt


create table manager
(
  maid  char(10) not null primary key,
  maname  varchar(30),
  masex  char(2),
  mamobile  varchar(11),
  maemail varchar(50)
);
 
insert into  manager(maid ,maname ,masex,mamobile,maemail)values
( 'm0001','李璐','女','13393849807','lilu@163.com' ),
( 'm0002','张小杰','男','13328379293','zhangxj@163.com'),
(  'm0003','王子民','男','13328379282','wangzm@163.com' ),
(  'm0004','刘蕾','女','13328379267','liulei@163.com' ),
( 'm0005','文知东','男','13328379457','wenzhidong@163.com'); 


create table orders
(
  oid  char(14)  not null primary key,
  cid  char(6) ,
  odate  datetime,
  osum  double,
  ostatus  char(1)
) ;



		       

insert into orders(oid, cid,odate,osum,ostatus)values
( '201106051011','c0001','2011/6/5','106','0'),
('201106051022','c0002','2011/6/5','35','0' ),
('201106051023','c0003','2011/6/5','200','1' ),
( '201108231012','c0004','2011/8/23','240','1' ),
('201108231210','c0005','2011/8/23','480','0' ),
('201108231342','c0006','2011/8/23','293','0'  ),
( '201109201130','c0006','2011/9/20','170','0' );

create table orderdetails
(
  orid  char(6) not null primary key,
  oid  char(14)  references  orders(oid),
  gid  char(6)  references goods(gid),
  odprice double,
  odnumber  int 
);

     	  			
insert into  orderdetails(orid ,oid,gid,odprice,odnumber)values
( '1','201106051011','010001','70','2'),
('2','201106051011','020001','36','1' ),
('3','201106051022 ','010001','35','1' ),
('4','201106051023','030001','140','5'),
('5','201106051023','030002','60','1'),
('6','201108231012','040001','240','10' ),
( '7','201108231210','040001','480','20' ),
('8','201108231342 ','060001','208','4' ),
( '9','201108231342','070001','85','1'),
( '10','201109201130','070001','170','2' );



create table shopcar
(
  scid  char(6) not null primary key,
  cid  char(6)  references customers(cid),
  gid  char(6)  references goods(gid),
  gname  varchar(50),
  gprice  double,
  gnumber  int
);

insert into shopcar(scid,cid,gid,gname,gprice,gnumber)values
( 's10604','c0001 ','010001','高分子物理','35','2' ),
( 's10608','c0002','010001','高分子物理','35','3'),
( 's10609','c0003','030001','野外求生宝典','28','1' ),
( 's10615','c0007','040001','游园惊梦','24','8' ),
('s10826','c0004','060001','自动控制原理','52','2' );