import ast
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def main(subject):

  ROOT = 'https://www.classcentral.com'
  URL = 'https://www.classcentral.com/subject/cs'

  page = requests.get('https://www.classcentral.com/subject/' + subject)

  soup = BeautifulSoup(page.content, 'html.parser')

  listing = soup.find("section", {"class": "listing-table"})

  courses = soup.findAll("a", {"class": "color-charcoal block line-tight course-name"})
  courses = courses[:8]
  coursedict = {}


  for course in courses:
    link = course.get('href')
    lpage = requests.get(ROOT + link)
    lsoup = BeautifulSoup(lpage.content, 'html.parser')
    course_link = lsoup.find('a', {'class': 'btn-green btn-large padding-horz-xxlarge'}).get('href')
    
    info = ast.literal_eval(course.get('data-track-props'))
    course_type = info['type']
    course_meta = info['clickMetadata']
    course_institution = course_meta['institution']
    course_name = course_meta['course']
    course_provider = course_meta['provider']

    coursedict[course_name] = [course_institution, course_provider, course_link]

  return coursedict
    

def writeHTML(subject):

  diction = (main(subject))
  df = pd.DataFrame(data=diction)
  #df = df.fillna(' ').T
  df = df.transpose()
  return df.to_html()

if __name__ == '__main__':
  main('cs')

