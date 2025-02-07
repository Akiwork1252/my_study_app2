import os
from django import forms
from django.core.mail import EmailMessage
from .models import Category, LearningObjective


# 問い合わせ
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

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']
        subject = f'お問合せ {title}'
        message = f'送信者名: {name}\nメールアドレス: {email}\n\nお問合せ内容: \n{message}'
        from_email = os.environ.get('FROM_EMAIL')
        to_list = [os.environ('FROM_EMAIL')]
        if not from_email or not to_list[0]:
            raise ValueError('送信元または送信先のメールアドレスが設定されていません。')
        cc_list = [email] if email else []

        message = EmailMessage(
            subject=subject,
            body=message,
            from_email=from_email,
            to=to_list,
            cc=cc_list
        )


# 興味分野の追加
class AddInterestCategoryForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='追加する興味分野を選択してください。',
        widget=forms.Select(attrs={'class': 'form-select'})
    )


# 学習目標の追加
class CreateLearningObjectiveForm(forms.ModelForm):
    class Meta:
        model = LearningObjective
        fields = ('title', 'level_when_set', 'detail')
        labels = {'title': 'テーマ(必須)',
                  'level_when_set': 'テーマの学習経験',
                  'detail': '詳細'}
        widgets = {
            'title': forms.Textarea(attrs={
                'rows': 1,
                'class': 'form-control',
                'placeholder': '学びたいテーマを入力してください。(例:Python)'
            }),
            'level_when_set': forms.Textarea(attrs={
                'rows': 2,
                'class': 'form-control',
                'placeholder': '学習経験の有無や学習レベルを入力することで、より最適な学習プランを生成できます。'
            }),
            'detail': forms.Textarea(attrs={
                'rows': 6,
                'class': 'form-control',
                'placeholder': '目標レベルなどのテーマに関する詳細を入力することで、より最適な学習プランを生成できます。'
            })
        }
