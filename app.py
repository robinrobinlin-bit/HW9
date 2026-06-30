import json
import os
import re
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn

try:
    from google import genai
    from google.genai import types
    HAS_GEMINI = True
except ImportError:
    HAS_GEMINI = False

# Initialize Gemini Client if API key is present
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
client = None
if HAS_GEMINI and GEMINI_API_KEY:
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
    except Exception as e:
        print(f"Error initializing Gemini client: {e}")
        client = None

class GeminiResponse(BaseModel):
    reply: str
    recommended_titles: list[str]

app = FastAPI(title="Movie Scraper Chatbar App")

# Base directory paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MOVIES_JSON_PATH = os.path.join(BASE_DIR, "movies.json")
COVERS_DIR = os.path.join(BASE_DIR, "covers")
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Ensure static directory exists
if not os.path.exists(STATIC_DIR):
    os.makedirs(STATIC_DIR)

# Mount static files
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Serve covers statically
@app.get("/covers/{filename}")
async def get_cover(filename: str):
    file_path = os.path.join(COVERS_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return HTMLResponse(status_code=404, content="Image not found")

class ChatQuery(BaseModel):
    message: str

def load_movies():
    if not os.path.exists(MOVIES_JSON_PATH):
        return []
    with open(MOVIES_JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_chat_response_local(query: str, movies_data: list):
    query_lower = query.lower()
    
    # Extract number limit if present (e.g., "top 100", "top5", "前100", "100 ranking", "排名第5")
    limit = 5  # default limit
    num_match = re.search(r'(?:top|前|ranking|rank|排名|前\s*|top\s*)\s*(\d+)', query_lower)
    if not num_match:
        num_match = re.search(r'(\d+)\s*(?:ranking|rank|排名|前|top)', query_lower)
        
    if num_match:
        limit = int(num_match.group(1))
    elif "all" in query_lower or "全部" in query_lower or "100" in query_lower:
        limit = 100
        
    # Check for general top/ranking requests
    is_ranking_request = any(kw in query_lower for kw in ["top", "rank", "排名", "前", "最好", "最高"]) or num_match
    
    # Check for category matches
    detected_category = None
    categories_map = {
        "剧情": ["剧情", "drama", "故事"],
        "爱情": ["爱情", "romance", "love", "浪漫"],
        "动作": ["动作", "action", "武打", "打斗"],
        "犯罪": ["犯罪", "crime", "警匪"],
        "喜剧": ["喜剧", "comedy", "搞笑", "幽默"],
        "奇幻": ["奇幻", "fantasy", "魔幻"],
        "冒险": ["冒险", "adventure", "探险"],
        "动画": ["动画", "animation", "anime", "卡通"],
        "战争": ["战争", "war", "军旅"],
        "科幻": ["科幻", "sci-fi", "science fiction", "太空"],
        "悬疑": ["悬疑", "mystery", "烧脑"],
        "惊悚": ["惊悚", "thriller", "恐怖"],
        "纪录片": ["纪录", "doc", "documentary"],
        "传记": ["传记", "biography"],
        "音乐": ["音乐", "music", "musical", "歌舞"],
        "家庭": ["家庭", "family"],
        "武侠": ["武侠", "wuxia", "martial arts"],
        "古装": ["古装", "costume", "historical"]
    }
    
    for cat, keywords in categories_map.items():
        if any(kw in query_lower for kw in keywords):
            detected_category = cat
            break
            
    # Process queries
    # 1. Category Top N
    if detected_category and is_ranking_request:
        filtered = [m for m in movies_data if detected_category in m.get("categories", [])]
        filtered_sorted = sorted(filtered, key=lambda x: x.get("score", 0.0), reverse=True)[:limit]
        reply = f"Here are the top {len(filtered_sorted)} ranking movies under the **{detected_category}** category:"
        return reply, filtered_sorted
        
    # 2. General Category Filter
    elif detected_category:
        filtered = [m for m in movies_data if detected_category in m.get("categories", [])]
        filtered_sorted = sorted(filtered, key=lambda x: x.get("score", 0.0), reverse=True)[:limit]
        reply = f"I found some great **{detected_category}** movies for you. Here are the top {len(filtered_sorted)}:"
        return reply, filtered_sorted
        
    # 3. Overall Top N
    elif is_ranking_request:
        top_n = sorted(movies_data, key=lambda x: x.get("score", 0.0), reverse=True)[:limit]
        reply = f"Here are the top {len(top_n)} highest-ranking movies of all time in our catalog:"
        return reply, top_n
        
    # 4. Search by title
    else:
        matches = []
        for m in movies_data:
            m_title = m.get("title", "").lower()
            if query_lower in m_title:
                matches.append(m)
            else:
                words = [w for w in query_lower.split() if len(w) > 1]
                if words and any(word in m_title for word in words):
                    matches.append(m)
                    
        if matches:
            matches_sorted = sorted(matches, key=lambda x: x.get("score", 0.0), reverse=True)[:limit]
            reply = f"I found the following movie matches for '{query}' (showing up to {limit}):"
            return reply, matches_sorted
            
    # 5. Default fallback
    reply = ("Hello! I can help you find movie rankings. Try asking me:\n\n"
             "- \"Show the top 5 movies\"\n"
             "- \"List the top 100 movies\"\n"
             "- \"Show action rankings\"\n\n"
             "You can also click one of the quick-action chips below!")
    return reply, []

def generate_chat_response(query: str, movies_data: list):
    if client is not None:
        try:
            system_instruction = (
                "You are an AI conversational search assistant for the Scrape Center Movie database.\n"
                "You are provided with a complete dataset of movies in JSON format below.\n"
                "Your task is to answer the user's queries conversationally, offering movie summaries, regions, categories, comparisons, or recommendations based ONLY on the database.\n"
                "If you recommend, mention, or list any movies from the database, you MUST extract their EXACT titles (e.g. '素媛 - 소원' or '霸王别姬 - Farewell My Concubine') and put them into the `recommended_titles` array in your JSON output.\n"
                "Rules:\n"
                "1. If no movies are relevant to the query (e.g. greetings or completely unrelated topics), return an empty list for `recommended_titles`.\n"
                "2. Your conversational response in `reply` should be brief, engaging, and in the language of the user's query.\n"
                "3. Do not invent any movie data that is not in the database.\n\n"
                f"Movie Database:\n{json.dumps(movies_data, ensure_ascii=False)}"
            )
            
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=query,
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=GeminiResponse,
                    system_instruction=system_instruction
                )
            )
            
            res_data = json.loads(response.text)
            reply = res_data.get("reply", "")
            rec_titles = res_data.get("recommended_titles", [])
            
            # Map exact titles back to full movie details
            matched_movies = []
            lookup = {m.get("title", "").strip().lower(): m for m in movies_data}
            for title in rec_titles:
                title_clean = title.strip().lower()
                if title_clean in lookup:
                    matched_movies.append(lookup[title_clean])
                else:
                    # Try partial match if exact title lookup fails
                    for m in movies_data:
                        m_title = m.get("title", "").lower()
                        if title_clean in m_title or m_title in title_clean:
                            if m not in matched_movies:
                                matched_movies.append(m)
                                break
                                
            return reply, matched_movies
            
        except Exception as e:
            print(f"Gemini API error: {e}. Falling back to local search.")
            
    return generate_chat_response_local(query, movies_data)

@app.post("/api/chat")
async def chat_endpoint(query: ChatQuery):
    movies = load_movies()
    reply, results = generate_chat_response(query.message, movies)
    
    # Process results cover URLs to point to local fastapi serve
    processed_results = []
    for item in results:
        safe_title = re.sub(r'[\\/*?:"<>|]', "_", item["title"])
        local_cover = f"/covers/{safe_title}.jpg"
        processed_results.append({
            "title": item["title"],
            "score": item.get("score", 0.0),
            "categories": item.get("categories", []),
            "regions": item.get("regions", []),
            "duration": item.get("duration", "N/A"),
            "release_date": item.get("release_date", "N/A"),
            "cover_url": local_cover,
            "detail_link": item.get("detail_link", "#")
        })
        
    return {
        "reply": reply,
        "results": processed_results
    }

@app.get("/")
async def get_index():
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return HTMLResponse(content="<h2>Frontend files not loaded yet. Please wait!</h2>")

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
