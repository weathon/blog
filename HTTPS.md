# HTTPS doesn't means a security website
HTTPS means "HTTP over SSL" or "HTTP Secure". Because of this name, people often get an illusion tha using HTTPS on the website can protect data perfectly. But in fact, HTTPS is not omnipotent. Let's see in what ways HTTPS is not working.

      We are not going to discuss the vulnerability of HTTPS itself, but discuss the security risks in practical applications.

## 1. DNS resolution

We all know that we need to find out the IP address of the web server if we visit a website, but most of the website has a domain. When people visit that website, they need to send a request to a DNS server to get the IP adress, but DNS can be hijacked ([^DNS hijacking - Wikipedia]). An attacker can hijack users' DNS request and forge a destination address to make users go to their fake website (*Because HTTPS uses certificate checking, the attacker will only redirect the domain name to a normal HTTP connection.*). Although nowadays some APPs use HTTP DNS (HTTP DNS also can be hijacked) or DNS over HTTPS ([^DNS over HTTPS - Wikipedia]), some even most of the browsers are not using DNS over HTTPS.
(Though I cannot find data to support my opinion.)


[^DNS hijacking - wikipedia]:https://en.wikipedia.org/wiki/DNS_hijacking
[^DNS over HTTPS - Wikipedia]:https://en.wikipedia.org/wiki/DNS_over_HTTPS

## 2. HTTP and HTTPS

Although some websites support HTTPS, they also support a HTTP connect. And maybe sometimes they use the same cookie or token orve HTTPS and HTTP. This will allow attackers to gijack the HTTP cookie and use them to login users account over HTTPS.
