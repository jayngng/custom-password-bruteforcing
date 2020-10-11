# Capture The FLag
[THM] Year Of The Pig Walkthrough

Start with a simple nmap scan:

sudo nmap -sV -A $IP

![Screenshot 2020-10-12 001215](https://user-images.githubusercontent.com/72692401/95679646-fb9fb780-0c1f-11eb-9c54-bb4e65bbe84f.png)


See that there are two opened ports: 
- http:80
- ssh:22

Maybe we have something to do with the http port, so I run gobuster against the website to find hidden directories if exist. Let's have a look at this.




There are some other hidden directories but we are interested in the first one !!! (But I think you shouldn't ignore the rest, we are better to check all of them).

![homepage](https://user-images.githubusercontent.com/72692401/95679871-571e7500-0c21-11eb-98e5-cf590d279e00.png)

We notice that the website is Marco's blog, so marco is a possible username that we should pay attention to !

Recall gobuster, there are some hidden directories, but we are interested in the first one.

![gobuster](https://user-images.githubusercontent.com/72692401/95679743-9c8e7280-0c20-11eb-9813-eab78537d097.png)

Let's visit that directory.

![page](https://user-images.githubusercontent.com/72692401/95679980-fcd1e400-0c21-11eb-9c53-db3a2b46f9aa.png)

Hmm, it looks like we need to find credentials to login. I try to login with marco:marco but I failed.

![login](https://user-images.githubusercontent.com/72692401/95680061-82559400-0c22-11eb-8951-143d59d87204.png)

Luckily 







