import requests
from googlesearch import search
from bs4 import BeautifulSoup

'''
<script async src="https://cse.google.com/cse.js?cx=04f4d3e804cd44a96">
</script>
<div class="gcse-search"></div>
'''
api_key = 'AIzaSyCN6a3LjOvAXZUuRY2hJQmMvpxq6494-pA'  # Replace with your actual Google API key
cx = '04f4d3e804cd44a96'  # Replace with your actual Custom Search Engine ID


def search_websites(keyword):
    pass














'''
    search_query = f'intext:"meta name=keywords" {keyword}'
    num_results = 10

    try:
        # Perform the Google search
        search_results = search(search_query, num_results=num_results,  advanced = True )

        # Iterate through the search results and retrieve websites with matching meta keywords
        for result in search_results:
            try:
                # Get the HTML source code of the webpage
                response = requests.get(result)
                soup = BeautifulSoup(response.text, 'html.parser')

                # Find the meta keywords tag
                meta_keywords_tag = soup.find('meta', attrs={'name': 'keywords'})

                if meta_keywords_tag:
                    meta_keywords = meta_keywords_tag.get('content', '')
                    if keyword in meta_keywords:
                        print(result)

            except requests.exceptions.RequestException:
                continue

    except Exception as e:
        print(f"An error occurred: {e}")
'''
'''
    search_query = ''.join(keywords)
    api_key = 'AIzaSyCN6a3LjOvAXZUuRY2hJQmMvpxq6494-pA'  # Replace with your actual Google API key
    cx = '04f4d3e804cd44a96'  # Replace with your actual Custom Search Engine ID

    try:
        response = requests.get(
            f'https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={search_query}'
        )
        results = response.json()
        websites = results.get('items', [])

        for website in websites:
            print(website['link'])

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

'''
