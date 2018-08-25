

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def getname ():
    for i in range(len(students)):
        print(students[i]['first_name'], students[i]['last_name'])

getname()


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }


def get_users():

    for i in range(len(users['Students'])):
        print(i+1, " -- ", users['Students'][i]['first_name'], users['Students'][i]['last_name'], " -- ",
             len(users['Students'][i]['first_name'])+len(users['Students'][i]['last_name']))
    for k in range(len(users['Instructors'])):
        print(k + 1, " -- ", users['Instructors'][k]['first_name'], users['Instructors'][k]['last_name'], " -- ",
              len(users['Instructors'][k]['first_name']) + len(users['Instructors'][k]['last_name']))

get_users()
