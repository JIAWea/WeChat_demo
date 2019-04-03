from backend import models
from django.forms import ModelForm

class ReprotingForm(ModelForm):
    """
    进行表单验证和生成HTML
    """
    class Meta:
        model = models.Reporting
        fields = '__all__'
        error_messages = {
            'type':{'required': '报装类型不能为空',},
            'user':{'required': '报装人不能为空',},
            'remark':{'required': '备注不能为空',}
        }

    def __new__(cls, *args, **kwargs):  # cls 就是实例(self)
        for field_name in cls.base_fields:
            field_obj = cls.base_fields[field_name]
            field_obj.widget.attrs.update({'class': 'form-control'})
            # if field_name in cls.Meta.readonly_fields:
            #     field_obj.widget.attrs.update({'disabled': 'true'})
        return ModelForm.__new__(cls)