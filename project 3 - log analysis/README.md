# Installation

Here is the [news data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

To run that code you need to have to have vagrant installed and the udacity VM installed,
then go to vagrant subfolder in that VM and run vagrant up, after it finishes run vagrant ssh,
then go to shared directory cd /vagrant where yo should have newsdata.sql file with my **log.py** file.
**OR**
install [python]( https://www.python.org/downloads/ ) and [postgresql]( https://www.postgresql.org/download/ ) then in the go to direcory where **log.py** and **newsdata.sql** exist.

# Usage

Run in shell that command to build the database: `psql -d news -f newsdata.sql`
then run my programy by typing: `python log.py` , then press enter.
Now you will see results appearing in the shell.

## What does the **Log.py** file consist of?

### The project consists of three functions.

#### 1- The first function is `popularArticles()`

* which returns the most popular three articles.

* in it I created view called it pathfromslug to make use of that slug to have relation between articles and log tables.

    `create view pathfromslug as select '/article/' || slug as slugpath, title from articles;`

* then selecting results we wanted by one statement.

    `select title || ' -', count(log.id) as views from pathfromslug left join log on pathfromslug.slugpath = log.path group by title order by views desc limit 3;`

#### 2- The second function is `topAuthors()`

* which returns top authors sorted in descending order.

* I have created a view slugtopath to make a relatioon between log and articles tables.

* created another view by joining theview we made with author table.

    `create view theslugtopath as select '/article/' || slug as newslug, title, author from articles;`

    `create view thetopauthors as select author, title, count(log.id) as views from theslugtopath left join log on theslugtopath.newslug = log.path group by title, author order by views desc;`

* then selecting results we wanted by one statement.

    `select name || ' -' as name, sum(views) as views from thetopauthors join authors on author = id group by name order by views desc;`

#### 3- The third fsunction is `errorPercent()`

* which returns days in which error percent more than 1%.

* here I created a view to have every date with count of all status and error status in that day.

    `create view doitall as select date(time) as dates, count(status) as numberofall, sum(case when status <> '200 OK' then 1 else 0 end) as numberoferrors from log group by dates;`

* then selecting results we wanted by one statement.

    `select dates || ' -' as dates, (numberoferrors :: float / numberofall) * 100 as percent from do it all where (numberoferrors :: float / numberofall)* 100 > 1 order by percent desc;`

#### 4- Then calling to those three functions.

