# Git
* Git은 분산 버전 관리 시스템 기반의 버전 관리 도구입니다.  
  Git은 Git Hub, GitLab 같은 중앙 서버를 둘 수도 있지만 기본적으로는 로컬에서 사용하게 됩니다.
* git의 가장 큰 목적은 **버전관리**, **협업**, **백업**입니다

---

## Git 시작하기 (cli)  
> * Git bash를 이용한 Git 활용은 cli 특유의 장점을 살릴 수 있습니다.
> * `git config`를 이용한 Git 설정에 관해선 후술하고 있지 않습니다.

#### 1. dir을 새로 만듭니다.(`mkdir`)  

#### 2. Git bash를 사용하여 새로 만든 dir로 들어가 `git init`을 사용합니다.
> * `git init` : 현재 dir를 Git 시킵니다. 이는 현재 dir를 git 저장소에 등록시키는 것 입니다.
>> `git init` 이란 명령어는 현재 dir에 ".git"이란 하위 dir을 생성합니다. 이 dir에는 Git 저장소에 필요한 뼈대 파일이 들어있습니다. 

#### 3. Working Directory 에서 작업한 내용을 `git add`를 사용하여 stage 시킵니다.
> * Working Directory는 Git Directory 즉, 지역저장소에서 특정버전을 Check Out 하여 가져온 것입니다.
    이곳에서 프로젝트 작업, 개발 및 수정을 진행하게 됩니다.
> * `git add *.txt` : "\*.txt"를 stage area로 저장합니다. Untracked 상태였다면 Tracked 상태로 만들어 줍니다.  
>> 이는 또한 commit 할 준비를 마친 것입니다.  
> * `git status` : git 프로젝트의 상태를 확인할 수 있게 해주는 명령어입니다.  

#### 4. Staging area 에 있는 작업된 파일을 `git commit` 을 이용하여 Commit 합니다.
> * `git commit -m <커밋메시지>` : Staging area에 저장된 파일을 Commit하여 지역저장소(Git Repository)에 저장하는것입니다.
>> Working Directory 로 가져올 수 있는 Version을 만드는 행위입니다.
>>> 원거리저장소에 저장을 하기 위한 전 단계입니다.

5. push하기전에 github에 등록된 remote repository의 주소를 등록해줍니다. 이때 `git remote add origin (주소)` 를 사용합니다. 완료된후 `git push`를 이용해 remote repository에 등록합니다.  

---

##### Git의 세가지영역


> * `git remote add origin <원격저장소주소,GitHub의 저장소주소>` : 원격저장소 주소 등록
> * `git remote -v` : 원격저장소 주소확인
> * `git push origin <branch이름,master>` : 원격저장소에 올림, 여기서 origin 은 원격저장소의 이름, master은 push할 branch
>> *  `(--set-upsteram)` : 위의 push 와 origin사이에 두는, 설정하는것>이후엔 git push만으로 업로드가능
      `(-u)`

* .gitignore : 버전관리,commit관리에서 제외(사적인파일)

## Git Command Line  

* `git diff` : 마지막버전과 working tree와의 차이점을 보여준다.

* ` git reset --hard` : undo, 뒤에 버전을 입력하면 그버전으로 가겟다, 돌아가겟다.  
`git reset --soft` : reset시 수정본은 그대로둔다  >>**reset은 지우는거나 다름없다.**

> * reset : head가 branch를가리킬때, branch가 가리키는 commit을 바꾼다. 이전의 commit 즉, version은 삭제되다. 삭제의 개념

* `git revert "버전"` : 버전을 유지하고 버전을 revert 하고 그전 commit 으로 돌아간다.  
                        한버전씩 역순으로 내려가야 충돌이 일어나지않는다. **건너뛰면안됨**

* `git checkout "branch name"` : 해당 branch로 돌아간다. (**head의 값을바꾸는것**,단 head는 버전을 가리킬수도잇다 이럴때 head는 detached상태라고한다.)
                           
* ` git checkout master` : 최신상태로 복귀. (head가 master를 가리키게한다.)

* `git commit -am "name"` : a는 add, add와 commit 을 동시에 수행하는 명령어이다. 하지만 적어도 **최초 한번은 add**해서 tracked상태로 만들어줘야한다  
   `git commit` : editor 가 뜬다. commit message를 좀더길고 세세하게 쓸수잇다.

## Branch


* branch = 가지,같은뿌리 서로다른역사

* master : 기본 branch. 가장큰줄기

* head가 가리키는것 : 현재 우리가 속해잇는것  
> * branch를 만들고 branch사이를이동한다는것은 공통의 줄기를지닌 평행우주사이에서 별개로작업한다는것이다.

* `git merge` : branch의 **병합**
   
> * 합치려고하는 branch 간의 공통의 조상 : base  
>> * base를 기반으로 두개 이상의 branch가 합된것 : merge commit
   
>>> * `git merge "branch name"`: 현재의 branch로 "branch name"을 병합한다  
                                 merge할때 현재branch말고 통합되던 branch의 log도 통합된 branch의 log에 등장한다  
                                 merge 할때 같은 파일이더라도 수정부분이 다르면 알아서 git이 적용해준다.  
   
> * **conflict**는 같은부분을 수정햇을때 git스스로 처리하지못하니 나한테 맡기는것이다.

* 3way merge : 2개의 branch가 여러부분 충돌할때 base branch를 추가로 merge하여  
               base에서 수정된 부분을 데려와 comflict를 줄여 merge할수잇는 방법

* git workflow : 복잡한branch,merge 등을 병합

* cherrypick : branch(전체가아닌 당시버전)를 부분적으로 병합  
> * `git cherry-pick (버전값)` : 병합하고자한 branch위에서 실행시 현재 branch에 해당부분의 버전값을 끌고와 병합한다.  

* rebase : otherbranch의 base를 master branch에 순차적으로 병합시킨다, **타임라인(로그)이깔끔하게유지**    
           re+base > base를 옮긴다(log가 선형적으로, 깔끔하게 보인다)  
           **rebase와 merge 는 과정이다를뿐 결과는 같다. 같아야한다**
> *  `git rebase (branch이름)` : 옮기려는 branch로 가서 (branch이름)을 base로 삼는다  

* `git clone (remote repository URL)` : remote repository의 파일을 복사하여 내위치에 복제한다. 

* `git pull` : remote repository의 최신버전을 다운로드하는것 
> * clone과 차이점 clone은 전체를복사, pull은 최신변경점만수정

* 협업시 push,pull,commit을 자주해야한다, > 커뮤니케이션의 활발화가 중요하다, conflict방지

* pull vs fetch
> * git pull = git fetch; git merge origin/master(or FETCH_HEAD) 와 같다.  
    fetch 햇을시 local repository의 head는 remote repository의 head보다 1 commit뒤에잇다.  
    이때 fetch한 remote repository의 데이터는 .git/FETCH_HEAD 안에 들어잇다.  
    **fetch 는 조금더 신중하게 자료를 받고싶을때** 사용한다. 결합은나중에, 우선가져오기

* patch : push 할 권한이 없는 타인이 원래 주인에게 유효한 작업을 전달힐때사용
> * `git format-patch (origin\master의 버전)` : origin/master 버전 이후의 새로작업한 파일을 patch란 확장자로 새로 파일을 생성한다.
>> * 주인은` git commit amend (패치파일)` 이란 명령어를 사용 
>> * `git am -3 -i *.patch` : 3way merge를 통해 현명하게 적용 -i는 하나 적용할때마다 물어보기
