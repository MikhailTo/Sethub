import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="../../frontend/static"), name="static")

templates = Jinja2Templates(directory="../../frontend/templates")

lists = [
    {
        "title": "Top 10 Programming Languages",
        "description": "A curated list of the most popular programming languages in 2023.",
        "items_count": 10,
        "author": "JohnDoe",
        "updated": "2023-05-15",
        "entries": [
            "Python",
            "JavaScript",
            "Java",
            "C++",
            "C#",
            "Ruby",
            "Go",
            "Swift",
            "Kotlin",
            "TypeScript"
        ]
    },
    {
        "title": "Best Books of the 21st Century",
        "description": "A collection of must-read books published since 2000.",
        "items_count": 10,
        "author": "BookWorm42",
        "updated": "2023-04-30",
        "entries": [
            "The Road by Cormac McCarthy",
            "The Corrections by Jonathan Franzen",
            "Life of Pi by Yann Martel",
            "The Kite Runner by Khaled Hosseini",
            "The Help by Kathryn Stockett",
            "The Da Vinci Code by Dan Brown",
            "The Hunger Games by Suzanne Collins",
            "The Girl with the Dragon Tattoo by Stieg Larsson",
            "The Curious Incident of the Dog in the Night-Time by Mark Haddon",
            "Cloud Atlas by David Mitchell"
        ]
    },
    {
        "title": "Essential Tools for Remote Work",
        "description": "A comprehensive list of software and hardware for effective remote work.",
        "items_count": 10,
        "author": "RemoteGuru",
        "updated": "2023-05-10",
        "entries": [
            "Zoom",
            "Slack",
            "Trello",
            "Google Workspace",
            "Microsoft Teams",
            "Asana",
            "Noise-cancelling headphones",
            "Ergonomic chair",
            "Standing desk",
            "Reliable internet connection"
        ]
    },
    {
        "title": "Top Hiking Trails in North America",
        "description": "Discover the most scenic and challenging hiking trails across the continent.",
        "items_count": 10,
        "author": "NatureExplorer",
        "updated": "2023-05-05",
        "entries": [
            "Pacific Crest Trail",
            "Appalachian Trail",
            "John Muir Trail",
            "West Coast Trail",
            "Wonderland Trail",
            "Kalalau Trail",
            "Bright Angel Trail",
            "Half Dome Trail",
            "Grinnell Glacier Trail",
            "Skyline Trail"
        ]
    },
    {
        "title": "Must-Watch Sci-Fi Movies",
        "description": "A curated selection of the best science fiction films of all time.",
        "items_count": 10,
        "author": "CinemaGeek",
        "updated": "2023-05-12",
        "entries": [
            "2001: A Space Odyssey",
            "Blade Runner",
            "The Matrix",
            "Alien",
            "Star Wars: Episode IV - A New Hope",
            "E.T. the Extra-Terrestrial",
            "Inception",
            "The Terminator",
            "Back to the Future",
            "Jurassic Park"
        ]
    },
    {
        "title": "Healthy Breakfast Ideas",
        "description": "Quick and nutritious breakfast recipes to start your day right.",
        "items_count": 10,
        "author": "HealthyEater",
        "updated": "2023-05-08",
        "entries": [
            "Overnight oats",
            "Greek yogurt parfait",
            "Avocado toast",
            "Smoothie bowl",
            "Egg white frittata",
            "Chia seed pudding",
            "Whole grain pancakes",
            "Breakfast burrito",
            "Protein-packed muffins",
            "Fruit and nut butter wrap"
        ]
    },
    {
        "title": "Essential JavaScript Libraries",
        "description": "A list of must-know JavaScript libraries for modern web development.",
        "items_count": 10,
        "author": "WebDevPro",
        "updated": "2023-05-14",
        "entries": [
            "React",
            "Vue.js",
            "Angular",
            "jQuery",
            "Lodash",
            "Axios",
            "D3.js",
            "Three.js",
            "Moment.js",
            "Chart.js"
        ]
    },
    {
        "title": "Top Productivity Apps",
        "description": "Boost your efficiency with these carefully selected productivity applications.",
        "items_count": 10,
        "author": "ProductivityNinja",
        "updated": "2023-05-11",
        "entries": [
            "Todoist",
            "Evernote",
            "RescueTime",
            "Forest",
            "Any.do",
            "Toggl",
            "IFTTT",
            "LastPass",
            "Grammarly",
            "Notion"
        ]
    },
    {
        "title": "Best Podcasts for Entrepreneurs",
        "description": "A collection of insightful podcasts for aspiring and seasoned entrepreneurs.",
        "items_count": 10,
        "author": "StartupFanatic",
        "updated": "2023-05-09",
        "entries": [
            "How I Built This",
            "Masters of Scale",
            "Startup",
            "The Tim Ferriss Show",
            "Mixergy",
            "Entrepreneurs on Fire",
            "The GaryVee Audio Experience",
            "The $100 MBA Show",
            "Freakonomics Radio",
            "Smart Passive Income"
        ]
    },
    {
        "title": "Must-Visit European Cities",
        "description": "Explore the rich culture and history of these top European destinations.",
        "items_count": 10,
        "author": "TravelEnthusiast",
        "updated": "2023-05-13",
        "entries": [
            "Paris, France",
            "Rome, Italy",
            "Barcelona, Spain",
            "Amsterdam, Netherlands",
            "Prague, Czech Republic",
            "Vienna, Austria",
            "London, United Kingdom",
            "Berlin, Germany",
            "Venice, Italy",
            "Budapest, Hungary"
        ]
    }
]

@app.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    context = {
        "title": "Sethub",
        "lists": lists
        }
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=context
    )

@app.get("/create", response_class=HTMLResponse)
async def create_list(request: Request):
    context = {
        "title": "Create New List - Sethub"
    }
    return templates.TemplateResponse(
        request=request,
        name="create_list.html",
        context=context
    )

@app.get("/search", response_class=HTMLResponse)
async def search(request: Request, q: str = ""):
    context = {
        "title": "Search - Sethub",
        "query": q
    }
    return templates.TemplateResponse(
        request=request,
        name="search.html",
        context=context
    )

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    context = {
        "title": "About - Sethub",
    }
    return templates.TemplateResponse(
        request=request,
        name = "about.html", 
        context=context)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)