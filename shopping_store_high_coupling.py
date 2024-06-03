from diagrams import Diagram, Cluster
from diagrams.c4 import Person, Container, Relationship

with Diagram("Shopping Store - High Coupling and Low Cohesion", show=False):
    user = Person("Customer", "A user of the shopping store")

    with Cluster("Shopping Store System"):
        webapp = Container("Web Application", "JavaScript", "Handles user interactions and displays products")
        mobileapp = Container("Mobile Application", "Flutter", "Handles user interactions and displays products on mobile")
        
        # API mixed with business logic and direct DB access
        api = Container("API", "Node.js/Express", "Handles requests from web and mobile apps, direct DB access, and business logic")
        
        db = Container("Database", "MySQL", "Stores product information, user data, orders, etc.")
        
        # Payment gateway logic inside the API
        payment_logic = Container("Payment Logic", "Part of API", "Processes payments directly within API layer")

    user >> Relationship("Browses, buys products using") >> webapp
    user >> Relationship("Browses, buys products using") >> mobileapp
    
    # Web and mobile apps interact with API which is overly complex
    webapp >> Relationship("Sends requests to") >> api
    mobileapp >> Relationship("Sends requests to") >> api

    # Direct dependencies between API and database
    api >> Relationship("Directly accesses") >> db
    api >> Relationship("Processes payments directly through") >> payment_logic

    # Unnecessary direct interactions (showing high coupling)
    webapp >> Relationship("Directly accesses") >> db
    mobileapp >> Relationship("Directly accesses") >> db
    webapp >> Relationship("Contains some payment logic") >> payment_logic
    mobileapp >> Relationship("Contains some payment logic") >> payment_logic
