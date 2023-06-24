
from bs4 import BeautifulSoup

with open('/Users/Ahmed/PythonProjects/Learning Projects/Bs4/home.html', 'r') as html_file:
    
    # Reading the content of the file (or a HTML page):
    content = html_file.read()
    #print(content)

    # Passing the page through BeautifulSoup:
    soup = BeautifulSoup(content, 'lxml')
    #print(soup.prettify())

    #Finding a specific tag (It stops the execution after first find):
    '''
    tag = soup.find('h5')
    print(tag)
    '''

    # Find a specific tag (from the whole page):
    '''
    tag = soup.find_all('h5')
    print(tag)
    '''

    # Grabbing a specific element out of the search:
    '''
    courses = soup.find_all('h5')
    for course in courses:
        print(course.text)
    '''

    # Grabbing all prices with courses' names:
    '''
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text

        course_price = course.a.text.split()[-1] # -1 means Grabbing the last element =

        print(f'{course_name} costs {course_price}')
    '''

    