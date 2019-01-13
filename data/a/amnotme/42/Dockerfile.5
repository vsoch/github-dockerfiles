# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Dockerfile                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lhernand <lhernand@student.42.us.or>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/26 14:45:38 by lhernand          #+#    #+#              #
#    Updated: 2018/03/26 23:27:55 by lhernand         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# This is a dockerized version of valgrind to detect memory leaks
# A test file named test.c is created, compiled and then run with 
# Valgrind
#
# If you'd like to test it you can build the image and then simply run
# the container.
#		docker build -t val .
#		docker run --interactive --tty val
# 
# Pull latest debian distro
#

FROM debian:latest

# Get and install all packages: vim, gcc, valgrind

RUN  apt-get update -y && \
	 apt-get upgrade -y && \
	 apt-get install vim -y && \
	 apt-get install gcc -y && \
	 apt-get install valgrind -y 

# We'll create a test file with obvious memory leaks

RUN echo "#include <stdlib.h>" >> test.c && \
	echo "" >> test.c && \
	echo "void f(void)" >> test.c && \
	echo "{" >> test.c && \
	echo "		int *x =malloc(10 * sizeof(int));" >> test.c && \
	echo "		x[10] = 0;" >> test.c && \
	echo "}" >> test.c && \
	echo "" >> test.c && \
	echo "int main(void)" >> test.c && \
	echo "{" >> test.c && \
	echo "		f();" >> test.c && \
	echo "		return (0);" >> test.c && \
	echo "}" >> test.c

# Let's check that the file is valid

RUN cat test.c

# We'll compile and then run valgrind

RUN ["gcc", "-Wall", "-Wextra", "-Werror", "-g", "-o", "test", "test.c"]
CMD ["valgrind", "--leak-check=yes", "./test"]
