import requests

def get_random_wikipedia_page():
    # Endpoint for Wikipedia's random page
    random_url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

    # Making a GET request to fetch the random page URL
    response = requests.get(random_url)

    # Checking if the request was successful
    if response.status_code == 200:
        # Printing the URL of the random page
        print("URL of the random Wikipedia page:", response.url)

        # Returning the content of the page
        return response.text
    else:
        # Handling the case where the request failed
        return "Failed to retrieve a random Wikipedia page"

if __name__=="__main__":
    # Usage of the function
    page_content = get_random_wikipedia_page()
    print(page_content)  # Print the first 2000 characters of the page content
