FROM hseling/hseling-api-base:python3.6-alpine3.7 as build

LABEL maintainer="Lorenzo Tosi <info@linghub.ru>"

RUN mkdir /dependencies
COPY ./hseling_api_cross_lingual_morph_analysis/requirements.txt /dependencies/requirements.txt
COPY ./hseling_api_cross_lingual_morph_analysis/setup.py /dependencies/setup.py

RUN pip install -r /dependencies/requirements.txt

FROM hseling/hseling-api-base:python3.6-alpine3.7 as production

COPY --from=build /usr/local/lib/python3.6/site-packages /usr/local/lib/python3.6/site-packages
COPY --from=build /usr/lib/python3.6/site-packages /usr/lib/python3.6/site-packages

COPY --from=build /dependencies /dependencies

COPY ./hseling_lib_cross_lingual_morph_analysis /dependencies/hseling_lib_cross_lingual_morph_analysis
RUN pip install /dependencies/hseling_lib_cross_lingual_morph_analysis

COPY ./hseling_api_cross_lingual_morph_analysis/hseling_api_cross_lingual_morph_analysis /app/hseling_api_cross_lingual_morph_analysis
COPY ./hseling_api_cross_lingual_morph_analysis/main.py /app/main.py

ENV HSELING_API_CROSS_LINGUAL_MORPH_ANALYSIS_SETTINGS="/app/hseling_api_cross_lingual_morph_analysis/default_settings.py"

HEALTHCHECK CMD curl --fail http://localhost/healthz || exit 1
