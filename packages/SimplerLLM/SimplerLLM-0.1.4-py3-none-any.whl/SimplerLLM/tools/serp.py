from duckduckgo_search import DDGS, AsyncDDGS
from dotenv import load_dotenv
from urllib.parse import urlparse
from pydantic import BaseModel, HttpUrl
from typing import Optional, List

class SearchResult(BaseModel):
    URL: HttpUrl
    Domain: Optional[str] = None
    Title: Optional[str] = None
    Description: Optional[str] = None


def get_domain_from_url(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

# Load environment variables
load_dotenv()



async def search_with_duck_duck_go_async(query, max_results=50):
    """
    Perform an asynchronous search using the DuckDuckGo search engine.

    Args:
    query (str): The search query string.
    max_results (int, optional): The maximum number of results to return. Defaults to 50.

    Returns:
    str: A JSON string containing the search results, each result being a dictionary with URL, Title, and Description.
    """
    async with AsyncDDGS() as ddgs:
        results = []
        async for r in ddgs.text(query, max_results=max_results):
            results.append(r)
        result_data = []
        for result in results:
            # Ensure all keys exist to avoid key errors
            url = result.get("href", None)
            title = result.get("title", None)
            description = result.get("body", None)
            if url:
                domain = get_domain_from_url(url)
                result_data.append(SearchResult(URL=url, Domain=domain, Title=title, Description=description))
            else:
                result_data.append(SearchResult(URL=url, Title=title, Description=description))
        
        return result_data


def search_with_duck_duck_go(query: str, max_results: int = 10) -> List[SearchResult]:
    """
    Perform a synchronous search using the DuckDuckGo search engine.

    Args:
        query (str): The search query string.
        max_results (int, optional): The maximum number of results to return. Defaults to 50.

    Returns:
        List[SearchResult]: A list of SearchResult objects, each containing URL, Title, and Description from the search results.
    """
    with DDGS() as ddgs:
        results = [r for r in ddgs.text(query, max_results=max_results)]
        result_data = []
        for result in results:
            url = result.get("href", None)
            title = result.get("title", None)
            description = result.get("body", None)
            if url:
                domain = get_domain_from_url(url)
                result_data.append(SearchResult(URL=url, Domain=domain, Title=title, Description=description))
            else:
                result_data.append(SearchResult(URL=url, Title=title, Description=description))
        
        return result_data


