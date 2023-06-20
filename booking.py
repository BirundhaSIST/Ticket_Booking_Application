#login the user details
#select the city
#see the movies available each theaters_names in that city
#choose expected timing
#select the seat 4 row and 8 column totally 32 seats available in theater
#book the seat
#move to payment

profile=[{'userid':'1','username':'birundha','mailid':'bru@gmail.com','password':'bru@18'}]

city=['1.chennai','2.selam','3.mathurai']

movies=[{'theater_id':'ram@18','movie_id':'tiggor@5','movie_name':'the tiggor movie','language':'English','duration':'2.35 hours','realese_date':'18-04-2003','ticket_cost':'200'
         },{'theater_id':'marval@18','movie_id':'piglet@5','movie_name':'the piglet movie','language':'English','duration':'2.35 hours','realese_date':'31-05-2013','ticket_cost':'200'
         },{'theater_id':'jems@07','movie_id':'winne@5','movie_name':'winne the poo','language':'English','duration':'2.35 hours','realese_date':'16-02-2000','ticket_cost':'200'
         }]

theater=[{'theater_id':'ram@18','theater_name':'ram','location':'chennai','AC or NC':'AC','movie_name':'the tiggor movie'},
         {'theater_id':'marval@18','theater_name':'marval','location':'selam','AC or NC':'AC','movie_name':'the piglet movie'},
         {'theater_id':'jems@07','theater_name':'007','location':'mathurai','AC or NC':'AC','movie_name':'winne the poo'}]

select_timing=[{'theater_id':'ram@18','timing':['1.Morning show : 9.00 AM - 11.35 AM' , '2.Noon show : 12.00 AM - 2.35 PM', '3.Evening show : 3.00 PM - 5.35 PM', '4.Ninght show : 7.00 PM - 9.35 PM']},
               {'theater_id':'marval@18','timing':['1.Morning show : 9.00 AM - 11.35 AM' , '2.Noon show : 12.00 AM - 2.35 PM', '3.Evening show : 3.00 PM - 5.35 PM', '4.Ninght show : 7.00 PM - 9.35 PM']},
               {'theater_id':'jems@07','timing':['1.Morning show : 9.00 AM - 11.35 AM' , '2.Noon show : 12.00 AM - 2.35 PM', '3.Evening show : 3.00 PM - 5.35 PM', '4.Ninght show : 7.00 PM - 9.35 PM']}]

seats=[{'1':[[0,0,1,0,0,0,1,0,1],[0,0,1,0,0,0,1,0],[1,0,1,0,0,1,1,1]]},
       {'2':[[0,0,1,0,0,0,1,0,1],[0,1,1,0,0,0,1,0],[0,0,1,0,0,1,1,1]]},
       {'3':[[0,0,1,0,0,1,1,0,1],[0,0,1,0,0,0,1,0],[1,0,1,0,0,1,1,1]]},
       {'4':[[0,0,1,0,0,0,1,0,1],[0,0,1,0,0,0,1,0],[1,0,1,0,0,1,1,1]]}]

booking_history=[{'userid':'1','history':[{'booking_date':'17-06-2023','booking_time':'01:30 PM','theater_name':'marval','movie_name':'fast and furious'}]}]
payment_history=[{'userid':'1','history':[{'user_name':'birundha','amount':'200','booking_date':'18-04-2023','booking_time':'09:30 AM','theater_name':'007','movie_name':'The Nun'}]}]

