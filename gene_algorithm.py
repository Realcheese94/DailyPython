

import random
from operator import eq
#벽돌을 B 시멘트를 C로 한 target 유전자 리스트 생성
target1_gene=['B','C','B','C','B','C','B','C','B','C']
#target2_gene=['C','B','C','B','C','B','C','B','C','B']

#샘플 유전자 10개 정의
sample1_gene=['C','B','B','C','C','C','C','B','B','B']
sample2_gene=['C','C','C','B','C','C','C','C','B','C']
sample3_gene=['B','C','B','C','B','B','C','C','B','B']
sample4_gene=['C','C','C','C','B','C','C','C','C','B']
sample5_gene=['B','B','B','B','B','B','B','C','B','C']
sample6_gene=['B','B','C','B','C','B','B','B','B','C']
sample7_gene=['B','B','C','B','B','C','C','C','B','B']
sample8_gene=['C','B','B','B','B','B','B','C','C','C']
sample9_gene=['C','B','C','B','B','B','B','C','C','C']
sample10_gene=['C','B','C','B','C','C','B','B','C','C']
gene_similar=[]
sample_list =[sample1_gene,sample2_gene,sample3_gene,sample4_gene,sample5_gene,sample6_gene,sample7_gene,sample8_gene,sample9_gene,sample10_gene,]
myindex_list=[]
#적합도 검사 클래스
class next_Gene():
    def __init__(self,status,gene):
        self.status = status
        self.similar1 = 0
        self.gene = gene
        
    def what_similar(self,target_gene):
        for i in range(1,self.status):
            if self.gene[i] == target_gene[i]:
                self.similar1 += 1
        return self.similar1

#적합도 리스트 중 가장 강한 유전자2개만 검출하는 함수
def next_checkgene(maxvalue,myList):
    indexlist=[]
    for i in myList:
        if maxvalue == myList[i]:
            indexlist.append(i)
    return indexlist

def mating(list1,list2,num):
    num=0
    list3=list1[:rand]+list2[rand:]
    num+=1
    return list3

def simplechanging(indext ,mylist):
    if mylist[index] =='B':
        mylist[index] ='C'
    else:
        mylist[index] ='B'



        #총 샘플의 적합도를 검사한다. 후에 적합도만 모아놓은 리스트에 담는다.
sample1 = next_Gene(10,sample1_gene)
gene_similar.append(sample1.what_similar(target1_gene))
sample2 = next_Gene(10,sample2_gene)
gene_similar.append(sample2.what_similar(target1_gene))
sample3 = next_Gene(10,sample3_gene)
gene_similar.append(sample3.what_similar(target1_gene))
sample4 = next_Gene(10,sample4_gene)
gene_similar.append(sample4.what_similar(target1_gene))
sample5 = next_Gene(10,sample5_gene)
gene_similar.append(sample5.what_similar(target1_gene))
sample6 = next_Gene(10,sample6_gene)
gene_similar.append(sample6.what_similar(target1_gene))
sample7 = next_Gene(10,sample7_gene)
gene_similar.append(sample7.what_similar(target1_gene))
sample8 = next_Gene(10,sample8_gene)
gene_similar.append(sample8.what_similar(target1_gene))
sample9 = next_Gene(10,sample9_gene)
gene_similar.append(sample9.what_similar(target1_gene))
sample10 = next_Gene(10,sample10_gene)
gene_similar.append(sample10.what_similar(target1_gene))





#총 샘플의 적합도를 담은 리스트 출력(테스트 용)
gene_similar




for i in range(1,10):
    if gene_similar[i]==max(gene_similar):
        myindex_list.append(i)


#다음으로 계승될 유전자 2개 선택        
sample1 = sample_list[myindex_list[0]]
sample2 =sample_list[myindex_list[1]]

second_sample=[]

#새롭게 교배된 10개의 자식을 생성 및 list에 저장
for i in range(0,10):
    second_sample.append(sample1[:i]+sample2[i:])
    

#자식 유전자 리스트 출력
second_sample 


gene_similar.clear()
second_sample1=second_sample[0]
second_sample2=second_sample[1]
second_sample3=second_sample[2]
second_sample4=second_sample[3]
second_sample5=second_sample[4]
second_sample6=second_sample[5]
second_sample7=second_sample[6]
second_sample8=second_sample[7]
second_sample9=second_sample[8]
second_sample10=second_sample[9]



#자식 유전자 적합도 함수 처리과정
sample_data1 = next_Gene(10,second_sample1)
gene_similar.append(sample_data1.what_similar(target1_gene))

sample_data2 = next_Gene(10,second_sample2)
gene_similar.append(sample_data2.what_similar(target1_gene))

sample_data3 = next_Gene(10,second_sample3)
gene_similar.append(sample_data3.what_similar(target1_gene))

sample_data4 = next_Gene(10,second_sample4)
gene_similar.append(sample_data4.what_similar(target1_gene))

sample_data5 = next_Gene(10,second_sample5)
gene_similar.append(sample_data5.what_similar(target1_gene))

sample_data6 = next_Gene(10,second_sample6)
gene_similar.append(sample_data6.what_similar(target1_gene))

sample_data7 = next_Gene(10,second_sample7)
gene_similar.append(sample_data7.what_similar(target1_gene))

sample_data8 = next_Gene(10,second_sample8)
gene_similar.append(sample_data8.what_similar(target1_gene))

