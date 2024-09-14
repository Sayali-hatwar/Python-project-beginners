from googlesearch import search
import time
import streamlit as st

while True:
    query = input('What do you want to search? (or exit the search?) ')
    
    if query =='exit':
        print('Thanks for using google search')
        break
    
    try:
        num_result = int(input('How many search result do you want?: '))
        
        print(f'Showing top search {num_result} for {query}')
        for index, result in enumerate(search(query,start=0, stop=num_result)):
            print(f'{index+1}. {result}')
            time.sleep(0.5)
    
    except Exception as e:
        print(f'An error occurred {e}')
        print('Please try your network connection again.')
        
        
print('\n')
    





    
    
    