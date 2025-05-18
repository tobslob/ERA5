FROM continuumio/miniconda3

RUN conda config --add channels conda-forge && \
    conda config --set channel_priority strict

# Install all required packages from conda-forge
RUN conda install -y \
    fastapi \
    uvicorn \
    cdsapi \
    python-dotenv \
    xarray \
    netCDF4 \
    cfgrib \
    eccodes \
    numpy \
    && conda clean --all --yes

# Set env variables for ecCodes (important for cfgrib to work!)
ENV GRIB_DEFINITION_PATH=/opt/conda/share/eccodes/definitions
ENV GRIB_SAMPLES_PATH=/opt/conda/share/eccodes/samples

WORKDIR /app

COPY . .
COPY .env .env

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
