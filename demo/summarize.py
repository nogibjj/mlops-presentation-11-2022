"""Build a Hugging Face Summarize Library"""

from transformers import pipeline
import wikipedia


def summarize(text):
    """Summarize text"""
    summarizer = pipeline("summarization", model="t5-small")
    result = summarizer(text, max_length=180)
    print("Summarization process complete!")
    print("=" * 80)
    return result[0]["summary_text"]


# search wikipedia pages
def search_wiki(search_term):
    """Search wikipedia pages"""

    search_results = wikipedia.search(search_term)
    return search_results


# grab text from a wikipedia page
def get_wiki_text(page_title):
    """Grab text from a wikipedia page"""

    page = wikipedia.page(page_title)
    return page.content
