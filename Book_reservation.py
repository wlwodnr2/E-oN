import os

class Book_R:
    def __init__(self):
        self.Book_read = ''

    def change_txt(self):
        
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'input.txt')
        Book_list = open(my_file,'r')
        self.Book_read = Book_list.readlines()
        for i in range(len(self.Book_read)):
            self.Book_read[i] = self.Book_read[i].strip().split()
        
        Book_list.close()
        return self.Book_read
        

    def Book_input(self):
        try:
            self.Book_in = input("도서명, 저자, 출판연도, 출판사명, 장르를 차례대로 입력해주세요 : ").split()
            if len(self.Book_in) != 5:
                print ("입력이 누락되었습니다. 다시 입력해주세요")
                self.Book_input()
            real_number = self.Book_in[2]
            if real_number.isnumeric() != True:   #숫자로 입력했는지 확인하는 변수
                print ("출판연도가 잘못 되었습니다 숫자로 입력 바랍니다.")
                self.Book_input() 
            self.Book_read.append(self.Book_in)
            return self.Book_read
        except EOFError:
            print("E0FError 일어났습니다.")
       
    def Book_search(self):
        print("1.전체 입력으로 찾기, 2.개별 입력으로 찾기")
        number = int(input("어떻게 찾으시겠습니까? : "))
        if number == 1:
            self.search_b = input("도서명, 저자, 출판연도, 출판사명, 장르를 차례대로 입력해주세요 : ").split()
            for i in range(len(self.Book_read)):
                if self.search_b == self.Book_read[i]:
                    print (self.Book_read[i])
                else:
                    print ("목록에 없습니다.")
        elif number == 2:
            what = int(input("0.도서명, 1.저자, 2.출판연도, 3.출판사명, 4.장르 : "))
            self.search_one = input("찾으시는것을 입력해주세요 : ")
            for i in range(len(self.Book_read)):
                if self.search_one == self.Book_read[i][what]:
                    print (self.Book_read[i])
                    
        else:
            print ("잘못 입력하셨습니다.")
            self.Book_search()

    def Book_fix(self):
        self.print_all()
        choose_book = int(input("몇 번 도서를 수정하시겠습니까 ? : "))
        if choose_book > len(self.Book_read) or choose_book < 0:
            self.Book_fix()
        else:
            print ("1. 도서명 수정, 2. 저자 수정, 3. 출판연도 수정, 4. 출판사명 수정, 5. 장르 수정") 
            self.fix = int(input("어떤 것을 수정하시겠습니까? : "))
            self.Book_read[choose_book][self.fix-1] = input("수정할 내용을 입력해주세요 : ")
            return self.Book_read

    def Book_delete(self):
        self.print_all()
        delete_number = int(input("몇 번 도서를 삭제하시겠습니까? : "))
        if delete_number > len(self.Book_read) or delete_number < 0:
            self.Book_delete()
        else:
            del self.Book_read[delete_number]
    
    def print_all(self):
        for j in range(len(self.Book_read)):
            print (j,"번",self.Book_read[j])

    def save(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'input.txt')
        Book_list = open(my_file,'w')
        for k in range(len(self.Book_read)):
            Book_list.writelines(' '.join(self.Book_read[k]))
            Book_list.writelines('\n')
        Book_list.close()