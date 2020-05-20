import sys

class Train_reservation:
    def __init__(self):
        self.line = []
        self.now = []
        self.seat_train = []
        self.seat_change = []

    def T_list(self):
        try:
            self.Train_List = open("C:/Users/지재욱/Desktop/E-on_Train/TrainList.txt", 'r')
            self.line = self.Train_List.read().splitlines()
            del self.line[0]
            self.Train_List.close()
            return self.line
        except IOError:
            print ("IOError가 일어났습니다. 파일이 없어용")

    def train_menu(self):
        while True:
            print("1. 원하시는 시간, 출발역, 도착역, 열차종류 입력 및 빠른 시간대와 예약하기")
            print("2. 전체 기차 시간대 보기 ")
            print("3. 예약 현황, 예약 취소허기 ")
            print("4. 프로그램 종료 ")
            try:
                menu = int(input("메뉴를 입력해주세요 : "))
            except ValueError:   #int형이 아닌 문자형이나 형 오류를 받았을때 실행
                print("메뉴에 없는 내용입니다.")    
                self.train_menu() 
            
            if menu == 1:
                self.my_train()
            elif menu == 2:
                self.all_train_time()
            elif menu == 3:
                self.cancel_train()
            elif menu == 4:
                print(" 프로그램 종료하겠습니다.")
                self.program_off()
                break
            else:
                print ("메뉴에 없습니다. 다시 번호를 입력해주세요.")
                self.train_menu()          #이외의 값 대입시 다시 고르기 
        
    def info_train(self):
        try:
            self.want_train = input("찾으시는 시간, 출발역, 도착역, 열차종류를 입력하세요 : ").split()
            self.want_train[0] = list(map(int,self.want_train[0]))
            return self.want_train
        except ValueError:
            print ("입력이 잘못 되었습니다.")
            self.info_train()
    
    def calculator_train(self):
        self.T_list()
        self.info_train()
        self.time2 = []
        time3 = []
        self.Train_List = open("C:/Users/지재욱/Desktop/E-on_Train/TrainList.txt", 'r')
        self.time_diff = []
        self.start = []
        self.end = []

        while True:
            time1 = self.Train_List.readline()
            
            replacetime1 = time1.replace(":","")
            replacetime2 = replacetime1.replace("\n","")
            if time1:
                self.time2.append(replacetime2[0:4])
                time3.append(replacetime2[-2:])
                self.seat_change.append(replacetime2[0:-2])
                self.start.append(replacetime2[5:8].strip())
                self.end.append(replacetime2[11:14].strip())
            else:
                break  
        del self.time2[0], time3[0], self.seat_change[0],self.start[0],self.end[0]
        
        self.Train_List.close()
        for j in range(len(self.line)):
            self.time2[j] = list(map(int,self.time2[j]))
        self.seat_train = list(map(int,time3))

        for k in range(len(self.line)):
            try:
                self.time_diff.append(600*(self.time2[k][0] - self.want_train[0][0]) + 60*(self.time2[k][1] - self.want_train[0][1]) + 10*(self.time2[k][2] - self.want_train[0][2]) + (self.time2[k][3] - self.want_train[0][3]))
                if self.time_diff[k] < 0:
                    self.time_diff[k] = sys.maxsize
            except IndexError:
                print ("시간 입력이 잘못 되었습니다. ex)0733 으로 적어주세요.")
                self.info_train()
        return self.time_diff
        
    def reservation(self):
        self.calculator_train()
        self.T_list()
        self.near_time = []
        
        for z in range(len(self.time_diff)):
            if (self.want_train[1] == self.start[z]) and (self.want_train[2] == self.end[z]) is True:
                    if self.time_diff[z] == min(self.time_diff):
                        self.near_time.append(self.line[z])        
        return self.near_time

    def my_train(self):
        self.reservation()
        if not self.near_time: #만약 self.near_time에 아무것도  안 들어있으면 
            print ("가까운 시간대가 없거나 입력이 잘못 되었습니다.")
            self.info_train()
        for m in range(len(self.near_time)):
            print (m,".",self.near_time[m])
            if m == (len(self.near_time)-1):
                print (m+1,".","뒤로가기입니다.")         
        
        try: 
            answer = int(input("예매하시겠습니까 ? : "))
        except TypeError:
            print ("잘못 입력하셨습니다.") 
            self.my_train()

        if answer > len(self.near_time) or answer < 0:
            print("목록에 없습니다.")
            self.my_train()
        elif answer == len(self.near_time):
            self.train_menu()
        else:
            for n in range(len(self.line)):
                if self.line[n] == self.near_time[answer]:
                    if self.seat_train[n] == 0:
                        print ("매진 되었습니다.")
                    else: 
                        self.seat_train[n] = self.seat_train[n] - 1
                        self.line[n] = self.seat_change[n] + str(self.seat_train[n])
                        self.now.append(self.line[n])
                        print ("예매 되었습니다.") 
        
        return self.line, self.now, self.seat_train, self.seat_change
              
    def cancel_train(self):
        print ("1. 예매 내역을 출력합니다. ")
        print ("2. 예매 내역을 취소합니다. ")
        print ("3. 뒤로가기 ")
        self.cancel_line = []    
        cancel_input = int(input("입력해주세요 : "))
        if cancel_input == 1:
            print (self.now)
            if not self.now:
                print ("예매된 내역이 없습니다.")
            return self.now
            

        elif cancel_input == 2:
            for g in range(len(self.line)):
                if self.now:
                    if self.now[0] == self.line[g]:
                        self.seat_train[g] = self.seat_train[g] + 1
                        self.line[g] = self.seat_change[g] + str(self.seat_train[g])  
                        print ("예약이 취소되었습니다.") 
                elif not self.now:
                    print ("예매 된 내역이 없습니다.")
                    self.train_menu()
        elif cancel_input == 3:
            self.train_menu()
        else:
            print ("번호가 없습니다. 다시 입력해주세요 : ")
            self.cancel_train()
        
        del self.now[0]
        return self.line, self.now
    
    def all_train_time(self):
        if not self.line:
            self.T_list()
            for h in range(len(self.line)):
                print (self.line[h])
        else:
            for h in range(len(self.line)):
                print (self.line[h])
        
    def program_off(self):
        sys.exit()
                  
if __name__ == "__main__":                    
    j = Train_reservation()
    print (j.train_menu())
    