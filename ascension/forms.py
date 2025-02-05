from django import forms

class InquiryForm(forms.Form):
    name = forms.CharField(label='名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='タイトル', max_length=30)
    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form_control'
        self.fields['name'].widget.attrs['placeholder'] = 'ここに名前を入力してください。'

        self.fields['email'].widget.attrs['class'] = 'form_control'
        self.fields['email'].widget.attrs['placeholder'] = 'ここにメールアドレスを入力してください。'

        self.fields['title'].widget.attrs['class'] = 'form_control'
        self.fields['title'].widget.attrs['placeholder'] = 'ここにタイトルを入力してください。'

        self.fields['message'].widget.attrs['class'] = 'form_control'
        self.fields['message'].widget.attrs['placeholder'] = 'ここにメッセージを入力してください。'
