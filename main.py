OPENAI_API_KEY="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"
from search_website import search_websites_with_prompt
import analysis_website_layout
from script_search_website import search_websites

# _________ASYNK WORK_________
def main():

    #______________________FIND KEYWORD________________________
    # : FIND WEBSITE KEYWORD 



    #_____________________FIND LINKS____________________________
    # : FIND LINKS IN GOOGLE SERACH LINKS WEBSITE KEYWORD SEARCH

    with open("./key_word_for_serch_site.txt") as fp:

        key = fp.readline()
        key=key.strip()
        search_websites(key)


    #_____________________ANALYSIS SITE WITH CHAT GPT__________________________
    # : WE FEED PROMTS TO THE GPT CHAT
    # GET :
    # Url
    # Description 
    # KeyWords
    # ColorSCheme
    # WebsiteType


    #_____________________ANALYSIS SITE WITH BeautifulSoup__________________________
    # : GET METADATA SITE


if __name__ == "__main__":
    main() 