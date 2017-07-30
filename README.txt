Notes from article published in Linux Journal
'Python Scripts as a Replacement for Bash Utility Scripts'
By Richard Delaney

https://www.linuxjournal.com/content/python-scripts-replacement-bash-utility-scripts

"Instead of replacing a series of bash commands with one Python script, it often is better to have Python do only the heavy lifting in the middle. This allows for more modular and reusable scripts, while also tapping into the power of all that Python offers."

Let's say we have a log of the number of times a user is using our service
We can find the number of unique users using the linux lines below

$ cat names.log | sort | uniq | wc -l

What if we want the name of the users and the number of times they've logged in?
We can write a simple python script for that

$ cat data/names.log | python name_count.py

We can then sort so most frequent users are printed first
sort -rn (-r for reverse and -n for numeric)

$ cat data/names.log | python name_count.py | sort -rn

We can use this name_count.py script again for a different purpose
What if we have a csv file containing the user name and a comment, and we want to 
send a thank you email to the top 5 commenters.
ex: "email@example.com", "Thank you for your service"

We can use the csv module to parse the csv file and return only the column we desire
By default csv_column.py will return the content in the first column but we can pass in argument

$ cat data/comments.csv | python csv_column.py [optional column number] | python name_count.py | sort -rn | head -n 5

Now we can use the SMTP module to send emails to the top 5 commenters
name_count.py return the count and the username, but we only want the username
cut -f2 allows us to isolate the second column and use the username email to send the thank you email

$ cat data/comments.csv | python csv_column.py | python name_count.py | sort -rn | head -n 5 | cut -f2 | python send_email.py
