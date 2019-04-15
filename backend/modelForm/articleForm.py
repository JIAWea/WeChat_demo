from backend import models
from django.forms import ModelForm

class articleForm(ModelForm):
    """
    进行表单验证和生成HTML
    """
    class Meta:
        model = models.Article
        fields = '__all__'
        error_messages = {
            'title':{'required': '标题不能为空',},
            'content':{'required': '内容不能为空',},
        }

    def __new__(cls, *args, **kwargs):      # cls 就是实例(self)
        for field_name in cls.base_fields:
            if field_name=="content":
                field_obj = cls.base_fields[field_name]
                field_obj.widget.attrs.update({'class': 'form-control','id':'editor_id'})
            field_obj = cls.base_fields[field_name]
            field_obj.widget.attrs.update({'class': 'form-control'})
        return ModelForm.__new__(cls)