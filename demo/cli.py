#!/usr/bin/env python

"""Build a CLI for the Hugging Face Summarize Library"""

import click
from summarize import summarize, search_wiki, get_wiki_text


@click.group()
def cli():
    """Summarize text from Wikipedia articles"""


@cli.command("summarize")
@click.argument("search_term")
def summarize_cli(search_term):
    """Summarize text from Wikipedia articles"""
    search_results = search_wiki(search_term)
    print("Search results:")
    print("=" * 80)
    for result in search_results:
        print(result)
    print("=" * 80)
    page_title = click.prompt("Enter the page title to summarize")
    text = get_wiki_text(page_title)
    summary = summarize(text)
    print("Summary:")
    print("=" * 80)
    print(summary)
    print("=" * 80)


if __name__ == "__main__":
    cli()
