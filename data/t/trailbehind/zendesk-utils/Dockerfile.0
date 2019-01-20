FROM python:3.5

# Install chinese fonts, then update the font-cache.
# Based on: http://cnedelcu.blogspot.com/2015/04/wkhtmltopdf-chinese-character-support.html
RUN apt-get update && apt-get install --no-install-recommends -yq \
    fonts-wqy-microhei \
    ttf-wqy-microhei \
    fonts-wqy-zenhei \
    ttf-wqy-zenhei
RUN fc-cache -f -v

RUN mkdir -p /zendesk-utils
COPY requirements.txt /zendesk-utils
RUN pip install --no-cache-dir -r /zendesk-utils/requirements.txt

ENV PYTHONPATH /zendesk-utils:/zendesk-utils/helpcenter_to_pdf:/zendesk-utils/to_json:/zendesk-utils/localize:$PYTHONPATH

COPY . /zendesk-utils
WORKDIR /zendesk-utils
