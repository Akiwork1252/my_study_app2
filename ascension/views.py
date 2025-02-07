from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView, FormView, ListView, CreateView
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator

from .models import InterestCategory, UserInterest, LearningObjective
from .forms import InquiryForm, AddInterestCategoryForm, CreateLearningObjectiveForm


# TOP画面
class IndexView(TemplateView):
    template_name = 'ascension/index.html'


# 問い合わせフォーム
class InquiryView(FormView):
    template_name = 'ascension/inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('ascension:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'メッセージを送信しました。')
        return super().form_valid(form)


# 興味分野リスト画面
class InterestCategoryListView(LoginRequiredMixin, ListView):
    model = InterestCategory
    template_name = 'ascension/interest_category_list.html'

    def get_queryset(self):
        return InterestCategory.objects.prefetch_related('users').filter(users=self.request.user)


# 興味分野の追加
class AddInterestCategoryView(LoginRequiredMixin, FormView):
    form_class = AddInterestCategoryForm
    template_name = 'ascension/add_interest_category.html'
    success_url = reverse_lazy('ascension:interest_category_list')

    def form_valid(self, form):
        # フォームから選択されたカテゴリを取得
        selected_category = form.cleaned_data['category']
        # 興味分野を作成or取得
        interest_category, created = InterestCategory.objects.get_or_create(
            name=selected_category.name
        )
        # 中間モデルに追加
        UserInterest.objects.get_or_create(
            user=self.request.user,
            category=interest_category
        )
        return super().form_valid(form)


# 興味分野の削除(関連付けを削除)
class DeleteInterestCategoryView(LoginRequiredMixin, View):
    # 削除確認画面の表示
    def get(self, request, *args, **kwargs):
        category = get_object_or_404(InterestCategory, id=kwargs['category_id'])
        return render(request, 'ascension/delete_interest_category.html', {'category': category})
    
    # 関連付け削除
    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        # urlから削除するカテゴリを取得
        category = get_object_or_404(InterestCategory, id=kwargs['category_id'])
        # ユーザーとカテゴリの関連付け削除
        if request.user.interests.filter(id=category.id).exists():
            request.user.interests.remove(category)
            messages.success(request, f'{ request.user.username }の興味分野リストから"{category.name}"が削除されました。')
        else:
            messages.success(request, f'"{category.name}"は{ request.user.username}と関連付けられていません。')
        
        return redirect('ascension:interest_category_list')
    

# 学習目標リスト画面
class LearningObjectiveListView(LoginRequiredMixin, ListView):
    model = LearningObjective
    template_name = 'ascension/learning_objective_list.html'
    context_object_name = 'learning_objectives'

    # カテゴリごとの学習目標を取得
    def get_queryset(self):
        category_id = self.kwargs.get('category_id')  # urlからカテゴリidを取得
        return LearningObjective.objects.filter(user=self.request.user, category_id=category_id)
    
    # カテゴリ情報をテンプレートに渡す
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        context['category'] = get_object_or_404(InterestCategory, id=category_id)
        return context


# 学習目標の作成
class CreateLearningObjectiveView(LoginRequiredMixin, CreateView):
    model = LearningObjective
    template_name = 'ascension/create_learning_objective.html'
    form_class = CreateLearningObjectiveForm

    # カテゴリ情報をテンプレートに渡す
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        context['category'] = get_object_or_404(InterestCategory, id=category_id)
        return context
    
    # バリデーション成功で保存
    def form_valid(self, form):
        form.instance.user = self.request.user
        category_id = self.kwargs.get('category_id')  # urlからカテゴリidを取得
        form.instance.category = get_object_or_404(InterestCategory, id=category_id)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('ai_support:generate_plan_preview', kwargs={'learning_objective_id': str(self.object.id)})
    