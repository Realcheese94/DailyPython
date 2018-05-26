#추상화 된  META list 클래스
class BaseList:
    #데이터 추가
    def append(self,data):
        raise NotImplemented
    #데이터 검색
    def search(self,data):
        raise NotImplemented
    #데이터 참조
    def get(self,index):
        raise NotImplemented       
    #데이터 꺼내오기
    def pop(self):
        raise NotImplemented
    #데이터 삭제
    def remove(self,index):
        raise NotImplemented
    #데이터 전체 출
    def display(self):
        raise NotImplemented

##############################################

class MyList(BaseList):
    count = 0
    def __init__(self):
        self.list = []
        self.count = -1
        print("리스트 생성 완료 !")

    #추가
    def append(self):
        ap = input("추가할 요소를 입력해주세요")
        self.list.append(ap)
        self.count += 1
        print(self.list)
        
        


    #전체 출력
    def display(self):
        print(self.list)
        

    #삭제
    def remove(self):
        index = int(input("제거할 인덱스를 입력해주세요"))
        if index > self.count or index <0:
            print("인덱스 에러입니다. 올바른 인덱스 값을 입력해주세요")
        else:
            self.list.pop(index)
            print("제거를 성공했습니다. 현재 리스트 ",self.list)
        
        
    #검색
    def search(self):
        sn = input("찾고자 하는 값을 입력해주세요")
        if sn in self.list:
                 
                 print(sn,"이 리스트에 존재합니다. ",sn,"의 인덱스 값은 ",self.list.index(sn),"입니다")
        else:
                 print("검색 결과 없습니다.")
        

    #마지막 원소 삭제
    def pop(self):
        self.list.pop()
        print("마지막 원소 삭제를 성공했습니다. 현재 리스트는 ",self.list)
        
        
    
    def listclear(self):
        self.list=[]
        
    
list1 = MyList()
count = -1
while True:
    print('\n\n------------할 작업을 선택하세요-----------\n')
    print('1. append / 2. remove / 3. POP / 4. search / 5. display / 6.exit')
    num = int(input(">>>>"))
    
    if num ==1:
        list1.append()
        
    elif num ==2:
        list1.remove()            

    elif num ==3:
        list1.pop()

    elif num ==4:
        list1.search()
    elif num ==5:
        list1.display()
    else:
        print("프로그램을 종료합니다")
        break
            
        