sample_data9 = next_Gene(10,second_sample9)
gene_similar.append(sample_data9.what_similar(target1_gene))
sample_data10 = next_Gene(10,second_sample10)
gene_similar.append(sample_data10.what_similar(target1_gene))
sample_data1 = next_Gene(10,second_sample1)

sample2_list=[second_sample1,second_sample2,second_sample3,second_sample4,second_sample5,second_sample6,second_sample7,second_sample8,second_sample9,second_sample10,]
gene_similar


#자식 유전자 적합도 함수 처리과정
sample_data1 = next_Gene(10,second_sample1)
gene_similar.append(sample_data1.what_similar(target1_gene))

sample_data2 = next_Gene(10,second_sample2)
gene_similar.append(sample_data2.what_similar(target1_gene))

sample_data3 = next_Gene(10,second_sample3)
gene_similar.append(sample_data3.what_similar(target1_gene))

sample_data4 = next_Gene(10,second_sample4)
gene_similar.append(sample_data4.what_similar(target1_gene))

sample_data5 = next_Gene(10,second_sample5)
gene_similar.append(sample_data5.what_similar(target1_gene))

sample_data6 = next_Gene(10,second_sample6)
gene_similar.append(sample_data6.what_similar(target1_gene))

sample_data7 = next_Gene(10,second_sample7)
gene_similar.append(sample_data7.what_similar(target1_gene))

sample_data8 = next_Gene(10,second_sample8)
gene_similar.append(sample_data8.what_similar(target1_gene))

sample_data9 = next_Gene(10,second_sample9)
gene_similar.append(sample_data9.what_similar(target1_gene))
sample_data10 = next_Gene(10,second_sample10)
gene_similar.append(sample_data10.what_similar(target1_gene))
sample_data1 = next_Gene(10,second_sample1)

sample2_list=[second_sample1,second_sample2,second_sample3,second_sample4,second_sample5,second_sample6,second_sample7,second_sample8,second_sample9,second_sample10,]
gene_similar


myindex_list.clear()
for i in range(0,10):
    if gene_similar[i]==max(gene_similar):
        myindex_list.append(i)


#다음으로 계승될 유전자 2개 선택        
sample1 = sample2_list[myindex_list[0]]
sample2 =sample2_list[myindex_list[1]]

second_sample.clear()

for i in range(0,10):
    second_sample.append(sample1[:i]+sample2[i:])
    

#자식 유전자 리스트 출력
second_sample

gene_similar.clear()
second_sample1=second_sample[0]
second_sample2=second_sample[1]
second_sample3=second_sample[2]
second_sample4=second_sample[3]
second_sample5=second_sample[4]
second_sample6=second_sample[5]
second_sample7=second_sample[6]
second_sample8=second_sample[7]
second_sample9=second_sample[8]
second_sample10=second_sample[9]


#자식 유전자 적합도 함수 처리과정
sample_data1 = next_Gene(10,second_sample1)
gene_similar.append(sample_data1.what_similar(target1_gene))

sample_data2 = next_Gene(10,second_sample2)
gene_similar.append(sample_data2.what_similar(target1_gene))

sample_data3 = next_Gene(10,second_sample3)
gene_similar.append(sample_data3.what_similar(target1_gene))

sample_data4 = next_Gene(10,second_sample4)
gene_similar.append(sample_data4.what_similar(target1_gene))

sample_data5 = next_Gene(10,second_sample5)
gene_similar.append(sample_data5.what_similar(target1_gene))

sample_data6 = next_Gene(10,second_sample6)
gene_similar.append(sample_data6.what_similar(target1_gene))

sample_data7 = next_Gene(10,second_sample7)
gene_similar.append(sample_data7.what_similar(target1_gene))

sample_data8 = next_Gene(10,second_sample8)
gene_similar.append(sample_data8.what_similar(target1_gene))

sample_data9 = next_Gene(10,second_sample9)
gene_similar.append(sample_data9.what_similar(target1_gene))
sample_data10 = next_Gene(10,second_sample10)
gene_similar.append(sample_data10.what_similar(target1_gene))
sample_data1 = next_Gene(10,second_sample1)

sample2_list=[second_sample1,second_sample2,second_sample3,second_sample4,second_sample5,second_sample6,second_sample7,second_sample8,second_sample9,second_sample10,]
gene_similar
sample2_list



Mutation_data = sample2_list[0]
Mutation_data2 = Mutation_data
Mutation_data2


#정확도 수치 
gene_similar.clear()

#변경된 리스트
second_sample.clear()
Mutation_data = Mutation_data2

for i in range(0,10):
    
    if Mutation_data2[i] == 'B':
        Mutation_data2[i] = 'C'
        print(Mutation_data2)
        sample_data9 = next_Gene(10,Mutation_data2)
        second_sample.append(sample_data9.what_similar(target1_gene))
        Mutation_data2[i] = 'B'
        
   
    else:
        Mutation_data2[i]='B'
        print(Mutation_data2)
        sample_data9 = next_Gene(10,Mutation_data2)        
        second_sample.append(sample_data9.what_similar(target1_gene))
        Mutation_data2[i] = 'C'

second_sample
if 9 in second_sample:
    index = second_sample.index(9)
simplechanging(index,Mutation_data)

print(Mutation_data2)
