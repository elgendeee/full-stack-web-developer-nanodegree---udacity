#!/usr/bin/env python2.7

# import psycopg2 which is a postgresql adapter for python
import psycopg2


def popularArticles():
    """ A function to return the popular 3 articles """

    db = psycopg2.connect("dbname = news")  # Connecting to news database

    # Allows Python code to execute PostgreSQL command in a database session
    c = db.cursor()

    operation = '''

    create view pathfromslug as select '/article/' || slug \
    as slugpath, title from articles;

    select title || ' -', count(log.id) as views from pathfromslug \
    left join log on pathfromslug.slugpath = log.path \
    group by title order by views desc limit 3;

    '''
    # operation is variable wrapping commands to execute in database
    # first create view in which taking slug make
    # it similar to path in log table
    # so that  making relation between log table and articles table
    # then selecting title count(log.id) depending on that

    c.execute(operation)  # Executes the commands in postgresql

    articles = c.fetchall()  # Fetching all the results

    print "\n* The most popular three articles of all time:"

    # For every row reslting in articles fetched
    # we get the striing of it then print it
    for row in articles:
        mystring = ' '.join(map(str, (row)))
        print(mystring + ' views')

    # Closing our DataBase
    db.close()


def topAuthors():
    """ A function to return the top authors sorted in descending order """

    db = psycopg2.connect("dbname = news")  # Connecting to news database

    # Allows Python code to execute PostgreSQL command in a database session
    c = db.cursor()

    operation = '''

    create view theslugtopath as select '/article/' || slug as newslug, \
    title, author from articles;

    create view thetopauthors as select author, title, count(log.id) as \
    views from theslugtopath left join \
    log on theslugtopath.newslug = log.path \
    group by title, author order by views desc;

    select name || ' -' as name, sum(views) as \
    views from thetopauthors join authors \
    on author = id group by name order by views desc;

    '''
    # as above opertaion is a variable to wrap
    # commands to be executed in database
    # creating a view slugtopath to make like above function
    # a relatioon between log and articles tables
    # create another view by joining theview we made with author table
    # select name of author with sum of views of his
    # articles depending on author in the topauthors view
    # equals id in the authors table

    c.execute(operation)  # Executes the commands in postgresql

    authors = c.fetchall()  # Fetching all the results

    print "\n* The most popular article authors of all time:"

    # For every row reslting in articles fetched
    # we get the striing of it then print it
    for row in authors:
        mystring = ' '.join(map(str, (row)))
        print(mystring + ' views')

    # Closing our DataBase
    db.close()


def errorPercent():
    """ A function to return days in which error percent more than 1% """

    db = psycopg2.connect("dbname = news")  # Connecting to news database

    # Allows Python code to execute PostgreSQL command in a database session
    c = db.cursor()

    operation = '''

    create view doitall as \
    select date(time) as dates, \
    count(status) as numberofall, \
    sum(case when status <> '200 OK' then 1 else 0 end) as numberoferrors \
    from log \
    group by dates;

    select dates || ' -' as dates, \
    (numberoferrors :: float / numberofall) * 100 as percent \
    from doitall where (numberoferrors :: float / numberofall) * 100 > 1 \
    order by percent desc;

    '''
    # here I created a view to have every date
    # with count of all status and error status in that day
    # the select every date with percent of error status by all status in it

    c.execute(operation)  # Executes the commands in postgresql

    percent = c.fetchall()  # Fetching all the results

    print "\n* Days on which more than 1%"+" of requests lead to errors:"

    # For every row reslting in articles fetched
    # we get the striing of it then print it
    for row in percent:
        mystring = ' '.join(map(str, (row)))
        print(mystring + '% ' + 'errors')

    # Closing our DataBase
    db.close()

# Calling the above three funtions to show results
popularArticles()
topAuthors()
errorPercent()
