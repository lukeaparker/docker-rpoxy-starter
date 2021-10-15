# Base python image
FROM python:3.7-slim-buster


# Step 2: Copy the code into a folder named app
COPY appb/ /appb 

# Step 3: Switch the working directory to app
WORKDIR /appb

# Step 4: Download dependencies 
RUN pip3 install flask 
RUN pip3 install python-dotenv

# Step 5: Set ENV variables
EXPOSE ${APPB_PORT}

# Step 6: Start application
CMD ["flask", "run"]