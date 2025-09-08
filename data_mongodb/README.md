Data Sourcing from CSV to MongoDB Atlas using Python

Setting Up a MongoDB Atlas Cluster (Free Tier)

This section explains how to create a free MongoDB Atlas cluster, add a database and user, and connect it to your Python code.

Step 1: Create a MongoDB Atlas Account

Go to https://www.mongodb.com/cloud/atlas

Click "Start Free" and create an account.

After verifying your email, log in to the MongoDB Atlas dashboard.

Step 2: Create a Cluster (Free Tier)

Click "Build a Database"

Choose the Shared Cluster (Free) option

Choose a cloud provider and region (e.g., AWS, Azure)

Name your cluster (e.g., mlopscluster)

Click Create Cluster

It takes 1–2 minutes to finish provisioning.

Step 3: Create a Database User

Go to Database Access in the left-hand menu

Click "Add New Database User"

Set a username and password (you’ll use this in Python)

Select Read and Write to any database

Click Add User

Step 4: Allow Access from Anywhere

Go to Network Access in the left menu

Click "Add IP Address"

Choose Allow Access from Anywhere (0.0.0.0/0)

Click Confirm

This makes it easier to connect during testing, but for production, add specific IPs only.

Step 5: Get the Connection String

Go to Clusters → Connect → Connect your application

Choose:

Driver: Python

Version: e.g., 3.12 or later

Copy the connection string, which looks like this:

mongodb+srv://<username>:<password>@<clustername>.mongodb.net/?retryWrites=true&w=majority


Replace <username> and <password> with your actual values in your Python code.


Connect to MongoDB Atlas using Python (pymongo)

Upload CSV data to a MongoDB collection

Fetch and display the data (with or without _id)

 Prerequisites

Python installed

pymongo installed