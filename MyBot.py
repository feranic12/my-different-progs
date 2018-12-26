import apiai,json
api_ai_instance=apiai.ApiAI('82b7754ffbb14e0885eec615c190fc12','WordsFinderAIBot')
print("Сейчас Вы можете начать беседу.")
while True:
    request=api_ai_instance.text_request()
    request.lang='ru'
    request.query=input()
    if request.query=="Пока!":
        print("Пока!")
        break
    responseJson=json.loads(request.getresponse().read().decode('utf-8'))
    response=responseJson['result']['fulfillment']['speech']
    if response:
        print(response)
    else:
        print("Сударь, выражайтесь яснее, пожалуйста!")