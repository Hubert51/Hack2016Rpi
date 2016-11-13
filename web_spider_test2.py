"""
This program tries to use web-spride to find out all the course inforamtion in
Reansselaer. I use rpi catalog website to get the inforamtion.
"""

import string  
import urllib2  
import re  
  
class Course_Spider:  
    def __init__(self,url): 
        self.mainPage = url  # The main website of catalog.
    
        #These website pages contain whole courses . I need to change adress after finish one page since the website has anti-spride.
        self.myUrl = url+"content.php?catoid=15&catoid=15&navoid=367preview_course_nopop.php%3Fcatoid%3D15&filter%5Bitem_type%5D=3&filter%5Bonly_active%5D=1&filter%5B3%5D=1&filter%5Bcpage%5D={}#acalog_template_course_filter".format(i)   
        self.information = []                           # This list contains the descrption of the every course in one page  
        print u'The program is going on...'  
    
    def course_catalog(self):  
        # Change the URL into HTML 
        myPage = urllib2.urlopen(self.myUrl).read().decode("utf-8") 
        # I have known that the end page of catalog is 19 
        endPage = 19  
        # To get the final data which is description of course 
        self.save_data(self.myUrl,endPage)  

    # To save the description of course  
    def save_data(self,url,endPage):
        
        # Get the data from HTML  
        self.get_data(url,endPage)  
        f = open("list_of_des"+'.txt','a')  
        f.writelines(self.information)  
        f.writelines("\n\n\n")
        f.close()  
        print u'The program is finish'  
        raw_input(" ")
    
    # Get the data from website  
    def get_data(self,url,endPage): 
        
        # This funciton tries to get the data from HTML
        print u'Report: doing %d pages' % 1    # Since I need to aviod the anti-spride. I need to change the number of pages every time.
        myPage = urllib2.urlopen(self.myUrl).read()  
        self.deal_data2(myPage.decode('utf-8'))     # To call the funtion to deal the data       
  
    def deal_data2(self,myPage):
        """
        This function tries to get the data from the HTML
        """
        m = myPage.split("\n")  
        for i in range(len(m)): 
            if "preview_course_nopop.php?catoid=15&coid=" in m[i]:    # This is the second part of each course. 
                n = m[i].split(" ")
                course = n[2].lstrip("href=\"").rstrip("\"")
                self.mainPage += course                               # I add the first main part and second specific part of a course
                course_info = urllib2.urlopen(self.mainPage).read().decode('utf-8')
                course_des = course_info.split("\n")
                for line in course_des:
                    if "<p><h1>" in line:
                        # Try to remove all the meaningless characheristic 
                        line = line.replace("<p><h1>",'').strip()
                        line = line.replace("</h1><p><hr>",'').strip()                                                  
                        line = line.replace("</h1><hr>",': ').strip() 
                        line = line.replace("</strong>",'').strip()  
                        line = line.replace("<strong>",'').strip()                          
                        line = line.replace("</p>",'').strip() 
                        line = line.replace("<br>",'').strip()
                        line = line.replace("<em>",'').strip()   
                        line = line.replace("</em>",'').strip()  
                        line = line.replace("<p>",'').strip()  
                        line = line.replace("<sup>",'').strip()  
                        line = line.replace("<span>",'').strip() 
                        line = line.replace("</span>",'').strip()  
                        line = line.replace("</sup>",'').strip() 
                        line = line.replace("&#160;",'').strip()                         
                        line = line.replace("&#8216;",'').strip() 
                        line = line.replace("&#8217;",'').strip()                         
                        line = line.replace("&#8230;",'').strip() 
                        line = line.replace("&#8220;",'').strip()
                        line = line.replace("&#8221;",'').strip()                                                 
                        self.information.append(line.encode("utf-8"))
                        self.information.append("\n")  
                        print self.information[-2]   # To show the program is running correctly.

      
# The website catalog of course in Rensselaer school.  
bdurl = "http://catalog.rpi.edu/"
raw_input
mySpider = Course_Spider(bdurl)  
mySpider.course_catalog()