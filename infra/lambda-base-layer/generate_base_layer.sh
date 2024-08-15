# remove container first if exists
docker rm layer-container

# build the base layer
docker build -t lambda-base-layer .

# rename it to layer-container
docker run --name layer-container base-layer

# copy the generated zip artifact so our CDK can you it
docker cp layer-container:layer.zip . && echo "Create layer.zip with updated base layer successfully"
