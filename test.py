import logging
logging.basicConfig(filename="test.log",level=logging.DEBUG)

#inheritance:
try:
    class ineuron:
        def __init__(self ,student_name,class_mode,number_of_courses,class_name,job):
            self.student_name=student_name
            self.class_mode=class_mode
            self.number_of_courses=number_of_courses
            self.class_name=class_name
            self.job=job

            antu_var = ineuron("antu","full stack data science","online","20","ju.data scientist")
            logging.info(antu_var.student_name)
            logging.info(antu_var.class_name)
            logging.info(antu_var.class_mode)
            logging.info(antu_var.number_of_courses)
            logging.info(antu_var.job)
except Exception as e:
    logging.exception(e)

try:
    class Data_science:
        def __init__(self,candidate_name,position,salary,qualification,mode_of_work):
            self.candidate_name=candidate_name
            self.position=position
            self.salary=salary
            self.qualification=qualification
            self.mode_of_work=mode_of_work

            sudh=Data_science("sudhanshu","sr.data scientist","24 LPA","B.Tech","offline")
            logging.info(sudh.candidate_name)
            logging.info(sudh.position)
            logging.info(sudh.salary)
            logging.info(sudh.qualification)
            logging.info(sudh.mode_of_work)
except Exception as e:
    logging.exception(e)

try:
    class layoutdesign:
        def __init__(self,employee,work,position,qualification,grade):
            self._employee=employee
            self.__work=work
            self.position=position
            self._qualification=qualification
            self.__grade=grade

            avinash_var=layoutdesign("avinash","layout design","sr.engineer","B.tech","A")
            logging.info(avinash_var._employee)
            logging.info(avinash_var._layoutdesign.__work)
            logging.info(avinash_var.postion)
            logging.info(avinash_var._qualification)
            logging.info(avinash_var._layoutdesign.__grade)
except Exception as e:
    logging.exception(e)

try:
    class ssc:
       def __init__(self,name,department,designation,salary,work,grade):
            self.name=name
            self.department=department
            self.designation=designation
            self.salary=salary
            self.work=work
            self.grade=grade

            anuj=ssc("anuj kumar","CBDT/CBIC","Tax assistant","10000","clerical","C")
            logging.info(anuj.name)
            logging.info(anuj.department)
            logging.info(anuj.designation)
            logging.info(anuj.salary)
            logging.info(anuj.work)
            logging.info(anuj.grade)
except Exception as e:
    logging.exception(e)

try:
    class doctor:
        def __init__(self,name,designation,salary,hospital,city):
            self.name=name
            self.designation=designation
            self.salary=salary
            self.hospital=hospital
            self.city=city

            nalini=doctor("nalini","surgeon","252040","apollo","indore")
            logging.info(nalini.name)
            logging.info(nalini.designation)
            logging.info(salary)
            logging.info(hospital)
            logging.info(city)
except Exception as e:
    logging.exception(e)



try:
    class ineuron:
        def __init__(self,name,course,internship,salary,):
            self._name=name
            self.__course=course
            self._internship=internship
            self.__salary=salary

            antima_var=ineuron("antima","full stack data science","1 year","5 LPA")
            logging.info(antima_var._name)
            logging.info(antima_var._ineuron.__course)
            logging.info(antima_var._internship)
            logging.info(antima_var._ineuron.__salary)
except Exception as e:
    logging.exception(e)

try:
    class ineuron:
        def __init__(self,name,surname,email_id,salary,year_of_birth):
            self.name=name
            self.surname=surname
            self._email_id=email_id
            self.__salary=salary
            self.year_of_birth=year_of_birth
        def age(self,current_year):
            return current_year-self.year_of_birth

        sheetal=ineuron("sheetal","rathore","sheetalrathore123@gmail.com","12LPA","1999")
        logging.info(sheetal.age(2022))
        logging.info(sheetal.name)
        logging.info(sheetal.surname)
        logging.info(sheetal._email_id)
        logging.info(sheetal._ineuron__salary)
        logging.info(sheetal.year_of_birth)
except Exception as e:
    logging.exception(e)

