import mysql.connector
from mysql import connector


class StudentManager:
    def __init__(self):
        self.connection = connector.connect(
            host="localhost",
            user="root",
            password="Sana#2004",
            database="student_db"
        )

        print("Connected Successfully..!")


    def get_object(self, id=None):
        try:
            self.cursor = self.connection.cursor()
            query = "select * from student where id = %s"
            values = (id,)

            self.cursor.execute(query, values)

            record = self.cursor.fetchone()

            return record

        except Exception as e:
            return None

    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()

            query = """
            INSERT INTO student (name, age, course, phone, city)
            VALUES (%s, %s, %s, %s, %s)
            """

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)
            self.connection.commit()

            print("Student added Successfully..!")

        except Exception as e:
            print(e)

    def get(self):
        try:
            self.cursor = self.connection.cursor()

            query = "select * from student"

            self.cursor.execute(query)

            records = self.cursor.fetchall()

            for data in records:
                print(data)

        except Exception as e:
            print(e)

    def retrieve(self, id=None):
        try:
            record = self.get_object(id=id)

            if record == None:
                print("Record not found..")

            else:
                print(record)

        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            record = self.get_object(id=id)

            values = (id,)

            if record != None:
                query = "delete from student where id = %s"
                self.cursor.execute(query, values)
                self.connection.commit()
                print("student deleted Successfully..!")
            else:
                print("student not found..")

        except Exception as e:
            print(e)

    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)

            if record != None:
                self.cursor = self.connection.cursor()

                placeholder = ""

                for k in kwargs.keys():
                    placeholder += k + " = %s,"

                placeholder = placeholder.strip(",")

                query = f"update student set {placeholder} where id=%s"

                values = [v for v in kwargs.values()]
                values.append(id)

                self.cursor.execute(query, values)
                self.connection.commit()

                print("student details updated successfully...!!")

            else:
                # if no record is found
                print("student details not updated successfully...!!")

        except Exception as e:
            print(e)


student_instance = StudentManager()
# student_instance.post(
#     name="Anu",
#     age=21,
#     course="B.Tech AI & Data Science",
#     phone="9876543210",
#     city="Kochi"
# )
#
# student_instance.post(
#     name="Rahul",
#     age=22,
#     course="BCA",
#     phone="9123456780",
#     city="Thrissur"
# )
#
# student_instance.post(
#     name="Meera",
#     age=20,
#     course="B.Tech Computer Science",
#     phone="9012345678",
#     city="Aluva"
# )
#
# student_instance.post(
#     name="Arjun",
#     age=23,
#     course="MCA",
#     phone="8765432109",
#     city="Kottayam"
#)
print("---------------------get-------------")
student_instance.get()
print("----------------retrieve----------------")
student_instance.retrieve(1)
print("------------delete-------------")
student_instance.delete(1)
student_instance.get()
print("----------put/update---------------")
student_instance.put(2,city="calicut")
student_instance.get()