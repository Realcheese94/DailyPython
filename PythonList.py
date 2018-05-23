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
    def __init__(self):
        self.list = []
        self.count = -1
        print("리스트 생성 완료 !")

    #추가
    def append(self,data):
        self.list.append(data)
        self.count += 1


    #전체 출력
    def display(self,count):
        print(self.list[0:count+1])

    #삭제
    def remove(self,index,list,count):
        for i in range(index,count,1):
            self.list[i]=self.list[i+1]
            
        self.list[-1]=""
        
    #검색
    def search(self,index):
        try:
            print(index ,"번째 요소는", self.list[index])
        except IndexError:
            print("Index 가 올바르지 않습니다. 0~ ",self.count,"까지의 수를 입력하세요")

    #마지막 원소 삭제
    def pop(self):
        self.list[-1]=[]
        
    
    def listclear(self):
        self.list=[]
        
    
list1 = MyList()
count = -1
for i in range(1,10):
    print('\n\n------------할 작업을 선택하세요-----------\n')
    print('1. append / 2. remove / 3. POP / 4. display / 5. search')
    num = int(input(">>>>"))
    
    if num ==1:
        ap = input("append 할 요소를 입력해주세요")
        list1.append(ap)
        count += 1
        list1.display(count)
        print("현재 리스트의 최고인덱스 수는 ",count,"입니다")
        
    elif num ==2:
        rm = int(input("삭제할 인덱스를 입력해주세요"))
        #인덱스가 올바르게 입력되지 않은 경우.
        if rm < 0 or rm>count:
            print("인덱스 에러 다시 입력해주세요")
            
        else:
            list1.remove(rm,list1,count)
            count -= 1
            list1.display(count)

    elif num ==3:
        list1.pop()
        count-=1
        list1.display(count)
        #stop
            
        
