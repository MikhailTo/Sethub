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
        "items_count": 15,
        "author": "BookWorm42",
        "updated": "2023-04-30",
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
        "title": "Essential Tools for Remote Work",
        "description": "A comprehensive list of software and hardware for effective remote work.",
        "items_count": 12,
        "author": "RemoteGuru",
        "updated": "2023-05-10",
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
        "title": "Top Hiking Trails in North America",
        "description": "Discover the most scenic and challenging hiking trails across the continent.",
        "items_count": 20,
        "author": "NatureExplorer",
        "updated": "2023-05-05",
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
        "title": "Must-Watch Sci-Fi Movies",
        "description": "A curated selection of the best science fiction films of all time.",
        "items_count": 25,
        "author": "CinemaGeek",
        "updated": "2023-05-12",
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
        "title": "Healthy Breakfast Ideas",
        "description": "Quick and nutritious breakfast recipes to start your day right.",
        "items_count": 15,
        "author": "HealthyEater",
        "updated": "2023-05-08",
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
        "title": "Essential JavaScript Libraries",
        "description": "A list of must-know JavaScript libraries for modern web development.",
        "items_count": 12,
        "author": "WebDevPro",
        "updated": "2023-05-14",
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
        "title": "Top Productivity Apps",
        "description": "Boost your efficiency with these carefully selected productivity applications.",
        "items_count": 10,
        "author": "ProductivityNinja",
        "updated": "2023-05-11",
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
        "title": "Best Podcasts for Entrepreneurs",
        "description": "A collection of insightful podcasts for aspiring and seasoned entrepreneurs.",
        "items_count": 15,
        "author": "StartupFanatic",
        "updated": "2023-05-09",
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
        "title": "Must-Visit European Cities",
        "description": "Explore the rich culture and history of these top European destinations.",
        "items_count": 20,
        "author": "TravelEnthusiast",
        "updated": "2023-05-13",
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)