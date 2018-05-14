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

        
    def append(self,data):
        self.list.append(data)
        self.count += 1


        
    def display(self):
        print(self.list)



        
    def search(self,index):
        try:
            print(index ,"번째 요소는", self.list[index])
        except IndexError:
            print("Index 가 올바르지 않습니다. 0~ ",self.count,"까지의 수를 입력하세요")


    def pop(self):
        pass
    
list1 = MyList()

for i in range(1,10):
    print('\n\n------------할 작업을 선택하세요-----------\n')
    print('1. append / 2. remove / 3. POP / 4. display / 5. search')

    ip = int(input(">>>>>>>>>>>>>"))
    if ip==1:
        anum = print(input("append 요소 입력"))
        list1.append(anum)
    elif ip==2:
        index = print(int((input("remove index 입력"))
                          
