OPENAI_API_KEY="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"
from search_website import search_websites_with_prompt
import analysis_website_layout
from script_search_website import search_websites

def main():

    with open("./key_word_for_serch_site.txt") as fp:

        key = fp.readline()
        key=key.strip()
        search_websites(key)

'''
    search_query = "beautiful"
    search_websites_with_prompt(search_query,OPENAI_API_KEY)
'''


if __name__ == "__main__":
    main() 