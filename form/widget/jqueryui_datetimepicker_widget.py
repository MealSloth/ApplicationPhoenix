from django.forms import DateTimeInput


class JQueryUIDatetimepickerWidget(DateTimeInput):
    def __init__(self):
        super(DateTimeInput, self).__init__(attrs={"size": 10, "class": "datetimeinput"})
