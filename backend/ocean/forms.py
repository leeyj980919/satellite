from django import forms


class ObservationForm(forms.Form):
    x = forms.CharField(label='위도')
    y = forms.CharField(label='경도')

    # obsCode = forms.CharField(label='관측소 코드')
    date = forms.CharField(label="날짜", help_text='날짜형식:YYYYMMDD')

    def clean_data(self):
        date = self.cleaned_data['date']
        if not date.isdigit() or len(date) != 8:
            raise forms.ValidationError('날짜 형식은 YYYYMMDD여야 합니다.')
        return date
