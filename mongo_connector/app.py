import streamlit as st
from streamlit import experimental_connection, secrets
from connection import MongoDBConnection
from StringDropdown import StringDropdown
from NumberDropdown import NumberDropdown
from mongo_db import connect_mongo
from key_value_mapper import kvmapper
from json_cache import result_serialize, read_json

# mongo uri
mongo_uri = secrets['sample_mongo']['uri']
db = secrets['sample_mongo']['db']

mongo_db = connect_mongo(mongo_uri, db)

# Title of your App
st.markdown("<h1 style='text-align:center'> MongoDB Connection Demo </h1>", unsafe_allow_html=True)

# Choose a collection to connect to
con_option = st.selectbox("Choose a MongoDB collection: ", options=['sample', 'stock_market'])

# Connection object
conn = experimental_connection(con_option, type=MongoDBConnection)

# Setup a filter collector
filter_collector = []

# Sample from Mongo
sample = mongo_db[con_option]

# Key Value Mapping
# Sample documents
sample_docs = [doc for doc in sample.find()]

# Apply kvmapper
kv_mapped = kvmapper(sample_docs)

# Define updated_kv as kv_mapped
updated_kv = read_json('cache.json')

# Cols to Select
chosen_keys = st.multiselect("Choose columns you want to query: ", list(kv_mapped.keys()))

# Modify button
if st.button("Modify"):
    updated_kv = {k:v for k,v in kv_mapped.items() if k in chosen_keys}
    result_serialize('cache.json', updated_kv)
    widget_state = True

    
with st.expander("Expand to view your results: ", expanded=True):
    # Create logic to build the widgets
    for i, key in enumerate(updated_kv):
        # Build widget based on type
        if kv_mapped[key] == 'number':
            # Numerical Widget
            widget = NumberDropdown(sample_docs, key, i)
        elif kv_mapped[key] == 'string':
            # String Widget
            widget = StringDropdown(sample_docs, key, i)
        
        widget.create_dropdown(filter_collector)

    # Button
    if st.button("View sub-filters"):
        st.json(filter_collector)


# # Update filter collector into a dictionary
# start_filter = read_json('filter.json')




if st.button("Submit"):
    # Update filter collector into a dictionary
    start_filter = filter_collector[0]

    for i, obj in enumerate(filter_collector[1:]):
        inner_obj = obj
        key = list(inner_obj.keys())[0]
        start_filter[key] = inner_obj[key]

    result_serialize('filter.json', start_filter)

    # Write a query
    query = conn.query(start_filter, con_option)

    st.json(query)