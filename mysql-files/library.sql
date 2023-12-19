drop database if exists  library;
create database library;

use library;
create table booktype
(
   typeid int not null primary key,
   typename varchar(20)  
);

insert into booktype values
('1','自然科学'),
('2','数学'),
('3','计算机' ),
('4','建筑水利' ),
('5','旅游地理' ),
('6','励志/自我实现' ),
('7','工业技术' ),
('8','基础医学' ),
('9','室内设计' ),
('10','人文景观' );


#借阅次数
create table book
(
   bookid char(10) not null primary key,
   bookname varchar(20) not null,
   typeid int  references booktype(typeid) ,
   bookauthor varchar(20),
   bookpublisher varchar(50),
   bookprice double,
   borrowsum int    
);
insert into book values
('TP39/1712' ,'JAVA程序设计','3' ,'陈永红','机械工业出版社',35.5,30 ),
('013452' ,'离散数学','2' ,'张小新','清华大学出版社',45.5,10 ),
('TP/3452' ,'JSP程序设计案例','3' ,'刘城清','电子工业出版社',42.8,8),
('TH/2345' ,'机械设计手册','7' ,'黄明凡','人民邮电出版社',40,10 ),
('R/345677' ,'中医的故事','8' ,'李奇德','国防工业出版社',20.0,5 );



create table bookstorage
(
    bookbarcode char(20) not null  primary key,
    bookid char(10) not null references book(bookid),
    bookintime datetime,
    bookstatus varchar(4)
);
insert into bookstorage values
('132782','TP39/1712','2009-8-10','在馆' ),
( '132789','TP39/1712','2009-8-10','借出' ),
( '145234','013452','2008-12-6','借出'),
( '145321','TP/3452','2007-11-4','借出' ),
( '156833','TH/2345','2009-12-4','借出'),
( '345214','R/345677','2008-11-3','在馆');




create table readertype
(
   retypeid int not null primary key,
   typename varchar(20) not null,
   borrowquantity int not null,
   borrowday int 
);
insert into readertype values
('1','学生','10','30'),
('2','教师','20','60' ),
('3','管理员','15','30'),
('4','职工','15','20' );


 
create table reader
(
   readerid char(10) not null  primary key,
   readername varchar(20) not null,
   readerpass varchar(20) not null,
   retypeid int  references  readertype(typeid),
   readerdate datetime , 
   readerstatus varchar(4)
);
insert into reader values
('0016','苏小东','123456','1','1999-8-9','有效'),
('0017','张明','123456','1','2010-9-10','有效'  ),
('0018','梁君红','123456','1','2010-9-10','有效'  ),
('0021','赵清远','123456','2','2010-7-1','有效'),
('0034','李瑞清','123456','3','2009-8-3','有效' ),
('0042','张明月','123456','4','1997-4-23','有效');



create table bookborrow
(
    borrowid char(10) not null primary key, 
    bookbarcode  char(20) references bookstorage(bookbarcode) ,
    readerid char(10) references reader(readerid),
    borrowtime datetime,
    returntime datetime,
    borrowstatus varchar(4)
);
insert into bookborrow values
('001432','132782','0016','2011-3-4','2011-4-5','已还'),
('001328','132789','0017','2011-1-24','2011-2-28','已还'),
('001356','145234','0018','2011-2-12','2011-2-27','已还'),
('001435','145321','0021','2011-8-9','2011-9-2','已还' ),
('001578','156833','0034','2011-10-1','2011-11-1','未还'),
('001679','345214','0042','2011-2-21','2011-3-5','未还' );












