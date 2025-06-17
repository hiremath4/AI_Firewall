#!/bin/bash

# Run backend in background
python manage.py runserver

# Run frontend (e.g., Streamlit)
streamlit run Home.py 
