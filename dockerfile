# Create a Jekyll container from a Ruby Alpine image
# Find GitHub Pages Dependencies: https://pages.github.com/versions/
# Configured following: https://www.youtube.com/watch?v=owHfKAbJ6_M

# At a minimum, use Alpine 3.2, Ruby 3.3.4, and Jekyll 3.10.x
FROM ruby:3.2-alpine

# Working Directory for HTML and calculators
WORKDIR /app
ADD folder /app/scripts
ADD folder /app/config
ADD folder /app/templates
ADD folder /app/calcs
COPY ./scripts/* /app/scripts
COPY ./config/* /app/config
COPY ./templates/* /app/templates

# Add Jekyll dependencies to Alpine
RUN apk update
RUN apk add --no-cache build-base gcc cmake git 

# Add Python3 and IACS STAR requirements
# Install Python 3 and necessary build dependencies
RUN apk add --no-cache python3 python3-dev py3-pip build-base libffi-dev py3-yaml py3-jinja2 
# NOTE: Attempts to install PyYAML and Jinja2 using Pip and a 
#       requirements file were unsuccessful. Not sure why,
#       perhaps installer layers due to environments.

# NOTE: Build calculators here or in devcontainer.json file using a script
# Update the Ruby bundler and install Jekyll
RUN gem update bundler && gem install bundler jekyll

# If you wanted to run a script
# CMD ["python", "./your-daemon-or-script.py"]