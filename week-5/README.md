第三題

INSERT INTO member(id,name,username,password,follower_count,time ) VALUES(1,'John','test','test',30,now());
![1](https://user-images.githubusercontent.com/112928118/196859186-8ff73470-0b52-46d5-9a0a-35d0561442c9.png)

INSERT INTO member(name,username,password,follower_count,time ) VALUES('Mary','aaaa','aaaa',30,now());

INSERT INTO member(name,username,password,follower_count,time ) VALUES('Andy','bbbb','bbbb',30,now());

INSERT INTO member(name,username,password,follower_count,time ) VALUES('Mark','cccc','cccc',30,now());

INSERT INTO member(name,username,password,follower_count,time ) VALUES('Zack','dddd','dddd',30,now());
![2](https://user-images.githubusercontent.com/112928118/196859252-4a56657a-6e5a-46ca-811d-49e9e41edfc6.png)

SELECT*FROM member;
![3](https://user-images.githubusercontent.com/112928118/196860260-ae392f07-6896-4025-90d4-ca6ac002f46b.png)


SELECT*FROM member ORDER BY time DESC;
![4](https://user-images.githubusercontent.com/112928118/196859653-8d1c95c0-53f8-4112-a87b-4056d8a51a82.png)

SELECT*FROM member LIMIT 3 OFFSET 1 ;
![5](https://user-images.githubusercontent.com/112928118/196859675-9ebb43a3-c43a-493d-92fd-8c32982de9dc.png)

SELECT*FROM member WHERE username='test';
![6](https://user-images.githubusercontent.com/112928118/196859690-d0b26caa-0a52-483c-b5ab-2a98abf456f3.png)

SELECT*FROM member WHERE username='test'AND password='test';
![7](https://user-images.githubusercontent.com/112928118/196859705-392a38ce-6543-4fd5-9aa3-463406941e4f.png)

mysql> UPDATE member SET name='test2' WHERE username='test';

mysql>SELECT*FROM member;
![8](https://user-images.githubusercontent.com/112928118/196860439-65ecb547-bd6e-4648-89d5-b8e452366076.png)



======================================

第四題

SELECT COUNT(*) FROM member;
![9](https://user-images.githubusercontent.com/112928118/196860458-a59c5948-957c-4792-b7a8-06ca8ee2a28e.png)

SELECT SUM(follower_count) FROM member;
![10](https://user-images.githubusercontent.com/112928118/196860473-bd218e4d-19a6-4fb1-982f-9a66eaa0c802.png)

SELECT AVG(follower_count) FROM member;
![11](https://user-images.githubusercontent.com/112928118/196860484-cb56462b-327c-4bb4-abdb-9dd868c54f98.png)

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
![12](https://user-images.githubusercontent.com/112928118/196859766-52d080df-2608-46fa-bc8a-b9f509ac41b5.png)

===============================

第五題(題目)

SELECT member.username,message.content FROM member INNER JOIN message ON message.member_id=member.id;
![13](https://user-images.githubusercontent.com/112928118/196860520-3b389f99-918b-4839-9db0-c3fbbb6713be.png)

SELECT member.username,message.content FROM member INNER JOIN message ON message.member_id=member.id and member.username='test';
![14](https://user-images.githubusercontent.com/112928118/196860529-642c4adf-4455-4b63-887c-d3d56692ea0e.png)

SELECT AVG(like_count) FROM message INNER JOIN member ON  message.member_id=member.id and member.username='test';
![15](https://user-images.githubusercontent.com/112928118/196860537-9bda33e9-7953-4167-998f-0a805fb92cf3.png)




