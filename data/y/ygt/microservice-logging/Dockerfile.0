FROM ruby:2.3

COPY Gemfile .
RUN gem install rspec json rubocop
WORKDIR /var/app
CMD ["bash"]
