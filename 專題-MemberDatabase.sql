-- creat database
create database member_database;
use member_database;
-- drop database member_database;
-- drop table member_basic;

-- 1.Table member_basic
create table member_basic(
user_id int primary key auto_increment,
user_name varchar(20) not null unique,
user_password varchar(128) not null,
user_phone varchar(10) not null unique,
user_email varchar(120) not null unique,
user_nickname varchar(20) null,
user_gender varchar(10) null,
user_birth date null,
user_address text null,
vip_status int(1) default '0',
user_avatar varchar(50) null default 'default.png',
privacy_id int null,
created_at timestamp default current_timestamp,
updated_at timestamp default current_timestamp on update current_timestamp
-- foreign key (user_avatar) references member_photo(user_avatar) ON DELETE CASCADE
);

insert into member_basic(user_name, user_password, user_phone, user_email, user_nickname, user_gender, user_birth)
values
('Amanda', '1234qweasd', '0912123128', 'Amanda@gmail.com', '阿曼答', '女', '1996-10-15'),
('Brian', '1234qweasd', '0912123127', 'Brian@gmail.com', '布萊恩', '男', '2000-01-15'),
('Cally', '1234qweasd', '0912123126', 'Cally@gmail.com', '可立', '女', '1999-12-15'),
('Daniel', '1234qweasd', '0912123125', 'Daniel@gmail.com', '丹尼', '不願透漏', '1986-03-29'),
('Eddie', '1234qweasd', '0912123124', 'Eddie@gmail.com', '艾迪', '男', '2012-02-10'),
('Jessica', '1234qweasd', '0912123123', 'Jessica@gmail.com', '潔西卡', '女', '1987-10-26'),
('Ashley', '1234qweasd', '0912345673', 'Ashley@gmail.com', '愛須', '女', '1988-12-15'),
('Jay', '1234qweasd', '0912345672', 'forworkjayjay@gmail.com', '杰', '不願透漏', '2000-11-11'),
('Rosa', '1234qweasd', '0912345671', 'Rosa@gmail.com', '蘿莎', '女', '1988-10-15'),
('Jeremy', '1234qweasd', '0912345670', 'yuhaohong@gmail.com', '傑若米', '男', '1987-08-22'),
('Monica', '1234qweasd', '0912345600', 'Monica@gmail.com', '莫妮卡', '女', '2012-03-30');

-- 2.Table member_login
create table member_login(
login_id int primary key,
user_id int not null,
provider varchar(50) null,
provider_id_google varchar(50) null unique,
provider_id_line varchar(50) null unique,
provider_id_fb varchar(50) null unique,
access_token varchar(50) null unique,
created_at timestamp default current_timestamp,
updated_at timestamp default current_timestamp on update current_timestamp,
foreign key (user_id) references member_basic(user_id) ON DELETE CASCADE
);
select * from member_login;

-- 3.Table member_privacy
create table member_privacy(
privacy_id int primary key auto_increment,
user_id int not null,
user_email varchar(120),
privacy_name varchar(50) null,
privacy_value boolean default '0',
phone_change varchar(10) null unique,
email_change varchar(50) null unique,
account_verify boolean default "0",
activity_checked boolean default "0",
double_verify boolean default "0",
created_at timestamp default current_timestamp,
updated_at timestamp default current_timestamp on update current_timestamp,
foreign key (user_id) references member_basic(user_id) ON DELETE CASCADE
);
select * from member_privacy;
insert into member_privacy(user_id, user_email)
values
('1','Amanda@gmail.com'),
('2','Brian@gmail.com'),
('3','Cally@gmail.com'),
('4','Daniel@gmail.com'),
('5','Eddie@gmail.com'),
('6','Jessica@gmail.com'),
('7','Ashley@gmail.com'),
('8','forworkjayjay@gmail.com'),
('9','Rosa@gmail.com'),
('10','yuhaohong@gmail.com'),
('11','Monica@gmail.com');

-- 4.Table member_favorite
create table member_favorite(
type_id int primary key,
user_id int not null,
type_name varchar(50) null,
created_at timestamp default current_timestamp,
updated_at timestamp default current_timestamp on update current_timestamp,
foreign key (user_id) references member_basic(user_id)
);
select * from member_favorite;

-- 5.Table member_photo
create table member_photo(
user_avatar varchar(50) primary key,
user_id int not null,
image_url varchar(128) null,
updated_at timestamp default current_timestamp on update current_timestamp,
foreign key (user_id) references member_basic(user_id) ON DELETE CASCADE
);
select * from member_photo;

-- 6.Table member_orderdetails (尚未建立)
create table member_orderdetails(
user_id int primary key,
orderNumber int not null,
created_at timestamp default current_timestamp,
updated_at timestamp default current_timestamp on update current_timestamp
-- foreign key (orderNumber) references orderdetails(orderNumber) ON DELETE CASCADE
);
select * from member_orderdetails;

-- 7.Table member_coupon (尚未建立)
create table member_coupon(
user_id int primary key,
coupon_id int not null,
created_at timestamp default current_timestamp,
updated_at timestamp default current_timestamp on update current_timestamp
-- foreign key (coupon_id) references orderdetails(coupon_id) ON DELETE CASCADE
);
select * from member_coupon;


-- 8.Table member_verify
create table member_verify(
verify_id int primary key auto_increment,
user_id int,
user_email varchar(50),
verification_code varchar(6),
verification_token varchar(16),
code_used boolean default '0',
token_used boolean default '0',
created_at timestamp default current_timestamp,
expires_at timestamp default current_timestamp,
foreign key (user_id) references member_basic(user_id) ON DELETE CASCADE
); 
select * from member_verify;

insert into member_verify(user_id, user_email)
values
('1','Amanda@gmail.com'),
('2','Brian@gmail.com'),
('3','Cally@gmail.com'),
('4','Daniel@gmail.com'),
('5','Eddie@gmail.com'),
('6','Jessica@gmail.com'),
('7','Ashley@gmail.com'),
('8','forworkjayjay@gmail.com'),
('9','Rosa@gmail.com'),
('10','yuhaohong@gmail.com'),
('11','Monica@gmail.com');

-- drop table member_verify;
