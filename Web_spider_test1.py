import string  
import urllib2  
import re  
  
class Baidu_Spider:  
    def __init__(self,url):    
        self.myUrl = url  
        self.datas = []  
        print u'The program is going on...'  
    
    # To start "Rate my professor" website
    def baidu_tieba(self):  
        # Change the original website information into data 
        myPage = urllib2.urlopen(self.myUrl).read().decode("utf-8") 
        # Calculate the pages this website contains
        endPage = self.page_counter(myPage)  
        # To get the final data which is names of professor  
        self.save_data(self.myUrl,endPage)  
  
    # Calculate the pages this website contains
    def page_counter(self,myPage):  
        # To find the string "class=\"step\">{}</a>" to know how many pages do we have  
        page_list = []
        for i in range(2,1000):   
            if "class=\"step\">{}</a>".format(i) in  myPage:
                page_list.append(i)
                continue
        endPage = max(page_list)
        print u'Total pages: %d' % endPage
        return endPage  
  
   
  
  
    # To save the names of preofessor  
    def save_data(self,url,endPage):  
        # Add the name into list  
        self.get_data(url,endPage)  
        f = open("list_of_professor"+'.txt','w+')  
        f.writelines(self.datas)  
        f.close()  
        print u'The program is finish'  
        raw_input();  
  
    # Get the data from website  
    def get_data(self,url,endPage):  
        for i in range(1,endPage+1):  
            print u'Report: doing %d pages' % i  
            myPage = urllib2.urlopen(url).read()  
            url = url.replace(str((i-1)*20),str(i*20))            
            # Put the data into the deal_data2 list  
            self.deal_data2(myPage.decode('utf-8'))  
              
  
    # Get the data from website code. 
    def deal_data2(self,myPage):
        professor = []
        m = myPage.split("\n")
        for line in m:
            if "<span class=\"main\"" in line:
                professor = (line.lstrip("").lstrip("<span class=\"main\">").rstrip(" </span>\r"))
                self.datas.append(professor+'\t')
        self.datas.append('\n\n\n\n') 
        
            
        
                
                
        
        
        
    def deal_data(self,myPage):  
        myItems = re.findall('<span class="main">? </span>',myPage,re.S)  
        for item in myItems:  
            data = self.myTool.Replace_Char(item.replace("\n","").encode('gbk'))  
            self.datas.append(data+'\n')  
      
# The website "Rate my professor" with Rensselaer school.  
bdurl = 'https://www.ratemyprofessors.com/search.jsp?query=rpi&queryoption=HEADER&stateselect=&country=&dept=&queryBy=&facetSearch=&schoolName=&offset=0&max=20'    
mySpider = Baidu_Spider(bdurl)  
mySpider.baidu_tieba()