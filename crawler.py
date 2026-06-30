#!/usr/bin/env python3
"""
OpenCode Scraper CLI - ssr2.scrape.center Crawler
Author: Antigravity AI
Description: A robust, concurrent Python crawler for scraping movie data from
             https://ssr2.scrape.center, which uses self-signed SSL certificates.
"""

import argparse
import csv
import json
import logging
import os
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urljoin

import requests
import urllib3
from bs4 import BeautifulSoup

# Disable SSL verification warnings as ssr2.scrape.center has self-signed cert issues
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configure Logging to use UTF-8 for console safety on different Windows terminal locales
# We wrap stdout in an encoder helper or write directly to avoid encoding crashes
class SafeStreamHandler(logging.StreamHandler):
    def emit(self, record):
        try:
            msg = self.format(record)
            stream = self.stream
            # Safely encode text using the stream's default encoding or replace characters
            stream.write(msg.encode(stream.encoding, errors='replace').decode(stream.encoding) + self.terminator)
            self.flush()
        except Exception:
            self.handleError(record)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[SafeStreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

BASE_URL = "https://ssr2.scrape.center"
DEFAULT_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_page(page, session):
    """
    Fetches the HTML content of a specific page.
    """
    url = f"{BASE_URL}/page/{page}"
    logger.info(f"Fetching page {page}: {url}")
    try:
        response = session.get(url, timeout=10, verify=False)
        response.raise_for_status()
        return page, response.text
    except requests.RequestException as e:
        logger.error(f"Error fetching page {page}: {e}")
        return page, None

def parse_movie_item(item):
    """
    Parses a single movie item element and extracts details.
    """
    # 1. Title
    title_el = item.select_one(".name h2")
    title = title_el.get_text(strip=True) if title_el else "Unknown"

    # 2. Detail Link
    link_el = item.select_one(".name")
    detail_link = urljoin(BASE_URL, link_el["href"]) if link_el and link_el.has_attr("href") else None

    # 3. Cover Image
    cover_el = item.select_one(".cover")
    cover_url = cover_el["src"] if cover_el and cover_el.has_attr("src") else None

    # 4. Categories
    categories = [cat.get_text(strip=True) for cat in item.select(".categories .category span")]

    # 5. Info blocks (Region, Duration, Release Date)
    info_elements = item.select(".info")
    regions = []
    duration = None
    release_date = None

    for info in info_elements:
        text = info.get_text(strip=True)
        if "/" in text:
            # Typically "Region / Duration" e.g., "中国内地、中国香港 / 171 分钟"
            parts = [p.strip() for p in text.split("/")]
            if len(parts) >= 1:
                regions = [r.strip() for r in parts[0].split("、")]
            if len(parts) >= 2:
                duration = parts[1]
        elif "上映" in text:
            # Typically "YYYY-MM-DD 上映"
            release_date = text.replace("上映", "").strip()

    # 6. Score
    score_el = item.select_one(".score")
    score = float(score_el.get_text(strip=True)) if score_el else None

    return {
        "title": title,
        "detail_link": detail_link,
        "cover_url": cover_url,
        "categories": categories,
        "regions": regions,
        "duration": duration,
        "release_date": release_date,
        "score": score
    }

def parse_page_html(html):
    """
    Parses the raw HTML of a page and extracts all movies.
    """
    if not html:
        return []
    
    soup = BeautifulSoup(html, "html.parser")
    movie_elements = soup.select(".el-card.item")
    movies = []
    
    for element in movie_elements:
        try:
            movie_data = parse_movie_item(element)
            movies.append(movie_data)
        except Exception as e:
            logger.error(f"Error parsing movie element: {e}")
            
    return movies

def crawl(start_page=1, end_page=10, max_workers=5):
    """
    Crawls movies concurrently across pages.
    """
    all_movies = []
    pages_to_crawl = list(range(start_page, end_page + 1))
    
    # We use a session to reuse TCP connections
    session = requests.Session()
    session.headers.update(DEFAULT_HEADERS)
    
    logger.info(f"Starting crawl from page {start_page} to {end_page} with {max_workers} threads...")
    
    # Thread pool execution
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_page = {executor.submit(fetch_page, page, session): page for page in pages_to_crawl}
        
        # Collect and parse results as they complete
        results = {}
        for future in as_completed(future_to_page):
            page = future_to_page[future]
            try:
                page_num, html = future.result()
                results[page_num] = html
            except Exception as e:
                logger.error(f"Page {page} generated an exception: {e}")
                
        # Parse pages in correct sequential order
        for page in sorted(results.keys()):
            html = results[page]
            movies = parse_page_html(html)
            logger.info(f"Page {page}: Scraped {len(movies)} movies.")
            all_movies.extend(movies)
            
    logger.info(f"Crawl finished. Total movies scraped: {len(all_movies)}")
    return all_movies

def save_data(data, output_path, output_format):
    """
    Saves the scraped data to JSON, CSV, or Markdown Table.
    """
    if not data:
        logger.warning("No data to save.")
        return

    if output_format == "json":
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        logger.info(f"Successfully saved {len(data)} items to JSON file: {output_path}")
        
    elif output_format == "csv":
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            # Write Header
            writer.writerow(["Title", "Score", "Release Date", "Duration", "Regions", "Categories", "Detail Link", "Cover URL"])
            # Write Rows
            for item in data:
                writer.writerow([
                    item["title"],
                    item["score"],
                    item["release_date"],
                    item["duration"],
                    ", ".join(item["regions"]),
                    ", ".join(item["categories"]),
                    item["detail_link"],
                    item["cover_url"]
                ])
        logger.info(f"Successfully saved {len(data)} items to CSV file: {output_path}")

    elif output_format == "markdown":
        md_lines = [
            "# Scraped Movie Data Table\n",
            f"A complete list of {len(data)} movies scraped from https://ssr2.scrape.center.\n",
            "| Cover | Title | Categories | Regions | Duration | Release Date | Score | Link |",
            "| :---: | :--- | :--- | :--- | :--- | :--- | :---: | :---: |"
        ]
        for item in data:
            cover_url = item.get("cover_url", "")
            cover = f'<img src="{cover_url}" width="60" alt="{item["title"]}">' if cover_url else "N/A"
            title = f'**{item.get("title", "Unknown")}**'
            categories = ", ".join(item.get("categories", []))
            regions = ", ".join(item.get("regions", []))
            duration = item.get("duration", "N/A")
            release_date = item.get("release_date") if item.get("release_date") else "N/A"
            score = f'⭐ `{item.get("score", 0.0)}`'
            link = f'[Detail]({item.get("detail_link")})' if item.get("detail_link") else "N/A"
            md_lines.append(f"| {cover} | {title} | {categories} | {regions} | {duration} | {release_date} | {score} | {link} |")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(md_lines))
        logger.info(f"Successfully saved {len(data)} items to Markdown Table file: {output_path}")

