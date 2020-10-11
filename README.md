# Capture The FLag
[THM] Year Of The Pig Walkthrough

Start with a simple nmap scan:

sudo nmap -sV -A $IP

![Screenshot 2020-10-12 001215](https://user-images.githubusercontent.com/72692401/95679646-fb9fb780-0c1f-11eb-9c54-bb4e65bbe84f.png)




See that there are two opened ports: 
- http:80
- ssh:22

Maybe we have something to do with http port, so I run gobuster against the website to find hidden directories if exist




