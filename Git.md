# Git
* Git은 분산 버전 관리 시스템 기반의 버전 관리 도구입니다.  
  Git은 Git Hub, GitLab 같은 중앙 서버를 둘 수도 있지만 기본적으로는 로컬에서 사용하게 됩니다.
* git의 가장 큰 목적은 **버전 관리**, **협업**, **백업**입니다

---

## Git 시작하기 (Cli)  
> * Git Bash를 이용한 Git 활용은 Cli 특유의 장점을 살릴 수 있습니다.
> * `git config`를 이용한 Git 설정에 관해선 후술 하고 있지 않습니다.

#### 1. dir을 새로 만듭니다.(`mkdir`)  

#### 2. Git bash를 사용하여 새로 만든 dir로 들어가 `git init`을 사용합니다.
> * `git init` : 현재 Dir를 Git 시킵니다. 이는 현재 Dir를 Git 저장소에 등록시키는 것입니다.
>> `git init` 이란 명령어는 현재 Dir에 ".git"이란 하위 Dir을 생성합니다. 이 Dir에는 Git 저장소에 필요한 뼈대 파일이 들어있습니다. 

#### 3. Working Directory에서 작업한 내용을 `git add`를 사용하여 stage 시킵니다.
> * Working Directory는 Git Directory 즉, 지역 저장소에서 특정 버전을 Check Out 하여 가져온 것입니다.
    이곳에서 프로젝트 작업, 개발 및 수정을 진행하게 됩니다.
> * `git add *.txt` : "\*.txt"를 stage Area로 저장합니다. Untracked 상태였다면 Tracked 상태로 만들어 줍니다.  
>> 이는 또한 Commit 할 준비를 마친 것입니다.  
> * `git status` : git 프로젝트의 상태를 확인할 수 있게 해주는 명령어입니다.  

#### 4. Staging Area에 있는 작업된 파일을 `git commit`을 이용하여 Commit 합니다.
> * `git commit -m <커밋 메시지>` : Staging Area에 저장된 파일을 Commit 하여 지역 저장소(Git Repository)에 저장하는 것입니다.
>> Working Directory로 가져올 수 있는 Version을 만드는 행위입니다.
>>> 원거리 저장소에 저장을 하기 위한 전 단계입니다.

#### 5. Github에 등록된 Remote Repository의 주소를 등록해줍니다.
> * `git remote add origin (주소)` :  원격 저장소의 주소를 입력함으로써 원격 저장소를 등록합니다.
>> 'origin'의 자리는 저장소의 별칭입니다. 'origin'은 가장 기본 별칭입니다.
> * `git remote -v` : 원격 저장소의 상태를 확인합니다.

#### 6. `git push`를 사용해서 지역 저장소에 등록된 프로젝트를 원격 저장소에 저장합니다.
> * `git push origin <branch이름>` : 원격 저장소에 프로젝트를 등록합니다.

---

## Git의 세 가지 영역, 그리고 상태

#### Git의 세 가지 영역

