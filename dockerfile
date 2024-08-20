# Create a Jekyll container from a Ruby Alpine image
# Find GitHub Pages Dependencies: https://pages.github.com/versions/
# Configured following: https://www.youtube.com/watch?v=owHfKAbJ6_M

# At a minimum, use Alpine 3.2, Ruby 3.3.4, and Jekyll 3.10.x
FROM ruby:3.2-alpine

# Working Directory
WORKDIR /usr/src/app

# Add Jekyll dependencies to Alpine
RUN apk update
RUN apk add --no-cache build-base gcc cmake git 

# Add Python3 and IACS STAR requirements
## TODO: Run this out of .devcontainer for now, but might want a calculator folder in the future
COPY ./.devcontainer/iacs_star_python_requirements.txt ./requirements.txt
# Install Python 3 and necessary build dependencies
RUN apk add --no-cache python3 python3-dev py3-pip build-base libffi-dev
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Update the Ruby bundler and install Jekyll
RUN gem update bundler && gem install bundler jekyll

# If you wanted to run a script
# CMD ["python", "./your-daemon-or-script.py"]