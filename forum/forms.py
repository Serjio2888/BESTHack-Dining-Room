from django.forms import ModelForm, HiddenInput
from forum.models import Comment, Topic

class CommentForm(ModelForm):
	class Meta:
		model = Comment
		fields = ['author_nick', 'text', 'topic']
		widgets = {
			'topic': HiddenInput()
		}

class TopicForm(ModelForm):
	class Meta:
		model = Topic
		fields = ['subject', 'food_type','price','text','calories','weigth']
