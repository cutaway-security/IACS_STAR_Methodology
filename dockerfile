# Create a Jekyll container from a Ruby Alpine image
# Find GitHub Pages Dependencies: https://pages.github.com/versions/
# Configured following: https://www.youtube.com/watch?v=owHfKAbJ6_M

# At a minimum, use Alpine 3.2, Ruby 3.3.4, and Jekyll 3.10.x
FROM ruby:3.2-alpine

# Add Jekyll dependencies to Alpine
RUN apk update
RUN apk add --no-cache build-base gcc cmake git 

# Update the Ruby bundler and install Jekyll
RUN gem update bundler && gem install bundler jekyll