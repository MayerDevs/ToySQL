#Attributes Manager
from bintrees import FastRBTree
import uuid

class kernel_attributes:
    def __init__(self,name,attributes):
        self.name=name
        self.attributes=attributes
        self.attributesT=FastRBTree()
    def create_table(self):
        for i in range(len(self.attributes)):
            self.attributesT[self.attributes[i].name]=self.attributes[i]
    def insert_table(self,dat):
        id=str(uuid.uuid4())
        for i in range(len(self.attributes)):
           obj=self.attributesT[self.attributes[i].name]      
           obj.insert(dat[i],id)
           
    def select_table(self,dat,columns):
        id=self.selection(dat)
        query=[]
        for j in range(len(id)):
             for i in range(len(columns)):
                obj=self.attributesT[columns[i]]
                d=obj.select_uuid(id[j])
                query.append(d)
        return query
        
    def selection(self,dat):
        if len(dat)>0:
            obj=self.attributesT[dat[0]]
            id_f=obj.select_name(dat[1])
            for i in range (0,len(dat),2):
                obj=self.attributesT[dat[i]]
                id_s=obj.select_name(dat[i+1])
                intersection = list(set(id_f).intersection(id_s))
                if len(intersection)>0:
                   id_f=id_s
                else: 
                    print("Data doesn't founded")
                    break
            return intersection
        else:
            return 0
    
            