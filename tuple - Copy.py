import logging
logging.basicConfig(filename='tuple.log', level=logging.DEBUG)



class stringtasks:
    def __init__(self , my_string):
        self.my_string = my_string

    def jumping_3(self):
        """this function will extract data from index one to index 300 with a jump of 3"""
        try:
            val =self.my_string[0:300:3]
            logging.info(val)
        except Exception as e:
            logging.exception(e)

    def reverse_string(self):
        """this function reverse a string"""
        try:
            rev=self.my_string[1:1:-1]
            logging.info(rev)
        except Exception as e:
            logging.exception(e)

    def lower_case(self):
        """this function converse entire string into lower case"""
        try:
            val=my_string.upper()
            my_string=my_string.split()
            logging.info(my_string)
        except Exception as e:
            logging.info(e)

    def upper_case(self):
        """this function covert whole string into lower case"""
        try:
            val=my_string.lower()
            logging.info(val)
        except Exception as e:
            logging.info(e)

    def capitalize_str(self):
        "this function capitalize whole string"
        try:
            val=my_string.capitalize()
            logging.info(val)
        except Exception as e:
            logging.info(e)

    def expand_tab(self):
        s="xyzy/12345/tabc"
        try:
            val=s.expandtabs()
            logging.info(val)
        except Exception as e:
            logging.info(e)

    def strip(self):
        s='   sudhanshu   '
        try:
            val=s.strip()
            logging.info()
            return val
        except Exception as e:
            logging.exception(e)
        try:
            val=s.lstrip()
            logging.info()
            return val
        except Exception as e:
            logging.info(e)
        try:
            val=s.rstrip()
            logging.info()
            return val
        except Exception as e:
            logging.info(e)

    def replace_char(self):
        """this function replace string character by another character"""
        s="cold coffee"
        try:
             new_string=s.replace("coffee","chai")
             logging.info(new_string)
        except Exception as e:
            logging.exception (e)

    def string_centre_function(self):
        s="antima"
        try:
            val=s.center(10,'*')
            logging.info(val)
        except Exception as e:
            logging.exception(e)

            #my_string="this is my very First Python programming class and i am learNING python string and its function"
            s=stringtasks(my_string)
            s.jumping_3()
            s.reverse_string()
            s.lower_case()
            s.upper_case()
            s.capitalize_str()
            s.expand_tab()
            s.replace_char()
            s.string_centre_function()
            s.strip()

            logging.shutdown()

class tuple_tasks:
    def __init__(self,my_tuple):
        self.my_tuple=my_tuple

    def extract_all_tuple(self):
        l=[[1,2,3,4],[2,3,4,5,6],(3,4,5,6,7),([23,45,4,5]),
           {'k1':'sudh','k2':'ineuron','k3':'kumar',3:6,7:8},'ineuron','data science']
        "this function extracts all the values of tuple"
        try:
            l1=[]
            for i in l:
                if type(i)==tuple:
                    l1.append(i)
                    logging.info(l1)
        except Exception as e :
            logging.exception(e)


   # l = [[1, 2, 3, 4], [2, 3, 4, 5, 6], (3, 4, 5, 6, 7), ([23, 4, 5, 45]),{'k1': 'sudh', 'k2': 'ineuron', 'k3': 'kumar', 3: 6, 7: 8}, 'ineuron', 'data science']
            tu = tuple(l)
            tu.extract_all_tuple()

            logging.shutdown()


class listtasks:
    def __init__(self,my_list):
         self.my_list=my_list

    def extract_all_list(self):
        "this function extracts all the values of list"
        try:
            for i in l:
                if type(i) == list:
                    logging.info(i)
        except Exception as e:
            logging.exception(e)

    def extract_odd_values(self):
        "this function extracts all the odd values of list"
        try:
            for i in l:
                if type(i) == list:
                    for j in i:
                        if j % 2 == 0:
                            pass
                        else:
                            print(j)
        except Exception as e:
            logging.exception(e)

    def occurence_of_data_in_list():
        "this function extracts no of occurence of data in list"
        try:
            for i in l:
                if type(i) == list:
                    for j in i:
                        if type(j) == int:
                            logging.info(l.count(j))
        except Exception as e:
            logging.exception(e)

    def multiplication_of_num_value():
        try:
            for i in l:
                m = 1
                if type(i) == list:
                    if type(j) == int:
                        m = m * j
                        logging.info(m)
        except Exception as e:
            logging.exception(e)

    def unwrape_collection():
        l1 = []
        try:
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            logging.info(l1.append(j))
                            if type(i) == dict:
                                for k in i.items():
                                    if type(g) == int:
                                        logging.info(l1.append(g))
        except Exception as e:
            logging.exception(e)

             # my_list=[[1,2,3,4],[2,3,4,5,6],(3,4,5,6,7),([23,4,5,45]),{'k1':'sudh','k2':'ineuron','k3':'kumar'},'ineuron','datascience']
            l = listtasks(my_list)
            l.extract_all_list()
            l.extract_odd_values()
            l.multiplication_of_num_value()
            l.unwrape_collection()

            logging.shutdown()

class dicttask:
    def __init__(self,my_dict):
        self.my_dict = my_dict

    def extract_dict():
        """this function extract all the dictionary values"""
        #l = [[1, 2, 3, 4], [2, 3, 4, 5, 6], (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),{'k1': 'sudh', 'k2': 'ineuron', 'k3':'kumar',3:6,7:8},'ineuron','data science']
        try:
            for i in l:
                if type(i)==dict:
                    logging.info(i)
        except Exception as e:
            logging.exception(e)

    def no_of_keys():
        """this function counts no of keys in dict elements"""
        try:
            for i in l:
                if type(i)==dict:
                    logging.info(len(list(i.keys())))
        except Exception as e :
            logging.exception(e)

            d=dicttask(l)
            d.no_of_keys()
            d.extract_dict()

            logging.shutdown()











