#Start with a Miniconda image
FROM continuumio/miniconda3

#Create a conda environment from yml file
COPY rest-api-env.yml /tmp/rest-api-env.yml
RUN conda env create -f /tmp/rest-api-env.yml

#Copy our python files into a convenient place
COPY rest_api /src/rest_api/rest_api/

#Activate the environment and add to the PATH
RUN echo "source activate rest-api-env" > ~/.bashrc
ENV PATH /opt/conda/envs/rest-api-env/bin:$PATH

RUN pip install flask-rebar==1.1.0
RUN pip install marshmallow==2.16.3
