import schedule, requests, time 

phone = input("Phone number: ")
message = input("Message: ")

# technically this api dosen't work foor my country so just have to look for a better suited one
def send_message():
    response = requests.post('https://textbelt.com/text', {
        'phone': phone,
        'message': message,
        'key': 'textbelt'
    })
    print(response.json())

# schedule.every().day.at('06:00').do(send_message)

schedule.every(10).seconds.do(send_message)
while True:
    schedule.run_pending()
    time.sleep(11)