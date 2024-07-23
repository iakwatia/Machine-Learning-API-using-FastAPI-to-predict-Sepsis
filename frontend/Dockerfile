
# FROM python:3.8-slim

# # Set the working directory
# WORKDIR /frontend

# # Copy the current directory contents into the container at /frontend
# COPY . /frontend

# # Install any needed packages specified in requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

# # Make port 8501 available to the world outside this container
# EXPOSE 8501

# # Define environment variable
# ENV NAME Frontend

# # Run streamlit when the container launches
# CMD ["streamlit", "run", "main.py", "--server.port=8501"]


#*'''#runtime or python application
FROM python:3.11.0  
 
#copy the requrements to a tmp file
COPY requirements.txt /tmp/requirements.txt
 
# Install the dependencies specified in the requirements.txt file
RUN python -m pip install --timeout 300 -r /tmp/requirements.txt
 
COPY . /app
 
WORKDIR /app
 
EXPOSE 3000

CMD ["streamlit", "run", "main.py", "--server.port=8501"]
 