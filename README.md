# Capture The FLag
[THM] Year Of The Pig Walkthrough

Start with a simple nmap scan:

sudo nmap -sV -A $IP

![Screenshot 2020-10-12 001215](https://user-images.githubusercontent.com/72692401/95679646-fb9fb780-0c1f-11eb-9c54-bb4e65bbe84f.png)


See that there are two opened ports: 
- http:80
- ssh:22

Maybe we have something to do with the http port, so I run gobuster against the website to find hidden directories if exist. Found that there are some other hidden directories but we are interested in the first one !!! (But I think you shouldn't ignore the rest, we are better to check all of them).

![homepage](https://user-images.githubusercontent.com/72692401/95679871-571e7500-0c21-11eb-98e5-cf590d279e00.png)

We notice that the website is Marco's blog, so marco is a possible username that we should pay attention to !

Recall gobuster, there are some hidden directories, but we are interested in the first one.

![gobuster](https://user-images.githubusercontent.com/72692401/95679743-9c8e7280-0c20-11eb-9813-eab78537d097.png)

Let's visit that directory. Hmm, it looks like we need to find credentials to login. But before that, I try to login with marco:marco and I failed. However, we can see that website returns us a password hint.

![login](https://user-images.githubusercontent.com/72692401/95680061-82559400-0c22-11eb-8951-143d59d87204.png)

Do you remember marco blog page? He tells us a lot about his hobby which is all about planes and his favorite planes. Therefore, we can list them into the "a memorable word" referred to the password hint.

- A possible memorable word: marco, plane, planes, savoia, macchi, flying.

Next, there are 2 numbers and a special character at the end of the password. Until now, I think that I should try creating a simple python script to bruteforce login credentials. (I had included the script in github page site as well, for saving your time, I had removed some invalid combinations) (I'm really sorry because the script is not well organized).

![login](https://user-images.githubusercontent.com/72692401/95680440-7f0fd780-0c25-11eb-9eaf-1225623b50f7.png)

Successfully login, I immediately click onto "COMMANDS" page without any thinking and checking other pages !!!. 

I try different commands and also try escaping command filtering but it keeps returning "Invalid Command!".

However, you remember that we have another port is opening which is 22:ssh, I successfully login with the credentials that we found previously and read "flag1.txt"

![login](https://user-images.githubusercontent.com/72692401/95681024-525dbf00-0c29-11eb-8ccf-6f4390291964.png)

Listing home directory, there is another user is curtis, maybe I have to find a way to get to this user. Therefore, I tried to enumerate more about the current user and found that he belongs to "web-developers" group. The ability of this group is reading and writing files in "/var/www/html/admin/*".  