![](https://github.com/whdid502/DailyDeveloperDiary/blob/master/Image/Git/git_repository.png)
* 모두 같은 Dir에 존재하지만, 개념적으로 나눈 것입니다.
* Working Directory : 프로젝트를 진행하는 실제 작업 공간으로 개발한 소스 및 자원이 존재하며 이곳에서 파일을 수정 및 추가합니다.
* Staging Area : 프로젝트를 진행하는 실제 작업 공간으로 개발한 소스 및 자원이 존재하며 이곳에서 파일을 수정 및 추가합니다.
* Git Directory(지역 저장소) : 실제로는 .git/이라는 이름의 디렉토리이며, 여러 가지 버전의 커밋 데이터들과 Git 프로젝트에 대한 모든 정보를 담고 있는 핵심 데이터베이스 디렉토리입니다.

#### 프로젝트(디렉토리 혹은 파일)의 상태
![](https://github.com/whdid502/DailyDeveloperDiary/blob/master/Image/Git/tracked%2Cuntracked...png)
* 추적의 여부로 Tracked와 Untracked로 나뉠 수 있습니다. 
> * Tracked : 해당 파일을 Git이 추적해 관리하고 있다는 상태입니다.
>> Tracked 파일은 최소 한 번 이상 `git add`를 통해 Staging Area에 포함되거나, `git commit`을 통해 지역 저장소에 저장된 파일입니다.
> * Untracked : 해당 파일이 Git의 관리를 받고 있지 않은 상태입니다. 
>> Working Directory의 파일이라고 모두 Git의 관리 하에 있는 파일은 아닙니다.
> * Modified(변경 발생)와 Unmodified : Staged 되거나 Commit 된 시점 이후로 수정, 변경이 있다면 Modified라고 합니다.
>> Modified와 Unmodified파일은 Tracked 된 상태입니다.

---

## Git Command Line  

* `git diff` : 마지막 버전과 working tree와의 차이점을 보여줍니다.
> 단순한 변경내역이 아니라, 어떤 내용이 변경되었는지 차이점을 알 수 있습니다.
>> `git diff --staged` : Commit 한 Git 저장소의 내용과 Staging Area에 등록한 내용의 차이를 비교할 수 있습니다.

* ` git reset --hard` : 해당 버전을 입력하면 그 버전으로 돌아간다는 명령어입니다.  
> * **reset은 버전 삭제의 개념이 포함되어있습니다.**
>> * reset : head가 branch를 가리킬 때, branch가 가리키는 commit을 바꿉니다. 이전의 commit 즉, version은 삭제됩니다.

* `git revert "버전"` : 버전을 유지하고 그 전 commit으로 되돌아갑니다.  
                        한 버전씩 역순으로 내려가야 충돌이 일어나지 않습니다. **건너뛰면 안 됩니다.**  
> * [reset과 revert의 차이점](http://www.devpools.kr/2017/01/31/%EA%B0%9C%EB%B0%9C%EB%B0%94%EB%B3%B4%EB%93%A4-1%ED%99%94-git-back-to-the-future/)에 관한 만화

* `git checkout "branch name"` : 해당 branch로 돌아간다.
> * **단순히 head가 가리키는 것을 바꿉니다**
>> Head는 버전을 가리킬 수도 있습니다. 단, 이럴 때 Head는 Detached상태라고 합니다.
>>> ` git checkout master` : 최신상태로 복귀함을 의미합니다. (head가 master를 가리키게 합니다.)

* `git commit -am "name"` : Staging을 함과 동시에 Commit까지 수행합니다. 
> 하지만 **최초 한 번은 add** 해서 Tracked상태로 만들어줘야 합니다.  

---

## Branch

* Branch : 가지라는 의미입니다. 독립적으로 다른 작업을 진행하기 위한 개념입니다.
> 같은 소스코드(뿌리) 위에서 다른 작업(가지)을 서로 영향을 주지 않으며 진행할 수 있습니다.

* Master : 기본 브랜치입니다. 통합 브랜치로 쓰입니다.
> 가장 큰 줄기이며 최초로 만들어진 브랜치이자, 최후의 브랜치입니다.

* Head : 현재 사용 중인 브랜치의 선두 부분입니다.
> Head가 가리키는 것은 현재 우리가 속해 있는 곳입니다. 

* Merge : 브랜치의 **병합**입니다.
> * 합치려고 하는 브랜치 간의 공통된 조상을 "base"라고 합니다. 

#### fast-forward

![](https://github.com/whdid502/DailyDeveloperDiary/blob/master/Image/Git/fast_forward.png)
> * A-B가 Master의 계보이고, X-Y가 Master에서 분할해 나간 bugfix 브랜치인 상태입니다.
>> * Master 브랜치의 변경이 없으며, 또한 bugfix 브랜치는 Master 브랜치의 이력을 모두 포함한 상태입니다.
>>> * 이러한 상황에는 단순한 이동으로도 Merge가 이루어집니다. 이러한 것을 "fast-forward(빨리 감기)"라고 합니다.

#### merge commit

![](https://github.com/whdid502/DailyDeveloperDiary/blob/master/Image/Git/merge_commit.png)
> * 위와 비슷하지만 bugfix 브랜치가 분할된 후에 Master 브랜치의 변경이 생겼습니다.
>> * 이러한 경우 양쪽의 변경을 가져온 "merge commit(병합 커밋)"을 실행합니다.

> * `git merge "branch name"`: 현재의 브랜치로 "branch name"을 병합합니다.  
>> merge 할 때 현재 브랜치 이외에 통합되던 브랜치의 log도 통합된 브랜치의 log에 선형으로 등장합니다.  

#### rebase
![](https://github.com/whdid502/DailyDeveloperDiary/blob/master/Image/Git/rebase.png)
> * bugfix 브랜치의 base를 master 브랜치에 순차적으로 병합시킵니다.
>> D commit 상태를 base로 X를 병합해 C-D의 변경 부분을 수정해 "X'"가 만들어졌습니다. Y'도 같은 내용입니다.
>>> 이와 같이 log가 깔끔하게 보이도록 하는 방식을 "rebase"라고 합니다.
**rebase와 merge는 과정이 다를 뿐 최종 결과는 같습니다.**

> *  `git rebase branch_name` : 해당 Branch에서 "branch_name"을 base로 삼아 병합합니다. 

#### Cherry Pick
![](https://github.com/whdid502/DailyDeveloperDiary/blob/master/Image/Git/cherry_pick.png)
> * Master브랜치의 f42c5 버전(최신 버전)에서 ruby_client브랜치 전체가 아닌 e43a6 버전만 끌고 와 병합해 새로운 a0a41 버전을 생성해 냈습니다.
> * 이처럼 브랜치를 부분적으로 rebase 하는 것을 "Cherry Pick"이라고 합니다.
>> 이것은 하나의 commit만 rebase 하는 것을 의미합니다.
>>> * `git cherry-pick (버전 값)` : 병합하고자 한 브랜치 위에서 해당 부분의 버전 값을 끌고 와 병합합니다.  

##### merge와 rebase
* merges는 변경 내용의 이력이 모두 그대로 남아 있기 때문에 이력이 복잡해집니다.
* rebase는 이력은 단순해지지만, 원래의 커밋 이력이 변경됩니다.
> 정확한 이력을 남겨야 할 필요가 있을 경우에는 사용하면 안 됩니다.  

* 예시) 토픽 브랜치에 통합 브랜치의 최신 코드를 적용할 경우에는 rebase를 사용합니다.  
  통합 브랜치에 토픽 브랜치를 불러올 경우에는 우선 rebase를 한 후 merge 합니다.
 
#### conflict
* 병합 시 git이 자동 병합하지 못하는 항목은 충돌이 일어납니다. 이를 "conflict"라고 합니다.
* 3-way merge : 2개의 브랜치가 여러 부분 충돌할 때 base 브랜치를 추가로 merge하여 conflict를 줄여 merge할 수 있는 방법
![](https://github.com/whdid502/DailyDeveloperDiary/blob/master/Image/Git/3_way_merge.png)
> * Me브랜치와 Other브랜치의 병합(2-way merge)은 B부분을 제외하고 git이 스스로 병합해줄 수 있는 것이 없습니다.
>> 이럴 때 Base브랜치를 추가로 병합(3-way merge)을 이용합니다.
>>> Base브랜치를 기준으로 변형된 부분을 자동으로 병합해줍니다.

---

## pull, fetch 그리고 clone

#### pull
![](https://github.com/whdid502/DailyDeveloperDiary/blob/master/Image/Git/git_pull.png)
* `git pull` : remote repository의 최신의 커밋을 내려받고, 병합합니다.
> * 지역 브랜치와, 원격 저장소 Head가 같은 위치를 가리킵니다.

#### fetch
![](https://github.com/whdid502/DailyDeveloperDiary/blob/master/Image/Git/git_fetch.png)
* `git fetch` : 원격 저장소로부터 필요한 프로젝트를 내려받지만, 병합은 하지 않습니다.
> * 지역 브랜치는 가지고 있던 지역 저장소의 최신 커밋을 가리킵니다. 
    원격 저장소의 Head는 가져온 최신 커밋을 가리킵니다.

* **fetch 는 조금 더 신중하게 자료를 받고 싶을 때** 사용합니다.
> * 우선 커밋을 받은 뒤, 변경점과 커밋의 진행상황 등 세부사항을 확인한 뒤 병합합니다.
>> 이는 결국 `git pull`은 `git fetch; git merge origin/master(or FETCH_HEAD)` 와 같습니다.  

#### clone
* `git clone (remote repository URL)` : remote repository의 파일을 복사하여 내 위치에 복제합니다.
> 결과적으로 pull 과 같지만 클라이언트상에 아무것도 없는 상태에서 서버의 프로젝트를 내려받습니다.

---

<sub> 1) Git의 세 가지 영역, 그리고 상태 이미지 [출처 : dololak.tistory](https://dololak.tistory.com/category/%EA%B9%83%28Git%29?page=1)</sub>  
<sub> 2) merge의 이미지 [출처 : backlog.com](https://backlog.com/git-tutorial/kr/stepup/stepup1_1.html)</sub>  
<sub> 3) cherry pick의 이미지 [출처 : https://mobicon.tistory.com/230](https://mobicon.tistory.com/230)</sub>  
<sub> 4) 3-way merge의 이미지[출처 : opentutorials](https://opentutorials.org/module/2676/15307)</sub>


