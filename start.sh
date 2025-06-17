#!/bin/bash

# Run backend in background
python manage.py runserver 0.0.0.0:$PORT &

# Run frontend (e.g., Streamlit)
streamlit run Home.py --server.port 10000 --server.enableCORS false
