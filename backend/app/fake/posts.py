from datetime import datetime, timedelta
import random

class Posts:
    posts = [
        {
            "id": 1,
            "user_id": 101,
            "title": "Top 10 Programming Languages",
            "content": "A detailed exploration of the most popular programming languages in 2023.",
            "created_at": datetime.now() - timedelta(days=30),
            "updated_at": datetime.now() - timedelta(days=2),
            "description": "A curated list of the most popular programming languages in 2023.",
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
            "id": 2,
            "user_id": 102,
            "title": "Essential Tools for Remote Work",
            "content": "An in-depth guide to the best software and hardware for effective remote work.",
            "created_at": datetime.now() - timedelta(days=20),
            "updated_at": datetime.now() - timedelta(days=1),
            "description": "A comprehensive list of software and hardware for effective remote work.",
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
            "id": 11,
            "user_id": 111,
            "title": "Best Podcasts for Entrepreneurs",
            "content": "Dive deep into the world of entrepreneurship with these insightful podcasts.",
            "created_at": datetime.now() - timedelta(days=15),
            "updated_at": datetime.now() - timedelta(days=1),
            "description": "A collection of insightful podcasts for aspiring and seasoned entrepreneurs.",
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
            "id": 12,
            "user_id": 112,
            "title": "Must-Visit European Cities",
            "content": "Embark on a virtual tour of Europe's most captivating cities.",
            "created_at": datetime.now() - timedelta(days=10),
            "updated_at": datetime.now() - timedelta(hours=12),
            "description": "Explore the rich culture and history of these top European destinations.",
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
        },
        {
            "id": 13,
            "user_id": 113,
            "title": "Healthy Breakfast Ideas",
            "content": "Start your day right with these nutritious and delicious breakfast options.",
            "created_at": datetime.now() - timedelta(days=8),
            "updated_at": datetime.now() - timedelta(hours=6),
            "description": "Quick and nutritious breakfast recipes to start your day right.",
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
            "id": 14,
            "user_id": 114,
            "title": "Essential JavaScript Libraries",
            "content": "Enhance your web development skills with these crucial JavaScript libraries.",
            "created_at": datetime.now() - timedelta(days=5),
            "updated_at": datetime.now() - timedelta(hours=2),
            "description": "A list of must-know JavaScript libraries for modern web development.",
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
            "id": 15,
            "user_id": 115,
            "title": "Top Productivity Apps",
            "content": "Boost your efficiency and get more done with these powerful productivity tools.",
            "created_at": datetime.now() - timedelta(days=3),
            "updated_at": datetime.now() - timedelta(hours=1),
            "description": "Boost your efficiency with these carefully selected productivity applications.",
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
            "id": 16,
            "user_id": 116,
            "title": "Best Books of the 21st Century",
            "content": "Explore the literary masterpieces that have defined the 21st century so far.",
            "created_at": datetime.now() - timedelta(days=25),
            "updated_at": datetime.now() - timedelta(days=3),
            "description": "A collection of must-read books published since 2000.",
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
            "id": 17,
            "user_id": 117,
            "title": "Top Hiking Trails in North America",
            "content": "Lace up your boots and hit these breathtaking trails across North America.",
            "created_at": datetime.now() - timedelta(days=18),
            "updated_at": datetime.now() - timedelta(days=1),
            "description": "Discover the most scenic and challenging hiking trails across the continent.",
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
            "id": 18,
            "user_id": 118,
            "title": "Must-Watch Sci-Fi Movies",
            "content": "Embark on cinematic journeys through time, space, and imagination with these sci-fi classics.",
            "created_at": datetime.now() - timedelta(days=12),
            "updated_at": datetime.now() - timedelta(hours=8),
            "description": "A curated selection of the best science fiction films of all time.",
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
        }
    ]

    @classmethod
    def generate_mock_posts(cls, num_posts):
        for i in range(num_posts):
            cls.posts.append({
                "id": len(cls.posts) + 1,
                "user_id": random.randint(100, 999),
                "title": f"Mock Post {i+1}",
                "content": f"This is the content for Mock Post {i+1}.",
                "created_at": datetime.now() - timedelta(days=random.randint(1, 100)),
                "updated_at": datetime.now() - timedelta(days=random.randint(0, 30)),
                "description": f"Description for Mock Post {i+1}",
                "entries": [f"Entry {j+1}" for j in range(random.randint(3, 10))]
            })

# Generate additional mock posts
Posts.generate_mock_posts(5)
