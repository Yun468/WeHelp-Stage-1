第三題

INSERT INTO member(id,name,username,password,follower_count,time ) VALUES(1,'John','test','test',30,now());
![1](https://user-images.githubusercontent.com/112928118/196859186-8ff73470-0b52-46d5-9a0a-35d0561442c9.png)

INSERT INTO member(name,username,password,follower_count,time ) VALUES('Mary','aaaa','aaaa',30,now());

INSERT INTO member(name,username,password,follower_count,time ) VALUES('Andy','bbbb','bbbb',30,now());

INSERT INTO member(name,username,password,follower_count,time ) VALUES('Mark','cccc','cccc',30,now());

INSERT INTO member(name,username,password,follower_count,time ) VALUES('Zack','dddd','dddd',30,now());

SELECT*FROM member;

SELECT*FROM member ORDER BY time DESC;

SELECT*FROM member LIMIT 3 OFFSET 1 ;

SELECT*FROM member WHERE username='test';

SELECT*FROM member WHERE username='test'AND password='test';

mysql> UPDATE member SET name='test2' WHERE username='test';
select*from member;



======================================
第四題

SELECT COUNT(*) FROM member;

SELECT SUM(follower_count) FROM member;

SELECT AVG(follower_count) FROM member;

======================================
第五題(table設計)

mysql> CREATE TABLE message(
    -> id bigint PRIMARY KEY AUTO_INCREMENT,
    -> member_id bigint NOT NULL,
    -> content varchar(255) NOT NULL,
    -> like_count int unsigned NOT NULL DEFAULT 0,
    -> time datetime NOT NULL);

INSERT INTO message(id,member_id,content,like_count,time) VALUE(1,1,'我是第一個留言',1,now());

INSERT INTO message(member_id,content,like_count,time) VALUE(1,'我是第二個留言',2,now());

INSERT INTO message(member_id,content,like_count,time) VALUE(2,'我是第三個留言',3,now());

INSERT INTO message(member_id,content,like_count,time) VALUE(1,'我是第四個留言',4,now());

INSERT INTO message(member_id,content,like_count,time) VALUE(1,'我是第五個留言',5,now());

INSERT INTO message(member_id,content,like_count,time) VALUE(3,'我是第六個留言',6,now());

SELECT*FROM message;

===============================
第五題(題目)

SELECT member.username,message.content FROM member INNER JOIN message ON message.member_id=member.id;

SELECT member.username,message.content FROM member INNER JOIN message ON message.member_id=member.id and member.username='test';

SELECT AVG(like_count) FROM message INNER JOIN member ON  message.member_id=member.id and member.username='test';




