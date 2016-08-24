from django.forms import DateTimeInput


class JQueryUIDatepickerWidget(DateTimeInput):
    def __init__(self):
        super(DateTimeInput, self).__init__(attrs={"size": 10, "class": "dateinput"})
