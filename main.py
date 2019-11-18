import requests
import time


def checkin():
    base_url = 'https://xxx.com'
    email = ""
    password = ""

    email = email.split('@')
    email = email[0] + '%40' + email[1]

    session = requests.session()
    login_url = base_url + '/auth/login'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    post_data = 'email=' + email + '&passwd=' + password + '&code=&remember_me=week'
    post_data = post_data.encode()
    session.post(login_url, post_data, headers=headers)

    headers = {
        'Referer': base_url + '/user'
    }
    response = session.post(base_url + '/user/checkin', headers=headers)
    print(response.json())


if __name__ == "__main__":
    for _ in range(3):
        try:
            checkin()
        except requests.exceptions.RequestException:
            time.sleep(3)
            continue
        break
