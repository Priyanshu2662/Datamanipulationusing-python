Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>
import pandas as pd
import matplotlib.pyplot as pl
import numpy as np
print("welcome:))")
k=pd.read_csv("exams.csv")
print(k)

def Main_menu():
    print("1. Arithmetic data operations")
    print("2. Data visualizattion method")
    print("3. Data manipulation")
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
 
def arithmetic_data_operation():
    print("1.total of math score")
    print("2.total of writing score")
    print("3.total of reading score")
    print("4.maximum math score")
    print("5.mode of reading score")
    print("6.median of math score")
    print("7.mean of wrinting score")
    print("8.min of math score")
    print("9.min of reading score")
    print("10.min of writing score")
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")

def data_visualisation_operation():
    print("1.comparision between math score and writing score")
    print("2.comparision between writing score and reading score")
    print("3.parental level of education")
    print("4.male and female completed the test preaparetion course ")
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")

def data_manipulation():
    print("1.delete the race/ethnicity")
    print("2.add a new row piyush")
    print("3.add a new column")
    print("4.delete a column")
    print("5.add a new row")
    print("6.delete a row")
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")


Main_menu()
while True:
    ch=int(input("Enter the choice"))
    if ch==1:
        arithmetic_data_operation()
        r=int(input("Enter the choice"))
        if r==1:
            t=k["math score"].sum()
            print(t)
        elif r==2:
            t=k["writing score"].sum()
            print(t)
        elif r==3:
            t=k["reading score"].sum()
            print(t)
        elif r==4:
            t=k["math score"].max()
            print(t)
        elif r==5:
            t=k["reading score"].mode()
            print(t)
        elif r==6:
            t=k["math score"].median()
            print(t)
        elif r==7:
            t=k["writing score"].mean()
            print(t)
        elif r==8:
            t=k["math score"].min()
            print(t)
        elif r==9:
            t=k["reading score"].min()
            print(t)
        elif r==10:
            t=k["writing score"].min()
            print(t)
       
        else:
            print("invalid choice")
            print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")

    elif ch==2:
        data_visualisation_operation()
        p=int(input("Enter the choice"))
        if p==1:
            s=k["math score"]
            e=k["writing score"]
            pl.hist([s,e],bins=20,cumulative=False)
            pl.show()
            print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")

        elif p==2:
            s=k["writing score"]
            e=k["reading score"]
            pl.hist([s,e],bins=20,cumulative=False)
            pl.show()
            print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")

        elif p==3:
            p=[]
            c=[]
            p.append("high school")
            c.append(k["parental level of education"][k["parental level of education"]=="high school"].count())

            p.append("some high school")
            c.append(k["parental level of education"][k["parental level of education"]=="some high school"].count())

            p.append("some college")
            c.append(k["parental level of education"][k["parental level of education"]=="some college"].count())

            p.append("bachelor's degree")
            c.append(k["parental level of education"][k["parental level of education"]=="bachelor's degree"].count())

            p.append("associate's degree")
            c.append(k["parental level of education"][k["parental level of education"]=="associate's degree"].count())
            pl.hist([p,c],orientation='horizontal',bins=20,cumulative=False)
            pl.show()
            print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
        
        elif p==4:
            d={}
            new_df=k.copy()
            new_df.rename(columns={'gender':'g','race/ethnicity':'r', 'parental level of education':'pe', \
                                   'lunch':'l','test preparation course':'tp','math score':'ms',\
                                   'reading score':'rs','writing score':'ws'}, inplace=True)
            completed=[]
            notcompleted=[]
            completed.append(new_df[(new_df["g"]=="male") & (new_df["tp"]=="completed")].count()[0])
            completed.append(new_df[(new_df["g"]=="female") & (new_df["tp"]=="completed")].count()[0])
            notcompleted.append(new_df[(new_df["g"]=="male") & (new_df["tp"]=="none")].count()[0])
            notcompleted.append(new_df[(new_df["g"]=="female") & (new_df["tp"]=="none")].count()[0])
            print(completed,notcompleted)
            X=np.arange(2)
            pl.bar(['Male','Female'],completed,width=0.15, label='Completed')
            pl.bar(X+0.15,notcompleted,width=0.15, label='Not Completed')
            pl.legend(loc='upper left')
            pl.show()
            print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
            
    elif ch==3:
        data_manipulation()
        datama=int(input("Enter the choice"))
        if datama==1:
            k1=pd.read_csv('exams.csv')
            k1.drop(['race/ethnicity'],axis=1,inplace=True)
            print(k1)
            print('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')

        elif datama==2:
            k2=pd.read_csv("exams.csv")
            k2.loc[len(k2.index)]=["male","group C","high school","standard","not completed",45,78,23,'piyush']
            print(k2)
            print('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')

        elif datama==3:
            k3=pd.read_csv('exams.csv')
            k3['Average'] = k3.iloc[:,5:9].mean(axis=1,numeric_only=True)
            print(k3)
            print('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')

        elif datama==4:
            k4=pd.read_csv('exams.csv')
            k4['sum'] = k4.iloc[:,5:9].sum(axis=1,numeric_only=True)
            print(k4)
            print('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')
            

        elif datama==5:
            k5=pd.read_csv('exams.csv')
            k5['median'] = k5.iloc[:,5:9].median(axis=1,numeric_only=True)
            print(k5)
            print('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')

        elif datama==6:
            k6=pd.read_csv('exams.csv')
            k6.drop(14 ,axis=0,inplace = True)
            print(k6)
            print('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')

        elif datama==7:
            k7=pd.read_csv('exams.csv')
            k7['listning score'] =[65,98,32,24,14,78,59,54,78,98,47,16,35,21,73,89,17,45,28,94,24,21,68,59,14,41,28,49,17]
            print(k7)
            print('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')

        elif datama==8:
            k8=pd.read_csv('exams.csv')
            k8.drop([4,18],axis=0,inplace = True)
            print(k8)
            print('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')

        elif datama==9:
            k9=pd.read_csv('exams.csv')
            k9.drop('writing score',axis=1,inplace = True)
            print(k9)
            print('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')

        else:
            print('ivalid choice')
            print('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x')
