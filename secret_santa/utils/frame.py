from datetime import datetime
from secret_santa.utils.email import send_email

def save_to_file(txt, filename):
    with open('./results/' + filename, 'a') as f:
        f.write(txt)
        f.write("\n==========================\n")


def save_fields(frame, fields, filename):
    now = datetime.now()
    to_save = [now.strftime("%d/%m/%Y %H:%M:%S")]
    for field in fields:
        value = frame.get(field)
        to_save.append(f"{field}: {str(value)}")
    result = '\n'.join(to_save)
    save_to_file(result, filename)
    send_email(str(frame.get('name')), result)