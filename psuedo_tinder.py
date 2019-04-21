import mysql.connector
class ddlj:
    def __init__(self):
        self.conn=mysql.connector.connect(user="root",password="",host="localhost",database="ddlj")
        self.mycursor=self.conn.cursor()
        self.program_menu()
    def program_menu(self):
        program_input=input("""Welcome to our app...
        1.Press 1 to register
        2.Press 2 to login
        3.Press anything else to exit""")
        if program_input=="1":
            self.register()
        elif program_input=="2":
            self.login()
        else:
            exit()

    def user_menu(self):
        user_input=input("""What would u like to do ?
        1. Enter 1 to view all users and send proposals
        2. Enter 2 to see whom u proposed
        3. Enter 3 to see who proposed u
        4. Enter 4 to see all ur matches
        5. Enter anything else to logout.""")

        if user_input=='1':
            self.view_users()
        elif user_input=='2':
            self.view_proposed()
        elif user_input=='3':
            self.view_proposals()
        elif user_input=='4':
            self.view_matches()
        else:
            self.is_logged_in=0
            self.program_menu()

    def register(self):
        name =input("Enter your name..")
        email=input("Enter ur email")
        password=input("Enter ur password")
        gender =input("Specify ur gender")
        city=input("Where are u from ?")

        query="""INSERT INTO `users`
        (`user_id`, `name`, `email`,`password`,`gender`,`city`)
        VALUES
        (NULL,'{}','{}','{}','{}','{}')""".format(name,email,password,gender,city)

        self.mycursor.execute(query)
        self.conn.commit()
        print(" Congratulations Registration Successful")
        self.is_logged_in=1
        query = """SELECT * FROM `users` WHERE 
               `email` LIKE '{}' """.format(email)
        self.mycursor.execute(query)
        used_info = self.mycursor.fetchall()
        self.current_user_id=used_info[0][0]
        self.user_menu()

    def login(self):
        email=input("Enter ur email")
        password=input("Enter ur password")

        query="""SELECT * FROM `users` WHERE
        `email` LIKE '{}' AND `password`LIKE
         '{}'""".format(email,password)

        self.mycursor.execute(query)
        user_info=self.mycursor.fetchall()
        if len(user_info)==1:
            print(" :: Welcome :: ")
            self.is_logged_in=1
            self.current_user_id=user_info[0][0]
            self.user_menu()
        else:
            print("""Incorrect email / password
            Please try again...""")
            self.program_menu()

    def view_users(self):
        query="""SELECT * FROM `users` WHERE `user_id` NOT LIKE '{}'""".format(self.current_user_id)

        self.mycursor.execute(query)
        all_user_list=self.mycursor.fetchall()

        for i in all_user_list:
            print("---------------------------------")
            print(i[0],"|",i[1],"|",i[2],"|",i[4],"|",i[5])
            print("---------------------------------")

        self.proposed_users_id=input("Enter the id of the person whom u wanna propose")
        self.propose()


    def propose(self):
        query="""INSERT INTO `proposal`
        (`proposal_id`, `romeo_id`,`juliet_id`) VALUES(NULL,'{}','{}')""".format(self.current_user_id,self.proposed_users_id)
        self.mycursor.execute(query)
        self.conn.commit()
        print("Proposal sent")
        self.user_menu()



    def view_proposed(self):
        query="""SELECT * FROM `proposal` p 
        JOIN `users` u 
        ON u.`user_id`=p.`juliet_id`
        WHERE p.`romeo_id`='{}'""".format(self.current_user_id)

        self.mycursor.execute(query)
        proposed_user_list=self.mycursor.fetchall()
        if len(proposed_user_list) == 0:
            print(" U have not send any proposals yet \n  If want to send proposals enter 1 and if not enter 0" )
            proposed_input=input("Enter 1 or 0")
            if proposed_input=='1':
                self.view_users()
            else:
                self.user_menu()

        else:
            for i in proposed_user_list:
                print("------------------------------")
                print(i[4], "|", i[5], "|", i[7], "|", i[8])
                print("------------------------------")

        self.user_menu()

    def view_proposals(self):
        query = """SELECT * FROM `proposal` p 
         JOIN `users` u 
         ON u.`user_id`=p.`romeo_id`
         WHERE p.`juliet_id`='{}'""".format(self.current_user_id)

        self.mycursor.execute(query)
        proposals_user_list=self.mycursor.fetchall()
        if len(proposals_user_list) == 0:
            print(" Sorry!!! \n U have not recieved any proposals yet")
        else:
            for i in proposals_user_list:
                print("------------------------------")
                print(i[4], "|", i[5], "|", i[7], "|", i[8])
                print("------------------------------")

        self.user_menu()

    def view_matches(self):
        query="""SELECT * FROM `proposal` p
         JOIN `users`u ON u.`user_id`=p.`juliet_id` WHERE p.`juliet_id` IN
        (SELECT p.`romeo_id` FROM `proposal` p WHERE p.`juliet_id`='{}')
        AND p.`romeo_id`='{}'""".format(self.current_user_id,self.current_user_id)
        self.mycursor.execute(query)
        matched_user_list = self.mycursor.fetchall()

        if len(matched_user_list) == 0:
            print(" Sorry!!! No matches found yet")
        else:
            for i in matched_user_list:
                print("------------------------------")
                print(i[4], "|", i[5], "|", i[7], "|", i[8])
                print("------------------------------")


        self.user_menu()






# Object of the class
obj1=ddlj()

