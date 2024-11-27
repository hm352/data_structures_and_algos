# Use the latest Postgres image
FROM postgres:latest

# Set the environment variables
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydb

# Create a volume to store the data
VOLUME /var/lib/postgresql/data

# Copy the data directory from the host machine to the container
COPY data /var/lib/postgresql/data

# Expose the Postgres port
EXPOSE 5432

# Run the Postgres command
CMD ["postgres"]
