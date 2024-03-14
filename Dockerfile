# Use an ephemeral build stage to build the documentation
FROM python:3.12-alpine3.18 as build

WORKDIR /build

# Install required packages
COPY requirements.docs.txt .

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.docs.txt

# Copy the project files into the container
COPY . .

RUN python render_diagrams.py && \
    # Build the documentation; writes to the 'site' directory by default
    mkdocs build


# Create the final Docker image
FROM nginx:stable-alpine

# Copy the documentation files from the build stage to the web root directory
COPY --from=build /build/site /usr/share/nginx/html