import requests
import openai

def search_websites_with_prompt(query,API_KEY):
    # Set your OpenAI API key
    openai.api_key  = API_KEY

    # Set the search query and model name
    search_query = f'Find websites related to: "{query}"'
    model = "text-davinci-003"

    # Send the search prompt to the model
    response = openai.Completion.create(
        engine=model,
        prompt=search_query,
        n=5,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated websites from the response
    websites = [choice['text'].strip() for choice in response.choices]

    # Print the generated websites
    for index, website in enumerate(websites, start=1):
        print(f"Website {index}: {website}")

'''
    # Generate a completion using the ChatGPT API
    response = requests.post(
        "https://api.openai.com/v1/completions"
        "",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": model,
            "prompt": search_query,
        },
    )

    # Retrieve the response and print the generated completion
    if response.status_code == 200:
        data = response.json()
        completion = data["choices"][0]["text"].strip()
        print(f"Generated Completion: {completion}")
    else:
        print("Response is : ",response.text)
        print("Request failed with status code:", response.status_code)

'''
