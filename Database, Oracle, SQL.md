# Database

* 데이터를 저장하는 방법
> * file 많은장점, 배우기 쉽다, 어디에서나 사용가능, 간편한 전송
>> * file의 한계 : 성능, 보안, 편의성
>>> * 극복하기위한것이 바로 **'Database'** : 방대한기능을가지고잇는 정보도구

* input(입력)과 output(출력)이 중요
> * input : 'Creat', 'Update', 'Delete'
>> * output : 'Read'
>>> * **'CRUD'**가 중요하다.

* 압도적으로 많이사용되는 database 는 **관계형 데이터베이스(reational database)** 이다.  
  이 관계형데이터베이스의 핵심은 **표** 이다.  
  x와 y, 열과 행으로 표현한다면 방대한 데이터를 쉽고 효율적으로 처리할수잇다. 데이터베이스란 이 표를 기계화시킨다.

## ORACLE 

* 오라클에서 우리가 할것은 '표'에 정보를 기록&읽는것이다.  
  표가 많아질수록 연관된 표들끼리 Grouping할 체계가 필요하다. 이것을 Schema라고한다  
  User를 만들면 Schema가 만들어지고 user는 Schema를 관리한다. Schema와 User는 연관돼잇다.

* ORACLE은 해결하고자하는것을 인지하고, 검색해서 쓰자.

* 왜 sql로 복잡하게 사용할까, 쉬운 엑셀안쓰고??(Why Cli?)
> * 훨씬 가볍고, 방대하고, 효율좋게 처리할수잇다(잘햇다면)
> * 명령어를 이용해서 데이터베이스를 제어할수있다 > 자동화할수있다.
> * 이러한 명령어를 SQL(Structured Query Language,구조화된 정보를 처리하도록 요청하는 언어)라고한다.
> * 절대다수가 사용하는 관계형 데이터베이스는 SQL로 동작한다.

*  ORACLE은 표를 쪼갤수있다. 매우매우 큰 용량의 TABLE을 수정하고자 할때, 일일히 수정하는것보다, 표를 필요에 의해 분할시켜 원하는 부분만 수정하여 시간과 비용을 감축할수있다.  
하지만 이렇게 쪼개놓은 표는  UPDATE는 쉽지만 READ하기 어렵다. 이럴때 읽기 쉽게 하는것을 JOIN이라한다. 이는 분합된 표를 분합된것처럼 저장하는것을 말한다.

---------------------------------------------

# SQL


* TABLE 에서 중복은 좋지않다 > 데이터낭비, 수정이 힘들다
> 모든 표는 하나의 주제만 가져야 한다.
  
###### 1. table(표)만들기
```
CREATE TABLE tablename(
	id NUMBER NOT NULL,
	title VARCHAR2(50) NOT NULL,
	description VARCHAR2(4000) NULL,
	created DATE NOT NULL,
	CONSTRAINT PK_tablename PRIMARY KEY(id) 
);
```

id|title|description|created
--|-----|-----------|-------

> 1) 컬럼(열)은 ()로 묶어지정하고, ;으로 끝낸다  
> 2) 컬럼뒤에 데이터타입은 꼭 지정되어야한다. > NUMBER(숫자만) VARCHAR2(4000)4000이하의 문자, DATE(날짜)  
> 3) NULL(없다), NOT NULL(반드시있어야한다.)등의 제한명령어를 쓸수있다.  
> 4) CONSTRAINT(제한한다)도 제약조건이다. PK_tablenamed은 프라이머리키의 이름이고, PRIMARY KEY(id)는 id컬럼을 전부 고유값(중복된다면 명령이 실행  되지않게, 전부 구별되게)으로 만든다.  
>> PRIMARY KEY 의 행의 값은 유일무이하다! 후에 PRIMARY KEY로 지정한 행을 찾는것은 속도가 월등히 빠르다
 
###### 2. table에 행(row) 추가하기
```
INSERT INTO tablename
	(id,title,description,created)
	VALUES
	(1,'ORACLE','ORACLE is ..',SYSDATE);
```
```
commit;
```

id|title|description|created
--|-----|-----------|-------
1|ORACLE|ORACLE is ..|12/08/2019

> 1) 열은 ()묶어진다.
> 2) VALUES는 구체적인 값을 적는다
> 3) id 은 데이터타입을 숫자로 지정햇으므로 숫자를적고, title,description은 문자숫자제한 즉 문자로 지정햇으니 문자를 적어준다.
> 4) created는 데이터타입이 DATE,날짜이므로 SYSDATE(현재)등으로 적어준다.
> 5) **commit;까지 해야 완성(기계적으로하자, 무조건한다)**   

