## Streamlit Connections Hackathon Submission: MongoDB Connection

### Team Members

1. @sinlesscoder
2. @TheChanRProject
3. @kgtillis

### Submission Details

For this hackathon, we worked on two major Connections:

1. `MongoConnection`

This submission allows an application user to write queries on a MongoDB collection. The demo allows the user to choose between 3 different collections:

1. `employee_info`
2. `stock_market`
3. `spotify_tracks`

### Usage

```python
import streamlit as st
from mongo_connection import MongoConnection

# Experiment Connection for Mongo
st.experimental_connection('sample', type=MongoConnection)

```

### Sequence of Steps

#### Mongo Connector

- Due Date: August 1

1. Create a MongoDB instance for testing
2. Create an Experimental Connection that extends Streamlit's class with some authentication using `pymongo`
3. Import your class into the demo Streamlit app