class user_profile():
    
    def __init__(self):
        self.userid=None
        self.username=None
        self.mailid= None
        self.password=None
        self.login=None
        
    def login_Or_sign_up(self):
        print('--1.already have an account--\n--2.create new account--')
        choose=int(input('enter your choice :'))
        
        if (choose==1):
            self.mailid=input('enter your mail_id : ')
            self.password=input('enter your password : ')
            for i in range(0,len(profile)):
                if (profile[i]['mailid']==self.mailid and profile[i]['password']==self.password): #validating the mailid & password
                    self.username=profile[i]['username']
                    self.userid=profile[i]['userid']
                    print("-------------------you are succesfully loged in---------------------")
                    self.login=1
                    break
                elif i==len(profile)-1:
                    print("please enter valid username and password")
                    
        elif (choose==2):
            self.mailid= input('enter your mail_id : ')
            self.username=input('enter your username : ')
            self.password=input('enter your password : ')
            self.userid=(self.password)+'@30'
            profile.append({'userid':self.userid,'username':self.username,'mailid':self.mailid,'password':self.password})
            print("your account has been created succesfully")
            self.login=1

class choose_theater():
    
    def __init__(self):
        self.location=None
        self.theater_name=None
        self.theater_id=None
        
        print('___________________available cities___________________')
        for i in city:
            print(i)
        x=int(input("please enter your choise from above list :"))
        self.location=city[x-1][2::]
        print('\n')
        print(" The theaters available in "+self.location)
        
    def search(self):
        for i in theater:
            if i['location']==self.location: #searching the theaters in the specified location
                print('--------------------------------------------------------------')
                for j in list(i)[1::]:
                    print(j+' : '+i[j])
                print('--------------------------------------------------------------')
                    
        self.theater_name=input("choose the theater_name you want to watch movie : ")
        
        for i in theater:
            if i['theater_name']==self.theater_name:
                self.theater_id=i['theater_id']
                

class movie():
    
    def __init__(self):
        self.movie_name=None
        self.theater_id=c.theater_id
        
    def search(self): #plymorphysm
        for i in movies:
            if self.theater_id==i['theater_id']:  #searching the movie at the specified theater in movies list
                print("--------------informations about the movie in "+c.theater_name+" theater---------------------")
                for j in list(i)[2::]:
                    print(j+' : '+i[j])
                    if j=='movie_name':
                        self.movie_name=i[j]
                print('--------------------------------------------------------------')

class select_time():
    
    def __init__(self):
        self.show_time=None
        self.theater_id=c.theater_id
        self.time=None
        
    def search(self): #plymorphysm
        print("\n")
        print("_________________Available timings in "+c.theater_name+"__________________")
        for k in range(0,len(select_timing)):
            if select_timing[k]['theater_id']==self.theater_id:  #searching the timings available in that particula theater
                for j in select_timing[k]['timing']:
                        print(j)
        print("--------------------------------------------------------")
        self.time=input("Enter your choise of expected time from the list of times:")


class booking():
    
    def __init__(self):
        self.book=None
        self.time=t.time
        self.no_of_seats=None
        self.seat_no=[]
        self.all_seats=None
        self.available_seats=None
        
    def search(self): #searching the unbooked seats by using matrix
        print("------------------choose one of the available seats-------------------")
        y=seats[int(self.time)-1]
        x=y[self.time]
        l=[]
        for i in x:
            z=x.index(i)
            for j in range(0,len(i)):
                if i[j]==0:
                    l.append((z*8)+j)
        print(l) # printing only the available seats for the user
        self.all_seats=x
        self.available_seats=l
        
    def seat_booking(self): #bookin the user specified seats
        x=self.all_seats
        l=self.available_seats
        self.n=int(input("enter the number of seats you want : "))
        self.no_of_seats=self.n
        c=0
        s=[]
        for i in range(self.n):
            h=int(input("enter your "+str(i+1)+"th seat number from the list: "))
            s.append(h)
            (self.seat_no).append(h)
        for i in s:
            if i<8:
                x[0][i]=1
                c+=1
            elif i>=8 and i<=15:
                x[1][i-8]=1
                c+=1
            elif i>=16 and i<=23:
                x[2][i-16]=1
                c+=1
            else:
                print("seat number is invalid")
                break
        if c==self.n:
            self.book=1
            print("-------------------your seat booked succesfully-------------------------")
        print("\n")
        
    def history(self): # booking history 
        
        print("_____________________your booking history______________________")
        x=None
        for i in range(0,len(booking_history)):
            
            if booking_history[i]['userid']==l.userid: #linear search
                booking_history[i]['history'].append({'user_name':l.username,'no_of_seats':str(self.no_of_seats),'seat_no':str(self.seat_no),'booking_date':date_time[0],'booking_time':date_time[1],'theater_name':c.theater_name,'movie_name':m.movie_name})
       
            elif booking_history==[] or i==len(booking_history)-1:
                booking_history.append({})
                booking_history[-1]['userid']=l.userid
                booking_history[-1]['history']=[]
                booking_history[-1]['history'].append({'user_name':l.username,'no_of_seats':str(self.no_of_seats),'seat_no':str(self.seat_no),'booking_date':date_time[0],'booking_time':date_time[1],'theater_name':c.theater_name,'movie_name':m.movie_name})
                
        for i in range(0,len(booking_history)):
            if booking_history[i]['userid']==l.userid:
                x=(booking_history[i]['history'][::]).pop(-1) #LIFO stack
                
        for i in x:
            print(i+':'+x[i])
        print('___________________please go for payment________________')
        print('\n')   


