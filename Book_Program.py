import Book_reservation
import sys
import os

class Book_P:
    def __init__(self):
        self.Book_compare = Book_reservation.Book_R()
        self.Book_compare.change_txt()

    def Book_menu(self):
        while True:
            print("1. 도서 추가 ")
            print("2. 도서 검색 ")
            print("3. 도서 정보 수정 ")
            print("4. 도서 삭제 ")
            print("5. 현재 총 도서 목록 출력 ")
            print("6. 저장 ")
            print("7. 프로그램 나가기 ")

            try:
                menu = int(input("메뉴를 입력해주세요 : "))
            except ValueError:
                print("메뉴에 없는 내용입니다.")
                continue
            
            if menu == 1:
                self.Book_compare.Book_input()
            elif menu == 2:
                self.Book_compare.Book_search()
            elif menu == 3:
                self.Book_compare.Book_fix()
            elif menu == 4:
                self.Book_compare.Book_delete()
            elif menu == 5:
                self.Book_compare.print_all()
            elif menu == 6:
                self.Book_compare.save()
            elif menu == 7:
                print(" 프로그램 종료하겠습니다.")
                self.Book_compare.save()
                break
            else:
                print ("메뉴에 없습니다. 다시 번호를 입력해주세요.")
                self.Book_menu()          #이외의 값 대입시 다시 고르기 
    
if __name__ == "__main__":                    
    a = Book_P()
    print (a.Book_menu())
 