try:
    class ineuron:
        def __init__(self,name,class_name,number_of_courses,affiliates,blog):
            self.name=name
            self.class_name=class_name
            self.number_of_courses=number_of_courses
            self.affiliates=affiliates
            self.blog=blog

            i=ineuron("suraj","full stack data science","20","ineuron.ai","big data")
    class job(ineuron):
        pass
    j=job("anuj","full stack analyst","21","ineuron.ai","big data")
    logging.info(j)
except Exception as e:
    logging.exception(e)

#multilevel inheritance:
try:
    class ineuron:
        def opportunities(self):
            logging.info("you will get one by one opportunities during course")
        def internship(self):
            logging.info("this program will provide you one year internship")
        def salary(self):
            logging.info("you will be paid according to your experience")
    class data_science(ineuron):
        def num_of_courses(self):
            logging.info("this will show no of courses in ineuron")
    class scope(data_science):
        pass
    s=scope()
    s.num_of_courses()
    s.opportunities()
    s.internship()
    s.salary()
except Exception as e :
    logging.exception(e)

try:
    class schooling :
        def primary_school(self):
            logging.info("this will show the strength of students studying in primary school")
        def secondary_school(self):
            logging.info("this will show the strength of students studying in secondary school")
    class university(schooling):
        def affiliate_college(self):
            logging.info("this will show you the no.of students studying in affiliate college")
        def university(self):
            logging.info("this will show the no. of students studying in university")
    class education(university):
        pass
    e=education()
    e.primary_school()
    e.secondary_school()
    e.affiliate_college()
    e.university()
except Exception as e:
    logging.exception(e)

#multiple inheritance:
try:
    class ineuron:
        def students_strength(self):
            logging.info("this will show you no. of students gets enrolled in ineuron")
    class data_science:
        def hired_strength(self):
            logging.info("this will show strenth of people get hired")
    class job(ineuron,data_science):
        pass
    j=job()
    j.students_strength()
    j.hired_strength()
except Exception as e:
    logging.exception(e)

try:
    class science:
        def PCM(self):
            logging.info("this will show you PCM stdents strength")
    class biology:
        def bio(self):
            logging.info("this will show the strength of bio students")
    class commerce(science,biology):
        pass
    c=commerce()
    c.PCM()
    c.bio()
except Exception as e:
    logging.exception(e)

#multilevel inheritance:
try:
    class operations1:
        def addition(self):
            a=int(input("enter any digit"))
            b=int(input("enter any digit"))
            return a+b

        def multiplication(self):
            a = int(input("enter any digit"))
            b = int(input("enter any digit"))
            return a*b

        def subtraction(self):
            a = int(input("enter any digit"))
            b = int(input("enter any digit"))
            return a-b

    class operations2(operations1):
        def odd(self):
            try:
                n=int(input("enter any number"))
                if n%2!=0:
                    logging.info(n)
            except Exception as e:
                logging.exception(e)

        def even(self):
            try:
                n=int(input("enter any number"))
                if n%2==0:
                    logging.info(n)
            except Exception as e:
                logging.exception(e)

    class operations3(operations2):
        pass
    op=operations3()
    op.addition()
    op.multiplication()
    op.subtraction()
    op.even()
    op.odd()
except Exception as e:
    logging.exception(e)

#abstraction:
try:
    class ineuron:
        def __init__(self):
            self.__course="data science"
            self.__no_of_courses="20"
            self.__salary=="5LPA"
            self.__internship="1 year"
        def course(self):
            logging.info(ineuron.__course)
        def no_of_course(self):
            logging.info(ineuron.__no_of_courses)
        def salary(self):
            logging.info(ineuron.__salary)
        def internship(self):
            logging.info(ineuron.__internship)
            i = ineuron()
            i.no_of_course()
            i.course()
            i.internship()
            i.salary()
except Exception as e:
    logging.exception(e)

#encapsulations:
try:
    class army:
        def __init__(self):
            self.airforce="kashmir"
        def airforce(self):
            logging.info(self.airforce)
            a=army()
            a.airforce="manali"
except Exception as e:
    logging.exception(e)





