# Getting the image
FROM condaforge/mambaforge:latest

# Defining the Working directory
WORKDIR /app

# Copy environment.yaml in working directory
COPY environment.yml app/environment.yml

# create environment in image
RUN mamba env create -f environment.yml && mamba clean -a -y

# Create env variable
ENV CONDA_ENV=BioRAG
ENV LD_LIBRARY_PATH=/opt/conda/envs/${CONDA_ENV}/lib:${LD_LIBRARY_PATH}

COPY . /app

# Start a shell inside the conda env
CMD ["conda", "run", "--no-capture-output", "-n", "BioRAG", "bash"]