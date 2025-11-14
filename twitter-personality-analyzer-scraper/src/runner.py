thonimport json
import os
from extractors.twitter_parser import parse_tweets
from outputs.exporters import export_to_markdown
from config.settings import load_settings

def main():
    # Load configuration settings
    settings = load_settings()

    # Example username for analysis
    username = settings['username']
    
    # Step 1: Fetch and parse tweets (from an API or database)
    tweets = parse_tweets(username)
    
    # Step 2: Analyze the tweets to derive personality insights
    analysis_result = analyze_tweets(tweets)
    
    # Step 3: Export the results to a markdown file
    export_to_markdown(analysis_result, f"{username}_analysis.md")

def analyze_tweets(tweets):
    # Placeholder for real analysis logic
    return {
        "username": "@yaminirangan",
        "result": [{
            "format": "markdown",
            "response": "**This Twitter account exudes a dynamic blend of leadership, innovation, and social consciousness...**",
            "heading": "Personality Analysis For @yaminirangan"
        }],
        "htmlFile": "https://api.apify.com/v2/key-value-stores/null/records/twitter-personal-analysis-2025-06-06-09-00-12.html",
        "pdfFile": "https://api.apify.com/v2/key-value-stores/null/records/twitter-personal-analysis-2025-06-06-09-00-12.pdf",
        "markdownFile": "https://api.apify.com/v2/key-value-stores/null/records/twitter-personal-analysis-2025-06-06-09-00-12.md"
    }

if __name__ == "__main__":
    main()