###### 3. table 가져오기(확인하기)
```
SELECT * FROM tablename;
```
> 1) *은 모든 컬럼를 말한다.
> 2) sqlpls론 불편하다. SQL DEVELOPER를 사용하면 깔끔하게본다.

###### 4. table 분할해 가져오기(확인하기)
```
SELECT id,title,created FROM tablename;
```
> 1) *(모든컬럼)대신 id,title,create 컬럼만 보겟다

```
SELECT * FROM tablename WHERE id =(<,>) 1;
```				 
> 1) 모든 컬럼중에서 / id컬럼이 1인(1보다작은,1보다큰) 부분의 로우만 본다.  

###### 5. 출력된 결과를 정렬
```
SELECT * FROM tablename ORDER BY id DESC;
                                    ASC;
```
> 1) tablename 의 모든컬럼을 점령한다 `SELECT * FROM tablename`
>> id컬럼을 기준으로 `ORDER BY id`
>>> 큰숫자(혹 문자순)부터 내림으로 `DESC;`, 작은숫자(혹 문자순)부터 올림으로 `ASC;`

###### 6. 전체(*)에서 페이징 하기
> * 전체의 시트양이 너무많다면 *를 꺼내올때마다 데이터베이스는 마비된다.  
> 책에서 페이지가 나뉘어잇듯이, 시트를 분할하는것을 페이징이라 한다.
```
SECET * FROM tablename
	OFFSET 1 ROWS;
```
> 1) OFFSET 1은 '0번째 이후에 나오는 행들만 가져온다=우리가 봤을때 2번째
>> * 컴퓨터는 0부터 센다.


###### 7. 한 행을 가져오기
```
SELECT *FROM tablename   
	OFFSET 0 ROWS  
	FETCH NEXT 1 ROWS ONLY;  
```
> 1) 1번째 이후의 / 하나의 열만을 가져온다. 
> 2) 몇번째 페이지인가를 의미한다.

```
SELECT *FROM tablename
       OFFSET 1 ROWS
       FETCH NEXT 1 ROWS ONLY;
```
> 1) 2번째 이후의 / 하나의 열만을 가져온다.

###### 8. 행 내용 변경하기
```
UPDATE tablename
	SET
	title = 'MSSQL',
	description = 'MSSQL is ..'   >(여기까지하고 ; 로 마무리하면 모든 title과 description 컬럼이 저 내용으로바뀐다)
	WHERE                                       (무언가할때 WHERE이 없다면 다시 생각해보자)
	id = 3;
```
> 1) tablename이란 TABLE에서 title 컬럼을 'MSSQL', description컬럼을  'MSSQL is ..'이라고 업데이트한다. 단, 그 행은 id가 3인 행만 적용한다.
> 2) 이런 수정작업후엔 항상 'commit;'을 입력해서 수정내용이 적용되게한다.

###### 9. 삭제하기**(굉장히 파괴적인 결과를 불러일으킬수잇다, 항상조심하자)**
```
DELETE FROM tablename            >(여기까지하고 ;로 마무리하면, 토픽행이 모두 삭제된다)
	WHERE
	id = 3;
```
> 1) id 컬럼의 로우가 3인곳을 삭제한다.

###### 10.표 지우기
```
DROP TABLE tablename;
```
> 1) tablename이란 TABLE 삭제

###### 11.시퀀스 생성하기  
> * PRIMARY KEY와 가족이라고 생각하자, 같이 있으면 강력해진다.
```
CREATE SEQUENCE SEQ_tablename;
```
> 1) SEQ_tablename 이라는 시퀀스를 생성한다.

```
INSERT INTO tablename
	(id,title,description,created)
	VALUES
	(SEQ_tablename.NEXTVAL,'ORACLE','ORACLE is ..',SYSDATE);
```
> 1) id 컬럼에서 자동으로 다음값을 찾아 입력해준다. NEXT(다음)VAL(숫자)
>> 값이 충돌하지 않게끔한다.

```
SELECT SEQ_tablename.CURRVAL FROM tablename; > 현재 tablename 이란 TABLE에 잇는 모든행의 수만큼 값을 표시해준다
                             FROM DUAL;      > 가상 TABLE 에서 값을보여준다. 하나의 행에서만보여준다.
```
> 1) 현재 시퀀스의 값을 본다.

###### 12. 표 JOIN하기
예제와 함께 [동영상](https://opentutorials.org/course/3885/26417) 에서 확인하자.







