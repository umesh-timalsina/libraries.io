#!/usr/bin/python2.7
'''
    A general python utility to search and download 
    open source repositories from the internet
'''

import requests
import json
import os
import sys
from git import Repo
import pymysql


API_KEY = 'b2742f98a811f86911e5777a0a9d7193'
def search_codebase():
    '''
            A search to the public APIs in libraries.io
    '''
    search_keystring = raw_input("Enter Keywords: ")
    search_language = raw_input("Enter Language: ")
    search_language = '&languages=' + search_language
    url = 'https://libraries.io/api/search?q=' + str(search_keystring) + '&api_key=' + API_KEY + search_language 
    try:
        response = requests.get(url)
        data = response.json()
    except:
        print 'Error-- Failed to connect'
        sys.exit(1)
    with open("opfile.json", 'w') as file:
        file.write(json.dumps(data))
    for i in range(0, len(data)):
        print "Name of the project: ", data[i]['name']
        print "Description: ", data[i]['description']
        print "Repository Url: ", data[i]['repository_url']
        print "\n"
    if len(data)<5:
        return data
    else:
        return data[0:5]
    

def download_repo(result):
    '''
            Clone and download the repos
    '''
    for i in range(0,len(result)):
        path = "./" + result[i]['name']
        if os.path.isdir(path):
            path = path + str('(i)')
        
        try:
            Repo.clone_from(result[i]['repository_url'], path)
            print "Cloned ", result[i]['name']
        except:
            print "Failed to clone the repository" , result[i]['name'] 
                




def connect_store(result):
    '''
            Insert the result into data-base table
    '''
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='toor', db='mysql')

    cur = conn.cursor()

    cur.execute("use final_store;")
    insert_statement = (
      "INSERT INTO records (name, description) "
        "VALUES (%s, %s)"
        )
    for i in range(0, len(result)):
        data = (result[i]['name'], result[i]['description'])
        cur.execute("Insert Into records(name, description) values(%s, %s)", data)

    print(cur.description)

    print()

    for row in cur:
        print(row)

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
   result=search_codebase()
   download_repo(result)
   connect_store(result)
