# HTTPS doesn't means a security website
HTTPS means "HTTP over SSL" or "HTTP Secure", because of this name, people often get an illusion that the using HTTPS on the website can protect data very perfectly. But in fact, HTTPS is not omnipotent. Let's see in what way HTTPS is not working.

> We are not going to discuss the vulnerability of HTTPS itself, but discuss the security risks in practical applications.

## 1. DNS resolution
We all know, visit a website we need to find out the IP adress of the web server, but most of the website has a domain, when people visit that website, they need to send a request to a DNS server to get the IP adress. But DNS can be hijacked ([^DNS hijacking - Wikipedia]), an attacker can hijacking user's DNS request and forging a destination address to make user get to their fake website(*Because HTTPS uses certificate checking, the attacker will only redirects the domain name to a normal HTTP connection.*). Although nowadays some APP using HTTP DNS (HTTP DNS also can be hijacking) or DNS over HTTPS ([^DNS over HTTPS - Wikipedia]) but some even most the broser are not(Though Icannot find data to support my opinion.)!


[^DNS hijacking - wikipedia]:https://en.wikipedia.org/wiki/DNS_hijacking
[^DNS over HTTPS - Wikipedia]:https://en.wikipedia.org/wiki/DNS_over_HTTPS

##2. HTTP and HTTPS
Although some website support HTTPS, they also support HTTP, and maybe they use the same cookie or token or HTTPS and HTTP, this will allow attacker gijacking the HTTP
