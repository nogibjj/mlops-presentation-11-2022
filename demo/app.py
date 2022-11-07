"""Build a Gradio app that summarizes text from Wikipedia articles"""

import gradio as gr
from summarize import summarize, search_wiki, get_wiki_text


def summarize_gradio(search_term):
    """Summarize text from Wikipedia articles"""
    search_results = search_wiki(search_term)
    page_title = search_results[0]
    text = get_wiki_text(page_title)
    summary = summarize(text)
    return summary


iface = gr.Interface(
    fn=summarize_gradio,
    inputs="text",
    outputs="text",
    title="Hugging Face Summarize",
    description="Summarize text from Wikipedia articles",
    allow_flagging=False,
)

iface.launch()
