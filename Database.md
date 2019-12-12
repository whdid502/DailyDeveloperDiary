# Database

* 데이터베이스란 공통으로 사용되는 데이터의 공유와 운영을 위해 저장 관리할 수 있도록 하는 공간을 말합니다. 

* 압도적으로 많이사용되는 database 는 **관계형 데이터베이스(reational database)** 입니다.  
> * 이 관계형데이터베이스의 핵심은 **표** 이다.  
>> * 열과 행으로 표현한다면 방대한 데이터를 쉽고 효율적으로 처리할 수 있습니다.

#### 기본명칭

![](https://github.com/whdid502/DailyDeveloperDiary/blob/master/Image/database/database_table2.png)

* 표(Table)은 릴레이션이라고도 합니다.
* 식별자(identifier)는 여러개의 집합체를 담고있는 관계형 데이터베이스에서 각각의 구분할 수 있는 논리적인 개념입니다.
> * 유일성 : 하나의 테이블에서 모든 행은 서로 다른 키 값을 가져야 합니다.
> * 최소성 : 꼭 필요한 최소한의 속성들로만 키를 구성해야 합니다.
* 튜플(Tuple)은 행(Row)를 의미합니다. 행은 테이블에서 같은 값을 가질 수 없습니다. 데이터의 타입입니다. 튜플의 수를 카디날리티(Cardinality)라고 합니다.
* 어트리뷰트(Attribute)는 열(Columm)을 의미합니다. 데이터의 구조입니다. 어트리뷰트의 수를 디그리(Degree)라고 합니다.

#### Schema

*  스키마(schema)는 데이터베이스에서 자료의 구조, 자료의 표현 방법, 자료 간의 관계를 형식 언어로 정의한 구조입니다.
> * 단순히 말하자면 연관된 Table끼리 그룹화해둔것을 schema라고 합니다.

![](https://github.com/whdid502/DailyDeveloperDiary/blob/master/Image/database/schema.jpg)

* schema 3계층 예시

![](https://github.com/whdid502/DailyDeveloperDiary/blob/master/Image/database/schema_ex.jpg)

* 스키마는 3계층으로 이루어져 있습니다. 이는 관점에 따라 분류되었습니다.
* 외부스키마는 개인의 입장, '서브스키마'라고도 합니다. 사용자 뷰를 가리킵니다. 
> * 하나의 외부스키마는 여럿이 공유 가능하며, 하나의 DB시스템에 여러 개의 외부스키마가 존재 가능합니다.
* 내부스키마는 시스템 프로그래머나 설계자의 관점에서 바라보는 스키마입니다.
> * 데이터베이스의 물리적 구조를 가리킵니다.(= 실제 저장방법을 기술하는 물리적인 저장장치와 관련됨) 
* 개념스키마는 조직 전체의 입장, 전체적인 뷰를 가리킵니다.
> * 개체간의 관계와 제약조건을 나타내고, 데이터베이스의 접근권한/보안/무결성 규칙에 대한 명세를 정의합니다. 

---

# DBMS(DataBase Management System)

![](https://github.com/whdid502/DailyDeveloperDiary/blob/master/Image/database/DBMS.png)

* 데이터베이스를 조작하는 별도의 소프트웨어를 DBMS, 데이터베이스 관리 시스템이라고 합니다.
* 데이터베이스 관리 시스템이란 데이터베이스를 관리하며 응용 프로그램들이 데이터베이스를 공유하며 사용할 수 있는 환경을 제공하는 소프트웨어입니다.

### Type of DBMS

##### Oracle
* 오라클에서 만들어 판매중인 상업용 데이터베이스입니다.
* 윈도우즈, 리눅스, 유닉스 등 다양한 OS에 설치를 할 수 있습니다.
* MS_SQL , MY_SQL보다 대량의 데이터를 처리하기 좋습니다.
* 대기업에서 주로 사용하며 글로벌 DB시장 점유율 1위입니다.<sub>2019년 12월 기준</sub>
* 비공개 소스, 폐쇄적인 운영을 합니다.

##### MY_SQL
* MySQL사에서 개발, 썬마이크로시스템즈를 거쳐 현재 오라클에 흡수합병됬습니다.
* 윈도우즈, 리눅스, 유닉스 등 다양한 OS에 설치를 할 수 있습니다.
* 오픈소스로 이루어져있는 무료 프로그램입니다, 단, 상업적 사용시에는 비용이 발생합니다.
* 가격등의 장점을 앞세워 다수의 중소기업에서 사용 중입니다.

##### MS_SQL
* 마이크로소프트 사에서 개발한 상업용 데이터베이스입니다.
* 다른 OS에서도 사용가능하지만 윈도우즈에 특히 특화되어있습니다.
* 비공개 소스로 폐쇄적인 정책입니다. 단, 리눅스버전은 오픈소스입니다.
* 비교적 중소기업에서 주로 사용합니다.

---

# SQL

* 

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

---
<sub>1. Database 이미지 및 내용 [출처 : 코딩팩토리](https://coding-factory.tistory.com/77)</sub>  
<sub>2. Schema 예시 이미지 및 내용 [출처 : ykcb.tistory](https://ykcb.tistory.com/entry/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EC%8A%A4%ED%82%A4%EB%A7%88%EC%9D%98-%EA%B0%9C%EB%85%90-%ED%8A%B9%EC%A7%95)</sub>





