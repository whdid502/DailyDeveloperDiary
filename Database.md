# Database

* 데이터베이스란 공통으로 사용되는 데이터의 공유와 운영을 위해 저장 관리할 수 있도록 하는 공간을 말합니다. 

* 압도적으로 많이사용되는 database 는 **관계형 데이터베이스(reational database)** 입니다.  
> * 데이터베이스는 차등적으로 권한을 줄 수 있는 등, 보안적 으로 뛰어납니다.
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
* SQL의 구문은 암기보단 필요에 의한 검색으로 사용합니다.

### 예제1(CREATE)

```
CREATE TABLE `author` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `profile` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
```
id|name|profile
--|-----|-------

#### CREATE TABLE
> * 'author'이란 이름의 표를 만들었습니다.
> * 'author'에는 'id', 'name', 'profile' 이란 컬럼이 있습니다.

#### int, varchar
> * 각 컬럼의 값을 특정한 조건으로 제한할 수 있습니다.
> * int(m)은 '그 값을 정수로 제한하되, m개까지 검색이 가능합니다.'의 의미입니다.
> * varchar(m)은 '행의 문자가 m을 넘지 않는다.'입니다.
>> * 이러한 데이터 값은 지정되어야 합니다.

#### NULL, NOT NULL
> * NULL은 "값이 없는것을 허용합니다", NOT NULL은 "값이 없는것을 허용하지 않습니다."입니다.

#### PRIMARY KEY()
> * 괄호 안의 컬럼이 메인 컬럼이 되게 하며, 중복되지 않게 해줍니다. 각각의 행을 식별하는 식별자로 쓰기 위함입니다.

### 예제2(INSERT)

```
INSERT INTO 'author'
	(id,name,profile)
	VALUES
	(1,'egoing','developer');
```

### 예제2-1(INSERT)

```
INSERT INTO `author` VALUES (1,'egoing','developer');
INSERT INTO `author` VALUES (2,'duru','database administrator');
INSERT INTO `author` VALUES (3,'taeho','data scientist, developer');
COMMIT;
```

id|name|profile
--|-----|-------
1|egoing|developer
2|duru|database administrator
3|taeho|data scientist, developer

#### INSERT
> * 행을 삽입합니다.

#### COMMIT
> * 수정사항을 적용합니다.

### 예제3(SELECT)

```
SELCET 'name' FORM 'author' WHERE 'profile'='developer' ORDER BY 'id' DESC LIMIT 1;
```

#### SELECT
> * 표를 출력합니다.
>> * SELECT * FROM 'TABLENAME' : TABLENAME 표를 전부 출력합니다.

#### WHERE
> * 위치의 조건을 덧붙입니다.
>> * 위의 예시에선 'profile'이란 행의 값이 'developer'라는 위치조건을 덧붙였습니다.

#### ORDER BY ... DESC & ASC
> * 지정한 행을 기준으로 내림차순 혹 오름차순으로 출력합니다.
>> * 위의 예시에선 'id'행을 기준으로 내림차순한다는 조건을 덧붙였습니다.

#### LIMIT ()
> * 조건에 부합하는 표를 전부가 아닌 ()개만 출력합니다.

### 예제3-1(SELECT)

```
SELECT * FROM tablename   
	 OFFSET 0 ROWS  
	 FETCH NEXT 1 ROWS ONLY;  
```

> 1) 1번째 이후의(OFSET) 하나의 열만을(FETCH NEXT 1 ONLY) 가져옵니다. 

```
SELECT *FROM tablename
       OFFSET 1 ROWS
       FETCH NEXT 1 ROWS ONLY;
```
> 1) 2번째 이후의 하나의 열만을 가져옵니다.

### 8. 예제4(UPDATE)

```
UPDATE 'autohr'
	SET
	name = 'camp',
	profile = 'teacher'   >(여기까지하고 ; 로 마무리하면 모든 title과 description 컬럼이 저 내용으로 바뀝니다)
	WHERE                                       (무언가할때 WHERE이 없다면 다시 생각해 봐야 합니다.)
	id = 3;
```

###### UPDATE전

id|name|profile
--|-----|-------
1|egoing|developer
2|duru|database administrator
3|taeho|data scientist, developer

###### UPDATE후

id|name|profile
--|-----|-------
1|egoing|developer
2|duru|database administrator
3|camp|teacher

> 1) 'author'이란 표에서 name 컬럼을 'camp', profile 컬럼을  'teacher' 로 업데이트합니다. 단, 그 행은 id가 3인 행만 적용합니다.
> 2) 이런 수정작업후엔 항상 'commit;'을 입력해서 수정내용이 적용되게 합니다.

### 예제5(DELETE)

```
DELETE FROM author           >(여기까지하고 ;로 마무리하면, 토픽행이 모두 삭제됩니다.)
	WHERE
	id = 3;
```
> 1) id 컬럼의 로우가 3인곳을 삭제합니다.

### 예제5-1(DROP)
```
DROP TABLE tablename;
```
> 1) author이란 표를 삭제합니다.

# JOIN

* JOIN은 왜 관계형 데이터베이스인지 설명해줍니다.
* 수없이 많은 데이터를 지닌 표를 수정이 편하게 분할하며, 읽기 쉽게 합친것 처럼 보이게 할수 있습니다.
* 표를 쪼갬으로써 중복된 값을 제거할 수 있습니다.

#### topic
tid|title|descripition|name|city|job_title|job_description
---|-----|------------|----|----|---------|---------------
1|HTML|HTML is ...|egoing|seoul|developer|developer is...
2|CSS|CSS is ...|leezche|jeju|designer|designer is...
3|Dateabase|Database is ...|egoing|seoul|developer|developer is ...

#### comment
cid|descripition|name|city|job_title|job_description
---|------------|----|----|---------|---------------
1|HTML is ...|egoing|seoul|developer|developer is...

* topic표 내부와 topic과 comment사이에서 중복되는 내용이 있습니다.
> * 이럴때 표를 쪼갬으로서 수정을 간편히 할수 있습니다.


---
<sub>1. Database 이미지 및 내용 [출처 : 코딩팩토리](https://coding-factory.tistory.com/77)</sub>  
<sub>2. Schema 예시 이미지 및 내용 [출처 : ykcb.tistory](https://ykcb.tistory.com/entry/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4-%EC%8A%A4%ED%82%A4%EB%A7%88%EC%9D%98-%EA%B0%9C%EB%85%90-%ED%8A%B9%EC%A7%95)</sub>
<sub>3. JOIN의 표 및 내용 [출처 : opentutorials.org](https://opentutorials.org/course/3884/25179)</sub>




