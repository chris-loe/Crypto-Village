from django.shortcuts import render

def home(request):
    # Requesting API
    import requests
    import json # JS format file


    # Grab Crypto Price Data
    price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD')  # API call for this crypto news OBJECT
    price = json.loads(price_request.content) # get API content (therefore .content) and converts content to json format
    # price is the object

    # Grab Crypto News
    news_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')  # API call for this crypto news OBJECT
    news = json.loads(news_request.content) # get API content (therefore .content) and converts content to json format
    # news is the object

    return render(request,'crypto/home.html',{'news':news, 'price':price} )
    # context dictionary takes in the api variable defined above ---> news and price
    # template tagging uses the context dictionary KEY


def prices(request):
    if request.method == "POST":
        import requests
        import json

        quote = request.POST['quote']
        # because we named it quote in input name for the form in html file
        quote = quote.upper()  # for error handling

        crypto_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + quote + '&tsyms=USD')
        crypto = json.loads(crypto_request.content)
        return render(request, 'crypto/prices.html',{'quote':quote, 'crypto':crypto})

    else:
        notfound = "Enter a crypto currency symbol in the search bar above"
        return render(request, 'crypto/prices.html',{'notfound':notfound})