def download_single_cover(item, session, output_dir):
    """
    Downloads the cover image for a single movie item.
    """
    cover_url = item.get("cover_url")
    if not cover_url:
        return
    
    # Sanitize title for filename
    safe_title = re.sub(r'[\\/*?:"<>|]', "_", item["title"])
    filename = f"{safe_title}.jpg"
    filepath = os.path.join(output_dir, filename)
    
    if os.path.exists(filepath):
        return
        
    try:
        response = session.get(cover_url, timeout=15, verify=False)
        response.raise_for_status()
        with open(filepath, "wb") as f:
            f.write(response.content)
        logger.info(f"Downloaded cover: {filename}")
    except Exception as e:
        logger.error(f"Failed to download cover for {item['title']}: {e}")

def download_covers(movies_data, output_dir="covers", max_workers=5):
    """
    Downloads cover images for all movies concurrently.
    """
    if not movies_data:
        logger.warning("No movie data to download covers for.")
        return
        
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        logger.info(f"Created directory for covers: {output_dir}")
        
    session = requests.Session()
    session.headers.update(DEFAULT_HEADERS)
    
    logger.info(f"Starting cover downloads to {output_dir} using {max_workers} threads...")
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(download_single_cover, item, session, output_dir)
            for item in movies_data
        ]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logger.error(f"Error in cover download thread: {e}")
                
    logger.info("Cover download process completed.")

def main():
    parser = argparse.ArgumentParser(description="Concurrent Web Crawler for ssr2.scrape.center")
    parser.add_argument("--start", type=int, default=1, help="Start page (default: 1)")
    parser.add_argument("--end", type=int, default=10, help="End page (default: 10)")
    parser.add_argument("--workers", type=int, default=5, help="Number of concurrent scraper threads (default: 5)")
    parser.add_argument("--format", choices=["json", "csv", "markdown"], default="json", help="Output format (default: json)")
    parser.add_argument("--output", type=str, default="movies.json", help="Output file path (default: movies.json)")
    parser.add_argument("--download-covers", action="store_true", help="Download movie cover images")
    parser.add_argument("--cover-dir", type=str, default="covers", help="Directory to save cover images (default: covers)")
    
    args = parser.parse_args()
    
    # Adjust output extension if default output is used but format is changed
    output_file = args.output
    if output_file == "movies.json":
        if args.format == "csv":
            output_file = "movies.csv"
        elif args.format == "markdown":
            output_file = "movies.md"

    # Start crawling
    movies_data = crawl(start_page=args.start, end_page=args.end, max_workers=args.workers)
    
    # Save output
    save_data(movies_data, output_file, args.format)
    
    # Download covers if requested
    if args.download_covers:
        download_covers(movies_data, output_dir=args.cover_dir, max_workers=args.workers)

if __name__ == "__main__":
    main()
