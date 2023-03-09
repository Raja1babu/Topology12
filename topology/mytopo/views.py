from tkinter import Y
from turtle import circle
from urllib import response
from django.shortcuts import redirect, render
from numpy import size
from pyvis.network import Network as net
import pandas as pd
import random

from IPython.display import display
# Create your views here.

def home(request):
    return render (request,'index.html')


def generate_edge():
  s = random.randint(1,10)
  d = random.randint(1,10)
  return (s,d)
 
def generate_size_node():
  v = random.randint(5,20)
  return v
 
def generate_color():
  random_number = random.randint(0,16777215)
  hex_number = str(hex(random_number))
  hex_number ='#'+ hex_number[2:]
  return hex_number
 
def Topology(request):
  g_complete =net(height='600px',width='50%',
                bgcolor='white',font_color="red",notebook=True,
                heading="A Complete Networkx Graph",directed=True)
  
  colors=[]
  for i in range(1,11):  
    c = generate_color()
    colors.append(c)
    while(c in colors):
        c = generate_color()
    colors.append(c)
  
    val = generate_size_node()
    b = random.randint(3,5)
  
    g_complete.add_node(i,label=str(i),color=c,value=val,
                        title="Hello! I am Node "+str(i),borderWidth=b)
  
  i=0
  chosen_set = []
  while(i!=20):
    eg = generate_edge()
    if(eg[0]!=eg[1] and not (eg in chosen_set)):
        chosen_set.append(eg)
        g_complete.add_edge(eg[0],eg[1])
        i+=1
  
  g_complete.show_buttons(['physics'])
  #.show('A_Complete_Networkx_Graph.html')
  #g_complete.show('Topology.html')
  g_complete.save_graph('Topology.html')
  #display(HTML('A_Complete_Networkx_Graph.html'))  
  return redirect ('showTopology')
  
  

 
def showTopology(request):
  
  return render (request ,'Topology.html') 

def Topologyy(request):
    nvar = net(height='600px', width='50%',
               bgcolor='white', font_color="red", notebook=True,
               heading="Practise Graph", directed=False)
    df = read()

    nvar.add_node('Name',label='Name',shape='circle')
    for row in df.itertuples():
      nvar.add_node(row.name,label=row.name,shape='circle')
      nvar.add_edge(row.name,'Name')
      nvar.add_node(row.salary, label=f'salary {row.salary}')
      nvar.add_edge(row.salary, row.name)
      nvar.add_node(row.branch, label=f'branch{row.branch}',x=2000,Y=2000, size=2)
      nvar.add_edge(row.branch,row.salary)
      nvar.add_node(row.age,label=f'age{row.age}')
      nvar.add_edge(row.age, row.branch)

    nvar.show('edge.html')
    nvar.save_graph('Topologyy.html')

    return render (request ,'Topologyy.html') 

def read():
  df = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Topology Project\Topology12\topo.csv",skiprows=1,names=['id','name','salary','branch','age'])
  print(df)
  return df

def empRead():
  df1 = pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Topology Project\Topology12\sample_emp.xlsx", names=['Id','Gender','Birth_Date','Jobcat','Salary','JobTime','PrevExp','Minority'],engine='openpyxl')
  print(df1)
  return df1

def NewTopology(request):
  net1 =net(height='700px', width='100%',
              bgcolor='white', font_color="red", notebook=True,
              heading="Employee Graph", directed=False)
  #empRead()
  df1 = empRead()
  net1.add_node('Employee', label='Employee', shape='circle')

  for jobTime in df1.JobTime.unique():
    net1.add_node(f'{jobTime}time', label=f'{jobTime}time', shape='circle')
    net1.add_edge(f'{jobTime}time', 'Employee')
    net1.add_node(f'{jobTime}Male', label='Male', shape='circle')
    net1.add_node(f'{jobTime}Female', label='Female', shape='circle')
    net1.add_edge(f'{jobTime}time', f'{jobTime}Male')
    net1.add_edge(f'{jobTime}time', f'{jobTime}Female')
    for row in (df1[(df1['Gender']=='m') & (df1['JobTime']==jobTime)]).itertuples():
      net1.add_node(f'{row.Id}mid', label=f'{row.Id}id', shape='circle')
      net1.add_edge(f'{row.Id}mid',f'{jobTime}Male')
    for row in (df1[(df1['Gender']=='f') & (df1['JobTime']==jobTime)]).itertuples():
      net1.add_node(f'{row.Id}fid', label=f'{row.Id}id', shape='circle')
      net1.add_edge(f'{row.Id}fid',f'{jobTime}Female')



  net1.show('NewTopology.html')  
  net1.save_graph('NewTopology.html')  
  return render(request,'NewTopology.html')




def StationRead():
  df2 = pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Topology Project\Topology12\Station.xlsx")
  print(df2)
  return df2

def Station(request):
  net2 =net(height='700px', width='100%',
              bgcolor='white', font_color="red", notebook=True,
              heading="Staton Graph", directed=False)
  #StationRead()
  df2 =StationRead()  

  net2.add_node('Railway', label='Railway', shape='circle', color='blue')  

  for region in df2.Region.unique():
    net2.add_node(f'{region}', label=f'{region}', shape='circle')
    net2.add_edge(f'{region}','Railway')


    for row in  (df2[df2['Region']==region]).itertuples():
      net2.add_node(f'{row.Circle}' , label=f'{row.Circle}', shape='circle' )
      net2.add_edge(f'{row.Circle}', f'{region}')
      net2.add_node(f'{row.StationName}', label=f'{row.StationName}', shape='circle')
      net2.add_edge(f'{row.StationName}', f'{row.Circle}')

  station = net2.generate_html()
  return render (request , 'Station.html',{'station':station}) 


def CompanyEmp_Read():
  df3= pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Topology Project\Topology\Company_Emp.xlsx")
  print(df3)
  return df3

def Company_Emp(request):
  net3= net(height='700px', width='100%',
              bgcolor='white', font_color="red", notebook=True,
              heading="Company Graph", directed=False)
  #CompanyEmp_Read()
  df3 = CompanyEmp_Read() 

  net3.add_node('Company', label='Company', shape='circle', color='blue')

  for country in df3.Country.unique():
    net3.add_node(f'{country} Country', label=f'{country} Country', shape='circle')
    net3.add_edge(f'{country} Country', 'Company')

    for row in (df3[df3['Country']==country]).itertuples():
      net3.add_node(f'{row.City} City', label=f'{row.City} City',shape='circle')
      net3.add_edge(f'{row.City} City', f'{country} Country')
      net3.add_node(f'{row.Company_name} Company', label=f'{row.Company_name} Company', shape='circle')
      net3.add_edge(f'{row.Company_name} Company', f'{row.City} City')
      net3.add_node(f'{row.First_name} Name', label=f'{row.First_name} Name', shape='circle')
      net3.add_edge(f'{row.First_name} Name',f'{row.Company_name} Company' )
      net3.add_node(f'{row.Phone} Phone', label=f'{row.Phone}', shape='circle')
      net3.add_edge(f'{row.Phone} Phone',f'{row.First_name} Name' )

    

  company = net3.generate_html()
  return render (request, 'Company.html', {'company': company})

            

  