class payment():
    
    def __init__(self):

        self.payment_method=None
        self.cost=None
        self.payment_status=None
        for i in range(0,len(movies)):
            if movies[i]['theater_id']==c.theater_id :
                self.cost=movies[i]['ticket_cost']
                
        print('************************ticket cost is '+str(self.cost)+'************************')
        print('\n')
        print('------------------------Available payment methods-------------------------')
        print('1:online_payment\n2:card')
        self.payment_method=int(input('please enter your choice :'))

    def online_payment(self):
        print('please scan the QR code and pay the amount')
        self.payment_status='done'
        
    def card(self):
        card_number=input('please enter your credit card number :')
        card_holder_name=input('please enter card_holder_name :')
        CVV_number=input('please enter card CVV number which is the three-digit number on the back of your card :')
        print('please conform the three digit OTP which we sent to your mail')
        print('\n')
        self.payment_status='done'
        
    def history(self): #polymorphism
        if self.payment_method==1:
            method='online_payment'
        else:
            method='creadit_card_payment'
            
        if self.payment_status=='done':
            for i in range(0,len(payment_history)):
                if payment_history[i]['userid']==l.userid: #linear search
                    payment_history[i]['history'].append({'user_name':l.username,'amount':self.cost,'payment_method':method,'payment_date':date_time[0],'payment_time':date_time[1],'theater_name':c.theater_name,'movie_name':m.movie_name})
        
                elif payment_history==[] or i==len(payment_history)-1:
                    payment_history.append({})
                    payment_history[-1]['userid']=l.userid
                    payment_history[-1]['history']=[]
                    payment_history[-1]['history'].append({'user_name':l.username,'amount':self.cost,'payment_method':method,'payment_date':date_time[0],'payment_time':date_time[1],'theater_name':c.theater_name,'movie_name':m.movie_name})
        print("_____________________your payment history______________________")
        for i in range(0,len(booking_history)):
            if payment_history[i]['userid']==l.userid:
                x=payment_history[i]['history'][::].pop(-1) #LIFO stack
        for i in x:
            print(i+':'+x[i])
        print('\n')   
        print('-------------your payment has been succesfully done--------------------')
        print(' ')
        print('                      thankyou for booking have a nice day  (. _ .)                     ')


if __name__ == "__main__":
    
    from datetime import datetime
    import time
    
    now=datetime.now()
    
    date_time=list(str(now).split(" "))
    l=user_profile()
    l.login_Or_sign_up()
    
    if l.login==1:
        c=choose_theater()
        c.search()
        m=movie()
        m.search()
        t=select_time()
        t.search()
        b=booking()
        b.search()
        b.seat_booking()
        if b.book==1:
            b.history()
        if b.book==1:
            p=payment()
            x=p.payment_method
            if x==1:
                p.online_payment()
                p.history()
            elif x==2:
                p.card()
                p.history()
            else:
                print('please enter valid choice')










        
        
