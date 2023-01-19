# Lab_share

## 소개

내가 만든 프로그램을 그룹원들과 공유하기 위해 만듬.

에러나 오류등에 대해서 말씀해 주시면 감사하겠습니다.


## 접근 & 권한
  다음 파일에 접근해야합니다.
* .bashrc

home에 다음 폴더를 만들어야 합니다.
* .rws


## 설치 방법
1. 본 git repositories를 개인 ubuntu에 clone합니다. (어디에 하던지 상관 없음.)

```
git clone https://github.com/johninkorea/lab_share.git
```
2. 해당 폴더 안으로 들어갑니다.
```
cd lab_share
```
3. 설치파일을 실행해 줍니다.
```
sh setup.sh
```
4. 터미널을 다시 시작합니다.

(설치후 clone 한 레파지토리는 삭제해도 됌)


## 사용 방법
### murnaghan fitting
1. 에너지 데이터가 저장되어있는 폴더로 들어갑니다. (ex 폴더 안에 에너지 파일 예시가 있음.)

2. 아래 명령어를 실행.
```
mplot
```
2. fitting을 하기 위한 데이터 파일을 번호를 입력하여 줍니다.
3. plot된 그림을 확인하고 출력된 결과를 POSCAR에 이용합니다.

### make surface for MD
1. 평면 구조를 만드려는 bulk 구조가있는 폴더로 이동.

2. 아래 명령어를 실행.
```
surface -in=./POSCAR
```
* 옵션
  -in --input_file :: 평면을 구서할 인풋 벌크 구조. vasp POSCAR and Cif 가능
  
  -M  --miller_index :: 결과의 단면을 마일러 인덱스로 정의. defult=0,0,1
  
  -S  --slab :: 평면의 구께를 정의. defult=10A
  
  -V  --vacuum :: 진공의 길이를 정의. defult=10A
  
  -SC --supercell :: 기본 결과는 primitive cell로 나옴, 평면을 크게 정의하고 싶을 때 설정. ex) -SC=2,2,1
  
  -R  --result :: 결과 형식을 POSCAR or lammps 중에 선택. 문자로 p or l을 입력.
  
  -B  --bottom :: 평면을 cell의 바닥으로 내릴 것인지. defult=True. False를 원하면 숫자 0을 입력.

  주의!
    lammps 결과에서 3번째 열을 보면 0.000으로 나와있음. 이부분을 지워야함!!

3. 결과 확인


### ~~mscp~~ (현재 사용할 수 없음)

~~scp를 할때 코드를 줄여준다.~~

~~scp해서 파일이 도착할 지점에서 다음 코드를 입력~~
```
mscp
```
~~slurm에서 파일의 주소를 입력한다. (pwd 사용)~~


