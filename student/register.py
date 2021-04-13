import pandas as pd
import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "student.settings")
django.setup()
from check.models import Student


data = pd.read_csv(r"st.csv")
# print(data)
for num,school, grade, name, phone, time, date, st_phone, fee_day, step, reg_date in data.loc:

    phone = str(phone)
    phone = phone.replace('-', '')
    if phone!='nan' and phone[0] != 0:
        phone = '0'+phone
        phone = phone[:len(phone)-2]
    obj = Student(id=num,school=school, grade=grade, name=name, phone=phone,
                  time=time, date=date, st_phone=st_phone, fee_day=fee_day, step=step,reg_date=reg_date)
    if Student.objects.filter(name=name).exists():
        pass
    else:
        print(name)
        obj.save()
