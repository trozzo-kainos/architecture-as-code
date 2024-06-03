from diagrams import Diagram, Cluster
from diagrams.c4 import Container, SystemBoundary, Person, Relationship

with Diagram("Online Banking System - C4 Component Diagram", show=False, outformat="png",
             filename="Online_Banking_C4_Diagram"):
    customer = Person(name="Customer", description="A customer using the online banking system")

    with SystemBoundary("Online Banking System"):
        frontend = Container(name="Frontend Application", description="User Interface (React/Angular)",
                             technology="JavaScript/TypeScript")

        with SystemBoundary("Backend Services"):
            user_service = Container(name="User Service", description="Manages user information and authentication",
                                     technology="Python/Node.js")
            account_service = Container(name="Account Service", description="Manages bank accounts",
                                        technology="Python/Node.js")
            transaction_service = Container(name="Transaction Service",
                                            description="Handles transactions between accounts",
                                            technology="Python/Node.js")
            notification_service = Container(name="Notification Service", description="Sends notifications to users",
                                             technology="Python/Node.js")
            analytics_service = Container(name="Analytics Service", description="Provides analytics and reporting",
                                          technology="Python/Node.js")

            with SystemBoundary("Databases"):
                user_db = Container(name="User DB", description="Stores user information", technology="MySQL")
                account_db = Container(name="Account DB", description="Stores account information", technology="MySQL")
                transaction_db = Container(name="Transaction DB", description="Stores transaction information",
                                           technology="MySQL")
                analytics_db = Container(name="Analytics DB", description="Stores analytics data", technology="MySQL")

    # Relationships
    customer >> frontend
    frontend >> user_service
    frontend >> account_service
    frontend >> transaction_service
    frontend >> notification_service
    frontend >> analytics_service

    user_service >> user_db
    account_service >> account_db
    transaction_service >> transaction_db
    analytics_service >> analytics_db

    user_service >> account_service
    user_service >> transaction_service
    account_service >> transaction_service
    transaction_service >> analytics_service
    notification_service >> user_service
    notification_service >> account_service
    notification_service >> transaction_service
