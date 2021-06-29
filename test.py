from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

database={}
url= "https://www.programmableweb.com/category/tools/api"
api_no=0
name = []
link = []
category = []
description = []
while True:
    
    response=requests.get(url)
    data=response.text
    soup=bs(data,"html.parser")

    api_name_list=soup.find_all("td",{"class":"views-field views-field-title"})
    api_category_list=soup.find_all("td",{"class":"views-field views-field-field-article-primary-category"})
    api_description_list=soup.find_all("td",{"class":"views-field views-field-field-api-description"})

    lst= list(zip(api_name_list,api_category_list,api_description_list))
 
    for (i,j,z) in lst:
        api_name=i.find("a").text
        api_link=i.find("a").get("href")
        api_category=j.find("a").text
        api_description=z.text

        name.append(api_name)
        link.append(api_link)
        category.append(api_category)
        description.append(api_description)

        # print(api_name,"\n",api_link,"\n",api_category,"\n",api_description,"\n-----")
        api_no+=1

    url_tag=soup.find("a",{"id":"pager_id_apis_all"})

    try:
        if url_tag.get("href"):
            url= "https://www.programmableweb.com"+ url_tag.get('href')
            print(url)
            #chỗ này mà e bị fail á thì url k được cập nhật nên nó sẽ chạy với url fail này miết mà k thoát khoải vòng lặp
        else:
            break
    except:
        # cập nhật lại url nếu bị fail
        temp = url.split('page=')
        url = temp[0]+'page=' + str(int(temp[1])+1)
        print(url)
    
    ### print 5 page and break
    '''
    if (int(url.split('page=')[1])==5):
        database = {'API Name':name,
        'API (absolute) URL':link,
        'API Category':category,
        'API Description':description
        }
        df = pd.DataFrame(database)
        df.to_csv('API Database.csv')
        break
    '''

database = {'API Name':name,
        'API (absolute) URL':link,
        'API Category':category,
        'API Description':description
        }
df = pd.DataFrame(database)
df.to_csv('API Database.csv')
