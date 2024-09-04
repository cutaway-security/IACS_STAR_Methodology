# Create a Jekyll container from a Ruby Alpine image
# Find GitHub Pages Dependencies: https://pages.github.com/versions/
# Configured following: https://www.youtube.com/watch?v=owHfKAbJ6_M

# At a minimum, use Alpine 3.2, Ruby 3.3.4, and Jekyll 3.10.x
FROM ruby:3.2-alpine

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

# Working Directory for HTML and calculators
#WORKDIR /usr/src/app
#COPY ./scripts/ ./scripts
#COPY ./config/ ./config
#COPY ./templates/ ./templates
#COPY ./calcs/ ./calcs
#ADD ./scripts/calc.js /assets/js/calc.js

# If you wanted to run a script
# CMD ["python", "./your-daemon-or-script.py"]